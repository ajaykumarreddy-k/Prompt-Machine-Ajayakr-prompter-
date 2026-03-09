jsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import StatCard from '../components/StatCard';

const HomePage = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<div className="px-6 py-16 max-w-7xl mx-auto rounded-lg">
          <StatCard
            title="Total Users"
            value="5,200"
            description="Number of registered users"
          />
          <StatCard
            title="Active Projects"
            value="34"
            description="Current active projects"
          />
        </div>} />
      </Routes>
    </Router>
  );
};

export default HomePage;
