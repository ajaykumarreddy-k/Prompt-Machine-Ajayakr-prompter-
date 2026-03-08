import React from 'react';

const ProgressBar = ({ score, currentQuestion, timeLeft }) => {
  return (
    <div className="bg-zinc-200 h-4 rounded-full mt-4">
      <div className="bg-blue-500 h-4 rounded-full" style={{ width: `${(currentQuestion / (score + 1)) * 100}%` }}>
        {/* Progress bar content */}
      </div>
    </div>
  );
};

export default ProgressBar;
