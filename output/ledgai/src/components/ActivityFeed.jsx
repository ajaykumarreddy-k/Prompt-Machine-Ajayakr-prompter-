const ActivityFeed = ({ items = [] }) => {
  const defaultItems = [
    { title: "Invoice Paid", description: "Blue Horizon Corp paid $4,500.00", time: "2h ago" },
    { title: "Tax Alert", description: "Q1 estimated tax updated", time: "5h ago" },
    { title: "Expense Added", description: "AWS Cloud Services categorized as Softare", time: "1d ago" }
  ];

  const displayItems = items.length > 0 ? items : defaultItems;

  return (
    <div className="bg-slate-900 rounded-2xl border border-slate-800 shadow-lg p-6 w-full">
      <h3 className="text-lg font-bold text-white mb-6 flex items-center">
        <span className="w-2 h-2 bg-cyan-400 rounded-full mr-2"></span>
        Recent Activity
      </h3>
      <div className="space-y-6">
        {displayItems.map((item, index) => (
          <div key={index} className="flex space-x-4 relative">
            {index !== displayItems.length - 1 && (
              <div className="absolute left-2 top-8 bottom-[-24px] w-[1px] bg-slate-800"></div>
            )}
            <div className="w-4 h-4 rounded-full bg-slate-800 border border-slate-700 z-10 mt-1"></div>
            <div className="flex-1">
              <div className="flex justify-between items-start mb-1">
                <p className="text-sm font-semibold text-white">{item.title}</p>
                <span className="text-[10px] uppercase tracking-wider text-slate-500">{item.time}</span>
              </div>
              <p className="text-xs text-slate-400 leading-relaxed">{item.description}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ActivityFeed;
