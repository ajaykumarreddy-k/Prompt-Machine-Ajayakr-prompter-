const ChartWidget = ({ data }) => {
  return (
    <section className="bg-white shadow-md rounded-lg max-w-3xl mx-auto p-6 my-8">
      <h2 className="text-xl font-semibold text-zinc-900 mb-4">Data Visualization</h2>
      {/* Render chart here */}
      <div className="w-full h-56 bg-gray-100 rounded-lg"></div>
    </section>
  );
};

export default ChartWidget;
