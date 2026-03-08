# Cards

## Purpose
Cards encapsulate discrete data objects into unified, digestible surface areas that imply interaction or summarize rich structures.

## When To Use
- To display grids of pricing plans, features, or team members
- Representing physical objects or distinct digital files (e.g., projects, repos)
- Acting as entry points to deeper content views

## Structure
- Header/Visual (Icon, avatar, or banner image)
- Title Element
- Body Content (Text paragraph or metric array)
- Footer/Action (Action buttons or interaction hints)

## Variants
- Feature Card: Top-aligned icon, strong title, descriptive text.
- Stat Card: Huge typography displaying a metric, smaller label text, often possessing a trend indicator element.
- Profile Card: Centered avatar, bolded name, subtle role text, social links.

## Design Notes
- Rely on subtle borders (`border-gray-200`) and slight shadows (`shadow-sm`) to define edges.
- Provide ample inner padding (`p-6` or `p-8`).
- For hover states, elevate the card (`hover:shadow-md`) and perhaps slightly translate it on the Y-axis (`hover:-translate-y-1 transition-all`).
- When grouped, use a CSS grid with gaps (`grid-cols-1 md:grid-cols-3 gap-6`).

## React Component
// Card — synthesised from AKR scraper data
export default function Card() {
  return (
    <div className="group relative flex flex-col items-start justify-between rounded-2xl border border-gray-200 bg-white p-6 shadow-sm transition-all duration-200 hover:-translate-y-1 hover:shadow-md cursor-pointer overflow-hidden">
      <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-blue-50 text-blue-600 mb-4 transition-transform group-hover:scale-110">
        <svg fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="h-6 w-6">
          <path strokeLinecap="round" strokeLinejoin="round" d="M3.75 13.5l10.5-11.25L12 10.5h8.25L9.75 21.75 12 13.5H3.75z" />
        </svg>
      </div>
      <h3 className="mb-2 text-lg font-semibold text-gray-900">Lightning Velocity</h3>
      <p className="mb-6 text-sm leading-relaxed text-gray-600">
        Deploy globally distributed assets in milliseconds natively via edge architecture. Avoid long cold starts and build times.
      </p>
      <div className="mt-auto flex items-center text-sm font-semibold text-blue-600">
        Read docs
        <svg className="ml-1 h-4 w-4 transition-transform group-hover:translate-x-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
        </svg>
      </div>
    </div>
  );
}
