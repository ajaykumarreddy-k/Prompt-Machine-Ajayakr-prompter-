import React, { useState } from 'react';
import QuestionCard from '../components/QuestionCard';
import OptionButton from '../components/OptionButton';
import Timer from '../components/Timer';
import ProgressBar from '../components/ProgressBar';

const QuizPlayer = () => {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [score, setScore] = useState(0);
  const [timeLeft, setTimeLeft] = useState(60);

  const handleSelect = (selected) => {
    // Handle question selection logic
  };

  const handleTimeUp = () => {
    // Handle time up logic
  };

  return (
    <>
      <QuestionCard data={[]} selected={currentQuestion} onSelect={handleSelect} />
      <OptionButton onClick={() => setCurrentQuestion(currentQuestion + 1)}>Next</OptionButton>
      <Timer timeLeft={timeLeft} onTimeUp={handleTimeUp} />
      <ProgressBar score={score} currentQuestion={currentQuestion} timeLeft={timeLeft} />
    </>
  );
};

export default QuizPlayer;
