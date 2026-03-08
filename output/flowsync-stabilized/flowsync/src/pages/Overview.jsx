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
    </div>
  );
};

export default Overview;
