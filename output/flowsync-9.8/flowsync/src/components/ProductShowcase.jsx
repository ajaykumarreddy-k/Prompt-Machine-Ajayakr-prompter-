import React from 'react';

const ProductShowcase = ({ products }) => {
  return (
    <section className="product-showcase max-w-7xl mx-auto p-6 py-16 md:py-24 bg-white rounded-lg shadow-md">
      <h3 className="text-xl font-bold mb-4">Featured Products</h3>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
        {products.map((product, index) => (
          <div key={index} className="bg-zinc-50 rounded-lg p-6 shadow-md">
            <h4 className="text-xl font-bold mb-4">{product.name}</h4>
            <p className="text-sm text-zinc-900 opacity-70">{product.description}</p>
          </div>
        ))}
      </div>
    </section>
  );
};

export default ProductShowcase;
