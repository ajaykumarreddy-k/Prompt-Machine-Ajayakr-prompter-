import { GlassNavbar } from '@/components';

const GlassProjectsPage = () => {
  return (
    <div className="max-w-7xl mx-auto px-6">
      <GlassNavbar />
      <h1 className="text-3xl font-bold text-slate-900 mb-8">Projects</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className="bg-white/10 backdrop-blur-md border border-white/20 rounded-lg shadow-lg p-6">
          <h3 className="text-xl font-bold text-slate-900 mb-2">Project 1</h3>
          <p className="text-lg text-slate-900">Description of Project 1</p>
        </div>
        <div className="bg-white/10 backdrop-blur-md border border-white/20 rounded-lg shadow-lg p-6">
          <h3 className="text-xl font-bold text-slate-900 mb-2">Project 2</h3>
          <p className="text-lg text-slate-900">Description of Project 2</p>
        </div>
      </div>
    </div>
  );
};

export default GlassProjectsPage;
