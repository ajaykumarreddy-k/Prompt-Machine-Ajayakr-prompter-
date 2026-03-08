"""stage3_visual_hierarchy.py — Plan attention flow and visual weight."""

from ollama import ollama, extract_json

SYSTEM = "You are a visual designer specializing in UI hierarchy. Respond with valid JSON only."


def plan_visual_hierarchy(intent: dict, layout: dict) -> dict:
    primary_page = next(
        (p for p in layout["pages"] if p.get("priority") == 1),
        layout["pages"][0],
    )
    sections = primary_page.get("sections", [])

    prompt = f"""Plan the visual hierarchy for this UI.

Product: {intent['product_name']} ({intent['product_type']})
Tone: {intent.get('tone', 'professional')}
Primary page: {primary_page['name']} ({primary_page['type']})
Sections available: {', '.join(sections)}

Return ONLY valid JSON:
{{
  "primary_section":    "most important section",
  "secondary_sections": ["second-tier sections"],
  "supporting_sections":["utility/background sections"],
  "cta_text":           "main call-to-action button label",
  "hero_headline_style":"bold|elegant|minimal|impactful",
  "scroll_flow":        ["section order guiding user naturally"],
  "focal_point":        "where the user eye lands first",
  "visual_weight": {{
    "SectionName": "high|medium|low"
  }}
}}"""

    raw    = ollama(prompt, system=SYSTEM, label="Planning visual hierarchy")
    parsed = extract_json(raw)

    if not parsed:
        return {
            "primary_section":     sections[1] if len(sections) > 1 else "Hero",
            "secondary_sections":  sections[2:4],
            "supporting_sections": sections[-1:],
            "cta_text":            f"Get Started with {intent['product_name']}",
            "hero_headline_style": "bold",
            "scroll_flow":         sections,
            "focal_point":         "Hero headline and primary CTA",
            "visual_weight":       {},
        }

    return parsed
