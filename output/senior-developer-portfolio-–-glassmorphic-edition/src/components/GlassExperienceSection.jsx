import { motion, AnimatePresence } from 'framer-motion';

const GlassExperienceSection = ({ experiences }) => {
  return (
    <section className="py-16 md:py-24">
      <div className="max-w-7xl mx-auto px-6">
        <h2 className="text-3xl font-bold text-slate-900 mb-4">Experience</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {experiences.map((experience) => (
            <div key={experience.title} className="bg-white/10 backdrop-blur-md border border-white/20 rounded-lg shadow-lg p-6">
              <h3 className="text-xl font-bold text-slate-900 mb-2">{experience.title}</h3>
              <p className="text-lg text-slate-900">{experience.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default GlassExperienceSection;
