const CTASection = ({ callToActionText }) => {
  return (
    <section className="max-w-7xl mx-auto px-6 py-16 md:py-24 bg-white">
      <div className="text-center">
        <h2 className="text-3xl font-bold text-zinc-900 sm:text-4xl">Ready to Get Started?</h2>
        <p className="mt-4 text-lg text-zinc-700 opacity-70">Sign up now and transform your workflow.</p>
      </div>
      <Link to="/pricing" className="mt-6 inline-block px-6 py-3 rounded-xl bg-zinc-900 hover:opacity-90 text-white font-semibold transition-all">
        {callToActionText}
      </Link>
    </section>
  );
};

export default CTASection;
