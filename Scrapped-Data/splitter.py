"""
AKR Scraper Data Splitter
Reads all scraped .txt files and splits them into 13 focused files
ready to paste into Antigravity one at a time.

Run from inside your Scrapped-Data folder:
    python splitter.py

Outputs 13 files into a new folder: split-output/
"""

import os
import re
from pathlib import Path

# ── OUTPUT FOLDER ──────────────────────────────────────────────────────────────
OUTPUT_DIR = Path("split-output")
OUTPUT_DIR.mkdir(exist_ok=True)

# ── FILE ROUTING TABLE ─────────────────────────────────────────────────────────
# Each key = output filename, value = keywords that route an entry there
ROUTING = {
    "navbar":       ["nav", "navbar", "navigation", "header", "menu-bar", "topbar", "top-bar"],
    "hero":         ["hero", "banner", "jumbotron", "landing-hero", "headline", "cta-section"],
    "cards":        ["card", "cards", "tile", "feature-card", "stat-card", "metric", "pricing-card", "profile-card", "product-card"],
    "sidebar":      ["sidebar", "side-bar", "drawer", "side-panel", "side-nav", "sidenav"],
    "tables":       ["table", "data-table", "datagrid", "grid", "list-view", "data-grid"],
    "forms":        ["form", "input", "login", "auth", "register", "signup", "sign-up", "contact-form", "newsletter", "field"],
    "footer":       ["footer", "bottom-bar", "site-footer"],
    "dashboard":    ["dashboard", "admin", "panel", "app-shell", "control-panel", "workspace"],
    "landing":      ["landing", "landing-page", "homepage", "home-page", "marketing", "saas-page"],
    "palettes":     ["color", "colour", "palette", "theme", "token", "variable", "css-var", "--primary", "--accent", "--bg"],
    "effects":      ["blur", "glow", "gradient", "overlay", "shadow", "glassmorphism", "glass", "noise", "mesh", "aurora", "spotlight"],
    "animations":   ["animate", "animation", "transition", "fade", "slide", "typewriter", "typing", "scroll-animation", "motion", "keyframe", "framer"],
    "prompts":      ["prompt", "build a", "create a", "design a", "template", "v0", "bolt", "lovable"],
}

# ── SOURCE FILES AND THEIR BEST CATEGORY HINTS ────────────────────────────────
# Files that are entirely one category — route ALL their content there directly
WHOLE_FILE_ROUTES = {
    "animejs.txt":           "animations",
    "scroll-animation.txt":  "animations",
    "prompts.txt":           "prompts",
    "templates.txt":         "prompts",
    "v0dev-templates.txt":   "prompts",
    "olayouts.txt":          "landing",
    "www.landingfolio.com.txt": "landing",
    "dribbble.com.txt":      "landing",
    "lightwind.txt":         "cards",
    "lightwindwebsite.txt":  "cards",
    "floatui.com.txt":       "cards",
    "meterialtheme.txt":     "palettes",
    "metrialtheme.txt":      "palettes",
}

# ── FILES TO SPLIT BY ENTRY (mixed content) ────────────────────────────────────
MIXED_FILES = [
    "uiverse.txt",
    "Reactbits.txt",
    "components_components.txt",
    "21dev.txt",
    "freefrontend.com.txt",
    "aceternityui.txt",
]

# ── BUCKETS ────────────────────────────────────────────────────────────────────
buckets = {key: [] for key in ROUTING.keys()}

def route_text(text: str) -> str:
    """Return the best bucket key for a block of text."""
    text_lower = text.lower()

    # Check routing keywords — score each bucket
    scores = {key: 0 for key in ROUTING}
    for key, keywords in ROUTING.items():
        for kw in keywords:
            if kw in text_lower:
                scores[key] += 1

    best = max(scores, key=lambda k: scores[k])
    if scores[best] == 0:
        return "cards"  # default fallback
    return best

def parse_entries(text: str) -> list[str]:
    """Split a file into individual component entries."""
    # Split on the entry separator line or on [N] markers
    entries = re.split(r'(?=^\[\d+\])', text, flags=re.MULTILINE)
    # Also split on the long dashed separator lines
    result = []
    for entry in entries:
        parts = re.split(r'─{20,}', entry)
        for part in parts:
            part = part.strip()
            if len(part) > 100:  # skip tiny noise fragments
                result.append(part)
    return result

# ── PROCESS WHOLE-FILE ROUTES ─────────────────────────────────────────────────
print("\n── Processing whole-file routes ──")
for filename, bucket_key in WHOLE_FILE_ROUTES.items():
    filepath = Path(filename)
    if not filepath.exists():
        print(f"  SKIP (not found): {filename}")
        continue
    content = filepath.read_text(encoding="utf-8", errors="ignore")
    buckets[bucket_key].append(f"\n\n{'='*60}\n SOURCE: {filename}\n{'='*60}\n")
    buckets[bucket_key].append(content)
    lines = content.count('\n')
    print(f"  {filename:35s} → {bucket_key:12s}  ({lines:,} lines)")

# ── PROCESS MIXED FILES ────────────────────────────────────────────────────────
print("\n── Processing mixed files (entry-by-entry routing) ──")
for filename in MIXED_FILES:
    filepath = Path(filename)
    if not filepath.exists():
        print(f"  SKIP (not found): {filename}")
        continue
    content = filepath.read_text(encoding="utf-8", errors="ignore")
    entries = parse_entries(content)
    routed = {}
    for entry in entries:
        key = route_text(entry)
        buckets[key].append(entry)
        routed[key] = routed.get(key, 0) + 1
    summary = ", ".join(f"{k}:{v}" for k, v in sorted(routed.items(), key=lambda x: -x[1]))
    print(f"  {filename:35s} → {len(entries):,} entries → {summary}")

# ── WRITE OUTPUT FILES ─────────────────────────────────────────────────────────
print("\n── Writing split-output/ files ──")

# Map bucket keys to the final knowledge base file names
KB_NAMES = {
    "navbar":     "components--navbar",
    "hero":       "components--hero",
    "cards":      "components--cards",
    "sidebar":    "components--sidebar",
    "tables":     "components--tables",
    "forms":      "components--forms",
    "footer":     "components--footer",
    "dashboard":  "layouts--dashboard",
    "landing":    "layouts--landing-page",
    "palettes":   "design--color-palettes",
    "effects":    "design--visual-effects",
    "animations": "design--text-animations",
    "prompts":    "prompts--prompt-templates",
}

total_written = 0
for key, name in KB_NAMES.items():
    chunks = buckets[key]
    if not chunks:
        print(f"  {name:40s}  EMPTY — no data routed here")
        continue

    combined = "\n\n".join(chunks)
    lines = combined.count('\n')
    out_path = OUTPUT_DIR / f"{name}.txt"
    out_path.write_text(combined, encoding="utf-8")
    size_kb = out_path.stat().st_size // 1024
    print(f"  {name:40s}  {lines:>7,} lines  {size_kb:>5} KB  → {out_path}")
    total_written += 1

# ── SUMMARY ────────────────────────────────────────────────────────────────────
print(f"\n✓ Done. {total_written}/13 files written to split-output/")
print(f"\nNext step:")
print(f"  cd split-output && ls -lh")
print(f"  Then paste each file + the Antigravity prompt into your chat one at a time.")
def main():
    # your entire script logic here
    pass


if __name__ == "__main__":
    main()