const FeaturesSection = () => {
  return (
    <section className="bg-white shadow-md rounded-lg max-w-3xl mx-auto p-6 my-8">
      <h2 className="text-xl font-semibold text-zinc-900 mb-4">Key Features</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {/* Feature 1 */}
        <div className="bg-zinc-50 rounded-lg border border-zinc-200 shadow-md p-4">
          <img src="/path/to/feature1.png" alt="Feature 1" className="w-full h-48 object-cover mb-4" />
          <h3 className="text-xl font-semibold text-zinc-900">Dynamic Task Boards</h3>
          <p className="mt-2 text-sm text-zinc-700">Real-time syncing for seamless collaboration.</p>
        </div>
        {/* Feature 2 */}
        <div className="bg-zinc-50 rounded-lg border border-zinc-200 shadow-md p-4">
          <img src="/path/to/feature2.png" alt="Feature 2" className="w-full h-48 object-cover mb-4" />
          <h3 className="text-xl font-semibold text-zinc-900">Team Collaboration Tools</h3>
          <p className="mt-2 text-sm text-zinc-700">Chat, comments, and shared documents for efficient teamwork.</p>
        </div>
        {/* Feature 3 */}
        <div className="bg-zinc-50 rounded-lg border border-zinc-200 shadow-md p-4">
          <img src="/path/to/feature3.png" alt="Feature 3" className="w-full h-48 object-cover mb-4" />
          <h3 className="text-xl font-semibold text-zinc-900">Workflow Automation Engine</h3>
          <p className="mt-2 text-sm text-zinc-700">Visual builder for automating workflows.</p>
        </div>
      </div>
    </section>
  );
};

export default FeaturesSection;
