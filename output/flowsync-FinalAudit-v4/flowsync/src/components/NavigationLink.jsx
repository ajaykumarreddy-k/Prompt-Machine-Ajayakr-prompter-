import { Link } from 'react-router-dom';

const NavigationLink = ({ to, children }) => {
  return (
    <li className="text-white hover:text-gray-300">
      <Link to={to}>{children}</Link>
    </li>
  );
};

export default NavigationLink;
