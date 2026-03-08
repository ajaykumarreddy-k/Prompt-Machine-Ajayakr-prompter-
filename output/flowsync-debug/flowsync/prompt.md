# FlowSync — Frontend Prompt

Create a modern, high-performance SaaS application named FlowSync using an AI UI builder like v0.dev, Lovable, or Bolt. Follow the provided AST blueprint strictly to ensure consistency and coherence across all pages.

### Page Structure:
1. **Overview** (`src/pages/Overview.jsx`):
   - Define routes: `/`
   - Layout: `PageLayout`
     - Navbar
     - StatCard (title: "Tasks", stats: dynamic task count)
     - ActivityFeed (items: recent activities)
     - ProductShowcase (title: "FlowSync", items: featured products/services)
     - DataGrid (data: tasks, filters: status, priority)
     - PricingPreview
     - HeroSection (title: "Streamline Your Workflow", description: "Empower your high-performance teams with real-time task boards and collaborative tools.")
     - TestimonialsSection (testimonials: customer reviews)
     - ChartWidget (data: workflow metrics)
     - CTASection
     - BenefitsSection (benefits: dynamic list of key benefits)
     - FeaturesSection (features: detailed features like task boards, chat, automation, analytics)
     - UserMenu
     - Footer

2. **Analytics** (`src/pages/Analytics.jsx`):
   - Define route: `/analytics`
   - Layout: `PageLayout`
     - Navbar
     - ChartWidget (data: analytics data)
     - DataGrid (data: detailed analytics, filters: date range, category)
     - Footer

3. **Settings** (`src/pages/Settings.jsx`):
   - Define route: `/settings`
   - Layout: `PageLayout`
     - Navbar
     - Footer

### Component Mapping:
- Ensure each component name in the AST corresponds to exactly one file in `src/components/`.
- Use raw HTML with Tailwind tokens, adhering strictly to the design system tokens provided.

### Routing and Navigation:
- Implement routing using `react-router-dom` for `/`, `/analytics`, and `/settings`.
- Define routes in `src/App.jsx`.

### Folder Structure:
- Organize files as follows:
  - `src/pages/`: Overview.jsx, Analytics.jsx, Settings.jsx
  - `src/components/`: Navbar.jsx, StatCard.jsx, ActivityFeed.jsx, ProductShowcase.jsx, DataGrid.jsx, PricingPreview.jsx, HeroSection.jsx, TestimonialsSection.jsx, ChartWidget.jsx, CTASection.jsx, BenefitsSection.jsx, FeaturesSection.jsx, UserMenu.jsx, Footer.jsx

### Design Tokens:
- Use Tailwind CSS classes such as `max-w-7xl`, `px-6`, `py-16`, `rounded-lg`, and `bg-zinc-50` where applicable.
- Apply the Minimal Editorial palette: Primary (zinc-900), Secondary (zinc-500), Accent (red-500).

### Implementation Steps:
1. **Set Up Routing**: Configure routing in `src/App.jsx`.
2. **Create Components**: Develop each component based on its responsibilities.
3. **Implement Logic**: Ensure each component's logic aligns with the provided AST and design tokens.
4. **Test**: Validate the application’s responsiveness, performance, and visual consistency.

By following these instructions precisely, you will create a cohesive and functional SaaS application for high-performance teams that leverages real-time task boards, collaboration tools, workflow automation, and detailed analytics.