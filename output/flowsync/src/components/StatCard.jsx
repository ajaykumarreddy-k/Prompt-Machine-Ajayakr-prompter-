```jsx
const StatCard = ({ title, stats }) => {
  return (
    <section className="bg-zinc-50 rounded-lg border border-zinc-200 shadow-md p-6 max-w-sm mx-auto my-8">
      <h3 className="text-xl font-semibold text-zinc-900">{title}</h3>
      <p className="mt-4 text-lg font-medium text-zinc-900">{stats}</p>
    </section>
  );
};

export default StatCard;
```
