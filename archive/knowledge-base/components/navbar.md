# Navbar

## Purpose
The navigation bar operates as the primary orienting element for the application, providing users global routing access and housing critical brand identity and top-level actions.

## When To Use
- At the global top of all marketing and landing pages
- Across internal pages to maintain consistent cross-navigation
- When clear access to features, pricing, and authentication is required

## Structure
- Branding Container (Logo + Application Name)
- Primary Navigation Links (Desktop)
- Secondary Actions (Log In / Sign Up buttons)
- Mobile Collapse Toggle (Hamburger Menu)

## Variants
- Simple Brand + Auth: Basic layout with brand on left, auth on right.
- Centered Links: Links sit symmetrically in the center for marketing focus.
- Glassmorphism: Sticky transparent navbar with backdrop blur effect.

## Design Notes
- Utilize `backdrop-blur-md` and `bg-white/80` for a modern glass effect.
- Horizontal padding should be generous (`px-6` or `px-8`).
- Links should rely on hover transitions (e.g., `hover:text-primary-600` and `transition-colors duration-200`).
- Ensure the mobile menu falls cleanly into a vertical list below `md` breakpoint.

## React Component
// Navbar — synthesised from AKR scraper data
export default function Navbar() {
  return (
    <nav className="sticky top-0 z-50 w-full border-b border-gray-100 bg-white/80 px-6 py-4 text-sm font-medium backdrop-blur-md">
      <div className="mx-auto flex max-w-7xl items-center justify-between">
        <div className="flex items-center gap-2">
          <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-blue-600 text-white font-bold">B</div>
          <span className="text-xl font-bold tracking-tight text-gray-900">Brand</span>
        </div>
        <div className="hidden items-center gap-8 md:flex">
          <a href="#" className="text-gray-600 transition-colors hover:text-gray-900">Features</a>
          <a href="#" className="text-gray-600 transition-colors hover:text-gray-900">Pricing</a>
          <a href="#" className="text-gray-600 transition-colors hover:text-gray-900">Docs</a>
        </div>
        <div className="flex items-center gap-4">
          <a href="#" className="hidden text-gray-600 transition-colors hover:text-gray-900 md:block">Log in</a>
          <a href="#" className="rounded-lg bg-gray-900 px-4 py-2 text-white transition-colors hover:bg-gray-800">Sign up</a>
        </div>
      </div>
    </nav>
  );
}
