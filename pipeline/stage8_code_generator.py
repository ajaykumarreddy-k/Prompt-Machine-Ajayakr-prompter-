"""stage8_code_generator.py — Generate full React + Tailwind component files with Scaffolding."""

import json
from ollama import ollama_stream

def build_system_prompt(detected_styles: list[str], style_context: str) -> str:
    """Dynamically builds the system prompt based on active design styles."""
    styles_list = ", ".join(detected_styles) if detected_styles else "None"
    
    # Prefixing rules
    prefix_instructions = ""
    if "glassmorphism" in detected_styles:
        prefix_instructions = "- glassmorphism → prefix components with 'Glass' e.g. GlassCard, GlassHero"
    elif "neobrutalism" in detected_styles:
        prefix_instructions = "- neobrutalism  → prefix with 'Brutal' e.g. BrutalCard, BrutalHero"
    elif "futuristic" in detected_styles:
        prefix_instructions = "- futuristic    → prefix with 'Cyber' or 'Holo' e.g. CyberHero, HoloCard"
    elif "aurora" in detected_styles:
        prefix_instructions = "- aurora        → prefix with 'Aurora' e.g. AuroraHero, AuroraCard"
    elif "dark_mode" in detected_styles:
        prefix_instructions = "- dark_mode     → use 'Dark' prefix e.g. DarkCard, DarkHero"
    else:
        prefix_instructions = "- minimalist    → keep standard names, no prefix needed"

    base_system = """\
## REACT ROUTER v6 ONLY — NON-NEGOTIABLE:
- Import: from 'react-router-dom' use BrowserRouter, Routes, Route, Link
- CORRECT: <Routes><Route path="/" element={<Landing />} /></Routes>
- FORBIDDEN v5 syntax that will crash the app:
    Switch, exact, component={X}
- App.jsx has EXACTLY ONE route: path="/" pointing to Landing
- Landing.jsx imports ALL section components and stacks them vertically
- NEVER create separate page files for About, Skills, Experience, 
  Projects, Contact — these are SECTIONS inside Landing, not pages

## SINGLE-PAGE STRUCTURE — NON-NEGOTIABLE:
- This is a single-page app. ONE page: Landing.jsx
- Landing.jsx assembles all sections in this exact order:
  <Navbar />
  <HeroSection />
  <AboutSection />
  <SkillsSection />
  <ExperienceSection />
  <ProjectsSection />
  <FeaturesSection />
  <TestimonialsSection />
  <PricingSection />
  <ContactSection />
  <Footer />
- Each section is a separate file in src/components/
- App.jsx only contains the Router and one Route to Landing

## CORRECT App.jsx TEMPLATE — COPY THIS EXACTLY:
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Landing from './pages/Landing';

const App = () => (
  <Router>
    <Routes>
      <Route path="/" element={<Landing />} />
    </Routes>
  </Router>
);
export default App;

## CORRECT Landing.jsx TEMPLATE — FOLLOW THIS STRUCTURE:
import Navbar from '../components/Navbar';
import HeroSection from '../components/HeroSection';
import AboutSection from '../components/AboutSection';
import SkillsSection from '../components/SkillsSection';
import ExperienceSection from '../components/ExperienceSection';
import ProjectsSection from '../components/ProjectsSection';
import TestimonialsSection from '../components/TestimonialsSection';
import ContactSection from '../components/ContactSection';
import Footer from '../components/Footer';

const Landing = () => (
  <main>
    <Navbar />
    <HeroSection />
    <AboutSection />
    <SkillsSection />
    <ExperienceSection />
    <ProjectsSection />
    <TestimonialsSection />
    <ContactSection />
    <Footer />
  </main>
);
export default Landing;

## CRITICAL FRAMEWORK RULES — READ FIRST:
- This is a VITE + REACT project. NOT Next.js. NOT Remix. NOT Gatsby.
- NEVER import from 'next/link', 'next/router', 'next/image', or any 'next/*'
- NEVER use Next.js Link syntax: <Link href="/path">
- ALWAYS use react-router-dom for navigation:
    import { Link } from 'react-router-dom'
    <Link to="/path">text</Link>
- NEVER use TypeScript syntax in .jsx files:
    NO: FormEvent, MouseEvent, type annotations, interface, as keyword
    YES: plain JavaScript only
- ALWAYS import useState, useEffect, useRef from 'react' explicitly when used:
    import { useState, useEffect } from 'react'
    NEVER assume they are globally available
- NEVER import useScroll, useAnimation or any custom hook not 
  defined in the blueprint
- NEVER import from '@heroicons/react/outline' or '@heroicons/react/solid' (v1)
  ALWAYS use: import { Bars3Icon, XMarkIcon } from '@heroicons/react/24/outline'
- App.jsx MUST always wrap everything in BrowserRouter:
    import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
    const App = () => (
      <Router>
        <Routes>
          <Route path="/" element={<Landing />} />
        </Routes>
      </Router>
    )

You are an expert React and Tailwind CSS developer acting as a code compiler.
You will receive a structured JSON AST Blueprint, REFERENCE PATTERNS, and DESIGN TOKENS.
Synthesise them into production-quality React component files.

## GLASSMORPHISM COMPONENT RULES (active when glassmorphism detected):
When glassmorphism style is active, every section component MUST:
- Use dark background: bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900
- Cards use: bg-white/10 backdrop-blur-md border border-white/20 rounded-xl shadow-lg p-6
- Text: text-white for headings, text-white/70 for body
- Buttons: bg-white/20 hover:bg-white/30 backdrop-blur-sm border border-white/30
- NO light backgrounds (bg-white, bg-slate-50, bg-gray-100) anywhere
- Add subtle gradient overlays on sections for depth

## HERO SECTION RULES — ALWAYS:
- HeroSection is ALWAYS full viewport height: min-h-screen
- HeroSection ALWAYS has: large headline (text-5xl+), subtitle, CTA button
- HeroSection is NEVER a navbar or navigation element
- HeroSection background should reflect the active design style

STRICT RULES:
- Use `react-router-dom` for all navigation.
- **Page Structure**: A "page" file (e.g., `Landing.jsx`) imports components from `src/components/` and assembles them.
- FOLDER STRUCTURE:
  - `src/components/`: Reusable UI blocks.
  - `src/pages/`: Full-page compositions.
  - `src/App.jsx`: The main application entry point with the router.
- DESIGN TOKENS:
  - NEVER create arbitrary wrapper components like `<Container>`.
  - Apply Tailwind classes directly to HTML tags.

## NAVBAR RULES — CRITICAL:
- NEVER import from '@heroicons/react/outline' or '@heroicons/react/solid' (v1, broken)
- Use heroicons v2: import { Bars3Icon, XMarkIcon } from '@heroicons/react/24/outline'
- NEVER import useScroll or any custom hook that isn't explicitly listed in the blueprint
- For mobile menu toggle, use only useState from React
- Output raw code files using the `<file path="...">` structure. No explanation. No markdown fences."""

    style_section = f"""
## ACTIVE DESIGN STYLE: {styles_list}

{style_context}

CRITICAL: The above style instructions OVERRIDE all default component patterns.
You MUST generate components that visually match the detected style.
Generic white card UIs are FORBIDDEN when a design style is active.

Style-specific component naming convention:
{prefix_instructions}
"""
    return base_system + style_section

