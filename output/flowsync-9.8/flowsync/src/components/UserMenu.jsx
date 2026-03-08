import React from 'react';

const UserMenu = () => {
  return (
    <div className="user-menu max-w-7xl mx-auto p-6 py-16 md:py-24 bg-white rounded-lg shadow-md">
      <h3 className="text-xl font-bold mb-4">User Settings</h3>
      <ul className="flex flex-col space-y-4">
        <li className="flex items-center justify-between">
          <span className="text-sm text-zinc-900 opacity-70">Profile</span>
          <button className="btn btn-secondary">Edit</button>
        </li>
        <li className="flex items-center justify-between">
          <span className="text-sm text-zinc-900 opacity-70">Billing</span>
          <button className="btn btn-secondary">Manage</button>
        </li>
        <li className="flex items-center justify-between">
          <span className="text-sm text-zinc-900 opacity-70">Logout</span>
          <button className="btn btn-secondary">Sign Out</button>
        </li>
      </ul>
    </div>
  );
};

export default UserMenu;
