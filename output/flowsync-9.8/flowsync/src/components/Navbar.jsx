import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="bg-white shadow-lg sticky top-0 z-50">
      <div className="container mx-auto flex justify-between items-center py-4 px-6">
        <Link to="/" className="text-xl font-bold">FlowSync</Link>
        <ul className="flex space-x-8">
          <li><Link to="/analytics" className="hover:underline">Analytics</Link></li>
          <li><Link to="/settings" className="hover:underline">Settings</Link></li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
