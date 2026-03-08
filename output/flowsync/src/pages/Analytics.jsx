```jsx
import ChartWidget from '../components/ChartWidget';
import DataGrid from '../components/DataGrid';

const Analytics = () => {
  return (
    <div className="max-w-7xl mx-auto px-6">
      <ChartWidget data="Revenue: $12,345" />
      <DataGrid items={[['Task 1', 'John Doe'], ['Task 2', 'Jane Smith']]} filters={['Task', 'Assignee']} />
    </div>
  );
};

export default Analytics;
```
