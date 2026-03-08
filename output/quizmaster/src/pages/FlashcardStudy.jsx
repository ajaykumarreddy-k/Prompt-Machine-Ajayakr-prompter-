import React from 'react';
import Navbar from '../components/Navbar';
import FlashcardComponent from '../components/FlashcardComponent';
import Footer from '../components/Footer';

const FlashcardStudy = () => (
  <div className="Container">
    <Section>
      <Stack>
        <Navbar />
        <FlashcardComponent flashcards={['Card 1', 'Card 2']} selectedCard={0} />
        <Footer />
      </Stack>
    </Section>
  </div>
);

export default FlashcardStudy;
