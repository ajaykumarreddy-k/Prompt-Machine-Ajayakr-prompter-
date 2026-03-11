import { Bars3Icon, XMarkIcon } from '@heroicons/react/24/outline';

const GlassHeroSection = ({ title, subtitle, callToAction, backgroundImage }) => {
  return (
    <section className="relative min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 flex items-center justify-center">
      <div className="absolute inset-0 bg-white/10 backdrop-blur-md border border-white/20 rounded-xl shadow-lg p-6">
        <h1 className="text-5xl font-bold text-slate-900">{title}</h1>
        <p className="text-xl text-slate-900 opacity-70 mt-4">{subtitle}</p>
        <button className="bg-blue-600 hover:opacity-90 text-white px-6 py-3 rounded-xl font-semibold transition-all">
          {callToAction}
        </button>
      </div>
      <img src={backgroundImage} alt="Hero Background" className="absolute inset-0 object-cover w-full h-full opacity-50" />
    </section>
  );
};

export default GlassHeroSection;
