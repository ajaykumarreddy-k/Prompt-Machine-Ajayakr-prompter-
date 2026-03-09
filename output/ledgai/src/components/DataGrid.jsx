import { useState } from 'react';

export const DataGrid = ({ items, filters }) => (
  <div className="bg-slate-900 rounded-2xl border border-slate-800 shadow-lg p-6 max-w-sm mx-auto my-4 text-center">
    <table className="w-full mt-4">
      <thead>
        <tr>
          {filters.map(filter => (
            <th key={filter} className="p-3 bg-slate-900 border-b border-slate-800 text-left">
              {filter}
            </th>
          ))}
        </tr>
      </thead>
      <tbody>
        {items.map((item, index) => (
          <tr key={index}>
            {filters.map((_, filterIndex) => (
              <td key={filterIndex} className="p-3 border-b border-slate-800">
                {item[filters[filterIndex]]}
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  </div>
);
