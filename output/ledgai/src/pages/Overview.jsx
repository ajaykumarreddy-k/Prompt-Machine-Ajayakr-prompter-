import PageLayout from '../components/PageLayout';
import StatCard from '../components/StatCard';
import ActivityFeed from '../components/ActivityFeed';
import DataGrid from '../components/DataGrid';
import ChartWidget from '../components/ChartWidget';

const Overview = () => {
  const mockStats = [
    { title: "Total Revenue", value: "$124,500" },
    { title: "Active Invoices", value: "32" },
    { title: "Pending Taxes", value: "$12,400" }
  ];

  return (
    <PageLayout>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <StatCard stats={[mockStats[0]]} />
        <StatCard stats={[mockStats[1]]} />
        <StatCard stats={[mockStats[2]]} />
      </div>
      
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div className="space-y-8">
          <ChartWidget data={[]} />
          <DataGrid items={[]} filters={[]} />
        </div>
        <div>
          <ActivityFeed items={[]} />
        </div>
      </div>
    </PageLayout>
  );
};

export default Overview;
