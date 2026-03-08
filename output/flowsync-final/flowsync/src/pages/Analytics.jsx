import Navbar from '../components/Navbar';
import DataGrid from '../components/DataGrid';

const Analytics = () => {
  return (
    <div className="bg-white">
      <Navbar />
      <DataGrid items={[
        { name: 'John Doe', description: 'Created a new project' },
        { name: 'Jane Smith', description: 'Updated task status' }
      ]} filters={[{ label: 'Name', key: 'name' }, { label: 'Description', key: 'description' }]} />
    </div>
  );
};

export default Analytics;
