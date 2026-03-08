# FlowSync — Frontend Prompt

### Frontend Development Prompt for FlowSync

#### Overview:
Develop the frontend of FlowSync, a SaaS application designed for high-performance teams. The application features dynamic task boards with real-time syncing, team collaboration tools (chat, comments, shared docs), workflow automation engine, and detailed analytics.

#### Blueprint as Single Source of Truth:
Follow the provided AST structure strictly to ensure consistency across the application. Each page and component must adhere to its defined responsibilities.

#### Folder Structure:
- `src/pages/`: Overview, Analytics, Settings
- `src/components/`: Navbar, StatCard, ActivityFeed, DataGrid, FeaturesSection, ProductShowcase, PricingPreview, HeroSection, UserMenu, ChartWidget, TestimonialsSection, BenefitsSection, CTASection, Footer

#### Design System Tokens:
- Palette: Minimal Editorial (Primary: zinc-900, Secondary: zinc-500, Accent: red-500)
- Tailwind CSS classes: `max-w-7xl`, `px-6`, `py-16`, `rounded-lg`, `bg-zinc-50`

#### Routing:
Define routes for `/`, `/analytics`, and `/settings` using `react-router-dom`.

#### Component Responsibilities:
1. **Navbar**: Provides navigation options.
2. **StatCard**: Displays statistical information.
3. **ActivityFeed**: Shows recent activities or events.
4. **DataGrid**: Offers a grid view for data representation and manipulation.
5. **FeaturesSection**: Highlights key features of the application.
6. **ProductShowcase**: Displays products/services offered by the company.
7. **PricingPreview**: Provides pricing plans preview.
8. **HeroSection**: Serves as an introduction or call-to-action section.
9. **UserMenu**: Provides user-specific options and settings.
10. **ChartWidget**: Displays interactive charts for data visualization.
11. **TestimonialsSection**: Shows customer testimonials.
12. **BenefitsSection**: Lists the benefits of using the application.
13. **CTASection**: Encourages users to take specific actions.
14. **Footer**: Provides additional navigation and contact information.

#### Implementation Instructions:
- **Overview Page**:
  - Implement a `Navbar` component with links to `/analytics`, `/settings`.
  - Add a `HeroSection` with "FlowSync for High-Performance Teams" as the title and a brief description.
  - Include a `StatCard` displaying key metrics like total tasks, active users, etc.
  - Display recent activities using an `ActivityFeed` component.
  - Highlight features of FlowSync in a `FeaturesSection`.
  - Showcase products/services with a `ProductShowcase` component.
  - Provide pricing plans preview with a `PricingPreview` component.
  - Include testimonials and benefits sections.
  - Add a CTA section encouraging users to sign up or learn more.

- **Analytics Page**:
  - Implement a `Navbar` component with links back to the overview page.
  - Use a `ChartWidget` for data visualization.
  - Provide a `DataGrid` for detailed analytics and reporting.
  - Include a footer with navigation options and contact information.

- **Settings Page**:
  - Implement a `Navbar` component with links back to the overview page.
  - Add a footer with additional navigation and contact information.

#### Component Files:
Ensure each component is placed in its designated folder (`src/components/`). For example, `Navbar.jsx`, `StatCard.jsx`, etc. Use Tailwind CSS classes for styling as per the design system tokens.

#### Routing Setup:
- Import necessary components from `src/components/`.
- Define routes in `src/App.jsx` using `react-router-dom`.

```jsx
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Overview from './pages/Overview';
import Analytics from './pages/Analytics';
import Settings from './pages/Settings';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Overview />} />
        <Route path="/analytics" element={<Analytics />} />
        <Route path="/settings" element={<Settings />} />
      </Routes>
    </Router>
  );
}

export default App;
```

#### Testing and Validation:
- Ensure all components are responsive and visually consistent.
- Test real-time syncing functionality in the task boards.
- Validate that navigation works seamlessly across pages.

By following these instructions, you will create a modern, user-friendly interface for FlowSync that adheres to the provided structural blueprint.