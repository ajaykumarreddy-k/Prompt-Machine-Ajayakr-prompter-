import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import GlassNavbar from './components/GlassNavbar';
import GlassAboutPage from './pages/GlassAboutPage';
import GlassProjectsPage from './pages/GlassProjectsPage';
import GlassExperiencePage from './pages/GlassExperiencePage';
import GlassSkillsPage from './pages/GlassSkillsPage';
import GlassFeaturesPage from './pages/GlassFeaturesPage';
import GlassPricingPage from './pages/GlassPricingPage';
import GlassContactPage from './pages/GlassContactPage';
import GlassNewsletterSignupPage from './pages/GlassNewsletterSignupPage';

const App = () => {
  return (
    <Router>
      <GlassNavbar />
      <Routes>
        <Route path="/" element={<GlassAboutPage />} />
        <Route path="/about" element={<GlassAboutPage />} />
        <Route path="/projects" element={<GlassProjectsPage />} />
        <Route path="/experience" element={<GlassExperiencePage />} />
        <Route path="/skills" element={<GlassSkillsPage />} />
        <Route path="/features" element={<GlassFeaturesPage />} />
        <Route path="/pricing" element={<GlassPricingPage />} />
        <Route path="/contact" element={<GlassContactPage />} />
        <Route path="/signup" element={<GlassNewsletterSignupPage />} />
      </Routes>
    </Router>
  );
};

export default App;
