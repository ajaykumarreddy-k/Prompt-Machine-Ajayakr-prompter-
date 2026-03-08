import React from 'react';
import Navbar from '../components/Navbar';
import QuizList from '../components/QuizList';
import Footer from '../components/Footer';

const QuizSelection = () => (
  <div className="Container">
    <Section>
      <Stack>
        <Navbar />
        <QuizList />
        <Footer />
      </Stack>
    </Section>
  </div>
);

export default QuizSelection;
