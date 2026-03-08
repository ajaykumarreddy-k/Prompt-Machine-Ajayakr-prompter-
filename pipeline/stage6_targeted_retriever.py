"""stage6_targeted_retriever.py — Retrieves context exclusively for blueprint components."""

from vector_kb import retrieve, format_for_llm

# Pre-computed tag mappings for common ontology components to ensure targeted retrieval
RETRIEVAL_MAP = {
    "QuestionCard": ("card quiz form input select option interactive", "cards"),
    "QuizPlayer":   ("game player dashboard layout interactive", "layouts"),
    "OptionButton": ("button radio select option click target", "forms"),
    "Timer":        ("timer countdown clock progress status", "animations"),
    "ProgressBar":  ("progress bar step indicator visual status", "effects"),
    "Navbar":       ("navbar navigation link header top sticky", "navbar"),
    "Footer":       ("footer columns links bottom social bottom-bar", "footer"),
    "QuizList":     ("grid list cards selection menu flex", "cards"),
    "ScoreSummary": ("card metric stat result score highlight", "cards"),
    "ResultsSummary":("metric stat result dashboard complete", "cards")
}

def retrieve_targeted_context(blueprint: dict, required_components: list) -> str:
    """Searches vector DB ONLY for the components listed in the ontology/blueprint."""
    print("\033[90m  Retrieving targeted component references...\033[0m")
    
    context_blocks = []
    
    for comp in required_components:
        if comp in RETRIEVAL_MAP:
            query, tag = RETRIEVAL_MAP[comp]
            results = retrieve(query, top_k=3, tag_filter=tag)
            
            if results:
                block = f"={'='*50}\n=== REFS: {comp.upper()} ===\n{'='*50}\n{format_for_llm(query, results)}"
                context_blocks.append(block)
                print(f"\033[90m    Found {len(results)} references for: {comp}\033[0m")
        else:
            # Fallback for dynamic/unmapped components: search without strict tag
            results = retrieve(f"{comp} UI component React Tailwind", top_k=2)
            if results:
                block = f"={'='*50}\n=== REFS: {comp.upper()} ===\n{'='*50}\n{format_for_llm(comp, results)}"
                context_blocks.append(block)
                print(f"\033[90m    Found {len(results)} references for: {comp}\033[0m")

    # Fallback if empty
    if not context_blocks:
        print("\033[33m⚠  Targeted retriever found no specific context.\033[0m")
        return ""
        
    return "\n".join(context_blocks)
