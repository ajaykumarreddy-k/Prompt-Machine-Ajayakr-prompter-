```jsx
const UserMenu = () => {
  return (
    <nav className="bg-white shadow-md p-4 flex justify-between items-center max-w-7xl mx-auto my-4">
      <div className="flex items-center space-x-2">
        <span className="text-xl font-semibold">User Menu</span>
      </div>
      <ul className="flex items-center space-x-4">
        <li>
          <Link to="/settings">Settings</Link>
        </li>
        <li>
          <a href="#" className="hover:text-zinc-700">Logout</a>
        </li>
      </ul>
    </nav>
  );
};

export default UserMenu;
```
