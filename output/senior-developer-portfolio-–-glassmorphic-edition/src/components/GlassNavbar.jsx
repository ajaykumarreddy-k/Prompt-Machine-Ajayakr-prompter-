import { Bars3Icon, XMarkIcon } from '@heroicons/react/24/outline';
import { useState } from 'react';

const GlassNavbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <nav className="bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 py-4 px-6 flex items-center justify-between">
      <div className="flex items-center">
        <div className="hidden md:block">
          <a href="/">
            <img src="/logo.png" alt="Logo" className="h-8" />
          </a>
        </div>
        <div className="md:hidden">
          <button onClick={() => setIsOpen(!isOpen)} className="p-2 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
            <Bars3Icon className="w-6 h-6" />
          </button>
        </div>
      </div>
      <div className="hidden md:flex space-x-4">
        <a href="/about" className="text-slate-900 hover:text-blue-600">About</a>
        <a href="/projects" className="text-slate-900 hover:text-blue-600">Projects</a>
        <a href="/experience" className="text-slate-900 hover:text-blue-600">Experience</a>
        <a href="/skills" className="text-slate-900 hover:text-blue-600">Skills</a>
        <a href="/features" className="text-slate-900 hover:text-blue-600">Features</a>
        <a href="/pricing" className="text-slate-900 hover:text-blue-600">Pricing</a>
        <a href="/contact" className="text-slate-900 hover:text-blue-600">Contact</a>
      </div>
      <div className="md:hidden">
        {isOpen && (
          <div className="absolute top-16 left-0 right-0 mt-2 overflow-hidden rounded-lg shadow-lg">
            <div className="flex flex-col space-y-2 p-4">
              <a href="/about" className="text-slate-900 hover:text-blue-600">About</a>
              <a href="/projects" className="text-slate-900 hover:text-blue-600">Projects</a>
              <a href="/experience" className="text-slate-900 hover:text-blue-600">Experience</a>
              <a href="/skills" className="text-slate-900 hover:text-blue-600">Skills</a>
              <a href="/features" className="text-slate-900 hover:text-blue-600">Features</a>
              <a href="/pricing" className="text-slate-900 hover:text-blue-600">Pricing</a>
              <a href="/contact" className="text-slate-900 hover:text-blue-600">Contact</a>
            </div>
          </div>
        )}
      </div>
      <div className="ml-4">
        <button className="bg-blue-600 hover:opacity-90 text-white px-6 py-3 rounded-xl font-semibold transition-all">
          Get Started
        </button>
      </div>
    </nav>
  );
};

export default GlassNavbar;
