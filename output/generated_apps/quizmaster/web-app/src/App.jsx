import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import QuizSelection from './pages/QuizSelection';
import QuizPlayer from './components/QuizPlayer';
import Results from './pages/Results';
import FlashcardStudy from './pages/FlashcardStudy';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/quiz-selection" element={<QuizSelection />} />
        <Route path="/quiz-player" element={<QuizPlayer />} />
        <Route path="/results" element={<Results />} />
        <Route path="/flashcards" element={<FlashcardStudy />} />
      </Routes>
    </Router>
  );
}

export default App;
