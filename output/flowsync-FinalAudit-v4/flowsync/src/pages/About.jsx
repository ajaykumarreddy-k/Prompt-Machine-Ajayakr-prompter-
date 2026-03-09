import React from 'react';
import Header from '../components/Header';

const About = () => {
  return (
    <section className="bg-white py-16">
      <Header />
      <div className="container mx-auto px-6 max-w-7xl">
        <h2 className="text-3xl font-bold text-gray-900">About Us</h2>
        <p className="mt-4 text-gray-700">Learn more about our company.</p>
      </div>
    </section>
  );
};

export default About;
