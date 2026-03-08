# ExamForge — Frontend Prompt

Generate the frontend for ExamForge, a SaaS platform designed for students preparing for competitive exams and educators. The product features interactive quizzes, flashcards, timed mock tests, instant feedback, and progress tracking.

### Structural Blueprint Map

1. **Home Page**
   - Route: `/`
   - State Contract: None
   - Layout:
     - Header with navigation links (Navbar)
     - Hero section to introduce the platform
     - Grid of FlashcardComponent for quick engagement
     - FeatureGrid showcasing key features like quizzes, flashcards, and mock tests
     - TestimonialSlider to build trust

2. **Quiz Selection Page**
   - Route: `/quiz-selection`
   - State Contract: None
   - Layout:
     - Header with navigation links (Navbar)
     - Stack of QuizCard components for selecting different quiz categories or subjects
     - Footer

3. **Quiz Player Page**
   - Route: `/quiz-player`
   - State Contract: `currentQuestion`, `score`, and `timeLeft`
   - Layout:
     - Header with navigation links (Navbar)
     - Stack containing QuestionCard to display the current question, OptionButton for selecting answers, Timer component to show time left, ProgressBar for tracking progress, and Footer

4. **Results Page**
   - Route: `/results`
   - State Contract: None
   - Layout:
     - Header with navigation links (Navbar)
     - Stack of QuizCard components to display quiz results and PricingTable for subscription options
     - Footer

5. **Flashcard Study Page**
   - Route: `/flashcard-study`
   - State Contract: None
   - Layout:
     - Header with navigation links (Navbar)
     - Stack containing FlashcardComponent for studying flashcards, NewsletterSignup component to subscribe users
     - Footer

### Design System Tokens
- **Palette**: Primary color zinc-900, secondary color zinc-500, accent red-500
- **Background**: White
- **Text**: Zinc-900
- **Dark Mode**: Off
- **Visual Effect**: None at top-right corner
- **Font**: Inter
- **Container**: `max-w-7xl mx-auto px-6`
- **Section Spacing**: `py-16 md:py-24`
- **Card Style**: `bg-zinc-50 rounded-lg border border-zinc-200 shadow-md p-6`
- **Primary Button**: `bg-zinc-900 hover:opacity-90 text-white px-6 py-3 rounded-lg font-semibold transition-all`

### Tone
The tone should be professional and engaging, suitable for students and educators.

### Stack
Use React functional components with Tailwind CSS. Ensure the design is responsive and mobile-first.