import { useState } from 'react';
import HeroSection from '../components/HeroSection';
import StatCard from '../components/StatCard';
import ActivityFeed from '../components/ActivityFeed';
import BenefitsSection from '../components/BenefitsSection';

const Overview = () => {
  return (
    <div className="max-w-7xl mx-auto px-6 py-12">
      <HeroSection title="Welcome to FlowSync" description="Empower your team with seamless collaboration and automation." />
      <StatCard title="Tasks Completed" stats="5,000+" />
      <ActivityFeed items={['Task assigned', 'Comment added', 'Document shared']} />
      <BenefitsSection />
    </div>
  );
};

export default Overview;
