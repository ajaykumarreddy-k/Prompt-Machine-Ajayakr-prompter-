```jsx
import HeroSection from '../components/HeroSection';
import StatCard from '../components/StatCard';
import ActivityFeed from '../components/ActivityFeed';
import CTASection from '../components/CTASection';

const Overview = () => {
  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6">
      <HeroSection title="Welcome to FlowSync" description="Streamline your development process with FlowSync." />
      <StatCard
        title="Key Metrics"
        stats={[
          "10,000+ Projects",
          "500+ Teams",
          "98% Customer Satisfaction",
          "24/7 Support Available",
        ]}
      />
      <ActivityFeed items={[
        { user: 'John Doe', action: 'Completed project X' },
        { user: 'Jane Smith', action: 'Updated project Y' },
      ]} />
      <CTASection ctaText="Get Started Now" linkUrl="/signup" />
    </div>
  );
};

export default Overview;
```
