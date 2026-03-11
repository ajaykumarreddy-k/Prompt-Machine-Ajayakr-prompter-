"""stage10_blueprint_output.py — Render blueprint to terminal and save to disk."""

import json
from datetime import datetime
from pathlib import Path
import re

# ── ANSI COLOUR HELPERS ───────────────────────────────────────────────────────
class C:
    R  = "\033[0m"   ; B  = "\033[1m"   ; DIM = "\033[2m"
    CY = "\033[36m"  ; GR = "\033[32m"  ; YL  = "\033[33m"
    BL = "\033[34m"  ; MG = "\033[35m"  ; GY  = "\033[90m"
    WH = "\033[37m"

def _c(col: str, text: str) -> str:
    return f"{col}{text}{C.R}"

def _divider(char: str = "═", n: int = 62, col: str = C.MG) -> str:
    return _c(col, char * n)

def _section(title: str, num: str, col: str = C.CY) -> str:
    return (
        f"\n{_divider('─', 62, C.GY)}\n"
        f"  {_c(col, _c(C.B, f'{num} · {title}'))}\n"
        f"{_divider('─', 62, C.GY)}"
    )

def render_blueprint(blueprint: dict, verbose: bool = False) -> str:
    intent   = blueprint["intent"]
    layout   = blueprint.get("layout", {})
    ast      = blueprint.get("ast", {})
    hier     = ast.get("visual_hierarchy", {}) # FIX 6: Read from AST
    design   = blueprint.get("design", {})
    prompt   = blueprint["prompt"]
    code     = blueprint.get("code", "")
    p        = design.get("palette", {"name": "Custom", "primary": "N/A", "secondary": "N/A", "accent": "N/A"})
    tw       = design.get("tailwind", {})

    out: list[str] = []

    # ── HEADER ────────────────────────────────────────────────────────────────
    out.append(f"\n{_divider()}")
    out.append(_c(C.B, _c(C.MG, f"  ◈  FRONTEND BLUEPRINT — {intent['product_name'].upper()}  ◈")))
    out.append(_divider())

    # ── 01 PRODUCT SUMMARY ────────────────────────────────────────────────────
    out.append(_section("PRODUCT SUMMARY", "01", C.YL))
    out.append(f"  {_c(C.B,'Name:')}         {intent['product_name']}")
    out.append(f"  {_c(C.B,'Type:')}         {intent['product_type']}")
    out.append(f"  {_c(C.B,'Audience:')}     {intent['target_audience']}")
    out.append(f"  {_c(C.B,'Features:')}     {_c(C.GY, ' | '.join(intent.get('key_features', [])))}")

    # ── 02 PAGES & ROUTES ─────────────────────────────────────────────────────
    out.append(_section("PAGES & ROUTES", "02", C.CY))
    pages = ast.get("pages", [])
    for page in pages:
        name = _c(C.B, page.get("name", "Page"))
        rte  = _c(C.CY, page.get("route", "/"))
        out.append(f"  ○  {name}  →  {rte}")

    # ── 03 LAYOUT CONTRACT ────────────────────────────────────────────────────
    out.append(_section("LAYOUT CONTRACT", "03", C.CY))
    out.append(f"  {_c(C.B,'Pattern:')}  {'multi-page' if len(pages) > 1 else 'single-page'}")
    for page in pages:
        p_name = page.get("name")
        p_comps = [c["type"] for c in page.get("layout", {}).get("children", [])]
        out.append(f"  {_c(C.B, p_name + ':')}  {' → '.join(p_comps)}")

    # ── 04 VISUAL HIERARCHY ───────────────────────────────────────────────────
    out.append(_section("VISUAL HIERARCHY", "04", C.CY))
    out.append(f"  {_c(C.GR,'⬛ PRIMARY:')}     {hier.get('primary','')}")
    out.append(f"  {_c(C.YL,'▪ SECONDARY:')}   {', '.join(hier.get('secondary',[]))}")
    out.append(f"  {_c(C.GY,'· SUPPORT:')}     {', '.join(hier.get('support',[]))}")
    out.append(f"  {_c(C.B,'CTA:')}            {hier.get('cta','')}")
    out.append(f"  {_c(C.B,'Focal point:')}    {hier.get('focal_point','')}")
    out.append(f"  {_c(C.B,'Scroll flow:')}    {hier.get('scroll_flow','')}")

    # ── 05 DESIGN SYSTEM ──────────────────────────────────────────────────────
    out.append(_section("DESIGN SYSTEM", "05", C.CY))
    out.append(f"  {_c(C.B,'Palette:')}     {p.get('name')}")
    out.append(f"  {_c(C.B,'Colours:')}     primary {p.get('primary')}  ·  secondary {p.get('secondary')}  ·  accent {p.get('accent')}")
    out.append(f"  {_c(C.B,'Styles:')}      {', '.join(blueprint.get('detected_styles', []))}")
    out.append(f"\n  {_c(C.YL,'Tailwind tokens:')}")
    for k, v in tw.items():
        out.append(f"  {_c(C.GY, k + ':').ljust(20)} {v}")

    # ── 07 REFINED PROMPT ─────────────────────────────────────────────────────
    if verbose:
        out.append(_section("REFINED FRONTEND PROMPT", "07", C.GR))
        for line in prompt.splitlines():
            out.append(f"  {line}")

    # ── 08 GENERATED CODE (preview) ───────────────────────────────────────────
    if code:
        out.append(_section("GENERATED REACT CODE (preview)", "08", C.BL))
        lines = code.splitlines()
        for line in lines[:40]:
            out.append(f"  {_c(C.GY, line)}")
        if len(lines) > 40:
            out.append(_c(C.GY, f"  … {len(lines) - 40} more lines (see output/)"))

    # ── FOOTER ────────────────────────────────────────────────────────────────
    out.append(f"\n{_divider()}")
    out.append(_c(C.GR, _c(C.B, "  ✓  BLUEPRINT COMPLETE")))
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    out.append(_c(C.GY, f"  Prompt Machine v3.0  ·  {ts}"))
    out.append(_divider())

    return "\n".join(out)

def save_blueprint(blueprint: dict, output_dir: str = "output") -> None:
    slug = blueprint["intent"]["product_name"].lower().replace(" ", "-")
    out  = Path(output_dir) / slug
    out.mkdir(parents=True, exist_ok=True)

    # Save blueprint.json
    (out / "blueprint.json").write_text(json.dumps(blueprint, indent=2))

    # Save prompt.md
    (out / "prompt.md").write_text(f"# {blueprint['intent']['product_name']} prompt\n\n{blueprint['prompt']}")

    # full generated code parsing
    if blueprint.get("code"):
        code = blueprint["code"]
        # Match <file path="...">...</file>
        file_blocks = re.findall(r'<file\s+path="(.*?)">(.*?)</file>', code, re.DOTALL)
        
        for path, content in file_blocks:
            path = path.strip().lstrip("/")
            file_path = out / path
            file_path.parent.mkdir(parents=True, exist_ok=True)
            # Remove markdown fences if present inside block
            clean_content = re.sub(r"```[\w]*\n?", "", content)
            clean_content = clean_content.replace("```", "").strip()
            file_path.write_text(clean_content + "\n")

    print(f"\n\033[32m✓  Saved to {out}/\033[0m")
