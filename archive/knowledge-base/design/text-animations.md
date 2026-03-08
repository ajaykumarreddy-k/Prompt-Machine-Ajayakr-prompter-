# Text Animations

## Global Rules
- Maximum one animated element per section
- Must complete within 800ms
- Must not reduce readability at any point
- Must respect prefers-reduced-motion
- Applied primarily to hero headings and page titles

## Animations

### Fade In Up

**Purpose**
Executes a highly organic entry dynamic for dense typography grids pulling attention immediately into focus lines.

**Best Applied To**
- H1 inside a Landing Page Hero Section
- Major heading text appearing upon viewport scroll entry

**Tailwind Implementation**
```html
<h1 className="animate-[fade-in-up_0.8s_ease-out_forwards] opacity-0 text-5xl font-extrabold text-gray-900 motion-reduce:animate-none motion-reduce:opacity-100">
  Animated Headline
</h1>

<!-- Required tailwind.config.js extend payload -->
// keyframes: {
//   'fade-in-up': {
//     '0%': { opacity: '0', transform: 'translateY(20px)' },
//     '100%': { opacity: '1', transform: 'translateY(0)' },
//   }
// }
```

**Accessibility**
Uses `motion-reduce:animate-none` to instantaneously mount the element, halting all animation processing for necessary audiences.

### Typewriter Focus

**Purpose**
Manufactures extreme focal density exactly on specific action phrases inside headings simulating terminal input.

**Best Applied To**
- Highlighted subset spans enclosed within a larger static H1 (e.g., "Build your [next great app]").

**Tailwind Implementation**
```html
<span className="inline-block animate-[pulse_1.5s_infinite] border-r-2 border-blue-600 bg-clip-text text-transparent bg-gradient-to-r from-blue-600 to-indigo-600 pr-1 motion-reduce:animate-none">
  next great app
</span>
```

**Accessibility**
Stops recursive pulsing entirely assuming `motion-reduce` environments detected to prevent strobe disorientation constraints.
