```jsx
const SectionWrapper = ({ children }) => {
  return (
    <section className="container mx-auto py-16 md:py-24 max-w-7xl px-6 flex flex-col items-center justify-center text-center">
      {children}
    </section>
  );
};

export default SectionWrapper;
```
