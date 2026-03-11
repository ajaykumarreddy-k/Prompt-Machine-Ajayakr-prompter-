import { GlassNavbar, GlassPricingSection } from '@/components';

const GlassPricingPage = () => {
  return (
    <div className="max-w-7xl mx-auto px-6">
      <GlassNavbar />
      <GlassPricingSection
        title="Pricing"
        subtitle="Choose the plan that fits your needs."
        tiers={[
          {
            name: "Free",
            price: "Free",
            yearlyPrice: "Free",
            period: "Monthly",
            features: ["Feature 1", "Feature 2"],
            description: "This is the free plan.",
            buttonText: "Sign Up",
            href: "/signup",
            isPopular: false
          },
          {
            name: "Pro",
            price: "$9.99",
            yearlyPrice: "$99.99",
            period: "Monthly",
            features: ["Feature 1", "Feature 2", "Feature 3"],
            description: "This is the pro plan.",
            buttonText: "Sign Up",
            href: "/signup",
            isPopular: true
          }
        ]}
      />
    </div>
  );
};

export default GlassPricingPage;
