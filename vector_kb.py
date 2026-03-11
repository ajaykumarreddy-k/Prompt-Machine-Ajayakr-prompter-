#!/usr/bin/env python3
"""
Prompt Machine — Vector Knowledge Base (ChromaDB Migration)
Upgraded: ChromaDB persistent storage, BGE embeddings, and smart style-aware querying.
"""

import os
import sys
import json
import re
from pathlib import Path
from chromadb.utils import embedding_functions
from sentence_transformers import SentenceTransformer

# ── FORCE CPU ─────────────────────────────────────────────────────────────────
os.environ["CUDA_VISIBLE_DEVICES"] = ""

# ── CONFIG ────────────────────────────────────────────────────────────────────
SCRAPPED_DIR = Path("Scrapped-Data")
VECTOR_DB_DIR = Path("vector-kb/chroma")
COLLECTION_NAME = "ui_components"
EMBED_MODEL = "BAAI/bge-small-en-v1.5"

# ── MODEL CACHE ───────────────────────────────────────────────────────────────
_model = None

def get_model():
    """Returns cached SentenceTransformer model. Used by stage2_ontology_map."""
    global _model
    if _model is None:
        _model = SentenceTransformer(EMBED_MODEL, device="cpu")
    return _model

# ── FILE → CATEGORY MAP (WHOLE_FILE_ROUTES) ──────────────────────────────────
WHOLE_FILE_ROUTES = {
    "uiverse.txt": "components",
    "Reactbits.txt": "components",
    "21dev.txt": "components",
    "aceternityui.txt": "components",
    "freefrontend.com.txt": "components",
    "floatui.com.txt": "components",
    "animejs.txt": "animations",
    "scroll-animation.txt": "animations",
    "prompts.txt": "prompts",
    "templates.txt": "prompts",
    "v0dev-templates.txt": "prompts",
    "olayouts.txt": "layouts",
    "www.landingfolio.com.txt": "layouts",
    "dribbble.com.txt": "layouts",
    "meterialtheme.txt": "design",
    "metrialtheme.txt": "design",
}

