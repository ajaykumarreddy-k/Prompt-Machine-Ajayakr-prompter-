"""stage5_design_system.py — Palette selection + full Tailwind design tokens."""

from ollama import ollama, extract_json

SYSTEM = "You are a design system expert. Select palettes and design tokens. Respond with valid JSON only."

# ── PALETTES ──────────────────────────────────────────────────────────────────
# card_bg = explicit card background token (never the secondary color which may be dark)
PALETTES: dict[str, dict] = {
    "P-1": {
        "name": "SaaS Architecture",
        "primary": "blue-600",   "secondary": "slate-800",
        "accent":  "indigo-500", "bg": "slate-50",    "text": "slate-900",
        "card_bg": "white",      "border": "slate-200",
        "dark": False,
    },
    "P-2": {
        "name": "Neo-Brutalist",
        "primary": "yellow-400", "secondary": "neutral-950",
        "accent":  "pink-500",   "bg": "white",       "text": "black",
        "card_bg": "neutral-50", "border": "neutral-200",
        "dark": False,
    },
    "P-3": {
        "name": "Organic Utility",
        "primary": "emerald-600","secondary": "stone-700",
        "accent":  "teal-500",   "bg": "neutral-50",  "text": "stone-800",
        "card_bg": "white",      "border": "stone-200",
        "dark": False,
    },
    "P-4": {
        "name": "Midnight Dev",
        "primary": "violet-500", "secondary": "slate-900",
        "accent":  "cyan-400",   "bg": "slate-950",   "text": "slate-200",
        "card_bg": "slate-900",  "border": "slate-800",
        "dark": True,
    },
    "P-5": {
        "name": "Minimal Editorial",
        "primary": "zinc-900",   "secondary": "zinc-500",
        "accent":  "red-500",    "bg": "white",       "text": "zinc-900",
        "card_bg": "zinc-50",    "border": "zinc-200",
        "dark": False,
    },
}


def _rule_based_pick(intent: dict) -> str:
    hint = " ".join([
        intent.get("palette_hint", ""),
        intent.get("tone", ""),
        *intent.get("style_keywords", []),
    ]).lower()

    if any(k in hint for k in ["dark", "dev", "cyber", "web3", "ai", "violet", "purple", "night"]):
        return "P-4"
    if any(k in hint for k in ["green", "nature", "health", "organic", "eco", "emerald"]):
        return "P-3"
    if any(k in hint for k in ["brutal", "bold", "yellow", "pop", "edgy", "loud"]):
        return "P-2"
    if any(k in hint for k in ["minimal", "editorial", "clean", "type", "read", "white", "simple"]):
        return "P-5"
    return "P-1"


def inject_design_system(intent: dict, palette_override: str | None = None) -> dict:
    if palette_override and palette_override in PALETTES:
        pid = palette_override
        print(f"\033[90m  Palette override: {pid}\033[0m")
    else:
        pid = _rule_based_pick(intent)

    p = PALETTES[pid]

    # Ask LLM for effect + animation choices
    prompt = f"""Choose visual effects and animations for this product UI.

Product: {intent['product_name']}  ({intent['product_type']})
Tone: {intent.get('tone', 'professional')}
Palette: {p['name']}  dark={p['dark']}
UI interactions needed: {', '.join(intent.get('ui_interactions', []))}

Return ONLY valid JSON:
{{
  "visual_effect":    "corner-blur|gradient-mesh|none",
  "effect_placement": "top-right|top-left|bottom-right|bottom-left",
  "text_animation":   "typewriter|fade-in|slide-up|gradient-text|none",
  "border_radius":    "rounded-xl|rounded-lg|rounded-2xl",
  "shadow_style":     "shadow-sm|shadow-md|shadow-lg|shadow-none",
  "font_pair":        "Inter|Geist|Plus Jakarta Sans"
}}"""

    raw    = ollama(prompt, system=SYSTEM, label="Selecting design system")
    extras = extract_json(raw) or {}

    visual_effect    = extras.get("visual_effect",    "corner-blur" if p["dark"] else "none")
    effect_placement = extras.get("effect_placement", "top-right")
    text_animation   = extras.get("text_animation",   "fade-in")
    border_radius    = extras.get("border_radius",     "rounded-xl")
    shadow_style     = extras.get("shadow_style",      "shadow-sm")
    font_pair        = extras.get("font_pair",          "Inter")

    primary_base = p["primary"].split("-")[0]
    accent_base  = p["accent"].split("-")[0]

    tailwind = {
        "container":      "max-w-7xl mx-auto px-6",
        "section":        "py-16 md:py-24",
        # card uses card_bg (always a safe light/dark surface, never secondary)
        "card":           f"bg-{p['card_bg']} {border_radius} border border-{p['border']} {shadow_style} p-6",
        "btn_primary":    f"bg-{p['primary']} hover:opacity-90 text-white px-6 py-3 {border_radius} font-semibold transition-all",
        "btn_secondary":  f"border border-{primary_base}-300 text-{primary_base}-700 px-6 py-3 {border_radius} hover:bg-{primary_base}-50 transition-all",
        "text_heading":   f"text-{p['text']}",
        "text_body":      f"text-{p['text']} opacity-70",
        "bg_page":        f"bg-{p['bg']}",
        "accent_text":    f"text-{p['accent']}",
        "accent_bg":      f"bg-{accent_base}-500/10",
        "input":          f"w-full px-4 py-3 {border_radius} border border-{p['border']} bg-{p['card_bg']} text-{p['text']} focus:outline-none focus:ring-2 focus:ring-{primary_base}-500",
    }

    return {
        "palette_id":       pid,
        "palette":          p,
        "tailwind":         tailwind,
        "visual_effect":    visual_effect,
        "effect_placement": effect_placement,
        "text_animation":   text_animation,
        "border_radius":    border_radius,
        "shadow_style":     shadow_style,
        "font_pair":        font_pair,
        "dark_mode":        p["dark"],
    }
