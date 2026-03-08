"""stage10_blueprint_output.py — Render blueprint to terminal and save to disk."""

import json
from datetime import datetime
from pathlib import Path

OUTPUT_DIR = Path("output")


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


# ── MAIN RENDER ───────────────────────────────────────────────────────────────
def render_blueprint(blueprint: dict, verbose: bool = False) -> str:
    intent   = blueprint["intent"]
    layout   = blueprint.get("layout", {})
    hier     = blueprint.get("hierarchy", {})
    comps    = blueprint.get("components", {})
    design   = blueprint.get("design", {})
    skeleton = blueprint.get("skeletons", {})
    prompt   = blueprint["prompt"]
    code     = blueprint.get("code", "")
    p        = design["palette"]
    tw       = design["tailwind"]

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
    out.append(f"  {_c(C.B,'Tone:')}         {intent.get('tone','professional')}")
    out.append(f"  {_c(C.B,'Industry:')}     {intent.get('industry','technology')}")
    out.append(f"  {_c(C.B,'Complexity:')}   {intent.get('complexity','medium')}")
    feats = "  |  ".join(intent.get("key_features", []))
    out.append(f"  {_c(C.B,'Features:')}     {_c(C.GY, feats)}")
    if intent.get("custom_components"):
        cc = ", ".join(intent["custom_components"])
        out.append(f"  {_c(C.B,'Components:')}   {_c(C.GY, cc)}")
    if intent.get("ui_interactions"):
        ui = ", ".join(intent["ui_interactions"])
        out.append(f"  {_c(C.B,'Interactions:')} {_c(C.GY, ui)}")

    # ── 02 PAGES & ROUTES ─────────────────────────────────────────────────────
    out.append(_section("PAGES & ROUTES", "02", C.CY))
    for page in layout["pages"]:
        star = _c(C.GR, "★") if page.get("priority") == 1 else _c(C.GY, "○")
        name = _c(C.B, page.get("name", "Page"))
        typ  = _c(C.GY, f"({page.get('type', 'page')})")
        rte  = _c(C.CY, page.get("route", "/"))
        out.append(f"  {star}  {name} {typ}  →  {rte}")
        if verbose:
            out.append(f"     sections: {_c(C.GY, ' → '.join(page.get('sections', [])))}")

    # ── 03 LAYOUT CONTRACT ────────────────────────────────────────────────────
    out.append(_section("LAYOUT CONTRACT", "03", C.CY))
    out.append(f"  {_c(C.B,'Pattern:')}  {layout.get('layout_pattern','single-page')}")
    out.append(f"  {_c(C.B,'Global:')}   {', '.join(layout.get('global_components',[]))}")
    out.append(f"\n  {_c(C.YL,'Component map:')}")
    for pname, pcomps in comps.get("component_map", {}).items():
        page_obj = next((pg for pg in layout.get("pages", []) if pg.get("name") == pname), {})
        custom = page_obj.get("custom_components", [])
        comps_str = " → ".join(pcomps)
        line = f"  {_c(C.B, pname + ':')}  {comps_str}"
        if custom:
            custom_str = ", ".join(custom)
            line += _c(C.GY, f"  +custom: {custom_str}")
        out.append(line)

    # ── 04 VISUAL HIERARCHY ───────────────────────────────────────────────────
    out.append(_section("VISUAL HIERARCHY", "04", C.CY))
    out.append(f"  {_c(C.GR,'⬛ PRIMARY:')}     {hier.get('primary_section','')}")
    out.append(f"  {_c(C.YL,'▪ SECONDARY:')}   {', '.join(hier.get('secondary_sections',[]))}")
    out.append(f"  {_c(C.GY,'· SUPPORT:')}     {', '.join(hier.get('supporting_sections',[]))}")
    out.append(f"  {_c(C.B,'CTA:')}            \"{hier.get('cta_text','')}\"")
    out.append(f"  {_c(C.B,'Focal point:')}    {hier.get('focal_point','')}")
    out.append(f"  {_c(C.B,'Scroll flow:')}    {_c(C.GY,' → '.join(hier.get('scroll_flow',[])))}")

    # ── 05 DESIGN SYSTEM ──────────────────────────────────────────────────────
    out.append(_section("DESIGN SYSTEM", "05", C.CY))
    out.append(f"  {_c(C.B,'Palette:')}     {design['palette_id']} — {p['name']}")
    out.append(f"  {_c(C.B,'Colours:')}     primary {p['primary']}  ·  secondary {p['secondary']}  ·  accent {p['accent']}")
    out.append(f"  {_c(C.B,'Dark mode:')}   {_c(C.GR,'yes') if design['dark_mode'] else _c(C.YL,'no')}")
    out.append(f"  {_c(C.B,'Effect:')}      {design['visual_effect']} @ {design['effect_placement']}")
    out.append(f"  {_c(C.B,'Animation:')}   {design['text_animation']}")
    out.append(f"  {_c(C.B,'Font:')}        {design['font_pair']}")
    out.append(f"\n  {_c(C.YL,'Tailwind tokens:')}")
    out.append(f"  {_c(C.GY,'container:')}      {tw['container']}")
    out.append(f"  {_c(C.GY,'section:')}        {tw['section']}")
    out.append(f"  {_c(C.GY,'card:')}           {tw['card']}")
    out.append(f"  {_c(C.GY,'btn-primary:')}    {tw['btn_primary']}")
    out.append(f"  {_c(C.GY,'btn-secondary:')}  {tw['btn_secondary']}")

    # ── 06 CODE SKELETON ──────────────────────────────────────────────────────
    out.append(_section("CODE SKELETON", "06", C.CY))
    first_skel = next(iter(skeleton.values()), "") if skeleton else ""
    for line in first_skel.splitlines():
        out.append(f"  {_c(C.GY, line)}")

    # ── 07 REFINED PROMPT ─────────────────────────────────────────────────────
    out.append(_section("REFINED FRONTEND PROMPT", "07", C.GR))
    out.append("")
    for line in prompt.splitlines():
        out.append(f"  {line}")

    # ── 08 GENERATED CODE (preview) ───────────────────────────────────────────
    if code:
        out.append(_section("GENERATED REACT CODE (preview)", "08", C.BL))
        lines = code.splitlines()
        for line in lines[:70]:
            out.append(f"  {_c(C.GY, line)}")
        if len(lines) > 70:
            out.append(_c(C.GY, f"  … {len(lines) - 70} more lines (see output/)"))

    # ── FOOTER ────────────────────────────────────────────────────────────────
    out.append(f"\n{_divider()}")
    out.append(_c(C.GR, _c(C.B, "  ✓  BLUEPRINT COMPLETE")))
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    out.append(_c(C.GY, f"  Prompt Machine v3.0  ·  Qwen2.5  ·  {ts}"))
    out.append(_divider())

    return "\n".join(out)


