const BenefitsSection = ({ benefits }) => {
  return (
    <section className="bg-white py-16 md:py-24 max-w-7xl mx-auto px-6 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
      {benefits.map((benefit, index) => (
        <div key={index} className="shadow-lg rounded-lg overflow-hidden p-4">
          <h3 className="text-xl font-semibold mb-2">{benefit}</h3>
          <p className="text-sm text-zinc-900 opacity-70">Detailed description of the benefit.</p>
        </div>
      ))}
    </section>
  );
};

export default BenefitsSection;
