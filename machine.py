#!/usr/bin/env python3
"""
Prompt Machine v3.0 — Frontend Blueprint Engine
Invocation: uv run machine.py run Ajayakr-prompter

Flags:
  --model=qwen2.5        Override Ollama model
  --palette=P-4          Force palette (P-1 to P-5)
  --no-code              Skip React code generation (faster)
  --verbose              Show intermediate JSON at each stage
  --no-save              Don't write files to output/
"""

import os
import sys

# ── FORCE CPU for embeddings — Ollama owns the GPU ────────────────────────────
os.environ["CUDA_VISIBLE_DEVICES"] = ""


# ── ARG PARSING ───────────────────────────────────────────────────────────────
def _parse_flags() -> dict:
    flags = {
        "model":    None,
        "palette":  None,
        "input":    None,
        "output":   None,
        "no_code":  False,
        "verbose":  False,
        "no_save":  False,
    }
    for arg in sys.argv[1:]:
        if arg.startswith("--model="):
            flags["model"] = arg.split("=", 1)[1]
        elif arg.startswith("--palette="):
            flags["palette"] = arg.split("=", 1)[1]
        elif arg.startswith("--input="):
            flags["input"] = arg.split("=", 1)[1]
        elif arg.startswith("--output="):
            flags["output"] = arg.split("=", 1)[1]
        elif arg == "--no-code":
            flags["no_code"] = True
        elif arg == "--verbose":
            flags["verbose"] = True
        elif arg == "--no-save":
            flags["no_save"] = True
    return flags


# ── PRD INPUT ─────────────────────────────────────────────────────────────────
def _get_prd() -> str:
    from core.pipeline import C

    print(f"\n{C.CY}{'─' * 58}{C.R}")
    print(f"{C.B}  Paste your PRD.  Type END on a new line when done.{C.R}")
    print(f"{C.CY}{'─' * 58}{C.R}\n")

    lines: list[str] = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip() == "END":
            break
        lines.append(line)

    prd = "\n".join(lines).strip()
    if not prd:
        from core.pipeline import C
        print(f"{C.RD}{C.B}[ERROR]{C.R} No PRD provided.")
        sys.exit(1)
    if len(prd.split()) < 5:
        from core.pipeline import C
        print(f"{C.YL}⚠  Input is very short — proceeding anyway.{C.R}")
    return prd


# ── RUN ───────────────────────────────────────────────────────────────────────
def run() -> None:
    flags = _parse_flags()
    from core.pipeline import C, run_prompt_machine

    # Apply model override before any imports use it
    if flags["model"]:
        os.environ["OLLAMA_MODEL"] = flags["model"]

    if flags["input"]:
        if not os.path.exists(flags["input"]):
            print(f"{C.RD}{C.B}[ERROR]{C.R} Input file not found: {flags['input']}")
            sys.exit(1)
        with open(flags["input"], "r") as f:
            prd = f.read().strip()
        print(f"  {C.GY}Reading PRD from: {flags['input']}{C.R}")
    else:
        prd = _get_prd()
 
    run_prompt_machine(
        prd,
        no_code=flags["no_code"],
        verbose=flags["verbose"],
        palette_override=flags["palette"],
        save=not flags["no_save"],
        output_dir=flags["output"] if flags["output"] else "output"
    )


# ── ENTRY ─────────────────────────────────────────────────────────────────────
def main() -> None:
    if len(sys.argv) >= 3 and sys.argv[1] == "run" and sys.argv[2] == "Ajayakr-prompter":
        run()
    elif len(sys.argv) >= 3 and sys.argv[1] == "run" and sys.argv[2] == "promptmachine":
        from ui.dashboard import PromptMachineApp
        PromptMachineApp().run()
        from core.pipeline import C
        print(f"\n{C.B}Prompt Machine v3.0{C.R}")
        print(f"  {C.CY}uv run machine.py run Ajayakr-prompter{C.R}")
        print(f"  {C.CY}uv run machine.py run promptmachine{C.R}\n")
        print(f"  Flags:")
        print(f"  {C.GY}  --model=qwen2.5      override Ollama model{C.R}")
        print(f"  {C.GY}  --palette=P-4         force palette (P-1..P-5){C.R}")
        print(f"  {C.GY}  --no-code             skip React generation{C.R}")
        print(f"  {C.GY}  --verbose             show stage debug output{C.R}")
        print(f"  {C.GY}  --no-save             don't write to output/{C.R}\n")
        print(f"  Palettes:")
        print(f"  {C.GY}  P-1  SaaS Architecture   (blue / slate / indigo){C.R}")
        print(f"  {C.GY}  P-2  Neo-Brutalist        (yellow / black / pink){C.R}")
        print(f"  {C.GY}  P-3  Organic Utility      (emerald / stone / teal){C.R}")
        print(f"  {C.GY}  P-4  Midnight Dev         (violet / slate-950 / cyan){C.R}")
        print(f"  {C.GY}  P-5  Minimal Editorial    (zinc / white / red){C.R}\n")


if __name__ == "__main__":
    main()
