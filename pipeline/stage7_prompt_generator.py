"""stage7_prompt_generator.py — Build high-precision AST-centric UI prompt."""

import json

def generate_prompt(
    intent: dict,
    blueprint_ast: dict,
    kb_context: str,
    design: dict,
) -> str:
    p = design["palette"]
    
    # Extract component names for quick reference
    all_components = []
    for page in blueprint_ast.get('pages', []):
        for comp in page.get('layout', {}).get('children', []):
            all_components.append(comp.get('type', 'Unknown'))
    unique_components = sorted(list(set(all_components)))

    # Returning the RAW contract as requested by the user
    return f"""### AST-CENTRIC IMPLEMENTATION CONTRACT

This application MUST be built exactly following the provided JSON AST.

### 1. AST LAYOUT INSTRUCTIONS
{json.dumps(blueprint_ast, indent=2)}

### 2. COMPONENT RESPONSIBILITIES (EXTRACTED)
{chr(10).join([f"- {c['type']}: {', '.join(c.get('responsibilities', []))}" for p in blueprint_ast.get('pages', []) for c in p['layout']['children']])}

### 3. DESIGN SYSTEM (STRICT ENFORCEMENT)
- **Palette**: {p['name']}
- **Primary**: {p['primary']}
- **Secondary**: {p['secondary']}
- **Accent**: {p['accent']}
- **Mandatory Tokens**: `max-w-7xl`, `px-6`, `py-16`, `rounded-lg`, `bg-zinc-50`
- **FORBIDDEN (REJECT CODE IF PRESENT)**: `rounded-xl`, `container`, `bg-gradient`

### 4. ROUTING & FOLDER CONTRACT
- **Engine**: `react-router-dom`
- **Structure**: 
  - `src/pages/`: {", ".join([p['name'] for p in blueprint_ast.get('pages', [])])}
  - `src/components/`: {", ".join(unique_components)}
  - `src/App.jsx`: Routing definitions for {", ".join([p.get('route', '/') for p in blueprint_ast.get('pages', [])])}

### 5. KNOWLEDGE BASE INTELLIGENCE
{kb_context}

### FINAL INSTRUCTION:
Generate clean, modular React components. Every AST node MUST have a corresponding file. No monolithic files. No arbitrary wrappers. Direct Tailwind injection.
"""
