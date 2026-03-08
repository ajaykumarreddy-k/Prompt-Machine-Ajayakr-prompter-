const HeroSection = ({ title, description }) => {
  return (
    <section className="bg-white shadow-md rounded-lg max-w-3xl mx-auto p-6 my-8">
      <h1 className="text-2xl font-bold text-zinc-900 mb-4">{title}</h1>
      <p className="mb-8 text-sm text-zinc-700 opacity-70">{description}</p>
      <div className="flex items-center space-x-4">
        <button className="bg-zinc-900 hover:opacity-90 text-white px-6 py-3 rounded-lg font-semibold transition-all">Sign Up</button>
        <button className="border border-zinc-300 text-zinc-700 px-6 py-3 rounded-lg hover:bg-zinc-50 transition-all">Learn More</button>
      </div>
    </section>
  );
};

export default HeroSection;