def generate_scaffold_files(product_name: str, detected_styles: list) -> str:
    """Returns static file blocks for Vite/Tailwind project scaffolding."""
    slug = product_name.lower().replace(" ", "-")
    
    pkg_json = f"""{{
  "name": "{slug}",
  "version": "0.1.0",
  "type": "module",
  "scripts": {{
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  }},
  "dependencies": {{
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.22.0",
    "@heroicons/react": "^2.1.1"
  }},
  "devDependencies": {{
    "@vitejs/plugin-react": "^4.2.1",
    "autoprefixer": "^10.4.17",
    "postcss": "^8.4.35",
    "tailwindcss": "^3.4.1",
    "vite": "^5.1.0"
  }}
}}"""

    vite_config = """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
export default defineConfig({
  plugins: [react()],
})"""

    tailwind_config = """/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: { extend: {} },
  plugins: [],
}"""

    postcss_config = """export default {
  plugins: { tailwindcss: {}, autoprefixer: {} }
}"""

    index_html = f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{product_name}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>"""

    main_jsx = """import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)"""

    bg_style = "body { margin: 0; font-family: 'Inter', sans-serif; }"
    if any(s in detected_styles for s in ["glassmorphism", "aurora", "futuristic"]):
        bg_style = "body { background: linear-gradient(135deg, #0f172a, #1e1b4b); min-height: 100vh; margin: 0; font-family: 'Inter', sans-serif; }"

    index_css = f"""@tailwind base;
@tailwind components;
@tailwind utilities;

{bg_style}"""

    readme = f"""# {product_name}
Generated by Prompt Machine

## Quick Start
```bash
npm install
npm run dev
```"""

    return f"""
<file path="package.json">{pkg_json}</file>
<file path="vite.config.js">{vite_config}</file>
<file path="tailwind.config.js">{tailwind_config}</file>
<file path="postcss.config.js">{postcss_config}</file>
<file path="index.html">{index_html}</file>
<file path="src/main.jsx">{main_jsx}</file>
<file path="src/index.css">{index_css}</file>
<file path="README.md">{readme}</file>
"""

def generate_code(
    intent: dict,
    blueprint_ast: dict,
    components: dict,
    design: dict,
    kb_context: str,
    ui_prompt: str,
    detected_styles: list[str] = None,
    style_context: str = ""
) -> str:
    """Triggers multi-file code generation via LLM streaming, then appends scaffolds."""
    detected_styles = detected_styles or []
    system_prompt = build_system_prompt(detected_styles, style_context)
    
    tw = design["tailwind"]
    product_type = intent.get('product_type', 'app')
    routing_rule = "SINGLE-PAGE: All sections render on one page. Only one route: path=/." if product_type in ['portfolio', 'landing', 'marketing', 'saas'] else "MULTI-PAGE: Create separate routes only for top-level pages in the AST."

    spec = f"""
PRODUCT: {intent.get('product_name', 'App')}  ({product_type})
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

ROUTING RULE: This is a {product_type} application. {routing_rule}

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
3. **DESIGN TOKENS**: Apply `max-w-7xl`, `px-6`, `py-16`, and `rounded-lg` directly to HTML. NO custom layout wrappers.
4. **STYLE ALIGNMENT**: Every component MUST reflect the '{", ".join(detected_styles)}' style.
 
Write the React files using the `<file path="...">` blocks. Do not omit any files from the blueprint."""

    print("\033[35m\033[1m[OLLAMA]\033[0m Generating Style-Aware Multi-File React code...\n")
    
    # Get LLM generated code
    llm_output = ollama_stream(full_prompt, system=system_prompt)
    
    # Append Scaffolds
    scaffold = generate_scaffold_files(intent.get('product_name', 'App'), detected_styles)
    
    return llm_output + "\n" + scaffold
