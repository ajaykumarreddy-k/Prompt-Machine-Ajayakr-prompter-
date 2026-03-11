import Navbar from './Navbar';

const PageLayout = ({ children }) => {
  return (
    <div className="min-h-screen bg-slate-950 text-slate-200 font-sans selection:bg-cyan-500/30">
      <Navbar />
      <main className="max-w-7xl mx-auto px-6 py-8 md:py-12">
        {children}
      </main>
      <footer className="max-w-7xl mx-auto px-6 py-8 border-t border-slate-800 text-center text-sm text-slate-500">
        © 2026 LedgAI — AI-Powered Financial Excellence
      </footer>
    </div>
  );
};

export default PageLayout;
