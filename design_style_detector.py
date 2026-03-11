"""design_style_detector.py — Design style detection and LLM instruction generation."""

DESIGN_STYLES = {
    "glassmorphism": [
        "glass", "glassmorphism", "frosted", "frosted glass", "blur card",
        "backdrop blur", "translucent", "frosted ui", "glass card",
        "glass panel", "crystal ui"
    ],
    "neobrutalism": [
        "neobrutalism", "neo brutalism", "neo-brutalism", "brutalist",
        "bold borders", "raw design", "brutal ui", "thick border",
        "offset shadow", "hard shadow", "flat brutal", "chunky"
    ],
    "neumorphism": [
        "neumorphism", "neumorphic", "soft ui", "soft shadow",
        "embossed", "debossed", "clay ui", "inset shadow",
        "pressed button", "extruded"
    ],
    "dark_mode": [
        "dark mode", "dark ui", "dark theme", "night mode",
        "dark minimal", "carbon ui", "obsidian", "dark dashboard"
    ],
    "aurora": [
        "aurora", "aurora borealis", "gradient glow", "northern lights ui",
        "aurora gradient", "neon aurora", "plasma gradient"
    ],
    "cyberpunk": [
        "cyberpunk", "cyber", "neon glow", "dystopian", "terminal green",
        "matrix", "glitch ui", "neon grid", "hacker aesthetic", "synthwave dark"
    ],
    "bento": [
        "bento", "bento grid", "bento box", "modular grid", "bento layout",
        "bento cards", "asymmetric grid", "mosaic layout"
    ],
    "retro_80s": [
        "retro", "80s", "synthwave", "vaporwave", "retrowave", "neon retro",
        "miami vice", "outrun", "retroui", "crt screen", "scanlines"
    ],
    "minimalist": [
        "minimalist", "minimal", "clean ui", "whitespace",
        "less is more", "zen ui", "swiss design", "ultra clean"
    ],
    "material": [
        "material design", "material ui", "google design",
        "material you", "elevation shadow", "ripple effect"
    ],
    "claymorphism": [
        "claymorphism", "clay", "3d clay", "puffy ui", "inflated",
        "blob ui", "soft 3d", "clay card"
    ],
    "skeuomorphism": [
        "skeuomorphism", "realistic ui", "texture ui",
        "leather ui", "wood texture", "tactile design"
    ],
    "neon_glow": [
        "neon", "neon glow", "glow ui", "led ui", "electric glow",
        "luminous", "phosphor", "laser ui"
    ],
    "gradient_mesh": [
        "mesh gradient", "gradient mesh", "fluid gradient",
        "organic gradient", "gradient blob", "noise gradient"
    ],
    "monochrome": [
        "monochrome", "black and white ui", "grayscale ui",
        "single color", "tonal design", "achromatic"
    ],
    "corporate": [
        "corporate", "professional", "saas ui", "enterprise ui",
        "business clean", "b2b design", "dashboard clean"
    ],
    "futuristic": [
        "futuristic", "sci-fi ui", "space ui", "tech ui",
        "aerospace", "holographic", "hud interface", "heads up display"
    ],
    "organic": [
        "organic", "natural", "earthy", "biomorphic", "botanical ui",
        "nature inspired", "hand crafted feel"
    ],
    "pixelart": [
        "pixel art", "pixelated", "8bit", "8-bit", "retro pixel",
        "chiptune ui", "sprite ui", "pixelcraft"
    ],
    "y2k": [
        "y2k", "year 2000", "early internet", "chrome ui", "bubble ui",
        "iridescent", "holographic chrome", "cd aesthetic"
    ],
    "Memphis": [
        "memphis", "memphis design", "80s shapes", "geometric pattern",
        "squiggles", "bold geometry", "postmodern design"
    ],
    "Swiss": [
        "swiss", "swiss design", "international style", "helvetica",
        "grid based", "typographic layout", "modernist grid"
    ],
    "Japandi": [
        "japandi", "wabi sabi", "japanese minimal", "scandinavian minimal",
        "warm minimal", "neutral tones", "zen minimal"
    ],
    "cottagecore": [
        "cottagecore", "cozy ui", "warm ui", "botanical", "floral ui",
        "soft pastel", "handwritten font", "illustrated ui"
    ],
    "dopamine": [
        "dopamine design", "dopamine ui", "maximalist", "candy colors",
        "bold color", "vibrant", "joyful ui", "playful ui", "fun design"
    ]
}

