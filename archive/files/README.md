# Prompt Machine v3.0 — Frontend Blueprint Engine

Terminal AI tool. Paste a PRD → get a complete frontend blueprint.

## Invocation

```bash
uv run machine.py run Ajayakr-prompter
```

## Flags

| Flag | Effect |
|------|--------|
| `--model=qwen2.5` | Override Ollama model (default: qwen2.5) |
| `--palette=P-4` | Force palette P-1 to P-5 |
| `--no-code` | Skip React code gen (faster, prompt + blueprint only) |
| `--verbose` | Show intermediate JSON at each stage |
| `--no-save` | Don't write files to output/ |

## 10-Stage Pipeline

```
PRD input
  ↓  Stage 1  — Intent Parser        → product_name, features, tone, complexity
  ↓  Stage 2  — Layout Contract      → pages, routes, component order
  ↓  Stage 3  — Visual Hierarchy     → primary/secondary sections, CTA, focal point
  ↓  Stage 4  — Component Retriever  → vector KB lookup (top_k=6 per component)
  ↓  Stage 5  — Design System        → palette, dark mode, Tailwind tokens
  ↓  Stage 6  — Layout Skeleton      → JSX skeleton with blur accent
  ↓  Stage 7  — Prompt Generator     → structured prompt for v0/Lovable/Bolt
  ↓  Stage 8  — Code Generator       → full React + Tailwind (streams live)
  ↓  Stage 9  — Prompt Refiner       → final polish pass
  ↓  Stage 10 — Blueprint Output     → terminal render + output/ save
```

## Build the Vector KB

```bash
# First time only (indexes your 250k+ line Scrapped-Data/ files)
uv run vector_kb.py build

# Interactive search REPL
uv run vector_kb.py query

# Direct query
uv run vector_kb.py retrieve "navbar glassmorphism sticky"
```

## Palettes

| ID | Name | Primary | Dark |
|----|------|---------|------|
| P-1 | SaaS Architecture | blue-600 | no |
| P-2 | Neo-Brutalist | yellow-400 | no |
| P-3 | Organic Utility | emerald-600 | no |
| P-4 | Midnight Dev | violet-500 | **yes** |
| P-5 | Minimal Editorial | zinc-900 | no |

## Output Files

```
output/
  your-product/
    blueprint.json    ← full structured blueprint
    prompt.md         ← refined AI builder prompt
    code/
      home.jsx        ← page skeleton
      App.jsx         ← full generated component file
```

## Requirements

- Python ≥ 3.14
- `uv` package manager
- Ollama running: `ollama serve` + `ollama pull qwen2.5`
- Dependencies: `faiss-cpu`, `sentence-transformers`, `rich` (via pyproject.toml)
