import { useState } from 'react';

const StatCard = ({ title, stats }) => {
  return (
    <section className="bg-zinc-50 rounded-xl border border-zinc-200 shadow-md p-6">
      <h3 className="text-xl font-semibold text-zinc-900">{title}</h3>
      <p className="mt-4 text-lg font-medium text-zinc-700">{stats}</p>
    </section>
  );
};

export default StatCard;
