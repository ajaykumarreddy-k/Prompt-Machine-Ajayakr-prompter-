```jsx
const ChartWidget = ({ data }) => {
  return (
    <section className="bg-zinc-50 rounded-lg border border-zinc-200 shadow-md p-6 max-w-sm mx-auto my-8">
      <h3 className="text-xl font-semibold text-zinc-900">Insights</h3>
      <div className="mt-4">
        {/* Placeholder for chart */}
        <p className="text-lg font-medium text-zinc-900">Data: {data}</p>
      </div>
    </section>
  );
};

export default ChartWidget;
```
