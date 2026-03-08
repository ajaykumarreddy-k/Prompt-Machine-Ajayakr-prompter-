"""stage1_intent_parser.py — Extract structured intent from PRD text."""

from ollama import ollama, extract_json

SYSTEM = (
    "You are a PRD analysis expert. Extract structured information from product "
    "requirement documents. Respond with valid JSON only — no markdown, no explanation."
)

FALLBACK: dict = {
    "product_name":    "App",
    "product_type":    "landing",
    "target_audience": "general users",
    "key_features":    ["feature 1", "feature 2", "feature 3"],
    "tone":            "professional",
    "style_keywords":  ["modern", "clean"],
    "pages":           ["home"],
    "palette_hint":    "blue",
    "complexity":      "medium",
    "industry":        "technology",
}


def parse_intent(prd: str) -> dict:
    prompt = f"""Analyze this PRD and extract structured information.

PRD:
{prd}

Return ONLY valid JSON with this exact shape:
{{
  "product_name":    "short product name",
  "product_type":    "landing|dashboard|auth|saas|portfolio|ecommerce|tool",
  "target_audience": "who uses this",
  "key_features":    ["feature1", "feature2", "feature3"],
  "tone":            "professional|playful|minimal|bold|technical|creative",
  "style_keywords":  ["keyword1", "keyword2"],
  "pages":           ["home", "dashboard", ...],
  "palette_hint":    "color or mood hint",
  "complexity":      "simple|medium|complex",
  "industry":        "industry or domain"
}}"""

    raw    = ollama(prompt, system=SYSTEM, label="Parsing PRD intent")
    parsed = extract_json(raw)
    if not parsed or not isinstance(parsed, dict):
        print("\033[33m⚠  Intent parse failed — using defaults\033[0m")
        return FALLBACK

    # Fill any missing keys from fallback
    return {**FALLBACK, **parsed}
