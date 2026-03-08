import { useState } from 'react';
import ChartWidget from '../components/ChartWidget';

const Analytics = () => {
  return (
    <div className="max-w-7xl mx-auto px-6 py-12">
      <h1 className="text-3xl font-bold text-zinc-900">Analytics</h1>
      <p className="mt-4 text-lg text-zinc-700 opacity-70">
        Get insights into your team's performance and productivity.
      </p>
      <ChartWidget data={[] /* Add chart data here */} />
    </div>
  );
};

export default Analytics;
