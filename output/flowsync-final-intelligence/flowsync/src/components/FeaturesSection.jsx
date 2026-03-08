import { useState } from 'react';

const FeaturesSection = () => {
  return (
    <section className="bg-zinc-50 rounded-xl border border-zinc-200 shadow-md p-6">
      <h3 className="text-xl font-semibold text-zinc-900">Features</h3>
      <ul className="mt-4 list-disc pl-5 space-y-2">
        <li>Dynamic task boards with real-time syncing</li>
        <li>Team collaboration tools (chat, comments, shared docs)</li>
        <li>Workflow automation engine with visual builder</li>
        <li>Detailed analytics and reporting</li>
      </ul>
    </section>
  );
};

export default FeaturesSection;
