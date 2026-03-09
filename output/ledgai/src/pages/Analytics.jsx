import { useState } from 'react';
import ChartWidget from '../components/ChartWidget';
import DataGrid from '../components/DataGrid';

export const Analytics = () => (
  <div className="container mx-auto px-6">
    <Navbar />
    <ChartWidget data={[]} />
    <DataGrid items={[]} filters={[]} />
  </div>
);
