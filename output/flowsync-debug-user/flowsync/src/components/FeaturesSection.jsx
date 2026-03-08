```jsx
const FeaturesSection = ({ features }) => {
  return (
    <section className="bg-white py-16 md:py-24 max-w-7xl mx-auto px-6">
      <div className="mx-auto max-w-xl text-center">
        <h2 className="text-3xl font-bold tracking-tight text-zinc-900 sm:text-4xl lg:text-5xl">Key Features</h2>
        {features.map((feature, index) => (
          <div key={index} className="mt-6 flex items-center space-x-2">
            <span className="text-xl font-semibold">{feature.icon}</span>
            <p className="ml-4 text-lg leading-relaxed text-zinc-900 opacity-70">{feature.description}</p>
          </div>
        ))}
      </div>
    </section>
  );
};

export default FeaturesSection;
```
