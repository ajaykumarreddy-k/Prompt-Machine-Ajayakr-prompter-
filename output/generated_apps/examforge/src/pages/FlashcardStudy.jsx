import React from 'react';
import FlashcardComponent from '../components/FlashcardComponent';
import NewsletterSignup from '../components/NewsletterSignup';

const FlashcardStudy = () => {
  return (
    <>
      <FlashcardComponent data={[]} layout="Grid" />
      <NewsletterSignup />
    </>
  );
};

export default FlashcardStudy;
