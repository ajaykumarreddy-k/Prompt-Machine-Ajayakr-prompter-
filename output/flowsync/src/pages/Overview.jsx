```jsx
import StatCard from '../components/StatCard';
import ActivityFeed from '../components/ActivityFeed';
import DataGrid from '../components/DataGrid';
import UserMenu from '../components/UserMenu';
import ChartWidget from '../components/ChartWidget';

const Overview = () => {
  return (
    <div className="max-w-7xl mx-auto px-6">
      <StatCard title="Active Users" stats="1,234 users" />
      <ActivityFeed items={['User A joined the team', 'Project B was updated']} />
      <DataGrid items={[['Task 1', 'John Doe'], ['Task 2', 'Jane Smith']]} filters={['Task', 'Assignee']} />
      <ChartWidget data="Usage: 85%" />
      <UserMenu />
    </div>
  );
};

export default Overview;
```
