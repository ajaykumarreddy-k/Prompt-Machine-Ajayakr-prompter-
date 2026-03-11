import PageLayout from '../components/PageLayout';
import ChartWidget from '../components/ChartWidget';
import DataGrid from '../components/DataGrid';

const Analytics = () => (
  <PageLayout>
    <div className="space-y-8">
      <h2 className="text-3xl font-bold text-white">Analytics Overview</h2>
      <ChartWidget data={[]} />
      <DataGrid items={[]} filters={[]} />
    </div>
  </PageLayout>
);

export default Analytics;
