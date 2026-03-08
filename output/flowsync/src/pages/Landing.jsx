import { Link } from 'react-router-dom';
import HeroSection from '../components/HeroSection';
import FeaturesSection from '../components/FeaturesSection';
import ProductShowcase from '../components/ProductShowcase';
import BenefitsSection from '../components/BenefitsSection';
import TestimonialsSection from '../components/TestimonialsSection';
import PricingSection from '../components/PricingSection';
import CTASection from '../components/CTASection';
import NewsletterSignup from '../components/NewsletterSignup';

const Landing = () => {
  return (
    <div>
      <HeroSection title="Transform Your Workflow" subtitle="Effortlessly manage your tasks with FlowSync." />
      <FeaturesSection features={[
        { title: 'Task Management', description: 'Organize and prioritize your tasks.' },
        { title: 'Collaboration Tools', description: 'Work seamlessly with team members.' },
        { title: 'Real-Time Updates', description: 'Stay updated in real-time.' }
      ]} />
      <ProductShowcase products={[
        { title: 'Premium Plan', description: 'Unlimited features and support.' },
        { title: 'Standard Plan', description: 'Basic features for individual use.' },
        { title: 'Team Plan', description: 'Collaboration tools for teams.' }
      ]} />
      <BenefitsSection benefits={[
        { title: 'Efficiency', description: 'Streamline your workflow with FlowSync.' },
        { title: 'Flexibility', description: 'Access from anywhere, anytime.' },
        { title: 'Support', description: '24/7 customer support and resources.' }
      ]} />
      <TestimonialsSection testimonials={[
        { name: 'John Doe', text: "FlowSync has completely transformed the way I work." },
        { name: 'Jane Smith', text: "I love how easy it is to collaborate with my team using FlowSync." },
        { name: 'Alex Johnson', text: "The real-time updates feature is a game-changer for me." }
      ]} />
      <PricingSection pricingPlans={[
        { title: 'Free Plan', description: 'Limited features, ideal for individuals.' },
        { title: 'Pro Plan', description: 'Advanced features and support for professionals.' },
        { title: 'Enterprise Plan', description: 'Customized solutions for large organizations.' }
      ]} />
      <CTASection callToActionText="Sign Up Now" />
      <NewsletterSignup formFields={[]}/>
    </div>
  );
};

export default Landing;
