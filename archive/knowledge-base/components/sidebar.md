# Sidebar

## Purpose
The sidebar dictates local area routing in dense applications, remaining stubbornly anchored while inner content changes, establishing strong operational memory.

## When To Use
- Inside authenticated dashboards
- During deeply nested documentation flows
- Applications divided into many independent feature verticals

## Structure
- Branding Bar (Logo + Name, typically matching the height of standard horizontal navbars)
- Action Block (Quick "Create" or "Search" functions at the top)
- Navigation List (Vertically stacked active/inactive routing links)
- Settings/Profile Anchor (Fixed to the bottom of the column)

## Variants
- Full Fixed: Stays 250px-300px wide, persistently visible on desktop.
- Mini Rail: Collapses down to just an icon list (70px wide) to maximize workspace.
- Offcanvas Drawer: The mobile equivalent, completely hidden until summoned.

## Design Notes
- Differentiate the sidebar background slightly from the main content (e.g., `bg-gray-50` sidebar vs `bg-white` main).
- Active states must pop immediately — use a highlighted background like `bg-blue-50` and vivid text `text-blue-700`.
- Inactive links should be highly readable but subdued like `text-gray-600 hover:bg-gray-100`.
- Ensure it takes full screen height `h-screen` and applies `overflow-y-auto`.

## React Component
// Sidebar — synthesised from AKR scraper data
export default function Sidebar() {
  return (
    <aside className="fixed inset-y-0 left-0 flex w-64 flex-col border-r border-gray-200 bg-gray-50">
      <div className="flex shrink-0 items-center border-b border-gray-200 px-6 h-16">
        <div className="h-8 w-8 rounded bg-gray-900 text-white flex items-center justify-center font-bold mr-3">D</div>
        <span className="text-lg font-bold text-gray-900">Dashboard</span>
      </div>
      <div className="flex-1 overflow-y-auto px-4 py-6">
        <nav className="flex flex-col gap-y-1">
          <a href="#" className="flex items-center gap-x-3 rounded-lg bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-gray-200">
            <svg className="h-5 w-5 text-gray-900" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
            Home
          </a>
          <a href="#" className="flex items-center gap-x-3 rounded-lg px-3 py-2 text-sm font-medium text-gray-600 transition-colors hover:bg-gray-100 hover:text-gray-900">
            <svg className="h-5 w-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"/></svg>
            Team
          </a>
          <a href="#" className="flex items-center gap-x-3 rounded-lg px-3 py-2 text-sm font-medium text-gray-600 transition-colors hover:bg-gray-100 hover:text-gray-900">
            <svg className="h-5 w-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>
            Analytics
          </a>
        </nav>
      </div>
      <div className="shrink-0 border-t border-gray-200 p-4">
        <a href="#" className="flex items-center gap-x-3 rounded-lg p-2 transition-colors hover:bg-gray-100 cursor-pointer">
          <div className="flex h-9 w-9 items-center justify-center rounded-full bg-blue-100 text-sm font-bold text-blue-700">AK</div>
          <div className="flex flex-col text-sm">
            <span className="font-semibold text-gray-900">Alex Knight</span>
            <span className="text-xs text-gray-500">View profile</span>
          </div>
        </a>
      </div>
    </aside>
  );
}