# ── UTILS ─────────────────────────────────────────────────────────────────────
def clean_text(text: str) -> str:
    text = re.sub(r"[─=-]{10,}", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[^\x00-\x7F]+", " ", text)
    return text.strip()

def chunk_text(text: str, size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + size
        chunks.append(text[start:end])
        start += size - overlap
    return chunks

# ── CHROMA CLIENT ─────────────────────────────────────────────────────────────
def get_chroma_client():
    import chromadb
    return chromadb.PersistentClient(path=str(VECTOR_DB_DIR))

def get_embedding_function():
    return embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=EMBED_MODEL, 
        device="cpu"
    )

# ── BUILD ─────────────────────────────────────────────────────────────────────
def build():
    client = get_chroma_client()
    emb_fn = get_embedding_function()
    
    # Reset/Create collection
    try:
        client.delete_collection(COLLECTION_NAME)
    except:
        pass
        
    collection = client.create_collection(
        name=COLLECTION_NAME,
        embedding_function=emb_fn,
        metadata={"hnsw:space": "cosine"}
    )
    
    if not SCRAPPED_DIR.exists():
        print(f"Error: {SCRAPPED_DIR} not found.")
        return

    txt_files = list(SCRAPPED_DIR.glob("*.txt"))
    print(f"Found {len(txt_files)} files in {SCRAPPED_DIR}")

    for fp in txt_files:
        if fp.name not in WHOLE_FILE_ROUTES:
            continue
            
        category = WHOLE_FILE_ROUTES[fp.name]
        print(f"Processing {fp.name} [{category}]...")
        
        text = clean_text(fp.read_text(encoding="utf-8", errors="ignore"))
        chunks = chunk_text(text)
        
        batch_size = 100
        for i in range(0, len(chunks), batch_size):
            batch = chunks[i : i + batch_size]
            ids = [f"{fp.stem}_{i+j}" for j in range(len(batch))]
            metadatas = [
                {"source": fp.name, "category": category, "chunk_index": i+j} 
                for j in range(len(batch))
            ]
            
            collection.add(
                documents=batch,
                ids=ids,
                metadatas=metadatas
            )
        print(f"  Indexed {len(chunks)} chunks.")

    print("\n✓ Build complete.")

# ── QUERY ─────────────────────────────────────────────────────────────────────
def query(text: str, n=5):
    client = get_chroma_client()
    collection = client.get_collection(COLLECTION_NAME, embedding_function=get_embedding_function())
    
    results = collection.query(
        query_texts=[text],
        n_results=n
    )
    
    formatted = []
    for i in range(len(results["documents"][0])):
        formatted.append({
            "content": results["documents"][0][i],
            "source": results["metadatas"][0][i]["source"],
            "category": results["metadatas"][0][i]["category"],
            "score": 1 - results["distances"][0][i]
        })
    return formatted

def get_index():
    """Returns a dict with the collection and model for pipeline warmup."""
    client = get_chroma_client()
    model = get_model()
    collection = client.get_collection(COLLECTION_NAME, embedding_function=get_embedding_function())
    return {
        "collection": collection,
        "model": model
    }

def retrieve(query_text: str, n: int = 5):
    """Alias for query() returns list of dicts: {content, source, category, score}."""
    return query(query_text, n)

def format_for_llm(results: list[dict]) -> str:
    """Formats retrieve() output index into a string block for the LLM prompt."""
    if not results:
        return "No relevant context found."
    
    blocks = []
    for i, res in enumerate(results, 1):
        blocks.append(f"--- Component {i}: {res.get('category', 'unknown')} ({res.get('source', 'raw')}) ---")
        blocks.append(res["content"])
        blocks.append("") # Spacer
    return "\n".join(blocks)

def smart_query(prd_text: str, component_query: str, n: int = 5) -> list[dict]:
    """Style-aware query that prioritizes category matches based on PRD design styles."""
    from design_style_detector import detect_styles, get_style_retrieval_filter
    
    styles = detect_styles(prd_text)
    category_filters = get_style_retrieval_filter(styles)
    
    client = get_chroma_client()
    collection = client.get_collection(COLLECTION_NAME, embedding_function=get_embedding_function())
    
    # 1. First attempt filtered query
    filtered_results = collection.query(
        query_texts=[component_query],
        n_results=n,
        where={"category": {"$in": category_filters}}
    )
    
    f_docs = filtered_results["documents"][0]
    f_metas = filtered_results["metadatas"][0]
    f_dists = filtered_results["distances"][0]
    
    # Check if we have enough high-quality filtered results
    if len(f_docs) >= 3:
        final_results = []
        seen_content = set()
        
        # Priority: Boosted matches
        for i in range(len(f_docs)):
            content = f_docs[i]
            if content not in seen_content:
                final_results.append({
                    "content": content,
                    "source": f_metas[i]["source"],
                    "category": f_metas[i]["category"],
                    "score": 1 - f_dists[i],
                    "boosted": True
                })
                seen_content.add(content)
        
        # Backfill if we have space left
        if len(final_results) < n:
            normal_results = collection.query(query_texts=[component_query], n_results=n*2)
            n_docs = normal_results["documents"][0]
            n_metas = normal_results["metadatas"][0]
            n_dists = normal_results["distances"][0]
            
            for i in range(len(n_docs)):
                content = n_docs[i]
                if content not in seen_content:
                    final_results.append({
                        "content": content,
                        "source": n_metas[i]["source"],
                        "category": n_metas[i]["category"],
                        "score": 1 - n_dists[i],
                        "boosted": False
                    })
                    seen_content.add(content)
                if len(final_results) >= n:
                    break
        return final_results[:n]
    
    # 2. If filtered results < 3, just use normal query
    return query(component_query, n)

# ── CLI ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: vector_kb.py [build | query <text>]")
        sys.exit(1)
        
    cmd = sys.argv[1]
    if cmd == "build":
        build()
    elif cmd == "query" and len(sys.argv) > 2:
        q = " ".join(sys.argv[2:])
        res = query(q)
        for r in res:
            print(f"\n[{r['category']}] {r['source']} (Score: {r['score']:.3f})")
            print(r['content'][:200] + "...")
    else:
        print("Invalid command.")
