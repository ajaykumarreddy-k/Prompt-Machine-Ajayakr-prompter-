import React from 'react';

const Section = ({ children }) => {
  return (
    <section className="py-16 md:py-24 max-w-7xl mx-auto px-6">
      {children}
    </section>
  );
};

export default Section;
