import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="bg-white shadow-md flex items-center justify-between max-w-7xl mx-auto px-6 py-3">
      <div className="flex items-center space-x-4">
        <Link to="/" className="text-zinc-900 font-semibold text-lg">FlowSync</Link>
        <ul className="hidden md:flex items-center space-x-8">
          <li><Link to="/analytics" className="hover:text-zinc-700">Analytics</Link></li>
          <li><Link to="/settings" className="hover:text-zinc-700">Settings</Link></li>
        </ul>
      </div>
      <div className="hidden md:flex items-center space-x-4">
        <button className="bg-zinc-900 hover:opacity-90 text-white px-6 py-3 rounded-lg font-semibold transition-all">Sign In</button>
        <button className="border border-zinc-300 text-zinc-700 px-6 py-3 rounded-lg hover:bg-zinc-50 transition-all">Sign Up</button>
      </div>
    </nav>
  );
};

export default Navbar;
