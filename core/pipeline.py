import os
import sys

# ── COLOURS ───────────────────────────────────────────────────────────────────
class C:
    R  = "\033[0m" ; B  = "\033[1m" ; DIM = "\033[2m"
    CY = "\033[36m"; GR = "\033[32m"; YL  = "\033[33m"
    RD = "\033[31m"; BL = "\033[34m"; MG  = "\033[35m"
    GY = "\033[90m"


BANNER = f"""{C.MG}
██████╗ ██████╗  ██████╗ ███╗   ███╗██████╗ ████████╗
██╔══██╗██╔══██╗██╔═══██╗████╗ ████║██╔══██╗╚══██╔══╝
██████╔╝██████╔╝██║   ██║██╔████╔██║██████╔╝   ██║
██╔═══╝ ██╔══██╗██║   ██║██║╚██╔╝██║██╔═══╝    ██║
██║     ██║  ██║╚██████╔╝██║ ╚═╝ ██║██║        ██║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝        ╚═╝{C.R}

{C.CY}███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗
████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝
██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗
██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝
██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗
╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝{C.R}

{C.GY}                  designed and built by Ajay
    ─────────────────────────────────────────────────────{C.R}
"""


def _warm_kb() -> None:
    try:
        from vector_kb import get_model, get_index
        print(f"{C.GY}  Warming up vector KB (CPU)...{C.R}", end="", flush=True)
        get_model()
        get_index()
        print(f"\r  {C.GR}✓  Vector KB ready.{C.R}               ")
    except SystemExit:
        print(f"\r  {C.YL}⚠  KB index not built — retrieval will be skipped.{C.R}")
        print(f"  {C.GY}    Run:  uv run vector_kb.py build{C.R}")
    except Exception as e:
        print(f"\r  {C.YL}⚠  KB warm-up failed: {e}{C.R}")


def run_prompt_machine(prd: str, no_code: bool = False, verbose: bool = False, palette_override: str = None, save: bool = True, output_dir: str = "output") -> None:
    """
    Unified entry point for both CLI and TUI execution.
    Contains the full execution pipeline including ASCII banner, 
    Ollama networking checks, Knowledge Base warming, and calling the compiler.
    """
    from pipeline.pipeline import run_pipeline
    from ollama import check_ollama, MODEL

    print(f"{C.CY}{'─' * 58}{C.R}")
    print(f"  {C.B}System is firing up... Just a sec! ;]{C.R}")
    print(f"{C.CY}{'─' * 58}{C.R}\n")

    print(BANNER)
    sys.stdout.flush()

    check_ollama()
    print(f"  {C.GY}Model: {MODEL}{C.R}")
    print(f"  {C.GY}{'─' * 56}{C.R}")

    _warm_kb()

    print(f"\n{C.CY}{'─' * 58}{C.R}")
    print(f"  {C.GR}{C.B}Running pipeline…{C.R}")
    print(f"{C.CY}{'─' * 58}{C.R}")

    run_pipeline(
        prd,
        no_code=no_code,
        verbose=verbose,
        palette_override=palette_override,
        save=save,
        output_dir=output_dir
    )
