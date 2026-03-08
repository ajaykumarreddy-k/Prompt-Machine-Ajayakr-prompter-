import json
import urllib.request
import os

MODEL = "qwen2.5"
URL = "http://localhost:11434/api/generate"

PRD = """# QuizMaster PRD

## Product Overview
QuizMaster is a platform for creating and taking interactive quizzes. It targets educators and students.

## Key Features
- Create custom quizzes with multiple choice questions.
- Real-time leaderboard for students.
- Dashboard for educators to track performance.
- Search and browse public quizzes.

## Style & Tone
Clean, educational, trust-inspiring. Use a soft blue and neutral palette.

## Technical Requirements
- Use React with Tailwind CSS.
- Responsive design for mobile and desktop.
- Single Page Application with routing.
"""

payload = {
    "model": MODEL,
    "prompt": f"Analyze this PRD and extract structured information.\n\nPRD:\n{PRD}\n\nReturn ONLY valid JSON.",
    "stream": False
}

data = json.dumps(payload).encode()
req = urllib.request.Request(URL, data=data, headers={"Content-Type": "application/json"}, method="POST")

print("Sending request to Ollama...")
try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        print("Response received!")
        print(resp.read().decode())
except Exception as e:
    print(f"Error: {e}")
