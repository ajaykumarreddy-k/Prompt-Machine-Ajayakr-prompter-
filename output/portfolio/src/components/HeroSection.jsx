import React from 'react';

const HeroSection = ({ heroMessage, callToAction, backgroundMedia }) => {
  return (
    <section className="bg-gradient-to-br from-blue-600 to-indigo-600 p-8 text-white flex flex-col items-center justify-center max-w-7xl mx-auto px-6">
      <h1 className="text-3xl md:text-4xl font-bold mb-4">{heroMessage}</h1>
      <button className="bg-zinc-900 hover:opacity-90 text-white px-6 py-3 rounded-lg font-semibold transition-all">{callToAction}</button>
      <div className="mt-8">
        {backgroundMedia}
      </div>
    </section>
  );
};

export default HeroSection;
