import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="fixed top-0 left-0 right-0 z-50 bg-black px-6 py-4 shadow-lg">
      <div className="container mx-auto flex justify-between items-center max-w-7xl">
        <Link to="/" className="text-white text-xl font-bold">MyApp</Link>
        <ul className="flex space-x-8">
          <li><Link to="/home" className="text-white hover:text-gray-300">Home</Link></li>
          <li><Link to="/about" className="text-white hover:text-gray-300">About</Link></li>
          <li><Link to="/contact" className="text-white hover:text-gray-300">Contact</Link></li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
