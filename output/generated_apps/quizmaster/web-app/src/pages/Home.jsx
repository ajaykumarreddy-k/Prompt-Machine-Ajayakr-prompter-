import React from 'react';
import Navbar from '../components/Navbar';
import QuizList from '../components/QuizList';
import Footer from '../components/Footer';

const Home = () => (
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

export default Home;
