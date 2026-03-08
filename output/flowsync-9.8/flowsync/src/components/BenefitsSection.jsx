import React from 'react';

const BenefitsSection = () => {
  return (
    <section className="benefits-section max-w-7xl mx-auto p-6 py-16 md:py-24 bg-white rounded-lg shadow-md">
      <h3 className="text-xl font-bold mb-4">Why Choose FlowSync?</h3>
      <ul className="flex flex-col space-y-4 sm:flex-row sm:space-x-8 sm:space-y-0">
        <li className="flex items-center">
          <div className="w-12 h-12 rounded-full bg-blue-500 mr-4"></div>
          <p className="text-sm text-zinc-900 opacity-70">Real-time task syncing</p>
        </li>
        <li className="flex items-center">
          <div className="w-12 h-12 rounded-full bg-green-500 mr-4"></div>
          <p className="text-sm text-zinc-900 opacity-70">Collaborative tools</p>
        </li>
        <li className="flex items-center">
          <div className="w-12 h-12 rounded-full bg-orange-500 mr-4"></div>
          <p className="text-sm text-zinc-900 opacity-70">Automated workflows</p>
        </li>
        <li className="flex items-center">
          <div className="w-12 h-12 rounded-full bg-purple-500 mr-4"></div>
          <p className="text-sm text-zinc-900 opacity-70">Detailed analytics</p>
        </li>
      </ul>
    </section>
  );
};

export default BenefitsSection;
