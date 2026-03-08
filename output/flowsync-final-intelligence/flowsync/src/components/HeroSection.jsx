import { useState } from 'react';

const HeroSection = ({ title, description }) => {
  return (
    <section className="bg-white py-16 md:py-24 max-w-7xl mx-auto px-6">
      <h1 className="text-3xl font-bold text-zinc-900">{title}</h1>
      <p className="mt-4 text-lg text-zinc-700 opacity-70">{description}</p>
    </section>
  );
};

export default HeroSection;
