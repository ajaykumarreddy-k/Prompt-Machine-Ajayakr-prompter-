import { useState } from 'react';

const ActivityFeed = ({ items }) => {
  return (
    <section className="bg-zinc-50 rounded-xl border border-zinc-200 shadow-md p-6">
      <h3 className="text-xl font-semibold text-zinc-900">Recent Activities</h3>
      {items.map((item, index) => (
        <div key={index} className="mt-4 flex items-center space-x-2">
          <span className="text-sm text-zinc-700">{item}</span>
        </div>
      ))}
    </section>
  );
};

export default ActivityFeed;
