import { Route, Routes } from 'react-router-dom';
import Navbar from '../components/Navbar';
import ChartWidget from '../components/ChartWidget';
import DataGrid from '../components/DataGrid';

const Analytics = () => {
  return (
    <div className="flex flex-col min-h-screen">
      <Navbar />
      <ChartWidget data={/* Insert sample analytics data here */} />
      <DataGrid items={/* Insert sample data grid items here */} />
    </div>
  );
};

export default Analytics;
