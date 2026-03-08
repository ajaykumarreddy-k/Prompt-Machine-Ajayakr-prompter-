const TestimonialsSection = ({ testimonials }) => {
  return (
    <section className="bg-zinc-50 rounded-lg border border-zinc-200 shadow-md p-6">
      {testimonials.map((testimonial, index) => (
        <div key={index} className="mb-4 flex items-center space-x-2">
          <img src={testimonial.avatar} alt={testimonial.name} className="w-10 h-10 rounded-full" />
          <p className="text-sm">{testimonial.text}</p>
        </div>
      ))}
    </section>
  );
};

export default TestimonialsSection;
