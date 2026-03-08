# FlowSync — Frontend Prompt

Create a modern, high-performance SaaS application named FlowSync using an AI UI builder like v0.dev, Lovable, or Bolt. Follow the provided AST blueprint strictly to ensure consistency and coherence across all pages. 

### Overview Page:
- **Navbar**: Implement navigation options for users.
- **StatCard**: Display key statistics related to user performance or project status.
- **ActivityFeed**: Show recent activities within the application.
- **HeroSection**: Highlight main features or benefits of FlowSync, such as real-time task syncing and workflow automation.
- **CTASection**: Encourage users to take action by providing clear calls-to-action with relevant links.
- **ChartWidget**: Display interactive charts or graphs for analytics and reporting.
- **FeaturesSection**: List key features like dynamic task boards, team collaboration tools, and workflow automation engine.
- **TestimonialsSection**: Showcase customer testimonials to build trust and credibility.
- **ProductShowcase**: Highlight product offerings such as different plans and services.
- **DataGrid**: Display tabular data for detailed analytics and reporting.
- **UserMenu**: Provide user account options like profile settings or logout.
- **BenefitsSection**: List key benefits of FlowSync, emphasizing high performance and team collaboration.
- **PricingPreview**: Show pricing plans with clear comparisons.
- **Footer**: Include footer links and contact information.

### Analytics Page:
- **Navbar**: Implement navigation options for users.
- **ChartWidget**: Display interactive charts or graphs related to analytics data.
- **DataGrid**: Present tabular data for detailed analysis.
- **Footer**: Include footer links and contact information.

### Settings Page:
- **Navbar**: Implement navigation options for users.
- **Footer**: Include footer links and contact information.

### Architecture Constraints:
1. **DETERMINISTIC COMPONENT MAPPING**: Ensure every component name in the AST corresponds to exactly one file in `src/components/`.
2. **NO HALLUCINATIONS**: Use raw HTML with Tailwind tokens; do not add components or layout primitives like `<Container>`, `<Section>`, or `<Wrapper>`.
3. **COMPONENT RESPONSIBILITIES**: Follow the 'responsibilities' array in the AST to implement logic for each block.
4. **ROUTING**: Define routes using `react-router-dom` for: `/`, `/analytics`, and `/settings`.
5. **FOLDER STRUCTURE**:
   - `src/pages/`: Overview, Analytics, Settings
   - `src/components/`: All individual UI blocks.
   - `src/App.jsx`: The routing hub.

### Design System Tokens (STRICT):
- Use the Minimal Editorial palette: Primary color (`zinc-900`), Secondary color (`zinc-500`), and Accent color (`red-500`).
- Apply design tokens like `max-w-7xl`, `px-6`, `py-16`, `rounded-lg`, and `bg-zinc-50` where applicable.

Ensure all components are implemented in their respective files within the `src/components/` directory, adhering strictly to the provided AST blueprint.