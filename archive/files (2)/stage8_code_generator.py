"""stage8_code_generator.py — Generate full React + Tailwind component file."""

from ollama import ollama_stream

SYSTEM = """\
You are an expert React and Tailwind CSS developer.
You will receive REFERENCE PATTERNS from real UI component libraries.
Synthesise them into a production-quality, complete React component file.

STRICT RULES:
- Study the REFERENCE PATTERNS before writing code
- Adapt real class names and structure from references
- Use ONLY Tailwind CSS utility classes — zero inline styles, zero custom CSS
- Build ALL components listed in the spec in a SINGLE file
- Every component: named export, no required props (use realistic default data)
- Final export must be:  export default App
- Responsive with sm:/md:/lg: breakpoints
- Do not import any external libraries except React
- Make it realistic — use actual product name and real feature content, not placeholder text
- Output ONLY the complete code — no explanation, no markdown fences"""


def generate_code(
    intent: dict,
    layout: dict,
    components: dict,
    design: dict,
    kb_context: str,
    ui_prompt: str,
) -> str:
    primary_page = next(
        (p for p in layout["pages"] if p.get("priority") == 1),
        layout["pages"][0],
    )
    page_comps   = components["component_map"].get(primary_page["name"], [])
    custom_comps = primary_page.get("custom_components", intent.get("custom_components", []))
    ui_interacts = intent.get("ui_interactions", [])
    p            = design["palette"]
    tw           = design["tailwind"]

    # Build a comprehensive component list
    all_comps = list(dict.fromkeys(page_comps + custom_comps))  # deduplicated, ordered

    interactions_block = ""
    if ui_interacts:
        interactions_block = f"\nUI INTERACTIONS TO IMPLEMENT: {', '.join(ui_interacts)}"
        if "timer" in ui_interacts:
            interactions_block += "\n- Timer: use React useState + useEffect with setInterval"
        if "progress-bar" in ui_interacts:
            interactions_block += "\n- ProgressBar: visual indicator showing current question / total"
        if "instant-feedback" in ui_interacts:
            interactions_block += "\n- InstantFeedback: highlight correct/wrong answer after selection"

    spec = f"""
PRODUCT: {intent['product_name']}  ({intent['product_type']})
AUDIENCE: {intent['target_audience']}
FEATURES: {', '.join(intent.get('key_features', []))}
{interactions_block}

DESIGN TOKENS (use these exact Tailwind classes):
  Page bg:       {tw['bg_page']}
  Card:          {tw['card']}
  Primary btn:   {tw['btn_primary']}
  Secondary btn: {tw['btn_secondary']}
  Heading text:  {tw['text_heading']}
  Body text:     {tw['text_body']}
  Input:         {tw['input']}
  Container:     {tw['container']}
  Section:       {tw['section']}
  Accent text:   {tw['accent_text']}

COMPONENTS TO BUILD (all in one file): {', '.join(all_comps)}

UI SPEC:
{ui_prompt}
"""

    kb_block = kb_context[:10_000] if kb_context else "(no KB context)"

    full_prompt = f"""{spec}

REFERENCE PATTERNS FROM REAL COMPONENT LIBRARIES:
{kb_block}

Write the complete React file.
- Use realistic sample data for {intent['product_name']} (not "Lorem ipsum")
- Each component should be fully styled and functional
- Wire up interactive components with useState where needed
Start with:  import React, {{ useState, useEffect }} from 'react';
End with:    export default App;"""

    print("\033[35m\033[1m[OLLAMA]\033[0m Generating React code...\n")
    return ollama_stream(full_prompt, system=SYSTEM)
