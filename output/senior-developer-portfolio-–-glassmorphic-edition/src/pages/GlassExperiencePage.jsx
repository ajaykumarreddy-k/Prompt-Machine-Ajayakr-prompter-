import { GlassNavbar, GlassExperienceSection } from '@/components';

const GlassExperiencePage = () => {
  return (
    <div className="max-w-7xl mx-auto px-6">
      <GlassNavbar />
      <GlassExperienceSection
        experiences={[
          {
            title: "Company A",
            description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at justo euismod, convallis odio vel, facilisis nisl."
          },
          {
            title: "Company B",
            description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at justo euismod, convallis odio vel, facilisis nisl."
          }
        ]}
      />
    </div>
  );
};

export default GlassExperiencePage;
