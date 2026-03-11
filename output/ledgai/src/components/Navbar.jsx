import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="bg-[#1A202C] py-6 px-4 sm:px-6 lg:px-8 flex justify-between items-center sticky top-0 z-50 shadow-md">
      <div className="flex items-center space-x-4">
        <Link to="/" className="text-2xl font-bold text-white flex items-center">
          <span className="text-cyan-400 mr-2">◈</span> LedgAI
        </Link>
      </div>
      <div className="hidden md:flex space-x-8">
        <Link to="/" className="text-slate-200 hover:text-cyan-400 transition-colors font-medium">Overview</Link>
        <Link to="/analytics" className="text-slate-200 hover:text-cyan-400 transition-colors font-medium">Analytics</Link>
        <Link to="/settings" className="text-slate-200 hover:text-cyan-400 transition-colors font-medium">Settings</Link>
      </div>
      <div className="flex items-center space-x-4">
        <button className="bg-violet-500 hover:bg-violet-600 text-white px-4 py-2 rounded-xl text-sm font-semibold transition-all">
          New Invoice
        </button>
      </div>
    </nav>
  );
};

export default Navbar;
