const ChartWidget = ({ data }) => (
  <div className="bg-slate-900 rounded-2xl border border-slate-800 shadow-lg p-8 w-full min-h-[300px] flex flex-col items-center justify-center">
    <div className="w-16 h-16 rounded-full bg-cyan-500/10 flex items-center justify-center mb-4">
      <div className="w-8 h-8 text-cyan-400">📊</div>
    </div>
    <h3 className="text-xl font-bold text-white mb-2">Revenue Insights</h3>
    <p className="text-slate-400 text-center max-w-xs">AI is analyzing your transaction patterns to generate growth forecasts.</p>
    <div className="mt-6 flex space-x-2">
      {[40, 70, 45, 90, 65].map((h, i) => (
        <div key={i} className="w-8 bg-violet-500/20 rounded-t-lg relative group">
          <div 
            className="absolute bottom-0 left-0 right-0 bg-violet-500 transition-all group-hover:bg-cyan-400" 
            style={{ height: `${h}%` }}
          ></div>
        </div>
      ))}
    </div>
  </div>
);

export default ChartWidget;
