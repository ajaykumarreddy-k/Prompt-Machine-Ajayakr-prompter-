import React from 'react';

const Footer = () => {
  return (
    <footer className="footer max-w-7xl mx-auto p-6 py-16 md:py-24 bg-white rounded-lg shadow-md">
      <div className="container px-6 flex justify-between items-center">
        <p className="text-sm text-zinc-900 opacity-70">© 2023 FlowSync. All rights reserved.</p>
        <ul className="flex space-x-4">
          <li><a href="#" className="hover:underline">Privacy Policy</a></li>
          <li><a href="#" className="hover:underline">Terms of Service</a></li>
        </ul>
      </div>
    </footer>
  );
};

export default Footer;
