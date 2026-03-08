import React from 'react';

const OptionButton = ({ options, onSelect }) => (
  <div className="mt-8 space-y-4">
    {options.map((option) => (
      <button
        key={option}
        onClick={() => onSelect(option)}
        className="w-full py-2 rounded-lg bg-zinc-100 hover:bg-zinc-200"
      >
        {option}
      </button>
    ))}
  </div>
);

export default OptionButton;
