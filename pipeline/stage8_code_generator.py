"""stage8_code_generator.py — Generate full React + Tailwind component files."""

import json
from ollama import ollama_stream

SYSTEM = """\
You are an expert React and Tailwind CSS developer acting as a code compiler.
You will receive a structured JSON AST Blueprint, REFERENCE PATTERNS, and DESIGN TOKENS.
Synthesise them into production-quality React component files.

STRICT RULES:
- Use `react-router-dom` for all navigation. Your `App.jsx` MUST set up the router.
- **App.jsx Structure**: This file is for routing ONLY. It should import pages and set up routes.
  ```jsx
  // Example App.jsx
  import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
  import Navbar from './components/Navbar';
  import Landing from './pages/Landing';
  import Pricing from './pages/Pricing';
  import About from './pages/About';

  function App() {
    return (
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<Landing />} />
          <Route path="/pricing" element={<Pricing />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </Router>
    );
  }
  export default App;
  ```
- **Page Structure**:
  - A "page" file (e.g., `Landing.jsx`) imports components from `src/components/` and assembles them.
  - DO NOT create routes for individual sections of a page (e.g., `/features`). Sections belong inside a page.
- FOLDER STRUCTURE:
  - `src/components/`: Reusable UI blocks (HeroSection, PricingSection, etc.).
  - `src/pages/`: Full-page compositions (Landing.jsx, About.jsx, etc.).
  - `src/App.jsx`: The main application entry point with the router.
- COMPONENT NAMING & REUSE:
  - Use generic names like `HeroSection.jsx` or `FeaturesSection.jsx`.
  - DO NOT create page-specific variations (e.g., `AboutHero.jsx`).
- DESIGN TOKENS:
  - NEVER create arbitrary wrapper components like `<Container>` or `<Section>`.
  - Apply Tailwind classes like `max-w-7xl mx-auto px-6` and `py-16 md:py-24` directly to `<section>` or `<div>` tags.
- Study the AST Blueprint and "responsibilities" for each component before writing code.
- Output raw code files using the `<file path="...">` structure. No explanation. No markdown fences."""

def generate_code(
    intent: dict,
    blueprint_ast: dict,
    components: dict,
    design: dict,
    kb_context: str,
    ui_prompt: str,
) -> str:
    p            = design["palette"]
    tw           = design["tailwind"]

    spec = f"""
PRODUCT: {intent.get('product_name', 'App')}  ({intent.get('product_type', 'Application')})
AUDIENCE: {intent.get('target_audience', '')}
FEATURES: {', '.join(intent.get('key_features', []))}

DESIGN TOKENS (use these exact Tailwind classes):
  Page bg:       {tw['bg_page']}
  Card:          {tw['card']}
  Primary btn:   {tw['btn_primary']}
  Secondary btn: {tw['btn_secondary']}
  Heading text:  {tw['text_heading']}
  Body text:     {tw['text_body']}
  Input:         {tw['input']}
  Container:     {tw['container']}
  Section:       {tw['section']}

BLUEPRINT AST:
{json.dumps(blueprint_ast, indent=2)}

UI SPEC INSTRUCTIONS:
{ui_prompt}
"""

    kb_block = kb_context[:10_000] if kb_context else "(no KB context)"

    full_prompt = f"""{spec}
 
REFERENCE PATTERNS FROM REAL COMPONENT LIBRARIES:
{kb_block}
 
### CODE GENERATION CONTRACT (STRICT)
You are a deterministic code compiler. Your output MUST follow these rules:
1. **BLUEPRINT AS TRUTH**: Every component and page in the AST MUST have exactly one file.
2. **FOLDER STRUCTURE**: 
   - `src/components/[ComponentName].jsx` 
   - `src/pages/[PageName].jsx`
   - `src/App.jsx` (Routing)
3. **ROUTING**: Use `react-router-dom` (Version 6). Use `<Routes>` and `<Route element={{...}}>`.
4. **IMPORTS**: Components must import other components using relative paths (e.g., `import HeroSection from '../components/HeroSection'`).
5. **DESIGN TOKENS**: Apply `max-w-7xl`, `px-6`, `py-16`, and `rounded-lg` directly to HTML. NO custom layout wrappers.
6. **NO HALLUCINATIONS**: If it's not in the blueprint, don't generate it.
 
Write the React files using the `<file path="...">` blocks. Do not omit any files from the blueprint."""

    print("\033[35m\033[1m[OLLAMA]\033[0m Generating Multi-File React code...\n")
    return ollama_stream(full_prompt, system=SYSTEM)
