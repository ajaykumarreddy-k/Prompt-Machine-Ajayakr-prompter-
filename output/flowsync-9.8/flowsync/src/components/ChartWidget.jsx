import React from 'react';

const ChartWidget = ({ data }) => {
  return (
    <section className="chart-widget max-w-7xl mx-auto p-6 py-16 md:py-24 bg-white rounded-lg shadow-md">
      <h3 className="text-xl font-bold mb-4">Data Visualization</h3>
      <div className="w-full h-96 bg-zinc-50 rounded-lg border border-zinc-200 shadow-md">
        {/* Placeholder for chart */}
        <p className="p-8 text-center text-sm text-zinc-900 opacity-70">Loading data...</p>
      </div>
    </section>
  );
};

export default ChartWidget;
