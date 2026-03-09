"""pipeline.py — Orchestrates all 10 pipeline stages."""

import sys
import os

# ── SAFETY NET FOR TUI REDIRECTION ──────────────────────────────────────────
if not hasattr(sys.stdout, 'isatty'):
    sys.stdout.isatty = lambda: False
if not hasattr(sys.stderr, 'isatty'):
    sys.stderr.isatty = lambda: False

from pipeline.stage1_intent_parser       import parse_intent
from pipeline.stage2_ontology_map        import map_ontology_by_embedding
from pipeline.stage3_layout_planner      import plan_layout
from pipeline.stage4_blueprint_generator import generate_blueprint_ast
from pipeline.stage5_blueprint_validator import validate_blueprint
from pipeline.stage6_targeted_retriever  import retrieve_targeted_context
from pipeline.stage5_design_system       import inject_design_system
from pipeline.stage7_prompt_generator    import generate_prompt
from pipeline.stage8_code_generator      import generate_code
from pipeline.stage9_prompt_refiner      import refine_prompt
from pipeline.stage10_blueprint_output   import render_blueprint, save_blueprint
from pipeline.stage11_code_validator    import validate_generated_code


def _progress(n, total, label):
    filled  = "▰" * n
    empty   = "▱" * (total - n)
    bar_col = "\033[35m" if n == total else "\033[36m"
    bar     = f"{bar_col}{filled}\033[90m{empty}\033[0m"
    sys.stdout.write(f"\r  {bar}  \033[90m{n}/{total} — {label}\033[0m          ")
    sys.stdout.flush()
    if n == total:
        print()


def run_pipeline(prd, no_code=False, verbose=False, palette_override=None, save=True, output_dir="output"):
    TOTAL = 12
    print("\n\033[36m  Starting Compiler Pipeline Engine...\033[0m\n")

    _progress(1, TOTAL, "Intent Parsing")
    intent = parse_intent(prd)

    _progress(2, TOTAL, "Ontology Mapping")
    ontology = map_ontology_by_embedding(intent)

    _progress(3, TOTAL, "Layout Planning")
    layout = plan_layout(intent, ontology)

    _progress(4, TOTAL, "Blueprint Generation")
    raw_blueprint = generate_blueprint_ast(intent, layout)

    _progress(5, TOTAL, "Blueprint Validation")
    blueprint_ast = validate_blueprint(raw_blueprint, ontology["required_components"])

    _progress(6, TOTAL, "Targeted Retrieval")
    kb_context = retrieve_targeted_context(blueprint_ast, ontology["required_components"])

    _progress(7, TOTAL, "Design System Integration")
    design = inject_design_system(intent, palette_override)

    _progress(8, TOTAL, "Prompt Synthesis")
    raw_prompt = generate_prompt(intent, blueprint_ast, kb_context, design)
    
    _progress(9, TOTAL, "Prompt Refinement")
    final_prompt = refine_prompt(raw_prompt, intent)

    # Store complete metadata into a single dict 
    components_dict = {"kb_context": kb_context, "required_components": ontology["required_components"]}

    code = ""
    if not no_code:
        _progress(10, TOTAL, "Multi-File Code Generation")
        code = generate_code(intent, blueprint_ast, components_dict, design, kb_context, final_prompt)
    else:
        _progress(10, TOTAL, "Code Generation (skipped)")

    _progress(11, TOTAL, "Blueprint Output")
    print("\n")

    full_blueprint = {
        "intent": intent, "ontology": ontology, "layout": layout, "ast": blueprint_ast,
        "design": design, "prompt": final_prompt, "code": code,
    }

    if save:
        save_blueprint(full_blueprint, output_dir=output_dir)

    _progress(12, TOTAL, "Strict Token Validation")
    name = intent["product_name"].lower().replace(" ", "-")
    target_path = os.path.join(output_dir, name) if save else "tmp"
    validate_generated_code(target_path)

    print(render_blueprint(full_blueprint, verbose=verbose))

    return full_blueprint
