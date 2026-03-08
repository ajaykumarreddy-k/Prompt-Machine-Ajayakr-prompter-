const PricingPreview = () => {
  return (
    <section className="bg-white shadow-md rounded-lg max-w-3xl mx-auto p-6 my-8">
      <h2 className="text-xl font-semibold text-zinc-900 mb-4">Pricing Plans</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {/* Plan 1 */}
        <div className="bg-zinc-50 rounded-lg border border-zinc-200 shadow-md p-4">
          <p className="text-xl font-semibold text-zinc-900">FlowSync Pro</p>
          <p className="mt-2 text-sm text-zinc-700">$19.99/month</p>
          <ul className="list-disc pl-5 mt-2">
            <li>Unlimited projects</li>
            <li>Advanced features</li>
            <li>Priority support</li>
          </ul>
        </div>
        {/* Plan 2 */}
        <div className="bg-zinc-50 rounded-lg border border-zinz-200 shadow-md p-4">
          <p className="text-xl font-semibold text-zinc-900">FlowSync Basic</p>
          <p className="mt-2 text-sm text-zinc-700">$9.99/month</p>
          <ul className="list-disc pl-5 mt-2">
            <li>Basic features</li>
            <li>Standard support</li>
            <li>Up to 10 projects</li>
          </ul>
        </div>
        {/* Plan 3 */}
        <div className="bg-zinc-50 rounded-lg border border-zinz-200 shadow-md p-4">
          <p className="text-xl font-semibold text-zinc-900">FlowSync Enterprise</p>
          <p className="mt-2 text-sm text-zinc-700">$49.99/month</p>
          <ul className="list-disc pl-5 mt-2">
            <li>Customizable solutions</li>
            <li>Dedicated support</li>
            <li>Unlimited projects</li>
          </ul>
        </div>
      </div>
    </section>
  );
};

export default PricingPreview;
