"""stage2_layout_contract.py — Convert intent into a concrete layout contract."""

from ollama import ollama, extract_json

SYSTEM = "You are a UI architect. Convert product intent into layout contracts. Respond with valid JSON only."

# Sensible defaults per page type — used as fallback and as hint to the model
PAGE_DEFAULTS: dict[str, list[str]] = {
    "landing":   ["navbar", "hero", "cards", "footer"],
    "saas":      ["navbar", "hero", "cards", "footer"],
    "dashboard": ["sidebar", "cards", "tables"],
    "auth":      ["forms"],
    "ecommerce": ["navbar", "hero", "cards", "tables", "footer"],
    "portfolio":  ["navbar", "hero", "cards", "footer"],
    "tool":      ["navbar", "hero", "cards", "footer"],
}


def generate_layout_contract(intent: dict) -> dict:
    ptype     = intent.get("product_type", "landing")
    defaults  = PAGE_DEFAULTS.get(ptype, ["navbar", "hero", "cards", "footer"])
    features  = intent.get("key_features", [])
    pages_raw = intent.get("pages", ["home"])

    prompt = f"""Generate a layout contract for this product.

Product: {intent['product_name']} ({ptype})
Audience: {intent['target_audience']}
Features: {', '.join(features)}
Pages requested: {', '.join(pages_raw)}
Complexity: {intent.get('complexity', 'medium')}
Default components for {ptype}: {', '.join(defaults)}

Return ONLY valid JSON:
{{
  "layout_pattern": "single-page|multi-page|dashboard-app",
  "pages": [
    {{
      "name":       "Home",
      "type":       "landing|dashboard|auth|detail|list",
      "route":      "/",
      "priority":   1,
      "sections":   ["Navbar", "Hero", "Features", "Footer"],
      "components": ["navbar", "hero", "cards", "footer"]
    }}
  ],
  "global_components": ["navbar", "footer"]
}}

Rules:
- simple → max 3 pages, medium → max 5, complex → max 7
- components must come from: navbar, hero, cards, sidebar, tables, forms, footer, animations, effects
- always include at least one page with priority 1"""

    raw    = ollama(prompt, system=SYSTEM, label="Building layout contract")
    parsed = extract_json(raw)

    if not parsed or not parsed.get("pages"):
        return {
            "layout_pattern": "single-page",
            "pages": [{
                "name":       "Home",
                "type":       ptype,
                "route":      "/",
                "priority":   1,
                "sections":   ["Navbar", "Hero", "Features", "Footer"],
                "components": defaults,
            }],
            "global_components": ["navbar", "footer"],
        }

    return parsed
