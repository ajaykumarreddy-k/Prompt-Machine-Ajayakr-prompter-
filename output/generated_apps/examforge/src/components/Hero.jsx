import React from 'react';
import { Container } from './Container';

const Hero = () => {
  return (
    <section className="bg-white py-16 md:py-24 max-w-7xl mx-auto px-6">
      <Container>
        <div className="text-center">
          <h1 className="text-3xl font-bold text-zinc-900">Interactive Quizzes, Flashcards & More</h1>
          <p className="mt-4 text-lg text-zinc-700">Prepare for competitive exams with ExamForge's comprehensive learning tools.</p>
        </div>
      </Container>
    </section>
  );
};

export default Hero;
