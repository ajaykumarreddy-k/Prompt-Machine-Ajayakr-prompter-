import React from 'react';

const SkillsSection = ({ skills }) => {
  return (
    <section className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 p-8 gap-8 max-w-7xl mx-auto px-6">
      {skills.map((skill, index) => (
        <div key={index} className="col-span-1 md:col-span-1 lg:col-span-1">
          <div className="card bg-zinc-50 rounded-lg border border-zinc-200 shadow-md p-6">
            <h3 className="text-xl font-semibold mb-2">{skill.name}</h3>
            <p className="text-zinc-900 opacity-70">{skill.description}</p>
          </div>
        </div>
      ))}
    </section>
  );
};

export default SkillsSection;