STYLE_INSTRUCTIONS = {
    "glassmorphism": "Use bg-white/10 backdrop-blur-md border border-white/20. Apply subtle inner glow with shadow-inner. Layer translucent panels over gradient backgrounds. Avoid solid opaque backgrounds.",
    "neobrutalism": "Use border-2 border-black with translate-x-1 translate-y-1 shadow effects. Apply bg-yellow-300 or bg-lime-400 accent fills. Use font-black and uppercase text. Avoid rounded corners and subtle shadows.",
    "neumorphism": "Use soft box-shadows (e.g., shadow-[20px_20px_60px_#bebebe,-20px_-20px_60px_#ffffff]). Apply subtle gradients for convex/concave effects. Use rounded corners (rounded-3xl). Avoid high-contrast borders.",
    "dark_mode": "Use deep charcoal or slate backgrounds (bg-zinc-950). Apply subtle border-white/10 to define elements. Use dim gray for secondary text. Avoid pure black #000 backgrounds unless for contrast.",
    "aurora": "Use vibrant, swirling gradients (e.g., bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500). Apply soft glow effects. Use translucent cards over these backgrounds. Avoid flat, solid colors.",
    "cyberpunk": "Use neon green, cyan, and magenta accents over dark backgrounds. Apply glow-effects and grid-line backgrounds. Use monospaced fonts and 'glitch' styling elements. Avoid organic, soft shapes.",
    "bento": "Use grid layouts with asymmetric spans via col-span-2 row-span-2. Mix card sizes for visual hierarchy. Apply subtle border and rounded-2xl. Avoid equal-sized uniform grids.",
    "retro_80s": "Use scanlines, CRT effects, and vibrant neon pink/cyan. Apply synthwave-style gradients. Use bold, retro typography and pixel-deco. Avoid modern-minimalist aesthetics.",
    "minimalist": "Use maximum whitespace and very subtle borders. Apply clean, sans-serif typography (e.g., font-sans). Focus on content hierarchy without decorative elements. Avoid gradients and complex shadows.",
    "material": "Use elevation-based shadows (e.g., shadow-md). Apply ripple effects and Google-style 'Material You' color schemes. Use rounded-xl and consistent padding. Avoid flat designs without depth.",
    "claymorphism": "Use puffy, 3D-looking cards with large border-radius (rounded-[3rem]). Apply multiple inner shadows for volume. Use soft, saturated colors. Avoid sharp corners and flat shapes.",
    "skeuomorphism": "Use realistic textures (e.g., wood, leather, paper). Apply tactical lighting and realistic shadows. Focus on physical-world analogs for UI elements. Avoid flat, abstract vectors.",
    "neon_glow": "Use strong drop-shadow-neon or glow-blue-500. Apply luminous border effects. Use high-saturation colors against dark backgrounds for maximum pop. Avoid washed-out colors.",
    "gradient_mesh": "Use complex, fluid mesh gradients as backgrounds. Apply organic shapes with varying opacity. Transitions should be smooth and multi-color. Avoid linear or radial-strict gradients.",
    "monochrome": "Use only shades of white, gray, and black. Focus on texture, weight, and typography to create hierarchy. Apply high-contrast elements. Avoid using any hue-based colors.",
    "corporate": "Use professional blue-and-white palettes. Apply clean, standard layouts with clear data presentation. Use consistent iconography and rounded-md. Avoid experimental or loud designs.",
    "futuristic": "Use holographic panels and HUD-style data interfaces. Apply tech-grid overlays and sci-fi glowing lines. Use high-tech fonts and aerospace-inspired icons. Avoid traditional paper-like layouts.",
    "organic": "Use biomorphic shapes and earthy tones (green, brown, beige). Apply natural curves rather than straight lines. Use grainy textures or paper-like filters. Avoid mechanical, rigid grids.",
    "pixelart": "Use low-resolution pixelated aesthetics and 8-bit color scales. Apply blocky borders and sprite-based icons. Use fonts that look like they belong on a retro console. Avoid smooth anti-aliased curves.",
    "y2k": "Use chrome, iridescent, and silver textures. Apply bubble typography and early internet icons/graphics. Use translucent plastic effects (e.g., iMac G3 style). Avoid modern flat professional looks.",
    "Memphis": "Use squiggles, triangles, and dots in geometric patterns. Apply bold, contrasting colors like yellow and magenta. Focus on playful, asymmetrical compositions. Avoid rigid, corporate grids.",
    "Swiss": "Use a strict grid system and Helvetica-like typography. Apply high-contrast text and asymmetric layouts. Focus on functionalism and clarity. Avoid expressive decorations.",
    "Japandi": "Use a mix of Japanese 'wabi-sabi' and Scandinavian minimalism. Apply light wood textures and muted, warm tones. Use clean lines and natural materials. Avoid clutter and loud colors.",
    "cottagecore": "Use cozy, floral, and vintage-illustrated elements. Apply warm, soft pastel palettes and handwritten typography. Focus on a handmade, pastoral feel. Avoid high-tech, sleek surfaces.",
    "dopamine": "Use high-energy, candy-color palettes. Apply playful shapes and maximalist layouts. The UI should feel joyful and vibrant. Avoid dull, muted colors and overly serious layouts."
}

