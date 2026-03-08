import React from 'react';

const DataGrid = ({ items }) => {
  return (
    <section className="data-grid max-w-7xl mx-auto p-6 py-16 md:py-24 bg-white rounded-lg shadow-md">
      <h3 className="text-xl font-bold mb-4">Data Overview</h3>
      <table className="w-full text-left table-auto">
        <thead>
          <tr>
            <th className="p-4 border-b-2">ID</th>
            <th className="p-4 border-b-2">Name</th>
            <th className="p-4 border-b-2">Status</th>
            <th className="p-4 border-b-2">Due Date</th>
          </tr>
        </thead>
        <tbody>
          {items.map((item, index) => (
            <tr key={index} className="border-b">
              <td className="p-4">{item.id}</td>
              <td className="p-4">{item.name}</td>
              <td className="p-4">{item.status}</td>
              <td className="p-4">{item.dueDate}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  );
};

export default DataGrid;
