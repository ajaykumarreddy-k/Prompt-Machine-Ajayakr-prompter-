# Footer

## Purpose
The footer serves as the absolute baseline boundary for a web page layout, housing supplementary links, legal documentation, and secondary branding reinforcing the endpoint of scrolling.

## When To Use
- Included natively at the bottom of all marketing webpages
- As a minimized variant in documentation directories
- Highly functional mega-footers acting as a massive sitemap for SEO

## Structure
- Branding Intro (Logo and catchphrase)
- Link Directories (Columns organized categorically)
- Newsletter Form (Optional capture method)
- Canonical Terminals (Copyright string, privacy policy, social links)

## Variants
- Full Multi-Column: Expansive structure covering solutions, company info, and legal links.
- Split Tone Minimal: A single dark bar emphasizing logo on left, standard links on right.
- Subscription Driven: Upper half pushes an action (newsletter signup), lower half holds boilerplate context.

## Design Notes
- Can contrast sharply using dark modes (`bg-gray-900 text-white`) or remain lightweight (`bg-white border-t border-gray-200`).
- Implement large vertical bounds to conclude the page, routinely `py-12` or `pt-16 pb-8`.
- Hyperlinks must leverage muted sizing `text-sm` with delicate hover responses like `hover:text-gray-900`.
- Category headings require robust distinction involving uppercase strings (`text-xs font-semibold tracking-widest uppercase`).

## React Component
// Footer — synthesised from AKR scraper data
export default function Footer() {
  return (
    <footer className="w-full border-t border-gray-200 bg-white">
      <div className="mx-auto max-w-7xl px-6 py-12 md:py-16">
        <div className="xl:grid xl:grid-cols-3 xl:gap-8">
          <div className="space-y-8 xl:col-span-1">
            <div className="flex items-center gap-2">
              <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-gray-900 text-white font-bold">B</div>
              <span className="text-xl font-bold tracking-tight text-gray-900">Brand</span>
            </div>
            <p className="text-sm leading-6 text-gray-500 max-w-xs">
              Designing exceptional software ecosystems, offering premium utility to engineering squads on a global scale.
            </p>
            <div className="flex space-x-4">
              <a href="#" className="text-gray-400 transition-colors hover:text-gray-500">Twitter</a>
              <a href="#" className="text-gray-400 transition-colors hover:text-gray-500">GitHub</a>
              <a href="#" className="text-gray-400 transition-colors hover:text-gray-500">Discord</a>
            </div>
          </div>
          <div className="mt-16 grid grid-cols-2 gap-8 xl:col-span-2 xl:mt-0">
            <div className="md:grid md:grid-cols-2 md:gap-8">
              <div>
                <h3 className="text-sm font-semibold text-gray-900">Solutions</h3>
                <ul className="mt-6 space-y-4">
                  <li><a href="#" className="text-sm text-gray-600 hover:text-gray-900">Marketing</a></li>
                  <li><a href="#" className="text-sm text-gray-600 hover:text-gray-900">Analytics</a></li>
                  <li><a href="#" className="text-sm text-gray-600 hover:text-gray-900">Commerce</a></li>
                </ul>
              </div>
              <div className="mt-10 md:mt-0">
                <h3 className="text-sm font-semibold text-gray-900">Support</h3>
                <ul className="mt-6 space-y-4">
                  <li><a href="#" className="text-sm text-gray-600 hover:text-gray-900">Pricing</a></li>
                  <li><a href="#" className="text-sm text-gray-600 hover:text-gray-900">Documentation</a></li>
                </ul>
              </div>
            </div>
            <div className="md:grid md:grid-cols-2 md:gap-8">
              <div>
                <h3 className="text-sm font-semibold text-gray-900">Company</h3>
                <ul className="mt-6 space-y-4">
                  <li><a href="#" className="text-sm text-gray-600 hover:text-gray-900">About</a></li>
                  <li><a href="#" className="text-sm text-gray-600 hover:text-gray-900">Blog</a></li>
                </ul>
              </div>
              <div className="mt-10 md:mt-0">
                <h3 className="text-sm font-semibold text-gray-900">Legal</h3>
                <ul className="mt-6 space-y-4">
                  <li><a href="#" className="text-sm text-gray-600 hover:text-gray-900">Privacy Policy</a></li>
                  <li><a href="#" className="text-sm text-gray-600 hover:text-gray-900">Terms of Service</a></li>
                </ul>
              </div>
            </div>
          </div>
        </div>
        <div className="mt-16 flex flex-col items-center justify-between border-t border-gray-200 pt-8 sm:mt-20 sm:flex-row lg:mt-24">
          <p className="text-sm text-gray-500">&copy; 2024 Brand Inc. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
}
