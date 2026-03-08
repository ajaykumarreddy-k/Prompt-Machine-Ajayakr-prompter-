import React, { useState } from 'react';

const Timer = ({ timeLeft, onTimeUp }) => {
  const [remainingTime, setRemainingTime] = useState(timeLeft);

  const handleTimeUp = () => {
    if (onTimeUp) onTimeUp();
  };

  return (
    <div className="mt-4 flex items-center space-x-2">
      <span>{`${Math.floor(remainingTime / 60)}:${remainingTime % 60 < 10 ? '0' : ''}${remainingTime % 60}`}</span>
      <button
        onClick={handleTimeUp}
        className="bg-red-500 text-white px-4 py-2 rounded-lg"
      >
        Time Up!
      </button>
    </div>
  );
};

export default Timer;
