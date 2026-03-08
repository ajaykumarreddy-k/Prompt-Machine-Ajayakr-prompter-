# QuizMaster — Frontend Prompt

Generate the frontend for QuizMaster, a tool designed for students and developers to practice with timed quizzes and flashcards. The application will have five main pages: Home, QuizSelection, QuizPlayer, Results, and FlashcardStudy.

### Structural Blueprint Map

1. **Home**:
   - Route: /
   - State Contract: None
   - Layout: Container > Section (Stack containing Navbar, QuizList, Footer)
   - Components: Navbar, QuizList, Footer

2. **QuizSelection**:
   - Route: /quiz-selection
   - State Contract: None
   - Layout: Container > Section (Stack containing Navbar, QuizList, Footer)
   - Components: Navbar, QuizList, Footer

3. **QuizPlayer**:
   - Route: /quiz-player
   - State Contract: { currentQuestion: number, score: number, timeLeft: number }
   - Layout: Container > Section (Stack containing Navbar, ProgressBar, Timer, QuestionCard, OptionButton, Footer)
   - Components: Navbar, ProgressBar, Timer, QuestionCard, OptionButton, Footer

4. **Results**:
   - Route: /results
   - State Contract: { score: number }
   - Layout: Container > Section (Stack containing Navbar, ScoreSummary, ResultsSummary, Footer)
   - Components: Navbar, ScoreSummary, ResultsSummary, Footer

5. **FlashcardStudy**:
   - Route: /flashcards
   - State Contract: None
   - Layout: Container > Section (Stack containing Navbar, FlashcardComponent, Footer)
   - Components: Navbar, FlashcardComponent, Footer

### Design System Tokens

- Palette: Minimal Editorial — primary zinc-900, secondary zinc-500, accent red-500
- Background: white | Text: zinc-900
- Dark mode: False
- Visual effect: none at top-right
- Font: Inter
- Container: max-w-7xl mx-auto px-6
- Section spacing: py-16 md:py-24
- Card style: bg-zinc-50 rounded-lg border border-zinc-200 shadow-md p-6
- Primary button: bg-zinc-900 hover:opacity-90 text-white px-6 py-3 rounded-lg font-semibold transition-all

### Tone and Stack

- Tone: Professional
- Stack: React functional components + Tailwind CSS only. Responsive, mobile-first.

Ensure that the UI is clean, professional, and user-friendly, with a focus on readability and ease of navigation.