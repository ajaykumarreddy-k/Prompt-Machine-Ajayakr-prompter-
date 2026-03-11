const StatCard = ({ stats }) => (
  <div className="bg-slate-900 rounded-2xl border border-slate-800 shadow-lg p-6 w-full transition-all hover:border-slate-700">
    {stats.map((stat, index) => (
      <div key={index}>
        <p className="text-sm font-medium text-slate-400 uppercase tracking-wider mb-1">{stat.title}</p>
        <p className="text-3xl font-bold text-white">{stat.value}</p>
      </div>
    ))}
  </div>
);

export default StatCard;
