```jsx
const CTASection = ({ ctaText, linkUrl }) => {
  return (
    <section className="bg-white py-16 md:py-24 max-w-7xl mx-auto px-6">
      <div className="mx-auto max-w-xl text-center">
        <p className="text-lg leading-relaxed text-zinc-900 opacity-70">Ready to get started?</p>
        <Link
          href={linkUrl}
          className="mt-4 inline-block rounded-lg bg-zinc-900 px-6 py-3 font-semibold text-white transition duration-200 ease-in-out hover:bg-zinc-800"
        >
          {ctaText}
        </Link>
      </div>
    </section>
  );
};

export default CTASection;
```
