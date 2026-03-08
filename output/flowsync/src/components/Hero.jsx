import React from 'react';

const Hero = ({ title, subtitle }) => {
  return (
    <div className="bg-zinc-50 rounded-lg shadow-md p-6">
      <h1 className="text-3xl font-bold text-zinc-900">{title}</h1>
      <p className="mt-4 text-xl text-zinc-700 opacity-70">{subtitle}</p>
    </div>
  );
};

export default Hero;
