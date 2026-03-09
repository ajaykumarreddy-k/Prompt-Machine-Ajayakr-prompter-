import { Link } from 'react-router-dom';

const Header = () => {
  return (
    <header className="bg-white shadow-lg">
      <div className="container mx-auto py-8 px-6 max-w-7xl rounded-lg">
        <h1 className="text-3xl font-bold text-gray-900">Welcome to MyApp</h1>
        <p className="mt-4 text-gray-700">Explore our services and features.</p>
      </div>
    </header>
  );
};

export default Header;
