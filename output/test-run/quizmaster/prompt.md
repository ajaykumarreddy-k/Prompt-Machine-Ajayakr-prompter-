# QuizMaster — Frontend Prompt

Create a modern frontend interface for QuizMaster, a SaaS platform tailored for educators and students to engage with quizzes and track performance. The application will be structured according to the provided AST, ensuring a consistent design system and component hierarchy.

### Home Page:
- **Navbar**: Display navigation options (Home, Create Quiz, Browse Quizzes).
- **QuizList**: List available public quizzes.
- **Footer**: Display footer content including copyright information and links to terms of service and privacy policy.

### Quiz Selection Page:
- **Navbar**: Same as the Home page.
- **QuizList**: List available public quizzes for selection.
- **Footer**: Same as the Home page.

### Quiz Player Page:
- **Navbar**: Same as previous pages.
- **ProgressBar**: Display progress bar indicating quiz completion percentage.
- **Timer**: Show formatted time remaining, trigger `onTimeUp` when zero.
- **QuestionCard**: Display current question text and render options list.
- **OptionButton**: Handle option selection with `onClick`.
- **Footer**: Same as previous pages.

### Results Page:
- **Navbar**: Same as previous pages.
- **ScoreSummary**: Display user score.
- **ResultsSummary**: Show detailed results of the quiz.
- **Footer**: Same as previous pages.

### Flashcard Study Page:
- **Navbar**: Same as previous pages.
- **FlashcardComponent**: Display flashcard content with interactive elements.
- **Footer**: Same as previous pages.

### Routing & Navigation:
- Use `react-router-dom` for all navigation. Ensure each page in the AST represents a unique route and does not rely on conditional state like `currentSection` or `currentPage`.

### Design System Tokens (Strict Enforcement):
- Palette: Primary - zinc-900, Secondary - zinc-500, Accent - red-500.
- Text Colors: zinc-900 | Background: white.
- Layout Tokens: max-w-7xl mx-auto px-6 | py-16 md:py-24.
- Interactive Tokens: bg-zinc-900 hover:opacity-90 text-white px-6 py-3 rounded-lg font-semibold transition-all | border border-zinc-300 text-zinc-700 px-6 py-3 rounded-lg hover:bg-zinc-50 transition-all | bg-zinc-50 rounded-lg border border-zinc-200 shadow-md p-6.
- Typography: Inter.

### Component Structure & Reusability:
- Place components in `src/components/` and pages in `src/pages/`.
- Avoid duplicating component names (e.g., use `HeroSection.jsx`, not `LandingHero.jsx` or `PricingHero.jsx`).
- Ensure every blueprint component is generated.
- Use Tailwind utility classes strictly as per the design tokens provided.

### Example Correct Component Structure:
```jsx
// src/components/Navbar.jsx
import React from 'react';
import { Navbar } from '@components';

const Home = () => {
  return (
    <main className="max-w-7xl mx-auto px-6 py-16 md:py-24">
      <Navbar />
      {/* Other components */}
      <Footer />
    </main>
  );
};

export default Home;
```

Ensure all components are generated and follow the provided AST structure.