def detect_styles(prd_text: str) -> list[str]:
    """Detects design styles from PRD text using keyword matching."""
    prd_lower = prd_text.lower()
    matched_styles = []
    
    for style, keywords in DESIGN_STYLES.items():
        if any(kw in prd_lower for kw in keywords):
            matched_styles.append(style)
            
    return matched_styles if matched_styles else ["minimalist"]

def get_style_retrieval_filter(styles: list[str]) -> list[str]:
    """Returns list of category strings from WHOLE_FILE_ROUTES to prioritize."""
    categories = set()
    
    for style in styles:
        if style in ["glassmorphism", "neobrutalism", "neumorphism", "aurora", "cyberpunk", "neon_glow"]:
            categories.update(["components", "effects"])
        elif style in ["retro_80s", "y2k", "Memphis", "pixelart"]:
            categories.update(["components", "animations"])
        elif style in ["bento", "material", "corporate", "Swiss"]:
            categories.update(["components", "layouts"])
        elif style in ["minimalist", "Japandi", "organic", "cottagecore", "monochrome"]:
            categories.update(["components"])
        elif style in ["dopamine", "gradient_mesh", "futuristic"]:
            categories.update(["components", "effects", "animations"])
        else:
            categories.add("components")
            
    return list(categories)

def build_style_context_prompt(styles: list[str]) -> str:
    """Returns a dense instructional paragraph for the LLM based on detected styles."""
    instructions = [STYLE_INSTRUCTIONS.get(style, "") for style in styles if style in STYLE_INSTRUCTIONS]
    
    if not instructions:
        instructions = [STYLE_INSTRUCTIONS["minimalist"]]
        
    prompt = " ".join(instructions)
    return f"DESIGN STYLE INSTRUCTIONS: {prompt}"

if __name__ == "__main__":
    prd = input("Paste PRD: ")
    styles = detect_styles(prd)
    print(f"\nDetected: {styles}")
    print(f"\nPrompt injection:\n{build_style_context_prompt(styles)}")
