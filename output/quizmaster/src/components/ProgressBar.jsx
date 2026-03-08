import React from 'react';

const ProgressBar = ({ progress }) => (
  <div className="mt-4 flex items-center space-x-2">
    <div className="bg-zinc-200 h-2 w-full rounded-lg">
      <div className="h-2 bg-blue-500 rounded-lg" style={{ width: `${progress}%` }}></div>
    </div>
    <span>{`${progress}% Complete`}</span>
  </div>
);

export default ProgressBar;
