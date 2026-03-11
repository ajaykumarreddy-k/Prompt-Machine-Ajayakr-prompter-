import { PricingCard } from '@/components/ui/pricing-card';

const GlassPricingSection = ({ title, subtitle, tiers }) => {
  return (
    <section className="py-16 md:py-24">
      <div className="max-w-7xl mx-auto px-6">
        <h2 className="text-3xl font-bold text-slate-900 mb-4">{title}</h2>
        <p className="text-lg text-slate-900 mb-8">{subtitle}</p>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {tiers.map((tier) => (
            <PricingCard key={tier.name} {...tier} />
          ))}
        </div>
      </div>
    </section>
  );
};

export default GlassPricingSection;
