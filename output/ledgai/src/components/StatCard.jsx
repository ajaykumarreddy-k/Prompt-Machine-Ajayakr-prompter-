import { useState } from 'react';

export const StatCard = ({ stats }) => (
  <div className="bg-slate-900 rounded-2xl border border-slate-800 shadow-lg p-6 max-w-sm mx-auto my-4 text-center">
    {stats.map((stat, index) => (
      <div key={index} className="mb-4">
        <p className="text-xl font-semibold">{stat.title}</p>
        <p className="text-slate-200 opacity-70">{stat.value}</p>
      </div>
    ))}
  </div>
);
