import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="bg-white shadow-lg p-4 flex justify-between items-center max-w-7xl mx-auto">
      <div>
        <Link to="/" className="text-xl font-bold">ExamForge</Link>
      </div>
      <ul className="flex space-x-8">
        <li><Link to="/quiz-selection" className="hover:text-zinc-900">Quiz Selection</Link></li>
        <li><Link to="/quiz-player" className="hover:text-zinc-900">Quiz Player</Link></li>
        <li><Link to="/results" className="hover:text-zinc-900">Results</Link></li>
        <li><Link to="/flashcard-study" className="hover:text-zinc-900">Flashcard Study</Link></li>
      </ul>
    </nav>
  );
};

export default Navbar;
