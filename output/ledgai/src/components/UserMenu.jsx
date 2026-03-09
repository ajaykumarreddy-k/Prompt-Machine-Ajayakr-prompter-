import { useState } from 'react';

export const UserMenu = () => (
  <div className="bg-slate-900 rounded-2xl border border-slate-800 shadow-lg p-6 max-w-sm mx-auto my-4 text-center">
    {/* User-specific actions like profile, settings, logout */}
    <button className="w-full bg-violet-500 hover:opacity-90 text-white px-6 py-3 rounded-2xl font-semibold transition-all">Profile</button>
    <button className="mt-4 w-full border border-violet-300 text-violet-700 px-6 py-3 rounded-2xl hover:bg-violet-50 transition-all">Settings</button>
    <button className="mt-4 w-full bg-violet-500 hover:opacity-90 text-white px-6 py-3 rounded-2xl font-semibold transition-all">Logout</button>
  </div>
);
