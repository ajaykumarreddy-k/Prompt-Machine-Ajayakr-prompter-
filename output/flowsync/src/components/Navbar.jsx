```jsx
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="bg-white shadow-md fixed top-0 left-0 right-0 z-50">
      <div className="max-w-7xl mx-auto px-6">
        <div className="flex justify-between items-center py-3">
          <Link to="/" className="text-xl font-semibold text-zinc-900">FlowSync</Link>
          <ul className="flex space-x-4">
            <li><Link to="/analytics" className="hover:underline">Analytics</Link></li>
            <li><Link to="/settings" className="hover:underline">Settings</Link></li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
```
