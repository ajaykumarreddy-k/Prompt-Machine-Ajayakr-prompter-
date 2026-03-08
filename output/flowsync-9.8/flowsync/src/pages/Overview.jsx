import React from 'react';
import Navbar from '../components/Navbar';
import StatCard from '../components/StatCard';
import ActivityFeed from '../components/ActivityFeed';
import BenefitsSection from '../components/BenefitsSection';
import PricingPreview from '../components/PricingPreview';
import DataGrid from '../components/DataGrid';
import UserMenu from '../components/UserMenu';
import HeroSection from '../components/HeroSection';
import TestimonialsSection from '../components/TestimonialsSection';
import FeaturesSection from '../components/FeaturesSection';
import ProductShowcase from '../components/ProductShowcase';
import ChartWidget from '../components/ChartWidget';
import CTASection from '../components/CTASection';

const Overview = () => {
  const stats = [
    { value: '10K+', label: 'Users' },
    { value: '500+', label: 'Projects' }
  ];

  return (
    <div>
      <Navbar />
      <HeroSection title="FlowSync" subtitle="Transform Your Workflow with Seamless Collaboration and Automation." />
      <StatCard stats={stats} />
      <ActivityFeed />
      <BenefitsSection />
      <PricingPreview />
      <DataGrid items={[
        { id: 1, name: 'Project A', status: 'In Progress', dueDate: '2023-10-30' },
        { id: 2, name: 'Project B', status: 'Completed', dueDate: '2023-10-25' }
      ]} />
      <UserMenu />
      <TestimonialsSection testimonials={[
        { text: "FlowSync has revolutionized the way we collaborate on projects.", author: "John Doe" },
        { text: "The automation features save us so much time and effort.", author: "Jane Smith" }
      ]} />
      <FeaturesSection features={[
        { title: 'Real-time Task Syncing', description: 'Stay updated with real-time task updates.' },
        { title: 'Collaborative Tools', description: 'Enhance teamwork with integrated communication tools.' },
        { title: 'Automated Workflows', description: 'Streamline your processes with automated workflows.' },
        { title: 'Detailed Analytics', description: 'Gain insights into project performance and progress.' }
      ]} />
      <ProductShowcase products={[
        { name: 'Basic Plan', description: 'Unlimited tasks for a single user. Email support included.' },
        { name: 'Pro Plan', description: 'Unlimited tasks for up to 5 users. Chat and email support included.' }
      ]} />
      <ChartWidget data={[] /* Placeholder for chart data */} />
      <CTASection title="Join the Flow" description="Experience the future of project management today." buttonLabel="Sign Up" buttonText="Get Started" />
    </div>
  );
};

export default Overview;
