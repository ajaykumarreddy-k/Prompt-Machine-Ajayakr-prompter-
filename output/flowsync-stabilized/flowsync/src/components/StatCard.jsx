const StatCard = ({ stats }) => {
  return (
    <section className="bg-zinc-50 rounded-lg border border-zinc-200 shadow-md p-6">
      {stats.map((stat, index) => (
        <div key={index} className="mb-4 flex items-center">
          <span className="text-xl mr-2">{stat.value}</span>
          <span className="font-semibold">{stat.label}</span>
        </div>
      ))}
    </section>
  );
};

export default StatCard;
