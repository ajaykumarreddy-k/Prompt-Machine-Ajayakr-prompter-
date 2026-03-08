import React from 'react';

const TestimonialsSection = ({ testimonials }) => {
  return (
    <section className="testimonials-section max-w-7xl mx-auto p-6 py-16 md:py-24 bg-white rounded-lg shadow-md">
      <h3 className="text-xl font-bold mb-4">Customer Testimonials</h3>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
        {testimonials.map((testimonial, index) => (
          <div key={index} className="bg-zinc-50 rounded-lg p-6 shadow-md">
            <p className="text-sm text-zinc-900 opacity-70">{testimonial.text}</p>
            <cite className="block mt-2 text-sm font-bold text-zinc-900">{testimonial.author}</cite>
          </div>
        ))}
      </div>
    </section>
  );
};

export default TestimonialsSection;
