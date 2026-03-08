const FeaturesSection = ({ features }) => {
  return (
    <section className="bg-white py-16 md:py-24 max-w-7xl mx-auto px-6">
      {features.map((feature, index) => (
        <div key={index} className="mb-8 flex items-center space-x-4">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6 text-zinc-900">
            <path strokeLinecap="round" strokeLinejoin="round" d="M9.75 17L9 20l4-3m-.75-4H4a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2V9.5M9 20h6a2 2 0 002-2v-8a2 2 0 00-2-2H9a2 2 0 00-2 2v8a2 2 0 002 2z" />
          </svg>
          <div>
            <h3 className="text-xl font-semibold mb-1">{feature}</h3>
            <p className="text-sm text-zinc-900 opacity-70">Detailed description of the feature.</p>
          </div>
        </div>
      ))}
    </section>
  );
};

export default FeaturesSection;
