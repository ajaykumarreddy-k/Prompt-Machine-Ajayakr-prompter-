import React from 'react';

const OptionButton = ({ children }) => {
  return (
    <button className="bg-zinc-900 hover:opacity-90 text-white px-6 py-3 rounded-lg font-semibold transition-all">
      {children}
    </button>
  );
};

export default OptionButton;
