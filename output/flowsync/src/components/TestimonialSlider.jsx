import React from 'react';

const TestimonialSlider = ({ testimonials }) => {
  return (
    <div className="bg-zinc-50 rounded-lg shadow-md p-6">
      {testimonials.map((testimonial, index) => (
        <div key={index} className="mb-6">
          <p className="text-xl font-semibold text-zinc-900">{testimonial.name}</p>
          <p className="mt-2 text-zinc-700 opacity-70">{testimonial.text}</p>
        </div>
      ))}
    </div>
  );
};

export default TestimonialSlider;
