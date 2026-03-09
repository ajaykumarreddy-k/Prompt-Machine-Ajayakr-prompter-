# LedgAI — Frontend Prompt

### Improved Prompt for React Components

Generate clean, modular React components with explicit layout instructions and specific Tailwind class hints. Each AST node should have a corresponding file without arbitrary wrappers.

**Design Language:**
- Professional
- High-tech
- Slightly futuristic

**Responsive Breakpoints:**
- Mobile (≤768px)
- Tablet (769px - 1024px)
- Desktop (≥1025px)

**Component Layout and Order:**
```jsx
// Card Component
export const Card = () => (
  <div className="relative bg-white shadow-lg rounded-lg overflow-hidden">
    {/* Content */}
  </div>
);

// Header Component
export const Header = () => (
  <header className="bg-[#1A202C] py-6 px-4 sm:px-6 lg:px-8">
    <h1 className="text-3xl font-bold text-white">LedgAI Dashboard</h1>
  </header>
);

// Sidebar Component
export const Sidebar = () => (
  <aside className="hidden md:block w-64 bg-[#2B313F] p-4">
    {/* Navigation Links */}
  </aside>
);

// Main Content Component
export const MainContent = () => (
  <main className="flex flex-col md:flex-row gap-8 px-4 sm:px-6 lg:px-8 py-6 bg-white rounded-lg shadow-md w-full max-w-screen-xl mx-auto">
    {/* Left Column */}
    <div className="w-full md:w-3/5">
      {/* Content Area */}
    </div>
    
    {/* Right Column */}
    <div className="w-full md:w-2/5">
      {/* Sidebar or Additional Content */}
    </div>
  </main>
);
```

**Tailwind Class Hints:**
- `relative` for positioning
- `bg-[#1A202C]` for dark background color
- `py-6 px-4 sm:px-6 lg:px-8` for padding with responsive adjustments
- `text-3xl font-bold text-white` for heading styles

**Responsive Notes:**
- Mobile: Use `hidden md:block` to show on tablet and desktop.
- Tablet: Ensure content reflows appropriately.
- Desktop: Optimize layout for larger screens.

Ensure all components are modular, with clear file names corresponding to their purpose.