const HeroSection = ({ title, description }) => {
  return (
    <section className="bg-white py-16 md:py-24 text-center max-w-7xl mx-auto px-6">
      <h1 className="text-3xl font-bold mb-4">{title}</h1>
      <p className="text-lg text-zinc-900 opacity-70 mb-8">{description}</p>
    </section>
  );
};

export default HeroSection;
