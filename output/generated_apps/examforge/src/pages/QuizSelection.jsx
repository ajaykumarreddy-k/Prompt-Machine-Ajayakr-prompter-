import React from 'react';
import QuizCard from '../components/QuizCard';

const QuizSelection = () => {
  return (
    <>
      <div className="grid grid-cols-2 gap-4 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5">
        <QuizCard quizzes={[]} />
        <QuizCard quizzes={[]} />
      </div>
    </>
  );
};

export default QuizSelection;
