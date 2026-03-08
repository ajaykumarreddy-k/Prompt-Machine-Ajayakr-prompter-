#!/usr/bin/env python3
"""
Prompt Machine — Vector Knowledge Base
Upgraded: section-based chunking, component-aware tags, nomic embeddings supported,
cached model + index globals, CPU-only (Ollama owns the GPU).

Usage:
    uv run vector_kb.py build           # index all Scrapped-Data/*.txt files
    uv run vector_kb.py query           # interactive search REPL
    uv run vector_kb.py retrieve "navbar glassmorphism"
"""

import os, sys, json, pickle, re
from pathlib import Path
import numpy as np

# ── FORCE CPU ─────────────────────────────────────────────────────────────────
os.environ["CUDA_VISIBLE_DEVICES"] = ""

# ── CONFIG ────────────────────────────────────────────────────────────────────
# Auto-detect Scrapped-Data/ — checks cwd, parent, and grandparent
def _find_dir(name: str) -> Path:
    here = Path(__file__).parent
    for candidate in [here, here.parent, here.parent.parent]:
        p = candidate / name
        if p.exists():
            return p
    return here / name   # fallback (may not exist — handled gracefully)

SCRAPPED_DIR  = _find_dir("Scrapped-Data")
KB_MD_DIR     = _find_dir("knowledge-base")
INDEX_DIR     = _find_dir("vector-kb")
CHUNK_SIZE    = 600
CHUNK_OVERLAP = 80
TOP_K         = 6
EMBED_MODEL   = "BAAI/bge-small-en-v1.5"        # swap to nomic-ai/nomic-embed-text-v1 for higher quality

# ── GLOBAL CACHE — loaded once ────────────────────────────────────────────────
_model  = None
_index  = None
_chunks = None


def get_model():
    global _model
    if _model is None:
        from sentence_transformers import SentenceTransformer
        _model = SentenceTransformer(EMBED_MODEL, device="cpu")
    return _model


def get_index():
    global _index, _chunks
    if _index is None:
        import faiss
        idx_path = INDEX_DIR / "index.faiss"
        chk_path = INDEX_DIR / "chunks.pkl"
        if not idx_path.exists():
            print("Index not found. Run:  uv run vector_kb.py build")
            sys.exit(1)
        _index  = faiss.read_index(str(idx_path))
        with open(chk_path, "rb") as f:
            _chunks = pickle.load(f)
    return _index, _chunks


# ── FILE → CATEGORY MAP ───────────────────────────────────────────────────────
FILE_CATEGORIES = {
    "uiverse.txt":                   "components",
    "Reactbits.txt":                 "components",
    "components_components.txt":     "components",
    "21dev.txt":                     "components",
    "aceternityui.txt":              "components",
    "freefrontend.com.txt":          "components",
    "floatui.com.txt":               "components",
    "lightwind.txt":                 "components",
    "lightwindwebsite.txt":          "components",
    "animejs.txt":                   "animations",
    "scroll-animation.txt":          "animations",
    "prompts.txt":                   "prompts",
    "templates.txt":                 "prompts",
    "v0dev-templates.txt":           "prompts",
    "olayouts.txt":                  "layouts",
    "www.landingfolio.com.txt":      "layouts",
    "dribbble.com.txt":              "layouts",
    "meterialtheme.txt":             "design",
    "metrialtheme.txt":              "design",
}

# ── COMPONENT TAGS ────────────────────────────────────────────────────────────
COMPONENT_TAGS: dict[str, list[str]] = {
    "navbar":     ["nav", "navbar", "navigation", "header", "topbar", "menu", "sticky"],
    "hero":       ["hero", "banner", "headline", "cta", "above-the-fold", "landing"],
    "cards":      ["card", "tile", "feature-card", "stat", "metric", "pricing", "grid"],
    "sidebar":    ["sidebar", "drawer", "side-panel", "sidenav", "navigation-rail"],
    "tables":     ["table", "data-table", "thead", "tbody", "datagrid", "rows"],
    "forms":      ["form", "input", "login", "auth", "register", "signup", "label", "field"],
    "footer":     ["footer", "bottom-bar", "copyright", "links"],
    "animations": ["animate", "keyframe", "transition", "fade", "slide", "typewriter",
                   "motion", "scroll", "reveal", "framer"],
    "effects":    ["blur", "glow", "gradient", "glassmorphism", "shadow",
                   "backdrop", "radial", "aurora"],
    "palettes":   ["color", "palette", "theme", "--primary", "--accent", "hsl", "rgb("],
    "prompts":    ["prompt", "build a", "create a", "design a", "generate"],
    "layouts":    ["landing", "dashboard", "admin", "marketing", "homepage"],
}


