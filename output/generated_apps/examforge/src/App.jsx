import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import FlashcardComponent from './components/FlashcardComponent';
import FeatureGrid from './components/FeatureGrid';
import TestimonialSlider from './components/TestimonialSlider';
import QuizSelection from './pages/QuizSelection';
import QuizPlayer from './pages/QuizPlayer';
import Results from './pages/Results';
import FlashcardStudy from './pages/FlashcardStudy';

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/quiz-selection" element={<QuizSelection />} />
        <Route path="/quiz-player" element={<QuizPlayer />} />
        <Route path="/results" element={<Results />} />
        <Route path="/flashcard-study" element={<FlashcardStudy />} />
      </Routes>
    </Router>
  );
}

function Home() {
  return (
    <>
      <Hero />
      <FlashcardComponent data={[]} layout="Grid" />
      <FeatureGrid />
      <TestimonialSlider />
    </>
  );
}

export default App;
