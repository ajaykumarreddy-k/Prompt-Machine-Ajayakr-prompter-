import { useState } from 'react';
import StatCard from '../components/StatCard';
import ActivityFeed from '../components/ActivityFeed';
import DataGrid from '../components/DataGrid';
import ChartWidget from '../components/ChartWidget';
import UserMenu from '../components/UserMenu';

export const Overview = () => (
  <div className="container mx-auto px-6">
    <Navbar />
    <StatCard stats={[]} />
    <ActivityFeed items={[]} />
    <DataGrid items={[]} filters={[]} />
    <ChartWidget data={[]} />
    <UserMenu />
  </div>
);