# ── SAVE TO DISK ──────────────────────────────────────────────────────────────
def save_blueprint(blueprint: dict, output_dir: str = "output") -> None:
    slug = blueprint["intent"]["product_name"].lower().replace(" ", "-")
    out  = Path(output_dir) / slug
    (out / "code").mkdir(parents=True, exist_ok=True)

    # blueprint.json
    (out / "blueprint.json").write_text(
        json.dumps({
            "intent":   blueprint["intent"],
            "ontology": blueprint.get("ontology", {}),
            "layout":   blueprint.get("layout", {}),
            "ast":      blueprint.get("ast", {}),
            "design":   {k: v for k, v in blueprint.get("design", {}).items() if k != "palette"},
        }, indent=2)
    )

    # prompt.md
    (out / "prompt.md").write_text(
        f"# {blueprint['intent'].get('product_name', 'App')} — Frontend Prompt\n\n{blueprint.get('prompt', '')}"
    )

    # skeletons
    for page_name, skel in blueprint.get("skeletons", {}).items():
        fname = page_name.lower().replace(" ", "-")
        (out / "code" / f"{fname}.jsx").write_text(skel)

    # full generated code
    if blueprint.get("code"):
        code = blueprint["code"]
        import re
        
        # Parse XML file blocks generated by stage8
        file_blocks = re.findall(r'<file\s+path="(.*?)">\n?(.*?)</file>', code, re.DOTALL)
        
        if file_blocks:
            for path, content in file_blocks:
                file_path = out / path
                file_path.parent.mkdir(parents=True, exist_ok=True)
                # remove markdown fences
                content = re.sub(r"```[\w]*\n?", "", content)
                content = content.replace("```", "")
                file_path.write_text(content.strip() + "\n")
        else:
            # Fallback legacy formatting code 
            code = re.sub(r"```[\w]*\n?", "", code)
            (out / "code" / "App.jsx").write_text(code)

    print(f"\n\033[32m✓  Saved to {out}/\033[0m")
    print(f"\033[90m   ├─ blueprint.json\033[0m")
    print(f"\033[90m   ├─ prompt.md\033[0m")
    print(f"\033[90m   └─ code/   (skeletons + App.jsx)\033[0m")
