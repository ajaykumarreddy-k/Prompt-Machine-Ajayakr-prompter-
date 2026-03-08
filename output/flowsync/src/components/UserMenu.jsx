```jsx
const UserMenu = () => {
  return (
    <div className="max-w-sm mx-auto my-8">
      <h3 className="text-lg font-semibold text-zinc-900">User Settings</h3>
      <ul className="mt-4 flex space-x-2">
        <li><button className="secondary-btn">Profile</button></li>
        <li><button className="primary-btn">Logout</button></li>
      </ul>
    </div>
  );
};

export default UserMenu;
```
