import React from 'react';

const HeroSection = ({ title, subtitle }) => {
  return (
    <section className="hero-section max-w-7xl mx-auto p-6 py-16 md:py-24 bg-white rounded-lg shadow-md">
      <h1 className="text-3xl font-bold mb-4">{title}</h1>
      <p className="text-xl text-zinc-900 opacity-70 mb-8">{subtitle}</p>
    </section>
  );
};

export default HeroSection;
