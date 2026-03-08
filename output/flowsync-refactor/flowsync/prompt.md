# FlowSync — Frontend Prompt

### Frontend Development Prompt for FlowSync

#### Overview:
Create a modern, high-performance SaaS application named FlowSync using an AI UI builder like v0.dev, Lovable, or Bolt. The application should cater to high-performance teams and include dynamic task boards, team collaboration tools, workflow automation, and detailed analytics.

#### Folder Structure:
- `src/pages/`: 
  - Overview.jsx
  - Analytics.jsx
  - Settings.jsx
- `src/components/`:
  - Navbar.jsx
  - StatCard.jsx
  - ActivityFeed.jsx
  - Footer.jsx
  - ChartWidget.jsx
  - DataGrid.jsx

#### Routing and Navigation:
1. **Define Routes** using `react-router-dom` for the following paths: `/`, `/analytics`, `/settings`.
2. **Navbar Component**: 
   - Display navigation options such as "Overview", "Analytics", and "Settings".
3. **StatCard Component**: 
   - Display statistical information with a label.
4. **ActivityFeed Component**:
   - Show recent activities in the task board.
5. **Footer Component**:
   - Display footer content for each page.
6. **ChartWidget Component**:
   - Display chart data for analytics pages.
7. **DataGrid Component**:
   - Display tabular data for detailed analytics.

#### Blueprint as Single Source of Truth (AST):
```json
{
  "pages": [
    {
      "name": "Overview",
      "route": "/",
      "state_contract": {
        "currentQuestion": "number",
        "score": "number",
        "timeLeft": "number"
      },
      "layout": {
        "type": "PageLayout",
        "children": [
          {
            "type": "Navbar",
            "props": [],
            "responsibilities": [
              "display navigation options"
            ]
          },
          {
            "type": "StatCard",
            "props": [
              "value",
              "label"
            ],
            "responsibilities": [
              "display statistical information with label"
            ]
          },
          {
            "type": "ActivityFeed",
            "props": [
              "activities"
            ],
            "responsibilities": [
              "display recent activities"
            ]
          },
          {
            "type": "Footer",
            "props": [],
            "responsibilities": [
              "display footer content"
            ]
          }
        ]
      }
    },
    {
      "name": "Analytics",
      "route": "/analytics",
      "state_contract": {
        "currentQuestion": "number",
        "score": "number",
        "timeLeft": "number"
      },
      "layout": {
        "type": "PageLayout",
        "children": [
          {
            "type": "Navbar",
            "props": [],
            "responsibilities": [
              "display navigation options"
            ]
          },
          {
            "type": "ChartWidget",
            "props": [
              "data"
            ],
            "responsibilities": [
              "display chart data"
            ]
          },
          {
            "type": "DataGrid",
            "props": [
              "rows",
              "columns"
            ],
            "responsibilities": [
              "display tabular data"
            ]
          },
          {
            "type": "Footer",
            "props": [],
            "responsibilities": [
              "display footer content"
            ]
          }
        ]
      }
    },
    {
      "name": "Settings",
      "route": "/settings",
      "state_contract": {
        "currentQuestion": "number",
        "score": "number",
        "timeLeft": "number"
      },
      "layout": {
        "type": "PageLayout",
        "children": [
          {
            "type": "Navbar",
            "props": [],
            "responsibilities": [
              "display navigation options"
            ]
          },
          {
            "type": "Footer",
            "props": [],
            "responsibilities": [
              "display footer content"
            ]
          }
        ]
      }
    }
  ]
}
```

#### Design System Tokens:
- **Palette**: Minimal Editorial (Primary: zinc-900, Secondary: zinc-500, Accent: red-500)
- **Design Tokens**:
  - `max-w-7xl`
  - `px-6`
  - `py-16`
  - `rounded-lg`
  - `bg-zinc-50`

#### Implementation Guidelines:
1. **Navbar Component**: 
   - Implement navigation options for "Overview", "Analytics", and "Settings".
2. **StatCard Component**:
   - Display statistical information with a label.
3. **ActivityFeed Component**:
   - Show recent activities in the task board.
4. **Footer Component**:
   - Display footer content for each page.
5. **ChartWidget Component**:
   - Display chart data for analytics pages.
6. **DataGrid Component**:
   - Display tabular data for detailed analytics.

#### Tailwind CSS Usage:
- Use `max-w-7xl`, `px-6`, `py-16`, `rounded-lg`, and `bg-zinc-50` where applicable to ensure consistent styling across the application.

#### Routing Setup in `src/App.jsx`:
```jsx
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Overview from './pages/Overview';
import Analytics from './pages/Analytics';
import Settings from './pages/Settings';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Overview />} />
        <Route path="/analytics" element={<Analytics />} />
        <Route path="/settings" element={<Settings />} />
      </Routes>
    </Router>
  );
}

export default App;
```

#### Component Implementation:
- Ensure each component is implemented in its respective file under `src/components/` and adheres to the responsibilities defined in the AST.

This prompt ensures a structured, consistent, and modern UI for FlowSync, leveraging Tailwind CSS and React components.