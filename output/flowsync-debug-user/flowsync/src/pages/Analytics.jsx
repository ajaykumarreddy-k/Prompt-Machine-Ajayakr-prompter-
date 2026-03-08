```jsx
import ChartWidget from '../components/ChartWidget';
import DataGrid from '../components/DataGrid';

const Analytics = () => {
  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6">
      <HeroSection title="Analytics Dashboard" description="Gain insights into your project performance." />
      <ChartWidget data={[]} filters={[]} />
      <DataGrid data={[
        { header1: 'Project A', header2: '$5,000' },
        { header1: 'Project B', header2: '$7,500' },
      ]} />
    </div>
  );
};

export default Analytics;
```
