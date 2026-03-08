# FlowSync — Frontend Prompt

Create a modern, high-performance SaaS application named FlowSync using an AI UI builder like v0.dev, Lovable, or Bolt. Follow the provided AST blueprint strictly to ensure consistent and structured development. 

### Folder Structure:
- `src/pages/Overview.jsx`
- `src/pages/Analytics.jsx`
- `src/pages/Settings.jsx`
- `src/components/Navbar.jsx`
- `src/components/StatCard.jsx`
- `src/components/ActivityFeed.jsx`
- `src/components/CTASection.jsx`
- `src/components/TestimonialsSection.jsx`
- `src/components/UserMenu.jsx`
- `src/components/PricingPreview.jsx`
- `src/components/DataGrid.jsx`
- `src/components/HeroSection.jsx`
- `src/components/FeaturesSection.jsx`
- `src/components/ProductShowcase.jsx`
- `src/components/BenefitsSection.jsx`
- `src/components/ChartWidget.jsx`
- `src/components/Footer.jsx`

### Routing:
Define routes for the following paths:
1. `/` - Overview
2. `/analytics` - Analytics
3. `/settings` - Settings

### Blueprint Components and Responsibilities:

#### Overview Page (src/pages/Overview.jsx)
```jsx
import { Route, Routes } from 'react-router-dom';
import Navbar from '../components/Navbar';
import StatCard from '../components/StatCard';
import ActivityFeed from '../components/ActivityFeed';
import CTASection from '../components/CTASection';
import TestimonialsSection from '../components/TestimonialsSection';
import UserMenu from '../components/UserMenu';
import PricingPreview from '../components/PricingPreview';
import DataGrid from '../components/DataGrid';
import HeroSection from '../components/HeroSection';
import FeaturesSection from '../components/FeaturesSection';
import ProductShowcase from '../components/ProductShowcase';
import BenefitsSection from '../components/BenefitsSection';
import ChartWidget from '../components/ChartWidget';
import Footer from '../components/Footer';

const Overview = () => {
  return (
    <div className="flex flex-col min-h-screen">
      <Navbar />
      <HeroSection title="FlowSync" description="Empower your high-performance teams with real-time task boards and seamless collaboration." />
      <FeaturesSection features={['Dynamic Task Boards', 'Real-Time Syncing', 'Team Collaboration Tools', 'Workflow Automation', 'Detailed Analytics']} />
      <ProductShowcase products={["Task Management", "Chat & Comments", "Shared Docs", "Automation"]} />
      <BenefitsSection benefits={['Efficient Workflow', 'Enhanced Communication', 'Data-Driven Insights', 'Customizable Workflows']} />
      <ChartWidget data={/* Insert sample data here */} />
      <StatCard stats={/* Insert sample statistics here */} />
      <ActivityFeed items={/* Insert recent activities or events here */} />
      <CTASection />
      <TestimonialsSection testimonials={/* Insert customer testimonials here */} />
      <UserMenu />
      <PricingPreview pricing={/* Insert pricing options here */} />
      <DataGrid items={/* Insert sample data grid items here */} />
      <Footer />
    </div>
  );
};

export default Overview;
```

#### Analytics Page (src/pages/Analytics.jsx)
```jsx
import { Route, Routes } from 'react-router-dom';
import Navbar from '../components/Navbar';
import ChartWidget from '../components/ChartWidget';
import DataGrid from '../components/DataGrid';
import Footer from '../components/Footer';

const Analytics = () => {
  return (
    <div className="flex flex-col min-h-screen">
      <Navbar />
      <ChartWidget data={/* Insert sample analytics data here */} />
      <DataGrid items={/* Insert sample data grid items here */} />
      <Footer />
    </div>
  );
};

export default Analytics;
```

#### Settings Page (src/pages/Settings.jsx)
```jsx
import { Route, Routes } from 'react-router-dom';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';

const Settings = () => {
  return (
    <div className="flex flex-col min-h-screen">
      <Navbar />
      <Footer />
    </div>
  );
};

export default Settings;
```

### App Routing (src/App.jsx)
```jsx
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Overview from './pages/Overview';
import Analytics from './pages/Analytics';
import Settings from './pages/Settings';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Overview />} />
        <Route path="/analytics" element={<Analytics />} />
        <Route path="/settings" element={<Settings />} />
      </Routes>
    </Router>
  );
};

export default App;
```

### Design Tokens and Palette
Ensure all components use the following design tokens:
- Palette: Minimal Editorial (Primary: zinc-900, Secondary: zinc-500, Accent: red-500)
- Tailwind CSS classes like `max-w-7xl`, `px-6`, `py-16`, `rounded-lg`, and `bg-zinc-50` for consistent styling.

### Component Implementation
Each component should strictly follow the responsibilities outlined in the AST. Use Tailwind CSS for layout and styling, ensuring a modern and clean design.

This structure ensures that FlowSync is developed with a clear, modular approach, adhering to the provided blueprint and design constraints.