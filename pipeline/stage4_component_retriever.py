"""
stage4_component_retriever.py
Retrieves real component patterns from your 250k+ line vector KB.
Each component gets its own tagged query (top_k=6).
"""

import sys
from pathlib import Path

# Make sure vector_kb is importable from project root
sys.path.insert(0, str(Path(__file__).parent.parent))

# ── TAG QUERY MAP ─────────────────────────────────────────────────────────────
TAG_QUERIES: dict[str, tuple[str, str]] = {
    "navbar":     ("navbar sticky glassmorphism navigation header links React Tailwind", "navbar"),
    "hero":       ("hero headline CTA gradient large text animation above fold saas", "hero"),
    "cards":      ("card feature grid hover shadow metric pricing React Tailwind",      "cards"),
    "sidebar":    ("sidebar navigation drawer app dashboard fixed React Tailwind",      "sidebar"),
    "tables":     ("data table rows columns sort filter dashboard React Tailwind",      "tables"),
    "forms":      ("form input login auth register field submit React Tailwind",        "forms"),
    "footer":     ("footer links copyright columns brand social React Tailwind",        "footer"),
    "animations": ("text animation fade slide typewriter scroll reveal motion",         "animations"),
    "effects":    ("glassmorphism blur glow gradient aurora radial background",         "effects"),
}

# ── KB AVAILABILITY ───────────────────────────────────────────────────────────
def _kb_available() -> bool:
    try:
        from vector_kb import get_index
        get_index()
        return True
    except Exception:
        return False


def retrieve_components(
    intent: dict,
    layout: dict,
    hierarchy: dict,
) -> dict:
    """
    Returns:
        {
            "component_map": { "PageName": ["comp1", "comp2", ...] },
            "kb_context":    str,   # raw text injected into LLM prompts
        }
    """
    # Collect all unique components across all pages
    all_comps: list[str] = []
    for page in layout["pages"]:
        for c in page.get("components", []):
            if c not in all_comps:
                all_comps.append(c)

    style  = " ".join(intent.get("style_keywords", []))
    parts: list[str] = []
    retrieved_count  = 0

    kb_ok = _kb_available()
    if not kb_ok:
        print("\033[33m⚠  Vector KB not ready — run: uv run vector_kb.py build\033[0m")

    for comp in all_comps:
        if comp not in TAG_QUERIES:
            continue

        base_query, tag = TAG_QUERIES[comp]
        query = f"{base_query} {style}"

        if kb_ok:
            try:
                from vector_kb import retrieve, format_for_llm
                results = retrieve(query, top_k=6, tag_filter=tag)
                if results:
                    ctx = format_for_llm(query, results)
                    parts.append(f"\n{'='*50}\n=== {comp.upper()} PATTERNS ===\n{'='*50}\n{ctx}")
                    retrieved_count += 1
                    print(f"\033[90m  ↳ {comp}: {len(results)} chunks retrieved\033[0m")
                else:
                    print(f"\033[33m  ↳ {comp}: no results\033[0m")
            except Exception as e:
                print(f"\033[33m  ↳ {comp}: KB error — {e}\033[0m")

    print(
        f"\033[32m  ✓ {retrieved_count}/{len(all_comps)} components retrieved from KB\033[0m"
        if kb_ok else ""
    )

    # Build component_map per page
    component_map: dict[str, list[str]] = {}
    for page in layout["pages"]:
        component_map[page["name"]] = page.get("components", [])

    return {
        "component_map": component_map,
        "kb_context":    "\n".join(parts),
        "all_components": all_comps,
    }
