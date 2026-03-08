import { Link } from 'react-router-dom';

const HeroSection = ({ title, subtitle }) => {
  return (
    <section className="max-w-7xl mx-auto px-6 py-16 md:py-24 bg-white">
      <div className="text-center">
        <h1 className="text-3xl font-bold text-zinc-900 sm:text-4xl">{title}</h1>
        <p className="mt-4 text-lg text-zinc-700 opacity-70">{subtitle}</p>
      </div>
    </section>
  );
};

export default HeroSection;
