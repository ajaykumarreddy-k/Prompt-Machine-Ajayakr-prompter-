jsx
import React from 'react';
import { Link } from 'react-router-dom';

const StatCard = ({ title, value, description }) => {
  return (
    <div className="max-w-sm rounded-lg bg-white shadow-md dark:bg-gray-800 p-6">
      <h3 className="text-xl font-bold text-gray-900 dark:text-white">{title}</h3>
      <p className="mt-2 text-4xl font-semibold text-blue-500 dark:text-blue-400">{value}</p>
      <p className="mt-4 text-base text-gray-600 dark:text-gray-400">{description}</p>
    </div>
  );
};

export default StatCard;
