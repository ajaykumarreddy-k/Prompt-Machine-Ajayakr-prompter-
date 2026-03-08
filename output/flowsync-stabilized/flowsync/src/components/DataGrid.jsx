const DataGrid = ({ items }) => {
  return (
    <table className="w-full text-sm text-left text-zinc-900 dark:text-gray-400">
      <thead className="bg-zinc-50 border-b border-zinc-200">
        <tr>
          {items[0] && Object.keys(items[0]).map((key, index) => (
            <th key={index} scope="col" className="px-6 py-3">{key}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {items.map((item, index) => (
          <tr key={index}>
            {Object.values(item).map((value, subIndex) => (
              <td key={subIndex} className="px-6 py-4">{value}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default DataGrid;
