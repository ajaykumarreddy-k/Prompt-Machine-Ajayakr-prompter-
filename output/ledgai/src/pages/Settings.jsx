import PageLayout from '../components/PageLayout';

const Settings = () => (
  <PageLayout>
    <div className="max-w-2xl bg-slate-900 rounded-2xl border border-slate-800 shadow-lg p-8">
      <h2 className="text-3xl font-bold text-white mb-8">Settings</h2>
      <div className="space-y-6">
        <div>
          <label className="block text-sm font-medium text-slate-400 mb-2">Company Name</label>
          <input 
            type="text" 
            placeholder="LedgAI Inc." 
            className="w-full px-4 py-3 rounded-2xl border border-slate-800 bg-slate-950 text-slate-200 focus:outline-none focus:ring-2 focus:ring-violet-500 transition-all"
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-400 mb-2">AI Notification Level</label>
          <select className="w-full px-4 py-3 rounded-2xl border border-slate-800 bg-slate-950 text-slate-200 focus:outline-none focus:ring-2 focus:ring-violet-500 transition-all">
            <option>High (All Insights)</option>
            <option>Medium (Key Insights)</option>
            <option>Low (Critical Only)</option>
          </select>
        </div>
        <button className="w-full bg-violet-500 hover:bg-violet-600 text-white px-6 py-3 rounded-2xl font-semibold transition-all shadow-lg shadow-violet-500/20">
          Save Settings
        </button>
      </div>
    </div>
  </PageLayout>
);

export default Settings;
