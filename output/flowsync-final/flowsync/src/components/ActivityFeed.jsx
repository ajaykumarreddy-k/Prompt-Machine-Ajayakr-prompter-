const ActivityFeed = ({ items }) => {
  return (
    <section className="bg-white shadow-md rounded-lg max-w-3xl mx-auto p-6 my-8">
      <h2 className="text-xl font-semibold text-zinc-900 mb-4">Recent Activities</h2>
      {items.map((item, index) => (
        <div key={index} className="flex items-center space-x-4 py-4 border-b border-zinc-100 last:border-0">
          <img src={item.avatar} alt={item.name} className="w-8 h-8 rounded-full" />
          <div>
            <p className="text-sm font-medium text-zinc-900">{item.name}</p>
            <p className="text-xs text-zinc-700">{item.description}</p>
          </div>
        </div>
      ))}
    </section>
  );
};

export default ActivityFeed;
