import { useState } from 'react';

const DataGrid = ({ items = [], filters = [] }) => (
  <div className="bg-slate-900 rounded-2xl border border-slate-800 shadow-lg overflow-hidden">
    <div className="overflow-x-auto">
      <table className="w-full text-left border-collapse">
        <thead className="bg-slate-800/50">
          <tr>
            {filters.map(filter => (
              <th key={filter} className="px-6 py-4 text-sm font-semibold text-slate-300 uppercase tracking-wider border-b border-slate-800">
                {filter}
              </th>
            ))}
          </tr>
        </thead>
        <tbody className="divide-y divide-slate-800">
          {items.length > 0 ? (
            items.map((item, index) => (
              <tr key={index} className="hover:bg-slate-800/30 transition-colors">
                {filters.map((filter, filterIndex) => (
                  <td key={filterIndex} className="px-6 py-4 text-slate-300 text-sm">
                    {item[filter]}
                  </td>
                ))}
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan={filters.length} className="px-6 py-8 text-center text-slate-500 italic">
                No data available
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  </div>
);

export default DataGrid;
