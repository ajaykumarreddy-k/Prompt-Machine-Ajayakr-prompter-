import React from 'react';

const ActivityFeed = () => {
  return (
    <section className="activity-feed max-w-7xl mx-auto p-6 py-16 md:py-24 bg-white rounded-lg shadow-md">
      <h3 className="text-xl font-bold mb-4">Recent Activities</h3>
      <ul>
        <li className="flex items-center mb-4">
          <div className="w-8 h-8 flex-shrink-0 rounded-full bg-blue-500 mr-2"></div>
          <p className="text-sm text-zinc-900 opacity-70">John Doe created a new task</p>
        </li>
        <li className="flex items-center mb-4">
          <div className="w-8 h-8 flex-shrink-0 rounded-full bg-green-500 mr-2"></div>
          <p className="text-sm text-zinc-900 opacity-70">Jane Smith commented on a task</p>
        </li>
      </ul>
    </section>
  );
};

export default ActivityFeed;
