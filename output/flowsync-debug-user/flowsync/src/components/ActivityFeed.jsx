```jsx
const ActivityFeed = ({ items }) => {
  return (
    <div className="bg-white rounded-lg border border-zinc-200 shadow-md p-6 max-w-sm mx-auto my-4">
      <h2 className="text-xl font-semibold text-zinc-900">Recent Activities</h2>
      {items.map((item, index) => (
        <div key={index} className="mt-4 flex items-center space-x-2">
          <span className="text-sm font-medium text-zinc-700">{item.user}</span>
          <p className="text-sm text-zinc-900 opacity-70">{item.action}</p>
        </div>
      ))}
    </div>
  );
};

export default ActivityFeed;
```
