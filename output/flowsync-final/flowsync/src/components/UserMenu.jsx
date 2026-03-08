const UserMenu = () => {
  return (
    <div className="bg-white shadow-md rounded-lg max-w-sm mx-auto p-6 my-8">
      <h2 className="text-xl font-semibold text-zinc-900 mb-4">User Settings</h2>
      <ul className="list-disc pl-5 mt-2">
        <li>Profile</li>
        <li>Notifications</li>
        <li>Account Settings</li>
        <li>Logout</li>
      </ul>
    </div>
  );
};

export default UserMenu;
