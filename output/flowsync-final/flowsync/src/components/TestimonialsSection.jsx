const TestimonialsSection = () => {
  return (
    <section className="bg-white shadow-md rounded-lg max-w-3xl mx-auto p-6 my-8">
      <h2 className="text-xl font-semibold text-zinc-900 mb-4">Customer Testimonials</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {/* Testimonial 1 */}
        <div className="bg-zinc-50 rounded-lg border border-zinc-200 shadow-md p-4">
          <p className="text-sm text-zinc-900">"FlowSync has revolutionized our team's productivity. Highly recommend!"</p>
          <cite className="mt-2 text-sm text-zinc-700">— John Doe, CEO of XYZ Corp.</cite>
        </div>
        {/* Testimonial 2 */}
        <div className="bg-zinc-50 rounded-lg border border-zinc-200 shadow-md p-4">
          <p className="text-sm text-zinc-900">"The automation features have saved us countless hours. Thank you, FlowSync!"</p>
          <cite className="mt-2 text-sm text-zinc-700">— Jane Smith, COO of ABC Inc.</cite>
        </div>
        {/* Testimonial 3 */}
        <div className="bg-zinc-50 rounded-lg border border-zinc-200 shadow-md p-4">
          <p className="text-sm text-zinc-900">"FlowSync is a game-changer for our small team. Keep up the great work!"</p>
          <cite className="mt-2 text-sm text-zinc-700">— Mike Johnson, CTO of DEF Ltd.</cite>
        </div>
      </div>
    </section>
  );
};

export default TestimonialsSection;
