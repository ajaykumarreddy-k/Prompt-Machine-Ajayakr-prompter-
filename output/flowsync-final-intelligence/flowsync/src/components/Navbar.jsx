import { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';

const Navbar = () => {
  const location = useLocation();

  return (
    <nav className="bg-white shadow-lg sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-6 py-3 flex items-center justify-between">
        <Link to="/" className="text-xl font-bold text-zinc-900">FlowSync</Link>
        <ul className="flex space-x-4">
          <li>
            <Link
              to="/"
              className={`${
                location.pathname === '/' ? 'bg-zinc-50 hover:opacity-90' : ''
              } px-6 py-3 rounded-lg text-zinc-700`}
            >
              Overview
            </Link>
          </li>
          <li>
            <Link
              to="/analytics"
              className={`${
                location.pathname === '/analytics'
                  ? 'bg-zinc-50 hover:opacity-90'
                  : ''
              } px-6 py-3 rounded-lg text-zinc-700`}
            >
              Analytics
            </Link>
          </li>
          <li>
            <Link
              to="/settings"
              className={`${
                location.pathname === '/settings'
                  ? 'bg-zinc-50 hover:opacity-90'
                  : ''
              } px-6 py-3 rounded-lg text-zinc-700`}
            >
              Settings
            </Link>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
