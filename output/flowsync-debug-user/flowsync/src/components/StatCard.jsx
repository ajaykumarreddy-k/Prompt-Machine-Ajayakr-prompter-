```jsx
const StatCard = ({ title, stats }) => {
  return (
    <div className="bg-zinc-50 rounded-lg border border-zinc-200 shadow-md p-6 max-w-sm mx-auto my-4">
      <h2 className="text-xl font-semibold text-zinc-900">{title}</h2>
      {stats.map((stat, index) => (
        <p key={index} className="mt-2 text-lg font-medium text-zinc-900 opacity-70">
          {stat}
        </p>
      ))}
    </div>
  );
};

export default StatCard;
```
