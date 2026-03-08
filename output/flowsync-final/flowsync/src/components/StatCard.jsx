const StatCard = ({ title, stats }) => {
  return (
    <div className="bg-zinc-50 rounded-lg border border-zinc-200 shadow-md p-6 max-w-sm mx-auto my-8">
      <h3 className="text-xl font-semibold text-zinc-900">{title}</h3>
      {stats.map((stat, index) => (
        <div key={index} className="mt-4 flex items-center space-x-2">
          <span className="text-lg font-semibold text-zinc-900">{stat.value}</span>
          <span className="text-sm text-zinc-700">{stat.label}</span>
        </div>
      ))}
    </div>
  );
};

export default StatCard;
