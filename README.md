# IAM Access Advisor

An AI assistant that reviews access requests the way an Identity & Access Management (IAM) reviewer would. Pick a common scenario (or type your own) and get a risk level, a recommendation, the reasoning, and follow-up questions in seconds.

Built with Python, Tkinter, and Google's Gemini API.

## Features
- Dropdown of 9 common IAM scenarios (joiner, mover, leaver, privileged access, contractors, sensitive data), plus **Other** for custom requests
- Structured output every time: Risk level, Recommendation, Reason, Questions to ask
- Fast, streaming responses (answers appear as they're generated)
- Works on Mac and Windows (Tkinter ships with Python)
  

## How to run

1. Install Python 3.10+ from [python.org](https://www.python.org/downloads/)
2. Install the Gemini library:
   ```bash
   pip install google-genai
   ```
3. Get a free API key from [Google AI Studio](https://aistudio.google.com/apikey) and set it as an environment variable:
   - **Mac/Linux:** `export GEMINI_API_KEY="your-key-here"`
   - **Windows (Command Prompt):** `setx GEMINI_API_KEY "your-key-here"` (then reopen the window)
4. Run the app:
   ```bash
   python iam_access_advisor.py
   ```

## How it works
1. You choose an access request from the dropdown or type your own.
2. The app sends it to Gemini with a prompt that sets the AI's role as an IAM reviewer and fixes the reply format.
3. Gemini's answer streams back into the window.

## Tech stack
- Python
- Tkinter (desktop UI)
- Google Gemini API (`google-genai`)

## Disclaimer
This is a learning project. AI recommendations should support, not replace, a human access reviewer's decision.

## Author
Anuja Pawar, IAM professional (SailPoint, Saviynt) exploring AI × Identity.
