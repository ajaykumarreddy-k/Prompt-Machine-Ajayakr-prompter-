import { GlassNavbar, GlassTestimonialsSection } from '@/components';

const GlassSkillsPage = () => {
  return (
    <div className="max-w-7xl mx-auto px-6">
      <GlassNavbar />
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

export default GlassSkillsPage;
