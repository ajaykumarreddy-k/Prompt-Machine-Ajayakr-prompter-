import React from 'react';

const TestimonialsSection = ({ testimonials }) => {
  return (
    <section className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 p-8 gap-8 max-w-7xl mx-auto px-6">
      {testimonials.map((testimonial, index) => (
        <div key={index} className="col-span-1 md:col-span-1 lg:col-span-1">
          <div className="card bg-zinc-50 rounded-lg border border-zinc-200 shadow-md p-6">
            <p className="text-zinc-900 opacity-70">{testimonial.quote}</p>
            <footer className="mt-4 flex items-center">
              <img src={testimonial.avatar} alt={testimonial.name} className="w-10 h-10 rounded-full mr-2" />
              <span className="text-zinc-900 font-semibold">{testimonial.name}</span>
            </footer>
          </div>
        </div>
      ))}
    </section>
  );
};

export default TestimonialsSection;
