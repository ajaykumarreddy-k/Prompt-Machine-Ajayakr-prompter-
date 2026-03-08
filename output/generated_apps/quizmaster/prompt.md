# QuizMaster — Frontend Prompt

### Prompt for AI UI Builder:

Generate a modern SaaS interface for QuizMaster, a tool designed for students and developers to create and take quizzes.

#### Section Order:
1. **Navbar**
2. **Hero**
3. **Features**
4. **Footer**

#### Components:
- Navbar
- Hero
- Cards (for features)
- Footer

#### Visual Hierarchy:
- Primary focus: Hero section
- Secondary: Navbar, Features
- Call-to-action button label: "Get Started Now"
- Focal point: Hero section headline and CTA button

#### Design System:
- **Palette**: Minimal Editorial — primary zinc-900, secondary zinc-500, accent red-500
- **Background**: white | Text: zinc-900
- **Dark mode**: False
- **Visual effect**: none at top-right
- **Hero animation**: typewriter
- **Container**: max-w-7xl mx-auto px-6
- **Section spacing**: py-16 md:py-24
- **Card style**: bg-zinc-50 rounded-lg border border-zinc-200 shadow-md p-6
- **Primary button**: bg-zinc-900 hover:opacity-90 text-white px-6 py-3 rounded-lg font-semibold transition-all

#### Tone:
Professional and user-friendly.

#### Stack:
React functional components + Tailwind CSS only. Responsive, mobile-first.

---

#### Navbar:
- Create a flex container with `justify-between` and `items-center`.
- Add the QuizMaster logo on the left.
- Place navigation links on the right using `text-zinc-900`.

#### Hero Section:
- Use a full-width container with `max-w-screen-lg mx-auto px-6 py-16 md:py-24`.
- Apply typewriter animation to the headline text.
- Place "Get Started Now" CTA button at the bottom of the section using `bg-zinc-900 hover:opacity-90 text-white px-6 py-3 rounded-lg font-semibold transition-all`.

#### Features Section:
- Organize features into 2 columns on larger screens and stack them vertically on smaller screens.
- Use cards for each feature with the following classes: `bg-zinc-50 rounded-lg border border-zinc-200 shadow-md p-6 py-16 md:py-24`.

#### Footer:
- Create a simple layout using `flex` and `justify-center`.
- Include links to social media or additional resources.

Ensure the design is responsive, with mobile-first approach and appropriate use of Tailwind CSS classes for spacing, padding, and typography.