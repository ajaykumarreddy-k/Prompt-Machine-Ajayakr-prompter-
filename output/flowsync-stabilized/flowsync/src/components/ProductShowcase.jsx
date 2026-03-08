const ProductShowcase = ({ products }) => {
  return (
    <section className="bg-white py-16 md:py-24 max-w-7xl mx-auto px-6 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
      {products.map((product, index) => (
        <div key={index} className="shadow-lg rounded-lg overflow-hidden">
          <img src={`/${product}.png`} alt={product} className="w-full" />
          <h3 className="text-xl font-semibold p-4">{product}</h3>
          <p className="text-sm text-zinc-900 opacity-70 p-4">Detailed description of the product.</p>
        </div>
      ))}
    </section>
  );
};

export default ProductShowcase;
