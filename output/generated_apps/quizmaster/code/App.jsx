import React, { useState, useEffect } from 'react';

const Navbar = () => {
  return (
    <nav className="sticky top-0 z-50 w-full border-b border-gray-100 bg-white/80 px-6 py-4 text-sm font-medium backdrop-blur-md">
      <div className="mx-auto flex max-w-7xl items-center justify-between">
        <div className="flex items-center gap-2">
          <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-blue-600 text-white font-bold">B</div>
          <span className="text-xl font-bold tracking-tight text-gray-900">QuizMaster</span>
        </div>
        <div className="hidden md:flex items-center gap-8">
          <a href="#" className="text-gray-600 transition-colors hover:text-gray-900">Features</a>
          <a href="#" className="text-gray-600 transition-colors hover:text-gray-900">Pricing</a>
          <a href="#" className="text-gray-600 transition-colors hover:text-gray-900">Docs</a>
        </div>
        <div className="flex items-center gap-4">
          <a href="#" className="hidden text-gray-600 transition-colors hover:text-gray-900 md:block">Log in</a>
          <button className="rounded-lg bg-blue-500 px-4 py-2 text-white transition-colors hover:bg-blue-700">Get Started Now</button>
        </div>
      </div>
    </nav>
  );
};

const HeroSection = () => {
  return (
    <section className="section_class">
      <div className="container mx-auto px-6 py-16 md:py-24">
        <h1 className="text-3xl font-bold text-gray-900">Take Your Quizzes to the Next Level with QuizMaster</h1>
        <p className="mt-4 text-base text-zinc-700 opacity-70">QuizMaster is a powerful tool designed for students and developers to create engaging quizzes. Start building your quizzes today!</p>
        <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-8">Get Started Now</button>
      </div>
    </section>
  );
};

const QuizCard = ({ title, description }) => {
  return (
    <div className="card mb-6">
      <h3 className="text-xl font-semibold text-gray-900">{title}</h3>
      <p className="mt-2 text-base text-zinc-700 opacity-70">{description}</p>
    </div>
  );
};

const FeaturesSection = () => {
  return (
    <section className="section_class">
      <div className="container mx-auto px-6 py-16 md:py-24 grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
        <QuizCard title="Quiz Selection" description="Choose from a wide range of pre-built quizzes or create your own." />
        <QuizCard title="Timed Questions" description="Set time limits for each question to challenge your participants." />
        <QuizCard title="Score Calculation" description="Automatically calculate scores and provide detailed feedback." />
        <QuizCard title="Instant Feedback" description="Get immediate results after answering each question." />
        <QuizCard title="Results Dashboard" description="View comprehensive reports on quiz performance and progress." />
      </div>
    </section>
  );
};

const Footer = () => {
  return (
    <footer className="section_class">
      <div className="container mx-auto px-6 py-16 md:py-24 flex justify-center items-center gap-8">
        <a href="#" className="text-gray-600 transition-colors hover:text-gray-900">Privacy Policy</a>
        <a href="#" className="text-gray-600 transition-colors hover:text-gray-900">Terms of Service</a>
        <a href="#" className="text-gray-600 transition-colors hover:text-gray-900">Contact Us</a>
      </div>
    </footer>
  );
};

const QuizPlayer = () => {
  const [currentQuestion, setCurrentQuestion] = useState(1);
  const [selectedOption, setSelectedOption] = useState(null);
  const [isCorrect, setIsCorrect] = useState(false);

  useEffect(() => {
    if (currentQuestion > 5) {
      alert('Quiz completed!');
    }
  }, [currentQuestion]);

  return (
    <div className="container mx-auto px-6 py-16 md:py-24">
      <h3 className="text-2xl font-semibold text-gray-900">Question {currentQuestion}</h3>
      <p className="mt-4 text-base text-zinc-700 opacity-70">What is the capital of France?</p>
      <div className="mt-8 flex gap-4">
        <OptionButton label="Paris" onClick={() => setSelectedOption('Paris')} isCorrect={selectedOption === 'Paris'} isSelected={selectedOption !== null} />
        <OptionButton label="Berlin" onClick={() => setSelectedOption('Berlin')} isCorrect={selectedOption === 'Paris'} isSelected={selectedOption !== null} />
        <OptionButton label="London" onClick={() => setSelectedOption('London')} isCorrect={selectedOption === 'Paris'} isSelected={selectedOption !== null} />
      </div>
      {isCorrect && (
        <p className="mt-4 text-green-600">Correct!</p>
      )}
      {!isCorrect && selectedOption && (
        <p className="mt-4 text-red-500">Incorrect, the correct answer is Paris.</p>
      )}
    </div>
  );
};

const OptionButton = ({ label, onClick, isCorrect, isSelected }) => {
  return (
    <button
      onClick={onClick}
      className={`w-full px-6 py-3 rounded-lg ${isSelected ? 'border-2 border-zinc-900' : ''} ${isCorrect ? 'bg-green-100' : 'bg-red-100'} text-white`}
    >
      {label}
    </button>
  );
};

const App = () => {
  return (
    <div className="bg-white">
      <Navbar />
      <HeroSection />
      <FeaturesSection />
      <QuizPlayer />
      <Footer />
    </div>
  );
};

export default App;
