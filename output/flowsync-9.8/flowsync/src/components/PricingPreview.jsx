import React from 'react';

const PricingPreview = () => {
  return (
    <section className="pricing-preview max-w-7xl mx-auto p-6 py-16 md:py-24 bg-white rounded-lg shadow-md">
      <h3 className="text-xl font-bold mb-4">Pricing Options</h3>
      <div className="flex flex-col space-y-8 sm:flex-row sm:space-x-8 sm:space-y-0">
        <div className="w-full md:w-1/2 p-6 bg-zinc-50 rounded-lg border border-zinc-200 shadow-md">
          <h4 className="text-xl font-bold mb-4">Basic</h4>
          <p className="text-sm text-zinc-900 opacity-70">$9.99/month</p>
          <ul className="mt-4 list-disc pl-5 space-y-2">
            <li>Unlimited tasks</li>
            <li>1 team member</li>
            <li>Email support</li>
          </ul>
        </div>
        <div className="w-full md:w-1/2 p-6 bg-zinc-50 rounded-lg border border-zinc-200 shadow-md">
          <h4 className="text-xl font-bold mb-4">Pro</h4>
          <p className="text-sm text-zinc-900 opacity-70">$19.99/month</p>
          <ul className="mt-4 list-disc pl-5 space-y-2">
            <li>Unlimited tasks</li>
            <li>Up to 5 team members</li>
            <li>Email and chat support</li>
          </ul>
        </div>
      </div>
    </section>
  );
};

export default PricingPreview;
