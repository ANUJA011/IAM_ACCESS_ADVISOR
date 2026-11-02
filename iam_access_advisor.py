import tkinter as tk
from google import genai
from google.genai import types

API_KEY = "GEMINI_API_KEY"
client = genai.Client(api_key=API_KEY)

config = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(thinking_budget=0),
    max_output_tokens=300,
    temperature=0.2,
)

# 9 common access requests + "Other..." = 10 options
USE_CASES = [
    "New joiner needs standard access for their department",
    "Developer requests production database admin access",
    "Contractor needs VPN access for 3 months",
    "Employee requests access to a shared finance folder",
    "Mover changing teams wants to keep old access",
    "Leaver's account still active after last working day",
    "User requests local admin rights on their laptop",
    "Intern requests access to customer PII data",
    "Manager requests temporary access to approve payroll",
    "Other...",
]

def explain_request(request_text):
    prompt = f"""
You are an IAM reviewer. Reply briefly in this exact format:

Risk level: Low / Medium / High
Recommendation: Approve / Deny / Needs more info
Reason: (2 short sentences)
Questions to ask: (1 question)

Access request: {request_text}
"""
    output.delete("1.0", tk.END)
    for chunk in client.models.generate_content_stream(
        model="gemini-3.8-flash", contents=prompt, config=config
    ):
        output.insert(tk.END, chunk.text or "")
        window.update()          # show text as it arrives

def on_select(choice):
    # Show the typing box only when "Other..." is picked
    if choice == "Other...":
        other_box.pack(after=dropdown, fill="x", padx=10, pady=5)
    else:
        other_box.pack_forget()

def on_explain():
    choice = selected.get()
    text = other_box.get().strip() if choice == "Other..." else choice
    if text:
        explain_request(text)

# ---- Window ----
window = tk.Tk()
window.title("Access Request Explainer")
window.geometry("560x420")

tk.Label(window, text="Choose an access request:").pack(anchor="w", padx=10, pady=(10, 0))

selected = tk.StringVar(value=USE_CASES[0])
dropdown = tk.OptionMenu(window, selected, *USE_CASES, command=on_select)
dropdown.pack(fill="x", padx=10, pady=5)

other_box = tk.Entry(window)   # hidden until "Other..." is picked

tk.Button(window, text="Explain", command=on_explain).pack(pady=5)

output = tk.Text(window, wrap="word", height=14)
output.pack(fill="both", expand=True, padx=10, pady=10)

window.mainloop()
