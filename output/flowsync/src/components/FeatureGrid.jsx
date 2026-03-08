import React from 'react';

const FeatureGrid = ({ features }) => {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {features.map((feature, index) => (
        <div key={index} className="bg-zinc-50 rounded-lg shadow-md p-6 mb-6">
          <h2 className="text-xl font-semibold text-zinc-900">{feature.title}</h2>
          <p className="mt-4 text-zinc-700 opacity-70">{feature.description}</p>
        </div>
      ))}
    </div>
  );
};

export default FeatureGrid;
