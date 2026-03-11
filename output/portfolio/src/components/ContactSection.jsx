import React from 'react';

const ContactSection = ({ contactForm, officeLocation }) => {
  return (
    <section className="p-8 max-w-7xl mx-auto px-6">
      <h2 className="text-2xl md:text-3xl font-bold mb-4">Contact Us</h2>
      <div className="mb-4">
        <p className="text-zinc-900 opacity-70">{officeLocation}</p>
      </div>
      <form className="space-y-4">
        {contactForm}
      </form>
    </section>
  );
};

export default ContactSection;
