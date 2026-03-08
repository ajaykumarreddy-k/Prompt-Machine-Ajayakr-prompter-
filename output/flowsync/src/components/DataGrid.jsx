```jsx
const DataGrid = ({ items, filters }) => {
  return (
    <div className="max-w-2xl mx-auto my-8 overflow-x-auto">
      <table className="w-full text-left text-sm font-light">
        <thead className="bg-zinc-50 border-b border-zinc-200">
          <tr>
            {filters.map((filter) => (
              <th key={filter} scope="col" className="px-6 py-4">{filter}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {items.map((item, index) => (
            <tr key={index} className="border-b border-zinc-200">
              {filters.map((_, i) => (
                <td key={i} className="px-6 py-4">{item[i]}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default DataGrid;
```
