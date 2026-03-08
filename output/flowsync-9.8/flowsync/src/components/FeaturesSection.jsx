import React from 'react';

const FeaturesSection = ({ features }) => {
  return (
    <section className="features-section max-w-7xl mx-auto p-6 py-16 md:py-24 bg-white rounded-lg shadow-md">
      <h3 className="text-xl font-bold mb-4">Key Features</h3>
      <ul className="flex flex-col space-y-8 sm:flex-row sm:space-x-8 sm:space-y-0">
        {features.map((feature, index) => (
          <li key={index} className="w-full md:w-1/2 p-6 bg-zinc-50 rounded-lg border border-zinc-200 shadow-md">
            <h4 className="text-xl font-bold mb-4">{feature.title}</h4>
            <p className="text-sm text-zinc-900 opacity-70">{feature.description}</p>
          </li>
        ))}
      </ul>
    </section>
  );
};

export default FeaturesSection;
