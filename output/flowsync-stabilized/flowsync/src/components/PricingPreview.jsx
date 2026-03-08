const PricingPreview = ({ pricing }) => {
  return (
    <section className="bg-zinc-50 rounded-lg border border-zinc-200 shadow-md p-6 flex items-center space-x-4">
      {pricing.map((plan, index) => (
        <div key={index} className="flex-1">
          <h3 className="text-xl font-semibold mb-4">{plan.name}</h3>
          <p className="text-sm">{plan.description}</p>
          <button className="primary-btn">Get Started</button>
        </div>
      ))}
    </section>
  );
};

export default PricingPreview;
