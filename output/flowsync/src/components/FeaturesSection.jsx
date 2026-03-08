import { Link } from 'react-router-dom';

const FeaturesSection = ({ features }) => {
  return (
    <section className="max-w-7xl mx-auto px-6 py-16 md:py-24 bg-white">
      <div className="text-center">
        <h2 className="text-3xl font-bold text-zinc-900 sm:text-4xl">Key Features</h2>
        <p className="mt-4 text-lg text-zinc-700 opacity-70">Discover what makes FlowSync unique.</p>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mt-6">
        {features.map((feature, index) => (
          <div key={index} className="border border-zinc-200 rounded-xl p-4 shadow-md flex items-center justify-between">
            <span className="text-lg font-semibold text-zinc-900">{feature.title}</span>
            <p className="mt-1 text-sm text-zinc-700 opacity-70">{feature.description}</p>
          </div>
        ))}
      </div>
    </section>
  );
};

export default FeaturesSection;
