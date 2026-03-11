import React from 'react';
import HeroSection from '../components/HeroSection';
import AboutSection from '../components/AboutSection';
import PortfolioSection from '../components/PortfolioSection';
import SkillsSection from '../components/SkillsSection';
import TestimonialsSection from '../components/TestimonialsSection';
import ContactSection from '../components/ContactSection';

const Landing = () => {
  return (
    <div className="max-w-7xl mx-auto px-6">
      <HeroSection
        heroMessage="Welcome to Our Portfolio"
        callToAction="Explore Our Work"
        backgroundMedia={<img src="/hero-image.jpg" alt="Hero Image" className="w-full h-96 object-cover" />}
      />
      <AboutSection
        teamMembers={[
          { name: 'John Doe', role: 'Software Engineer' },
          { name: 'Jane Smith', role: 'UI/UX Designer' },
        ]}
        missionVision="To deliver innovative solutions that empower businesses to thrive in the digital age."
      />
      <PortfolioSection
        projects={[
          { title: 'Project X', description: 'A cutting-edge software solution for data analysis.', url: '/project-x' },
          { title: 'Project Y', description: 'A user-friendly web application for project management.', url: '/project-y' },
        ]}
      />
      <SkillsSection
        skills={[
          { name: 'React', description: 'Build dynamic and interactive user interfaces.' },
          { name: 'Node.js', description: 'Develop scalable and efficient backend services.' },
        ]}
      />
      <TestimonialsSection
        testimonials={[
          { quote: 'Great work! They delivered exactly what we needed.', name: 'Client A' },
          { quote: 'Their team is highly professional and responsive.', name: 'Client B' },
        ]}
      />
      <ContactSection
        contactForm={<input type="email" className="input" placeholder="Enter your email" />}
        officeLocation="123 Tech Street, Cityville, USA"
      />
    </div>
  );
};

export default Landing;
