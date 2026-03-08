const ActivityFeed = ({ items }) => {
  return (
    <section className="bg-zinc-50 rounded-lg border border-zinc-200 shadow-md p-6">
      {items.map((item, index) => (
        <div key={index} className="mb-4 flex items-center">
          <span className="text-sm text-zinc-700 mr-2">{item.time}</span>
          <span>{item.message}</span>
        </div>
      ))}
    </section>
  );
};

export default ActivityFeed;
