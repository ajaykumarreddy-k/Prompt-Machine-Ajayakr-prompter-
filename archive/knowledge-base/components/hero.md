# Hero

## Purpose
The hero dictates the first impression of a page, quickly conveying the core value proposition and demanding an immediate user action.

## When To Use
- At the top of any product introduction page
- Marketing landing pages directing to a single funnel
- Whenever massive visual emphasis and a strong CTA are necessary

## Structure
- Primary Headline (H1, visually dominant)
- Subhealine / Context Paragraph (Descriptive, medium text size)
- Primary Action Group (Main CTA button + Secondary Link)
- Visual Asset (Dashboard illustration, abstract gradient, or product image)

## Variants
- Text-Centric: Centered large typography with no image, reliant on a subtle gradient mesh background.
- Split Layout: Left-aligned typography and CTA, right-aligned floating product image.
- Background Visual: Image or video filling the entire container with dark overlay and white text.

## Design Notes
- The headline must utilize `tracking-tight` and `font-extrabold` to look punchy.
- Apply high vertical margins (`py-24` or `py-32`) to isolate the message.
- A primary CTA should have high contrast (e.g., pure black or strong primary color).
- Supporting sub-text should be faded (`text-gray-500` or `text-gray-600`) to enforce hierarchy.

## React Component
// Hero — synthesised from AKR scraper data
export default function Hero() {
  return (
    <section className="relative overflow-hidden bg-white px-6 py-32 sm:py-40">
      <div className="absolute inset-x-0 -top-40 -z-10 transform-gpu overflow-hidden blur-3xl sm:-top-80">
        <div className="relative left-[calc(50%-11rem)] aspect-[1155/678] w-[36.125rem] -translate-x-1/2 rotate-[30deg] bg-gradient-to-tr from-[#ff80b5] to-[#9089fc] opacity-30 sm:left-[calc(50%-30rem)] sm:w-[72.1875rem]"></div>
      </div>
      <div className="mx-auto max-w-4xl text-center">
        <h1 className="text-5xl font-extrabold tracking-tight text-gray-900 sm:text-7xl">
          Build faster with <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-violet-600">modern tools</span>
        </h1>
        <p className="mt-6 text-lg leading-8 text-gray-600 sm:text-xl">
          Streamline your workflow, increase velocity, and deploy scalable systems directly from your terminal using our comprehensive unified platform.
        </p>
        <div className="mt-10 flex items-center justify-center gap-x-6">
          <a href="#" className="rounded-xl bg-gray-900 px-6 py-3 text-sm font-semibold text-white shadow-sm hover:bg-gray-800 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-gray-900">
            Get started
          </a>
          <a href="#" className="text-sm font-semibold leading-6 text-gray-900 group">
            Learn more <span className="inline-block transition-transform group-hover:translate-x-1">→</span>
          </a>
        </div>
      </div>
    </section>
  );
}
