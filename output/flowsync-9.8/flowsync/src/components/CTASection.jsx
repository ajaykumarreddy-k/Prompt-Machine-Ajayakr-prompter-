import React from 'react';
import { Button } from '../Button/Button';

const CTASection = ({ title, description, buttonLabel, buttonText }) => {
  return (
    <section className="cta-section max-w-7xl mx-auto p-6 py-16 md:py-24 bg-white rounded-lg shadow-md">
      <div className="container px-6">
        <h2 className="title text-xl font-bold mb-4">{title}</h2>
        <p className="description text-sm text-zinc-900 opacity-70 mb-8">{description}</p>
        <Button label={buttonLabel} text={buttonText} variant="primary" />
      </div>
    </section>
  );
};

export default CTASection;
