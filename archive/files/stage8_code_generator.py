"""stage8_code_generator.py — Generate full React + Tailwind component file."""

from ollama import ollama_stream

SYSTEM = """\
You are an expert React and Tailwind CSS developer.
You will receive REFERENCE PATTERNS extracted from real UI component libraries.
Your job is to synthesise them into a production-quality React component file.

STRICT RULES:
- Study the REFERENCE PATTERNS before writing any code
- Adapt real class names, structure, and patterns from the references
- Use ONLY Tailwind CSS utility classes — zero inline styles, zero custom CSS
- Every component: named export, no required props
- Build ALL components listed in the spec in a SINGLE file
- Final export must be:  export default App
- Responsive with sm:/md:/lg: breakpoints
- Do not import any external libraries except React
- Output ONLY complete code — no explanation, no markdown fences"""


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
    page_comps = components["component_map"].get(primary_page["name"], [])
    p          = design["palette"]

    spec = f"""
PRODUCT: {intent['product_name']}  ({intent['product_type']})
AUDIENCE: {intent['target_audience']}
FEATURES: {', '.join(intent.get('key_features', []))}

PALETTE (use these exact Tailwind class names):
  bg-{p['bg']}          ← page background
  text-{p['text']}       ← body text
  bg-{p['primary']}     ← primary buttons/highlights
  text-{p['accent']}    ← accent text / icons
  bg-{p['secondary']}   ← secondary elements / cards

COMPONENTS TO BUILD: {', '.join(page_comps)}

UI SPEC:
{ui_prompt}
"""

    # Limit KB context to stay inside context window
    kb_block = kb_context[:10_000] if kb_context else "(no KB context available)"

    full_prompt = f"""{spec}

REFERENCE PATTERNS FROM REAL COMPONENT LIBRARIES:
{kb_block}

Now write the complete React file.
Start with:  import React from 'react';
End with:    export default App;"""

    print("\033[35m\033[1m[OLLAMA]\033[0m Generating React code...\n")
    return ollama_stream(full_prompt, system=SYSTEM)
