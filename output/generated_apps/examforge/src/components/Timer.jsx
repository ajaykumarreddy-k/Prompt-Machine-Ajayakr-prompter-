import React from 'react';

const Timer = ({ timeLeft, onTimeUp }) => {
  return (
    <div className="text-center mt-4">
      <p>{timeLeft} seconds left</p>
      {/* Time up logic */}
    </div>
  );
};

export default Timer;
