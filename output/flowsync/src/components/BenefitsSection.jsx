const BenefitsSection = ({ benefits }) => {
  return (
    <section className="max-w-7xl mx-auto px-6 py-16 md:py-24 bg-white">
      <div className="text-center">
        <h2 className="text-3xl font-bold text-zinc-900 sm:text-4xl">Why Choose FlowSync?</h2>
        <p className="mt-4 text-lg text-zinc-700 opacity-70">Explore the benefits of our product.</p>
      </div>
      <ul className="grid grid-cols-1 md:grid-cols-3 gap-8 mt-6">
        {benefits.map((benefit, index) => (
          <li key={index} className="border border-zinc-200 rounded-xl p-4 shadow-md flex items-center justify-between mb-4">
            <span className="text-lg font-semibold text-zinc-900">{benefit.title}</span>
            <p className="mt-1 text-sm text-zinc-700 opacity-70">{benefit.description}</p>
          </li>
        ))}
      </ul>
    </section>
  );
};

export default BenefitsSection;
