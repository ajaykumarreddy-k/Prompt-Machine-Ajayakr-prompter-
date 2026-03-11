import React from 'react';

const AboutSection = ({ teamMembers, missionVision }) => {
  return (
    <section className="grid grid-cols-1 md:grid-cols-2 p-8 gap-8 max-w-7xl mx-auto px-6">
      <div className="col-span-1 md:col-span-1">
        <h2 className="text-2xl md:text-3xl font-bold mb-4">Our Mission and Vision</h2>
        <p className="text-zinc-900 opacity-70">{missionVision}</p>
      </div>
      <div className="col-span-1 md:col-span-1">
        <h2 className="text-2xl md:text-3xl font-bold mb-4">Meet the Team</h2>
        {teamMembers.map((member, index) => (
          <div key={index} className="mb-4">
            <h3 className="text-xl font-semibold mb-2">{member.name}</h3>
            <p className="text-zinc-900 opacity-70">{member.role}</p>
          </div>
        ))}
      </div>
    </section>
  );
};

export default AboutSection;
