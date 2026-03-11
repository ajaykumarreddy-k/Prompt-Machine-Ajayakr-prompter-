# Portfolio — Frontend Prompt

### Improved Prompt

Generate clean, modular React components for a professional portfolio website. Follow the layout instructions explicitly, ensuring exact component order and column counts. Use specific Tailwind class hints for the AI to follow. Strengthen the design language description with precise aesthetic details. Include responsive breakpoint notes (mobile → tablet → desktop). Ensure the tone is professional and focused on the portfolio. Output only the components, with each AST node corresponding to a file.

#### Layout Instructions

1. **Hero Section**
   - `Hero` component
   - Order: `Hero`
   - Classes: `bg-gradient-to-br from-blue-600 to-indigo-600 p-8 text-white flex flex-col items-center justify-center`
   - Breakpoints: 
     - Mobile: `max-w-sm`
     - Tablet: `max-w-md`
     - Desktop: `max-w-xl`

2. **About Section**
   - `About` component
   - Order: `About Hero`
   - Classes: `grid grid-cols-1 md:grid-cols-2 p-8 gap-8`
   - Breakpoints: 
     - Mobile: `max-w-sm`
     - Tablet: `max-w-md`
     - Desktop: `max-w-xl`

3. **Portfolio Section**
   - `Portfolio` component
   - Order: `About Hero`
   - Classes: `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 p-8 gap-8`
   - Breakpoints: 
     - Mobile: `max-w-sm`
     - Tablet: `max-w-md`
     - Desktop: `max-w-xl`

4. **Skills Section**
   - `Skills` component
   - Order: `Portfolio About Hero`
   - Classes: `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 p-8 gap-8`
   - Breakpoints: 
     - Mobile: `max-w-sm`
     - Tablet: `max-w-md`
     - Desktop: `max-w-xl`

5. **Testimonials Section**
   - `Testimonials` component
   - Order: `Skills Portfolio About Hero`
   - Classes: `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 p-8 gap-8`
   - Breakpoints: 
     - Mobile: `max-w-sm`
     - Tablet: `max-w-md`
     - Desktop: `max-w-xl`

6. **Contact Section**
   - `Contact` component
   - Order: `Testimonials Skills Portfolio About Hero`
   - Classes: `p-8`
   - Breakpoints: 
     - Mobile: `max-w-sm`
     - Tablet: `max-w-md`
     - Desktop: `max-w-xl`

#### Design Language

- **Aesthetic**: Modern, clean, and minimalistic. Use a color palette of blue, indigo, and white.
- **Typography**: Roboto font family. Headings in `font-bold` and body text in `font-normal`.
- **Spacing**: Use consistent spacing with `p-4`, `p-6`, and `p-8` for padding.

#### Components

1. **Hero Component**
   - `Hero.tsx`
   - Classes: `bg-gradient-to-br from-blue-600 to-indigo-600 p-8 text-white flex flex-col items-center justify-center`

2. **About Component**
   - `About.tsx`
   - Classes: `grid grid-cols-1 md:grid-cols-2 p-8 gap-8`

3. **Portfolio Component**
   - `Portfolio.tsx`
   - Classes: `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 p-8 gap-8`

4. **Skills Component**
   - `Skills.tsx`
   - Classes: `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 p-8 gap-8`

5. **Testimonials Component**
   - `Testimonials.tsx`
   - Classes: `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 p-8 gap-8`

6. **Contact Component**
   - `Contact.tsx`
   - Classes: `p-8`