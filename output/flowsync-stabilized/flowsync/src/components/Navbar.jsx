import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="bg-white shadow-lg p-6">
      <div className="container mx-auto flex justify-between items-center">
        <Link to="/" className="text-zinc-900 font-semibold text-xl">
          FlowSync
        </Link>
        <ul className="flex space-x-4">
          <li><Link to="/">Home</Link></li>
          <li><Link to="/analytics">Analytics</Link></li>
          <li><Link to="/settings">Settings</Link></li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
