const DataGrid = ({ items, filters }) => {
  return (
    <div className="bg-white shadow-md rounded-lg max-w-3xl mx-auto p-6 my-8">
      <h2 className="text-xl font-semibold text-zinc-900 mb-4">Data Grid</h2>
      <table className="w-full border-collapse">
        <thead>
          <tr>
            {filters.map((filter, index) => (
              <th key={index} className="border-b border-zinc-100 px-6 py-3 text-left">{filter.label}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {items.map((item, rowIndex) => (
            <tr key={rowIndex} className="border-b border-zinc-100">
              {filters.map((filter, colIndex) => (
                <td key={colIndex} className="px-6 py-3">{item[filter.key]}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default DataGrid;
