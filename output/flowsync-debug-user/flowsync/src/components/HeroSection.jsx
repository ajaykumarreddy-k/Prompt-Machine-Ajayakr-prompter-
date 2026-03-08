```jsx
const HeroSection = ({ title, description }) => {
  return (
    <section className="bg-white py-16 md:py-24 max-w-7xl mx-auto px-6">
      <div className="mx-auto max-w-xl text-center">
        <h1 className="text-3xl font-bold tracking-tight text-zinc-900 sm:text-4xl lg:text-5xl">{title}</h1>
        <p className="mt-4 text-lg leading-relaxed text-zinc-700 opacity-70 max-w-xl mx-auto">
          {description}
        </p>
      </div>
    </section>
  );
};

export default HeroSection;
```
