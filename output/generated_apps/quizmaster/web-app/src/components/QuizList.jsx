import React from 'react';

const QuizList = () => (
  <div className="mt-8 space-y-4">
    <h2 className="text-xl font-semibold">Available Quizzes</h2>
    <ul className="space-y-4">
      <li><a href="/quiz-selection">Quiz 1: Introduction to React</a></li>
      <li><a href="/quiz-selection">Quiz 2: Advanced JavaScript</a></li>
      <li><a href="/quiz-selection">Quiz 3: Tailwind CSS Fundamentals</a></li>
    </ul>
  </div>
);

export default QuizList;
