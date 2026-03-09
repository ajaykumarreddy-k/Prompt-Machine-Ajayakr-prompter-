### File: `src/components/StatCard.jsx`

import React from 'react';

const StatCard = ({ title, value }) => {
  return (
    <div className="bg-white shadow-lg rounded-lg p-6 max-w-sm mx-auto my-4">
      <h2 className="text-xl font-semibold mb-2">{title}</h2>
      <p className="text-3xl font-bold text-gray-800">{value}</p>
    </div>
  );
};

export default StatCard;

### File: `src/components/ActivityFeed.jsx`

import React from 'react';

const ActivityFeed = ({ activities }) => {
  return (
    <div className="bg-white shadow-lg rounded-lg p-6 max-w-sm mx-auto my-4">
      {activities.map((activity, index) => (
        <div key={index} className="py-4 border-b last:border-b-0">
          <p className="text-gray-700">{activity}</p>
        </div>
      ))}
    </div>
  );
};

export default ActivityFeed;

### File: `src/components/ActivityItem.jsx`

import React from 'react';

const ActivityItem = ({ activity }) => {
  return (
    <div className="py-4 border-b last:border-b-0">
      <p className="text-gray-700">{activity}</p>
    </div>
  );
};

export default ActivityItem;

### File: `src/App.jsx`

import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import StatCard from './components/StatCard';
import ActivityFeed from './components/ActivityFeed';

function App() {
  const activities = [
    "User logged in",
    "New message received",
    "Profile updated",
    "Payment successful"
  ];

  return (
    <Router>
      <Routes>
        <Route path="/stat-card" element={<StatCard title="Total Users" value="1,234"} />}
        <Route path="/activity-feed" element={<ActivityFeed activities={activities} />} />
      </Routes>
    </Router>
  );
}

export default App;

### File: `src/pages/Index.jsx`

import React from 'react';
import StatCard from '../components/StatCard';

const Index = () => {
  return (
    <div className="max-w-7xl px-6 py-16 mx-auto">
      <h1 className="text-3xl font-bold text-center mb-8">Welcome to Float UI</h1>
      <StatCard title="Total Users" value="1,234" />
      <ActivityFeed activities={['User logged in', 'New message received']} />
    </div>
  );
};

export default Index;

### File: `src/pages/StatCard.jsx`

import React from 'react';
import StatCard from '../components/StatCard';

const StatCardPage = () => {
  return (
    <div className="max-w-7xl px-6 py-16 mx-auto">
      <h1 className="text-3xl font-bold text-center mb-8">Stat Card Page</h1>
      <StatCard title="Total Users" value="1,234" />
    </div>
  );
};

export default StatCardPage;

### File: `src/pages/ActivityFeed.jsx`

import React from 'react';
import ActivityFeed from '../components/ActivityFeed';

const ActivityFeedPage = () => {
  const activities = [
    "User logged in",
    "New message received",
    "Profile updated",
    "Payment successful"
  ];

  return (
    <div className="max-w-7xl px-6 py-16 mx-auto">
      <h1 className="text-3xl font-bold text-center mb-8">Activity Feed Page</h1>
      <ActivityFeed activities={activities} />
    </div>
  );
};

export default ActivityFeedPage;

### File: `src/pages/Home.jsx`

import React from 'react';
import StatCard from '../components/StatCard';
import ActivityFeed from '../components/ActivityFeed';

const HomePage = () => {
  return (
    <div className="max-w-7xl px-6 py-16 mx-auto">
      <h1 className="text-3xl font-bold text-center mb-8">Home Page</h1>
      <StatCard title="Total Users" value="1,234" />
      <ActivityFeed activities={['User logged in', 'New message received']} />
    </div>
  );
};

export default HomePage;

This setup follows the blueprint and ensures that each component has its own file. The routing is handled using `react-router-dom`, and design tokens are applied directly to HTML elements as specified.