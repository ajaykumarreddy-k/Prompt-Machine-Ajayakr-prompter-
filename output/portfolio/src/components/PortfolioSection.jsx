import React from 'react';

const PortfolioSection = ({ projects }) => {
  return (
    <section className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 p-8 gap-8 max-w-7xl mx-auto px-6">
      {projects.map((project, index) => (
        <div key={index} className="col-span-1 md:col-span-1 lg:col-span-1">
          <div className="card bg-zinc-50 rounded-lg border border-zinc-200 shadow-md p-6">
            <h3 className="text-xl font-semibold mb-2">{project.title}</h3>
            <p className="text-zinc-900 opacity-70">{project.description}</p>
            <a href={project.url} className="mt-4 block text-zinc-900 hover:text-zinc-700">View Project</a>
          </div>
        </div>
      ))}
    </section>
  );
};

export default PortfolioSection;
