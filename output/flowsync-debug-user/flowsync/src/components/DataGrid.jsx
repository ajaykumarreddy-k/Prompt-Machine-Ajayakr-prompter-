```jsx
const DataGrid = ({ data }) => {
  return (
    <div className="bg-white rounded-lg border border-zinc-200 shadow-md p-6 max-w-sm mx-auto my-4">
      <h2 className="text-xl font-semibold text-zinc-900">Data Grid</h2>
      {/* Placeholder for data grid */}
      <table className="mt-4 w-full whitespace-nowrap rounded-lg border-collapse bg-white divide-y divide-zinc-100">
        <thead className="bg-gray-50">
          <tr>
            <th className="px-6 py-3 text-left font-semibold text-zinc-900">Header 1</th>
            <th className="px-6 py-3 text-left font-semibold text-zinc-900">Header 2</th>
          </tr>
        </thead>
        <tbody>
          {data.map((row, rowIndex) => (
            <tr key={rowIndex} className="hover:bg-gray-50">
              <td className="px-6 py-4">{row.header1}</td>
              <td className="px-6 py-4">{row.header2}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default DataGrid;
```
