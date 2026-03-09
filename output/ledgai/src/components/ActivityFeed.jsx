import { useState } from 'react';

export const ActivityFeed = ({ items }) => (
  <div className="bg-slate-900 rounded-2xl border border-slate-800 shadow-lg p-6 max-w-sm mx-auto my-4 text-center">
    {items.map((item, index) => (
      <div key={index} className="mb-4">
        <p className="text-xl font-semibold">{item.title}</p>
        <p className="text-slate-200 opacity-70">{item.description}</p>
      </div>
    ))}
  </div>
);
