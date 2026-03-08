import React from 'react';

const StatCard = ({ stats }) => {
  return (
    <section className="card max-w-sm mx-auto p-6 bg-zinc-50 rounded-lg border border-zinc-200 shadow-md">
      {stats.map((stat, index) => (
        <div key={index} className="mb-4 flex items-center">
          <span className="text-xl mr-2">{stat.value}</span>
          <p className="text-sm text-zinc-900 opacity-70">{stat.label}</p>
        </div>
      ))}
    </section>
  );
};

export default StatCard;
