import { GlassNavbar, GlassHeroSection, GlassTestimonialsSection } from '@/components';

const GlassAboutPage = () => {
  return (
    <div className="max-w-7xl mx-auto px-6">
      <GlassNavbar />
      <GlassHeroSection
        title="About Us"
        subtitle="Learn more about our mission and values."
        callToAction="Explore Now"
        backgroundImage="/about.jpg"
      />
      <GlassTestimonialsSection
        testimonials={[
          {
            text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at justo euismod, convallis odio vel, facilisis nisl.",
            name: "John Doe"
          },
          {
            text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at justo euismod, convallis odio vel, facilisis nisl.",
            name: "Jane Smith"
          }
        ]}
      />
    </div>
  );
};

export default GlassAboutPage;
