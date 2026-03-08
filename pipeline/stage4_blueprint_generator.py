"""stage4_blueprint_generator.py — Enhances the layout tree with state contracts and design tokens."""

from ollama import ollama, extract_json

SYSTEM = """You are a senior React architect attaching state and prop contracts to an AST blueprint.
Respond with valid JSON only."""

def generate_blueprint_ast(intent: dict, planned_layout: dict) -> dict:
    """Enhance the nested component tree with explicit React state/prop rules."""
    
    prompt = f"""Here is a structural layout for a {intent['product_type']} application:

{planned_layout}

Modify this JSON to explicitly attach a 'state_contract' object for Pages and add 'props' arrays and 'responsibilities' arrays for individual components.
 
Rules for state_contract:
- If the domain is 'quiz', use keys like 'score', 'currentQuestion'.
- If the domain is 'dashboard', use keys related to 'data', 'filters', 'activeId'.
- If the domain is 'marketing', state_contract is usually empty {{}}.
 
Rules for props:
- Components should receive data they need to display (e.g. 'title', 'items', 'stats').
 
Rules for responsibilities:
- Be specific about what the component does based on the product name: {intent['product_name']}.
 
Output format expected:
{{
  "pages": [
    {{
      "name": "PageName",
      "route": "/route",
      "state_contract": {{ ... }},
      "layout": {{
        "type": "PageLayout",
        "children": [
           {{ 
             "type": "CompName", 
             "props": [...], 
             "responsibilities": [...] 
           }}
        ]
      }}
    }}
  ]
}}
 
Return the FULL ENHANCED JSON. Do not omit the layout structure. Do NOT use quiz examples if the domain is not quiz. Preserve all existing fields like 'type' and 'original_name'.
"""

    raw = ollama(prompt, system=SYSTEM, label="Generating Component Contracts")
    blueprint = extract_json(raw)
    
    if not blueprint:
        print("\033[33m⚠  Blueprint Generation failed — falling back to plain layout\033[0m")
        return planned_layout
        
    return blueprint
