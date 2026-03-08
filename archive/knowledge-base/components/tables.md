# Tables

## Purpose
Tables render repetitive, structured dataset iterations cleanly across vertical and horizontal planes for hyper-efficient visual analysis, sorting, and actioning.

## When To Use
- Lists of users, invoices, transactional logs, or event histories
- Administration panels requiring bulk selection capabilities
- Displaying numeric metrics that require strict comparative alignment

## Structure
- Header Ribbon (Table Title, Filters, Search Bar)
- Column Headings (Categorical labels, optionally sortable)
- Row Body (Map of data entries with text, badges, or avatars)
- Action Column (Edit, delete, or view buttons usually pinned right)
- Footer Bar (Pagination and current count information)

## Variants
- Contained Table: Floats within a shadow card, encased in borders, standard for white modern dashboards.
- Flat Striped: No outer border, alternating gray and white rows for high data-density reading.
- Minimal: No vertical dividers, very sheer horizontal lines, emphasizing white space.

## Design Notes
- Avoid heavy black borders. Use `border-gray-200` or `divide-gray-200` to let data breathe.
- Table headings should be capitalized, tiny, and muted (`text-xs uppercase text-gray-500 font-medium tracking-wider`).
- Always encase the table tag itself in an `overflow-x-auto` wrapper to permit mobile horizontal swiping gracefully.
- Highlight rows on hover with `hover:bg-gray-50`.

## React Component
// Table — synthesised from AKR scraper data
export default function Table() {
  return (
    <div className="mx-auto w-full max-w-5xl rounded-xl border border-gray-200 bg-white shadow-sm">
      <div className="flex items-center justify-between border-b border-gray-200 px-6 py-4">
        <h3 className="text-base font-semibold text-gray-900">Team Members</h3>
        <button className="rounded-lg bg-gray-900 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-gray-800">Add user</button>
      </div>
      <div className="overflow-x-auto">
        <table className="w-full text-left text-sm text-gray-600">
          <thead className="bg-gray-50 text-xs uppercase tracking-wider text-gray-500 border-b border-gray-200">
            <tr>
              <th scope="col" className="px-6 py-3 font-medium">Name</th>
              <th scope="col" className="px-6 py-3 font-medium">Role</th>
              <th scope="col" className="px-6 py-3 font-medium">Status</th>
              <th scope="col" className="px-6 py-3 font-medium text-right">Actions</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-200 bg-white">
            <tr className="transition-colors hover:bg-gray-50">
              <td className="px-6 py-4">
                <div className="flex items-center gap-3">
                  <div className="flex h-8 w-8 items-center justify-center rounded-full bg-blue-100 text-xs font-semibold text-blue-700">JD</div>
                  <div>
                    <div className="font-medium text-gray-900">Jane Doe</div>
                    <div className="text-gray-500">jane@example.com</div>
                  </div>
                </div>
              </td>
              <td className="px-6 py-4 font-medium text-gray-900">Admin</td>
              <td className="px-6 py-4">
                <span className="inline-flex items-center gap-1.5 rounded-md bg-green-50 px-2.5 py-1 text-xs font-medium text-green-700 ring-1 ring-inset ring-green-600/20">
                  <span className="h-1.5 w-1.5 rounded-full bg-green-500"></span>Active
                </span>
              </td>
              <td className="px-6 py-4 text-right">
                <button className="text-gray-400 transition-colors hover:text-gray-900 mx-2 font-medium">Edit</button>
              </td>
            </tr>
            <tr className="transition-colors hover:bg-gray-50">
              <td className="px-6 py-4">
                <div className="flex items-center gap-3">
                  <div className="flex h-8 w-8 items-center justify-center rounded-full bg-gray-100 text-xs font-semibold text-gray-700">MS</div>
                  <div>
                    <div className="font-medium text-gray-900">Mike Smith</div>
                    <div className="text-gray-500">mike@example.com</div>
                  </div>
                </div>
              </td>
              <td className="px-6 py-4 text-gray-600">Editor</td>
              <td className="px-6 py-4">
                <span className="inline-flex items-center gap-1.5 rounded-md bg-gray-50 px-2.5 py-1 text-xs font-medium text-gray-600 ring-1 ring-inset ring-gray-600/20">
                  <span className="h-1.5 w-1.5 rounded-full bg-gray-400"></span>Offline
                </span>
              </td>
              <td className="px-6 py-4 text-right">
                <button className="text-gray-400 transition-colors hover:text-gray-900 mx-2 font-medium">Edit</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}