def tag_chunk(text: str) -> str:
    t = text.lower()
    scores = {tag: sum(1 for kw in kws if kw in t) for tag, kws in COMPONENT_TAGS.items()}
    best = max(scores, key=lambda k: scores[k])
    return best if scores[best] > 0 else "general"


def clean_text(text: str) -> str:
    text = re.sub(r"[─=-]{10,}", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[^\x00-\x7F]+", " ", text)
    return text.strip()


# ── SECTION-BASED CHUNKING (new) ──────────────────────────────────────────────
def split_by_sections(text: str, source: str, category: str) -> list[dict]:
    """
    Split markdown / plain text into semantic sections by headings.
    Falls back to word-window chunking if no headings found.
    """
    # Try heading-based split first
    sections = re.split(r"\n(?=#{1,3} )", text)
    chunks = []
    cid = 0

    for sec in sections:
        sec = sec.strip()
        if len(sec) < 60:
            continue
        chunks.append({
            "id":       f"{source}_{cid}",
            "text":     sec,
            "source":   source,
            "category": category,
            "tag":      tag_chunk(sec),
        })
        cid += 1

    # If no heading structure, fall back to word-window chunks
    if len(chunks) < 2:
        words = text.split()
        cid = 0
        i = 0
        while i < len(words):
            chunk_text = " ".join(words[i : i + CHUNK_SIZE])
            if len(chunk_text) > 80:
                chunks.append({
                    "id":       f"{source}_{cid}",
                    "text":     chunk_text,
                    "source":   source,
                    "category": category,
                    "tag":      tag_chunk(chunk_text),
                })
                cid += 1
            i += CHUNK_SIZE - CHUNK_OVERLAP

    return chunks


# ── BUILD INDEX ───────────────────────────────────────────────────────────────
def build():
    import faiss

    INDEX_DIR.mkdir(exist_ok=True)
    print(f"\n── Embedding model (CPU): {EMBED_MODEL}")
    model = get_model()

    all_chunks: list[dict] = []

    # 1. Scrapped-Data .txt files
    if SCRAPPED_DIR.exists():
        txt_files = [f for f in sorted(SCRAPPED_DIR.glob("*.txt"))
                     if "split-output" not in str(f)]
        print(f"── {len(txt_files)} scraped files\n")
        for fp in txt_files:
            cat    = FILE_CATEGORIES.get(fp.name, "general")
            text   = clean_text(fp.read_text(encoding="utf-8", errors="ignore"))
            chunks = split_by_sections(text, fp.stem, cat)
            all_chunks.extend(chunks)
            print(f"  {fp.name:45s}  {len(chunks):>5} chunks  [{cat}]")
    else:
        print(f"── Scrapped-Data/ not found — skipping scraped files")

    # 2. knowledge-base .md files (your hand-crafted component docs)
    if KB_MD_DIR.exists():
        md_files = list(KB_MD_DIR.rglob("*.md"))
        print(f"\n── {len(md_files)} knowledge-base .md files\n")
        for fp in md_files:
            text   = fp.read_text(encoding="utf-8", errors="ignore")
            chunks = split_by_sections(text, fp.stem, "components")
            all_chunks.extend(chunks)
            print(f"  {fp.name:45s}  {len(chunks):>5} chunks  [kb-md]")

    print(f"\n── {len(all_chunks):,} total chunks")

    if not all_chunks:
        print("\n\033[31m✗  No chunks found.\033[0m")
        print(f"   Scrapped-Data/ looked for at: {SCRAPPED_DIR}")
        print(f"   knowledge-base/ looked for at: {KB_MD_DIR}")
        print("   Make sure at least one of those folders exists and contains files.")
        return

    print("── Embedding on CPU (this takes a while for 250k lines)...")

    texts = [c["text"] for c in all_chunks]
    embs  = []
    bs    = 128
    for i in range(0, len(texts), bs):
        batch = model.encode(
            texts[i : i + bs],
            normalize_embeddings=True,
            show_progress_bar=False,
        )
        embs.append(batch)
        done = min(i + bs, len(texts))
        pct  = done / len(texts) * 100
        print(f"  {done:>8,}/{len(texts):,}  ({pct:.0f}%)", end="\r")

    embeddings = np.vstack(embs).astype("float32")
    print(f"\n── Embedding shape: {embeddings.shape}")

    index = faiss.IndexFlatIP(embeddings.shape[1])
    index.add(embeddings)
    faiss.write_index(index, str(INDEX_DIR / "index.faiss"))

    with open(INDEX_DIR / "chunks.pkl", "wb") as f:
        pickle.dump(all_chunks, f)

    json.dump(
        {"total": len(all_chunks), "model": EMBED_MODEL,
         "dim": embeddings.shape[1], "device": "cpu"},
        open(INDEX_DIR / "meta.json", "w"),
        indent=2,
    )

    print(f"\n✓  Done — {len(all_chunks):,} chunks indexed.")
    print(f"   index.faiss : {(INDEX_DIR/'index.faiss').stat().st_size // 1024} KB")
    print(f"   chunks.pkl  : {(INDEX_DIR/'chunks.pkl').stat().st_size  // 1024} KB")


# ── RETRIEVE ──────────────────────────────────────────────────────────────────
def retrieve(query: str, top_k: int = TOP_K, tag_filter: str | None = None) -> list[dict]:
    model          = get_model()
    index, chunks  = get_index()

    q_emb    = model.encode([query], normalize_embeddings=True).astype("float32")
    search_k = top_k * 6 if tag_filter else top_k * 3
    scores, idxs = index.search(q_emb, search_k)

    results: list[dict] = []
    for score, idx in zip(scores[0], idxs[0]):
        if idx == -1:
            continue
        chunk = chunks[idx].copy()
        chunk["score"] = float(score)
        if tag_filter and chunk["tag"] != tag_filter:
            continue
        results.append(chunk)
        if len(results) >= top_k:
            break
    return results


def format_for_llm(query: str, results: list[dict]) -> str:
    lines = [f"QUERY: {query}", f"CONTEXT ({len(results)} chunks):", "=" * 60]
    for i, r in enumerate(results, 1):
        lines.append(f"\n[{i}] source={r['source']}  tag={r['tag']}  score={r['score']:.3f}")
        lines.append(r["text"])
        lines.append("-" * 40)
    return "\n".join(lines)


# ── QUERY REPL ────────────────────────────────────────────────────────────────
def query_mode():
    print("\nPrompt Machine — Vector KB  |  type 'quit' to exit\n")
    get_model(); get_index()
    print("Index ready.\n")
    tag_filter: str | None = None
    top_k = TOP_K

    while True:
        try:
            inp = input("query> ").strip()
        except (KeyboardInterrupt, EOFError):
            break
        if not inp or inp in ("quit", "q", "exit"):
            break
        if inp.startswith("filter:"):
            tag_filter = inp.split(":", 1)[1].strip() or None
            print(f"Tag filter → {tag_filter}"); continue
        if inp.startswith("top:"):
            try:
                top_k = int(inp.split(":", 1)[1])
            except ValueError:
                pass
            print(f"Top-K → {top_k}"); continue

        results = retrieve(inp, top_k=top_k, tag_filter=tag_filter)
        if not results:
            print("No results.\n"); continue
        for i, r in enumerate(results, 1):
            preview = r["text"][:200].replace("\n", " ")
            print(f"[{i}] {r['source']:30s}  tag={r['tag']:12s}  score={r['score']:.3f}")
            print(f"    {preview}...")
        print()


# ── ENTRY ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "help"
    if cmd == "build":
        build()
    elif cmd == "query":
        query_mode()
    elif cmd == "retrieve" and len(sys.argv) > 2:
        q = " ".join(sys.argv[2:])
        print(format_for_llm(q, retrieve(q)))
    else:
        print("Usage:")
        print("  uv run vector_kb.py build")
        print("  uv run vector_kb.py query")
        print("  uv run vector_kb.py retrieve <query>")