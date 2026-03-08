"""pipeline.py — Orchestrates all 10 pipeline stages."""

import sys

from pipeline.stage1_intent_parser      import parse_intent
from pipeline.stage2_layout_contract    import generate_layout_contract
from pipeline.stage3_visual_hierarchy   import plan_visual_hierarchy
from pipeline.stage4_component_retriever import retrieve_components
from pipeline.stage5_design_system      import inject_design_system
from pipeline.stage6_layout_skeleton    import generate_skeleton
from pipeline.stage7_prompt_generator   import generate_prompt
from pipeline.stage8_code_generator     import generate_code
from pipeline.stage9_prompt_refiner     import refine_prompt
from pipeline.stage10_blueprint_output  import render_blueprint, save_blueprint


# ── PROGRESS BAR ──────────────────────────────────────────────────────────────
def _progress(n: int, total: int, label: str) -> None:
    filled  = "▰" * n
    empty   = "▱" * (total - n)
    bar_col = "\033[35m" if n == total else "\033[36m"
    bar     = f"{bar_col}{filled}\033[90m{empty}\033[0m"
    sys.stdout.write(f"\r  {bar}  \033[90m{n}/{total} — {label}\033[0m          ")
    sys.stdout.flush()
    if n == total:
        print()


# ── MAIN PIPELINE ─────────────────────────────────────────────────────────────
def run_pipeline(
    prd:              str,
    no_code:          bool       = False,
    verbose:          bool       = False,
    palette_override: str | None = None,
    save:             bool       = True,
) -> dict:
    TOTAL = 10
    print("\n\033[36m  Starting Frontend Blueprint Engine...\033[0m\n")

    # ── Stage 1 ───────────────────────────────────────────────────────────────
    _progress(1, TOTAL, "PRD Intent Parser")
    intent = parse_intent(prd)
    if verbose:
        import json; print("\n  [intent]", json.dumps(intent, indent=2))

    # ── Stage 2 ───────────────────────────────────────────────────────────────
    _progress(2, TOTAL, "Layout Contract")
    layout = generate_layout_contract(intent)
    if verbose:
        import json; print("\n  [layout]", json.dumps(layout, indent=2))

    # ── Stage 3 ───────────────────────────────────────────────────────────────
    _progress(3, TOTAL, "Visual Hierarchy Plan")
    hierarchy = plan_visual_hierarchy(intent, layout)

    # ── Stage 4 ───────────────────────────────────────────────────────────────
    _progress(4, TOTAL, "Component Retriever (Vector KB)")
    print()  # newline so KB logs show below the bar
    components = retrieve_components(intent, layout, hierarchy)

    # ── Stage 5 ───────────────────────────────────────────────────────────────
    _progress(5, TOTAL, "Design System Injection")
    design = inject_design_system(intent, palette_override)

    # ── Stage 6 ───────────────────────────────────────────────────────────────
    _progress(6, TOTAL, "Layout Skeleton")
    skeletons = generate_skeleton(layout, components, design)

    # ── Stage 7 ───────────────────────────────────────────────────────────────
    _progress(7, TOTAL, "Prompt Generator")
    raw_prompt = generate_prompt(intent, layout, hierarchy, components, design)

    # ── Stage 8 ───────────────────────────────────────────────────────────────
    code = ""
    if not no_code:
        _progress(8, TOTAL, "Code Generator")
        code = generate_code(intent, layout, components, design, components["kb_context"], raw_prompt)
    else:
        _progress(8, TOTAL, "Code Generator (skipped --no-code)")

    # ── Stage 9 ───────────────────────────────────────────────────────────────
    _progress(9, TOTAL, "Prompt Refiner")
    final_prompt = refine_prompt(raw_prompt, intent)

    # ── Stage 10 ──────────────────────────────────────────────────────────────
    _progress(10, TOTAL, "Blueprint Output")
    print("\n")

    blueprint = {
        "intent":    intent,
        "layout":    layout,
        "hierarchy": hierarchy,
        "components":components,
        "design":    design,
        "skeletons": skeletons,
        "prompt":    final_prompt,
        "code":      code,
    }

    rendered = render_blueprint(blueprint, verbose=verbose)
    print(rendered)

    if save:
        save_blueprint(blueprint)

    return blueprint
