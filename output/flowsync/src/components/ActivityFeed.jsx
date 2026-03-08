```jsx
const ActivityFeed = ({ items }) => {
  return (
    <div className="max-w-xl mx-auto my-8">
      <h3 className="text-lg font-semibold text-zinc-900">Recent Activities</h3>
      {items.map((item, index) => (
        <div key={index} className="mt-4 flex items-center space-x-2">
          <span className="bg-red-500 rounded-full w-3 h-3"></span>
          <p className="text-zinc-700 opacity-70">{item}</p>
        </div>
      ))}
    </div>
  );
};

export default ActivityFeed;
```
