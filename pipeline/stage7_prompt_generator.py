"""stage7_prompt_generator.py — Build high-precision AST-centric UI prompt with Style Injection."""

import json
import copy

def build_visual_hierarchy(blueprint_ast: dict, intent: dict) -> dict:
    landing = next(
        (p for p in blueprint_ast.get("pages", []) if p["name"] == "Landing"),
        blueprint_ast.get("pages", [{}])[0] if blueprint_ast.get("pages") else {}
    )
    children = landing.get("layout", {}).get("children", [])

    SKIP = {"Navbar", "Footer", "NavbarSection", "FooterSection"}
    content_children = [c for c in children if c["type"] not in SKIP]

    primary = content_children[0]["type"] if content_children else "HeroSection"
    secondary = [c["type"] for c in content_children[1:-1]] if len(content_children) > 2 else [c["type"] for c in content_children[1:]]
    support = ["Navbar", "Footer"] + [c["type"] for c in children if "CTA" in c.get("type", "")]
    cta = next((c["type"] for c in children if "CTA" in c.get("type", "") or "Newsletter" in c.get("type", "")), "")
    focal_point = f"{primary} with {intent.get('key_features', [''])[0]}" if intent.get("key_features") else primary
    scroll_flow = "single-page linear scroll" if len(blueprint_ast.get("pages", [])) == 1 else "multi-page with anchor navigation"

    return {
        "primary": primary,
        "secondary": secondary,
        "support": support,
        "cta": cta,
        "focal_point": focal_point,
        "scroll_flow": scroll_flow
    }

def override_design_from_styles(design: dict, detected_styles: list[str]) -> dict:
    """Overrides palette colors AND tailwind tokens based on detected_styles."""
    if not detected_styles:
        return design

    import copy
    design = copy.deepcopy(design)
    tw = design["tailwind"]
    p  = design["palette"]

    if "glassmorphism" in detected_styles:
        tw["card"]    = "bg-white/10 backdrop-blur-md border border-white/20 rounded-xl shadow-lg p-6"
        tw["bg_page"] = "bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 min-h-screen text-white"
        p["primary"]  = "white"
        p["accent"]   = "violet-400"
    elif "dark_mode" in detected_styles:
        tw["card"]    = "bg-gray-900 border border-gray-700 rounded-lg shadow-lg p-6"
        tw["bg_page"] = "bg-gray-950 text-white min-h-screen"
        p["primary"]  = "gray-950"
        p["accent"]   = "violet-500"
    elif "futuristic" in detected_styles:
        tw["card"]    = "bg-slate-900 border border-cyan-400/30 rounded-lg shadow-cyan-900/20 shadow-lg p-6"
        tw["bg_page"] = "bg-slate-950 text-white min-h-screen"
        p["primary"]  = "slate-950"
        p["accent"]   = "cyan-400"
    elif "neobrutalism" in detected_styles:
        tw["card"]    = "bg-white border-2 border-black shadow-[4px_4px_0px_0px_black] rounded-none p-6"
        tw["bg_page"] = "bg-yellow-50 min-h-screen"
        p["primary"]  = "yellow-300"
        p["accent"]   = "black"
    elif "aurora" in detected_styles:
        tw["card"]    = "bg-white/5 backdrop-blur-sm border border-purple-500/20 rounded-xl p-6"
        tw["bg_page"] = "bg-gradient-to-br from-indigo-950 via-purple-950 to-slate-950 min-h-screen"
        p["primary"]  = "indigo-950"
        p["accent"]   = "purple-400"
    elif "cyberpunk" in detected_styles:
        tw["card"]    = "bg-black border border-green-400/40 rounded-none p-6"
        tw["bg_page"] = "bg-black text-green-400 min-h-screen"
        p["primary"]  = "black"
        p["accent"]   = "green-400"
    elif "neumorphism" in detected_styles:
        tw["card"]    = "bg-gray-200 rounded-xl shadow-[6px_6px_12px_#b8b9be,-6px_-6px_12px_#ffffff] p-6"
        tw["bg_page"] = "bg-gray-200 min-h-screen"
        p["primary"]  = "gray-200"
        p["accent"]   = "blue-500"

    return design


