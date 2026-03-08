import React from 'react';

const Navbar = () => (
  <nav className="bg-white shadow-md p-4 flex justify-between items-center max-w-7xl mx-auto">
    <div className="text-xl font-semibold">QuizMaster</div>
    <ul className="flex space-x-4">
      <li><a href="/">Home</a></li>
      <li><a href="/quiz-selection">Select Quiz</a></li>
      <li><a href="/quiz-player">Play Quiz</a></li>
      <li><a href="/results">Results</a></li>
      <li><a href="/flashcards">Flashcard Study</a></li>
    </ul>
  </nav>
);

export default Navbar;
