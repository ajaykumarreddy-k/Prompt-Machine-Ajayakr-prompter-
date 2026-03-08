# Color Palettes

## Selection Rules
- One palette per project, applied globally to all pages
- Selected by LLM based on PRD keywords and product type
- Manual override available via --palette CLI flag

## Palettes

### Palette P-1: Corporate SaaS
- Primary: blue-600
- Secondary: slate-800
- Accent: indigo-500
- Background: slate-50
- Text: slate-900
- Best for: B2B operations, enterprise scale software, financial tech, analytics
- Mood: Hyper-professional, intensely structured, projecting supreme reliability.

### Palette P-2: Neo-Brutalist
- Primary: yellow-400
- Secondary: neutral-950
- Accent: pink-500
- Background: white
- Text: black
- Best for: Creative studios, portfolio iterations, boundary-pushing consumer tech
- Mood: Visually aggressive, extremely sharp contrasts, inherently modern.

### Palette P-3: Nature Minimalist
- Primary: emerald-600
- Secondary: stone-700
- Accent: teal-500
- Background: neutral-50
- Text: stone-800
- Best for: E-commerce, sustainability platforms, healthcare mapping, organic tracking
- Mood: Exceptionally calm, breathable layouts, reducing cognitive friction.

### Palette P-4: Midnight Developer
- Primary: violet-500
- Secondary: slate-800
- Accent: cyan-400
- Background: slate-950
- Text: slate-200
- Best for: Web3 mechanics, developer frameworks, gaming applications, AI clients
- Mood: Electric intensity, deeply focused, futuristic interface mechanics.

## Tailwind Class Mapping

| Role       | P-1 | P-2 | P-3 | P-4 |
|------------|-----|-----|-----|-----|
| Primary    | bg-blue-600 text-blue-600 | bg-yellow-400 text-black | bg-emerald-600 text-emerald-600 | bg-violet-500 text-violet-500 |
| Secondary  | bg-slate-800 text-slate-800 | bg-neutral-950 text-white | bg-stone-700 text-stone-700 | bg-slate-800 text-slate-800 |
| Accent     | text-indigo-500 | text-pink-500 border-pink-500 | text-teal-500 | border-cyan-400 text-cyan-400 |
| Background | bg-slate-50 | bg-white | bg-neutral-50 | bg-slate-950 |
| Text       | text-slate-900 | text-black | text-stone-800 | text-slate-200 |
