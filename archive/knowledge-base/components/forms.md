# Forms

## Purpose
Forms gather structured inputs from users, acting as the bridge for data entry, authentication flows, and profile management across applications.

## When To Use
- Login and registration walls
- Newsletter opt-in fields on marketing pages
- Product configuration options inside dashboards
- Updating system settings

## Structure
- Form Header (Greeting, Context or Title)
- Field Blocks (Visually grouped labels, inputs, and helper text)
- Interacting Elements (Checkboxes, Toggles, Select drop-downs)
- Validation Feedback (Red error states below inputs)
- Primary Action Trigger (Submit Button)

## Variants
- Centered Login Card: A floating card focusing completely on email/password collection.
- Inline Newsletter: A single row combining input and button natively into a layout.
- Vertical Dashboard Stack: Form flows grouped in standard layout columns.

## Design Notes
- Every input must be securely coupled with a visible, accessible `<label>`.
- Generous gap spacing (`space-y-4` or `space-y-6`) is required to easily identify input boundaries.
- Inputs must feature distinct focus rings (`focus:ring-2 focus:ring-blue-500 focus:border-blue-500`) to confirm keyboard navigation actively.
- Button width typically expands mapping to the input widths via `w-full` for cleaner alignment.

## React Component
// Form — synthesised from AKR scraper data
export default function Form() {
  return (
    <div className="flex min-h-screen items-center justify-center p-4 bg-gray-50">
      <div className="w-full max-w-sm rounded-2xl border border-gray-200 bg-white p-8 shadow-sm">
        <div className="mb-6 text-center">
          <h2 className="text-2xl font-bold tracking-tight text-gray-900">Welcome back</h2>
          <p className="mt-2 text-sm text-gray-500">Enter your details to access your account</p>
        </div>
        <form className="space-y-5" onSubmit={(e) => e.preventDefault()}>
          <div>
            <label htmlFor="email" className="mb-1.5 block text-sm font-medium text-gray-900">Email address</label>
            <input 
              type="email" 
              id="email" 
              className="block w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-gray-900 placeholder-gray-400 outline-none transition-all focus:border-blue-500 focus:ring-2 focus:ring-blue-500/20" 
              placeholder="you@company.com" 
            />
          </div>
          <div>
            <div className="mb-1.5 flex items-center justify-between">
              <label htmlFor="password" className="block text-sm font-medium text-gray-900">Password</label>
              <a href="#" className="text-xs font-semibold text-blue-600 hover:text-blue-500">Forgot password?</a>
            </div>
            <input 
              type="password" 
              id="password" 
              className="block w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-gray-900 placeholder-gray-400 outline-none transition-all focus:border-blue-500 focus:ring-2 focus:ring-blue-500/20" 
              placeholder="••••••••" 
            />
          </div>
          <button 
            type="submit" 
            className="mt-2 flex w-full items-center justify-center rounded-lg bg-gray-900 px-4 py-2.5 text-sm font-semibold text-white shadow-sm transition-colors hover:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-gray-900 focus:ring-offset-2 active:scale-95"
          >
            Sign in
          </button>
        </form>
        <div className="mt-8 text-center text-sm text-gray-500">
          Not a member? <a href="#" className="font-semibold text-blue-600 hover:text-blue-500">Create an account</a>
        </div>
      </div>
    </div>
  );
}
