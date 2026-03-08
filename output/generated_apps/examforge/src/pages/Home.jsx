import React from 'react';
import Hero from '../components/Hero';
import FlashcardComponent from '../components/FlashcardComponent';
import FeatureGrid from '../components/FeatureGrid';
import TestimonialSlider from '../components/TestimonialSlider';

const Home = () => {
  return (
    <>
      <Hero />
      <FlashcardComponent data={[]} layout="Grid" />
      <FeatureGrid />
      <TestimonialSlider />
    </>
  );
};

export default Home;
