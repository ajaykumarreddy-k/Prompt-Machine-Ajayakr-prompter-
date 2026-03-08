import React from 'react';
import Section from '../components/Section';
import Stack from '../components/Stack';
import Navbar from '../components/Navbar';
import HeroSection from '../components/HeroSection';
import ProductShowcase from '../components/ProductShowcase';
import TestimonialsSection from '../components/TestimonialsSection';
import BenefitsSection from '../components/BenefitsSection';
import FeaturesSection from '../components/FeaturesSection';
import PricingSection from '../components/PricingSection';
import CTASection from '../components/CTASection';

const About = () => {
  const features = [
    { title: 'Task Management', description: 'Organize and prioritize tasks with ease.' },
    { title: 'Team Collaboration', description: 'Collaborate with your team in real-time.' },
    { title: 'Workflow Automation', description: 'Automate repetitive tasks to save time.' }
  ];

  const testimonials = [
    { name: 'John Doe', text: 'FlowSync has revolutionized the way we manage our projects!' },
    { name: 'Jane Smith', text: 'The team collaboration features are a game changer for us.' },
    { name: 'Mike Johnson', text: 'Automation saves me hours every week.' }
  ];

  const products = [
    { name: 'Basic Plan', description: 'Perfect for small teams and individuals.' },
    { name: 'Professional Plan', description: 'Ideal for mid-sized teams with advanced features.' },
    { name: 'Enterprise Plan', description: 'Tailored solutions for large organizations.' }
  ];

  const benefits = [
    { title: 'Efficiency', description: 'Streamline your workflow and increase productivity.' },
    { title: 'Scalability', description: 'Grow with FlowSync as your team expands.' },
    { title: 'Security', description: 'Protect sensitive data with our robust security measures.' }
  ];

  const plans = [
    { title: 'Basic Plan', description: 'Start small and scale up as needed.' },
    { title: 'Professional Plan', description: 'Get all the features you need for your growing team.' },
    { title: 'Enterprise Plan', description: 'Customized solutions for enterprise-level needs.' }
  ];

  return (
    <div>
      <Navbar />
      <Section>
        <Stack>
          <HeroSection title="About FlowSync" subtitle="Learn more about our product." />
          <ProductShowcase products={products} />
          <TestimonialsSection testimonials={testimonials} />
          <BenefitsSection benefits={benefits} />
          <FeaturesSection features={features} />
          <PricingSection plans={plans} />
          <CTASection ctaText="Sign Up Now" ctaLink="/pricing" />
        </Stack>
      </Section>
    </div>
  );
};

export default About;
