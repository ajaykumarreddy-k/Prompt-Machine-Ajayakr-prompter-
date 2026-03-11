"""stage6_targeted_retriever.py — Retrieves context using style-aware smart_query."""

from vector_kb import smart_query

# Pre-computed tag mappings for common ontology components to ensure targeted retrieval
RETRIEVAL_MAP = {
    "QuestionCard": "card quiz form input select option interactive",
    "QuizPlayer":   "game player dashboard layout interactive",
    "OptionButton": "button radio select option click target",
    "Timer":        "timer countdown clock progress status",
    "ProgressBar":  "progress bar step indicator visual status",
    "Navbar":       "navbar navigation link header top sticky",
    "Footer":       "footer columns links bottom social bottom-bar",
    "QuizList":     "grid list cards selection menu flex",
    "ScoreSummary": "card metric stat result score highlight",
    "ResultsSummary":"metric stat result dashboard complete"
}

def retrieve_targeted_context(prd_text: str, blueprint: dict, required_components: list) -> str:
    """Searches vector DB using smart_query for the components listed in the ontology/blueprint."""
    print("\033[90m  Retrieving targeted component references (Style-Aware)...\033[0m")
    
    context_blocks = []
    
    for comp in required_components:
        query_text = RETRIEVAL_MAP.get(comp, f"{comp} UI component React Tailwind")
        results = smart_query(prd_text, query_text, n=3)
        
        if results:
            content_str = "\n".join([
                f"\n--- REF {i+1} [{r['source']}] (Boosted: {r['boosted']}) ---\n{r['content']}"
                for i, r in enumerate(results)
            ])
            block = f"={'='*50}\n=== REFS: {comp.upper()} ===\n{'='*50}\n{content_str}"
            context_blocks.append(block)
            print(f"\033[90m    Found {len(results)} references for: {comp}\033[0m")

    # Fallback if empty
    if not context_blocks:
        print("\033[33m⚠  Targeted retriever found no specific context.\033[0m")
        return ""
        
    return "\n".join(context_blocks)
