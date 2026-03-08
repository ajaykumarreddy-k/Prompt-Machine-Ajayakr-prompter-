const ProductShowcase = () => {
  return (
    <section className="bg-white shadow-md rounded-lg max-w-3xl mx-auto p-6 my-8">
      <h2 className="text-xl font-semibold text-zinc-900 mb-4">Products & Services</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {/* Product 1 */}
        <div className="bg-zinc-50 rounded-lg border border-zinc-200 shadow-md p-4">
          <img src="/path/to/product1.png" alt="Product 1" className="w-full h-48 object-cover mb-4" />
          <h3 className="text-xl font-semibold text-zinc-900">FlowSync Pro</h3>
          <p className="mt-2 text-sm text-zinc-700">Advanced features for high-performance teams.</p>
        </div>
        {/* Product 2 */}
        <div className="bg-zinc-50 rounded-lg border border-zinc-200 shadow-md p-4">
          <img src="/path/to/product2.png" alt="Product 2" className="w-full h-48 object-cover mb-4" />
          <h3 className="text-xl font-semibold text-zinc-900">FlowSync Basic</h3>
          <p className="mt-2 text-sm text-zinc-700">Essential tools for small teams.</p>
        </div>
        {/* Product 3 */}
        <div className="bg-zinc-50 rounded-lg border border-zinc-200 shadow-md p-4">
          <img src="/path/to/product3.png" alt="Product 3" className="w-full h-48 object-cover mb-4" />
          <h3 className="text-xl font-semibold text-zinc-900">FlowSync Enterprise</h3>
          <p className="mt-2 text-sm text-zinc-700">Customizable solutions for enterprise needs.</p>
        </div>
      </div>
    </section>
  );
};

export default ProductShowcase;
