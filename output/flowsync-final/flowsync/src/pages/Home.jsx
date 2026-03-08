import HeroSection from '../components/HeroSection';
import FeaturesSection from '../components/FeaturesSection';
import ProductShowcase from '../components/ProductShowcase';
import PricingPreview from '../components/PricingPreview';
import TestimonialsSection from '../components/TestimonialsSection';

const Home = () => {
  return (
    <div className="bg-white">
      <Navbar />
      <HeroSection title="Welcome to FlowSync" description="Elevate your team's productivity with FlowSync." />
      <FeaturesSection />
      <ProductShowcase />
      <PricingPreview />
      <TestimonialsSection />
    </div>
  );
};

export default Home;
