# Visual Effects

## Global Rules
- Maximum one effect per page
- Opacity between 10% and 25% only
- Must not overlap or obscure any content
- Color must match selected palette primary or accent color
- Must never be placed in the center of the layout

## Effects

### Background Glow

**Purpose**
Creates an immense soft-focus ambient lighting effect behind core content to anchor visuals without deploying massive images.

**When To Use**
- Backing a primary Hero section on a landing layout.
- Subtle rendering behind distinct Card layouts.

**Placement Options**
- Absolute Top Left
- Absolute Top Right

**Tailwind Implementation**
```html
<div className="absolute inset-x-0 -top-40 -z-10 transform-gpu overflow-hidden blur-3xl sm:-top-80" aria-hidden="true">
  <div className="relative left-[calc(50%-11rem)] aspect-[1155/678] w-[36.125rem] -translate-x-1/2 rotate-[30deg] bg-gradient-to-tr from-blue-300 to-indigo-300 opacity-20 sm:left-[calc(50%-30rem)] sm:w-[72.1875rem]"></div>
</div>
```

**Intensity Variants**

| Level  | Tailwind Class |
|--------|----------------|
| Low    | opacity-10 blur-2xl |
| Medium | opacity-20 blur-3xl |
| High   | opacity-30 blur-3xl |

### Glassmorphism Card

**Purpose**
Injects heavy modern aesthetics by allowing underlying layers to subtly bleed into floating top-layer elements via backdrop blurring.

**When To Use**
- Hero promotional metric overlay cards.
- Sticky Navbar backgrounds passing over complex scrolling arrays.

**Placement Options**
- Sticky Top
- Floating Center

**Tailwind Implementation**
```html
<div className="rounded-2xl bg-white/60 backdrop-blur-md ring-1 ring-gray-900/5 shadow-xl"></div>
```

**Intensity Variants**

| Level  | Tailwind Class |
|--------|----------------|
| Low    | bg-white/90 backdrop-blur-sm |
| Medium | bg-white/70 backdrop-blur-md |
| High   | bg-white/40 backdrop-blur-lg |
