"""stage7_prompt_generator.py — Build structured UI builder prompt."""

from ollama import ollama

SYSTEM = (
    "You are a senior frontend engineer writing precise prompts for AI UI builders "
    "like v0.dev, Lovable, and Bolt. Write clear, actionable instructions that produce "
    "modern SaaS interfaces. Output the prompt text directly — no JSON, no meta-commentary."
)


def generate_prompt(
    intent: dict,
    layout: dict,
    hierarchy: dict,
    components: dict,
    design: dict,
) -> str:
    primary_page = next(
        (p for p in layout["pages"] if p.get("priority") == 1),
        layout["pages"][0],
    )
    page_comps = components["component_map"].get(primary_page["name"], [])
    p          = design["palette"]
    tw         = design["tailwind"]

    # Build the context prompt
    features_block = "\n".join(f"- {f}" for f in intent.get("key_features", []))
    sections_block = " → ".join(primary_page.get("sections", []))
    comps_block    = ", ".join(page_comps)

    user_prompt = f"""Write a complete frontend generation prompt for this product.

Product name: {intent['product_name']}
Product type: {intent['product_type']}
Target audience: {intent['target_audience']}
Key features:
{features_block}

Primary page: {primary_page['name']} ({primary_page['type']})
Section order: {sections_block}
Components: {comps_block}

Visual hierarchy:
- Primary focus: {hierarchy.get('primary_section', 'Hero')}
- Secondary: {', '.join(hierarchy.get('secondary_sections', []))}
- CTA button label: "{hierarchy.get('cta_text', 'Get Started')}"
- Focal point: {hierarchy.get('focal_point', 'Hero headline')}

Design system:
- Palette: {p['name']} — primary {p['primary']}, secondary {p['secondary']}, accent {p['accent']}
- Background: {p['bg']}  |  Text: {p['text']}
- Dark mode: {design['dark_mode']}
- Visual effect: {design['visual_effect']} at {design['effect_placement']}
- Hero animation: {design['text_animation']}
- Container: {tw['container']}
- Section spacing: {tw['section']}
- Card style: {tw['card']}
- Primary button: {tw['btn_primary']}

Tone: {intent.get('tone', 'professional')}
Stack: React functional components + Tailwind CSS only. Responsive, mobile-first.

Write a 200–350 word structured prompt for an AI UI builder.
Specify exact section order, column counts, and Tailwind class hints.
Do not write code — write the instructions."""

    return ollama(user_prompt, system=SYSTEM, label="Generating UI prompt")
