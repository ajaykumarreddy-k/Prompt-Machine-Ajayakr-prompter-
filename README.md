# Prompt Machine (Ajayakr-prompter)

Prompt Machine is an intelligent, CLI-based UI Designer and Code Generator pipeline. It uses a local LLM through [Ollama](https://ollama.ai/) combined with a local FAISS-based Vector Knowledge Base to intelligently architect and generate production-quality React + Tailwind CSS components from a simple Product Requirements Document (PRD).

## Key Features

- **PRD Validation & Intent Extraction:** Intelligently reads your PRD and extracts product type, key features, target audience, style keywords, and tone.
- **Automated Page Planning:** Sets up a layout sequence (e.g., Navbar, Hero, Features, Footer) based on the inferred product type.
- **Smart Palette Selection:** Automatically selects comprehensive, beautiful Tailwind color palettes (e.g., 'Midnight Dev', 'Neo-Brutalist', 'SaaS Architecture') mapped to your desired tone.
- **RAG for UI Components:** Retrieves real-world, high-quality reference patterns (from Uiverse, FreeFrontend, Aceternity UI, React Bits, and more) from its FAISS vector database to ensure output code relies on verified solutions.
- **CPU-First Embedding & GPU-First LLM:** Keeps embeddings strictly on the CPU, allowing the Ollama LLM dedicated access to your GPU for maximum performance.
- **Zero-Dependency Output:** Produces single-file, copy-paste-ready React functional components styled exclusively with Tailwind CSS utility classes.

## Project Structure

- `machine.py`: Main generation pipeline combining validation, planning, retrieval, prompting, and code synthesis.
- `vector_kb.py`: Tool to build the vector index, chunk data, and execute semantic queries over the UI knowledge base.
- `Scrapper/`: Python scripts (e.g., `Ajay-Akr-Scrapper.py`, `scraper_uiverse.py`) used to extract high-quality UI components and code snippets from external libraries.
- `Scrapped-Data/`: The raw text data representing components, layouts, and animations scraped from the web, and tools like `splitter.py` for chunking them.
- `vector-kb/`: Stores the generated FAISS similarity search index (`index.faiss`) and associated chunk metadata.
- `knowledge-base/`: Documentation components, frontend effects, and design system guidelines.

## Prerequisites

- [Ollama](https://ollama.ai/) running locally for LLM generation.
- Python ^3.10 and [uv](https://github.com/astral-sh/uv) for fast, reliable package management.

### Model Requirements

By default, the pipeline uses `llama3.1`. Make sure you have it pulled:
```bash
ollama pull llama3.1
```

## Setup & Usage

### 1. Build the Vector Knowledge Base

The vector knowledge base uses `BAAI/bge-small-en-v1.5` sentence embeddings and FAISS to enable fast retrieval. You only need to build this once (or whenever you scrape new data).

```bash
uv run vector_kb.py build
```

To test the knowledge base manually:
```bash
uv run vector_kb.py query
```

### 2. Run the Prompt Machine

Start your locally installed Ollama instance if it isn't running:
```bash
ollama serve
```

Execute the pipeline using `uv`:
```bash
uv run machine.py run Ajayakr-prompter
```

You can optionally override the LLM model:
```bash
uv run machine.py run Ajayakr-prompter --model=mistral
```

### 3. Provide Your PRD

When prompted, paste your Product Requirements Document (PRD). You can format it as loosely or strictly as you prefer.
Type `END` on a new line and press Enter to begin the pipeline.

**Example PRD:**
```markdown
I need a modern SaaS landing page for an AI accounting tool called 'LedgAI'.
Target audience: Freelancers and small businesses.
Tone: Professional, very clean, highly trustworthy, high-tech, slightly futuristic.
Key Features: Auto-invoicing, AI expense categorization, tax estimates.
Color Preference: Dark mode, violet and slate accents.
```

### 4. Output

The system will parse the PRD, retrieve matching component patterns from its knowledge base, and synthesize the final application.
Check the `output/` directory for your generated React file (`.jsx`) and the detailed LLM prompt (`.md`) used to create it.

## Architecture Highlights
- **Vector Database**: FAISS (Facebook AI Similarity Search)
- **Embedding Model**: `BAAI/bge-small-en-v1.5` (via sentence-transformers)
- **Local LLM API**: Ollama
- **Output Structure**: React + Tailwind CSS
# Prompt-Machine-Ajayakr-prompter-