def generate_prompt(
    intent: dict,
    blueprint_ast: dict,
    kb_context: str,
    design: dict,
    style_prompt: str = "",
    detected_styles: list[str] = None
) -> str:
    """Builds the final implementation contract for the LLM."""
    detected_styles = detected_styles or []
    
    # Apply Overrides (Fix 4)
    design = override_design_from_styles(design, detected_styles)
    # Compute Visual Hierarchy (Fix 6)
    visual_hierarchy = build_visual_hierarchy(blueprint_ast, intent)
    blueprint_ast["visual_hierarchy"] = visual_hierarchy
    
    p = design["palette"]
    tw = design["tailwind"]
    
    # Extract component names for quick reference
    all_components = []
    for page in blueprint_ast.get('pages', []):
        for comp in page.get('layout', {}).get('children', []):
            all_components.append(comp.get('type', 'Unknown'))
    unique_components = sorted(list(set(all_components)))

    # Build Mandatory Tokens dynamically
    mandatory_tokens = ["max-w-7xl", "px-6", "py-16"]
    if "glassmorphism" in detected_styles or "neumorphism" in detected_styles or "claymorphism" in detected_styles:
        mandatory_tokens.append("rounded-xl")
    else:
        mandatory_tokens.append("rounded-lg")
    
    if "dark_mode" in detected_styles:
        mandatory_tokens.append("bg-gray-950")
    else:
        mandatory_tokens.append("bg-zinc-50")

    # Style-specific allowances in the prompt instructions (Fix 1 from previous flaw overhaul)
    style_overrides = f"""
### STYLE OVERRIDE — HIGHEST PRIORITY
The following style instructions OVERRIDE any default tokens.
DETECTED STYLES: {", ".join(detected_styles)}

{style_prompt}

CRITICAL: If a style like glassmorphism or neobrutalism is active, do NOT use generic white cards. 
Use the 'card' token from the design system which has been pre-configured for this style.
"""

    return f"""### AST-CENTRIC IMPLEMENTATION CONTRACT

This application MUST be built exactly following the provided JSON AST.

### 1. AST LAYOUT INSTRUCTIONS
{json.dumps(blueprint_ast, indent=2)}

### 2. VISUAL HIERARCHY & FLOW
- **Primary Focus**: {visual_hierarchy['primary']}
- **Secondary Alignment**: {", ".join(visual_hierarchy.get('secondary', []))}
- **Support Layer**: {", ".join(visual_hierarchy.get('support', []))}
- **CTA**: {visual_hierarchy.get('cta', 'None')}
- **Focal Point**: {visual_hierarchy.get('focal_point', 'Center')}
- **Scroll Strategy**: {visual_hierarchy.get('scroll_flow', 'Linear')}

### 3. COMPONENT RESPONSIBILITIES (EXTRACTED)
{chr(10).join([f"- {c['type']}: {', '.join(c.get('responsibilities', []))}" for p in blueprint_ast.get('pages', []) for c in p['layout']['children']])}

### 4. DESIGN SYSTEM (STRICT ENFORCEMENT)
- **Palette**: {p.get('name', 'Custom')}
- **Primary**: {p.get('primary', 'zinc-900')}
- **Secondary**: {p.get('secondary', 'zinc-500')}
- **Accent**: {p.get('accent', 'blue-500')}
- **Mandatory Tokens**: {", ".join([f"`{t}`" for t in mandatory_tokens])}
- **FORBIDDEN (REJECT CODE IF PRESENT)**: {'' if any(s in detected_styles for s in ['futuristic', 'aurora', 'cyberpunk', 'retro_80s', 'glassmorphism']) else '`bg-gradient`,'} undefined custom class patterns.

{style_overrides}

### 5. ROUTING & FOLDER CONTRACT
- **Engine**: `react-router-dom`
- **Structure**: 
  - `src/pages/`: {", ".join([p.get('name', 'Page') for p in blueprint_ast.get('pages', [])])}
  - `src/components/`: {", ".join(unique_components)}
  - `src/App.jsx`: Routing definitions for {", ".join([p.get('route', '/') for p in blueprint_ast.get('pages', [])])}

### 6. KNOWLEDGE BASE INTELLIGENCE
{kb_context}

### FINAL INSTRUCTION:
Generate clean, modular React components. Every AST node MUST have a corresponding file. No monolithic files. No arbitrary wrappers. Direct Tailwind injection.
"""
