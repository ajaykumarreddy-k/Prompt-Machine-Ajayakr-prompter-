const NewsletterSignup = ({ formFields }) => {
  return (
    <section className="max-w-7xl mx-auto px-6 py-16 md:py-24 bg-white">
      <div className="text-center">
        <h2 className="text-3xl font-bold text-zinc-900 sm:text-4xl">Stay Updated</h2>
        <p className="mt-4 text-lg text-zinc-700 opacity-70">Join our mailing list for the latest updates.</p>
      </div>
      <form className="flex flex-col items-center">
        <input
          type="email"
          placeholder="Enter your email address"
          className="bg-gray-50 border border-zinc-300 text-zinc-900 sm:text-sm rounded-lg p-2 mb-4 focus:outline-none focus:ring-1 focus:ring-blue-500 transition ease-in-out duration-150"
        />
        <button
          type="submit"
          className="bg-gradient-to-r from-green-500 to-blue-500 text-white font-bold py-2 px-4 rounded-md hover:bg-green-600 hover:to-blue-600 transition ease-in-out duration-150"
        >
          Subscribe
        </button>
      </form>
    </section>
  );
};

export default NewsletterSignup;
