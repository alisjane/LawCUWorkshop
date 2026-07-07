from flask import Flask, render_template_string, request

from app import is_legal_age

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Thai Legal Age Checker</title>
    <style>
      :root {
        color-scheme: light;
        --bg: #f3efe6;
        --card: #fbf9f2;
        --text: #1f2933;
        --muted: #5c6470;
        --accent: #8b1e3f;
        --accent-dark: #5f142c;
        --accent-soft: #f6e9ee;
        --border: #d8c8b1;
        --bad: #7a1f2d;
        --bad-soft: #f8ebee;
        --cu-gold: #c8a96b;
      }
      body {
        margin: 0;
        min-height: 100vh;
        display: grid;
        place-items: center;
        background: linear-gradient(135deg, #f5efe2 0%, #e7decf 100%);
        font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
        color: var(--text);
      }
      .card {
        width: min(92vw, 480px);
        background: var(--card);
        border: 1px solid var(--border);
        border-radius: 22px;
        padding: 2rem;
        box-shadow: 0 16px 40px rgba(139, 30, 63, 0.12);
      }
      h1 {
        margin: 0 0 0.5rem;
        font-size: 2.05rem;
        letter-spacing: 0.03em;
        color: var(--accent);
        font-family: "Georgia", "Times New Roman", serif;
      }
      p { color: var(--muted); line-height: 1.6; }
      form { display: grid; gap: 0.85rem; margin-top: 1.2rem; }
      label { font-weight: 600; }
      input, select, button {
        width: 100%;
        border-radius: 10px;
        border: 1px solid var(--border);
        padding: 0.8rem 0.95rem;
        font: inherit;
        background: #fffdf8;
        box-sizing: border-box;
      }
      button {
        margin-top: 0.4rem;
        background: linear-gradient(135deg, var(--accent), var(--accent-dark));
        color: white;
        border: none;
        cursor: pointer;
        font-weight: 700;
        letter-spacing: 0.02em;
      }
      .result {
        margin-top: 1rem;
        padding: 1rem;
        border-radius: 12px;
        font-weight: 600;
      }
      .yes { background: var(--accent-soft); color: var(--accent); }
      .no { background: var(--bad-soft); color: var(--bad); }
      .note {
        margin-top: 1rem;
        padding: 0.9rem 1rem;
        border-left: 4px solid var(--accent);
        background: linear-gradient(90deg, #f6e9ee 0%, #faf5ea 100%);
        color: var(--text);
        border-radius: 8px;
        font-size: 0.95rem;
        line-height: 1.7;
      }
    </style>
  </head>
  <body>
    <main class="card">
      <h1>Thai Legal Age Checker</h1>
      <p>Enter the person's age and marital status to check whether they are legally an adult under Thai law.</p>
      <div class="note" style="border-left-color: var(--cu-gold);">
        A formal and university-aligned presentation for legal assessment and civic guidance.
      </div>
      <div class="note">
        Under Thai law, the general age of majority is 20 years old. The relevant rule is found in the Civil and Commercial Code of Thailand, which treats a person as having full legal capacity upon reaching majority. A person under 20 may still be treated as an adult for some legal purposes if they are married or divorced.
      </div>
      <form method="post">
        <label for="age">Age</label>
        <input id="age" name="age" type="number" min="0" max="120" placeholder="e.g. 19" required>
        <label for="marital_status">Marital status</label>
        <select id="marital_status" name="marital_status" required>
          <option value="single">Single</option>
          <option value="married">Married</option>
          <option value="divorced">Divorced</option>
          <option value="widowed">Widowed</option>
        </select>
        <button type="submit">Check</button>
      </form>
      {% if result is not none %}
        <div class="result {{ 'yes' if result else 'no' }}">
          {% if result %}
            This person is of legal age under Thai law.
          {% else %}
            This person is not of legal age under Thai law.
          {% endif %}
        </div>
        {% if result %}
          <div class="note">
            Once a person is legally an adult, they may generally enter into contracts, open bank accounts, apply for certain licenses, make legal decisions, and act for themselves in many civil matters. The exact rights and duties can depend on the specific law or transaction.
          </div>
        {% else %}
          <div class="note">
            If the person is not yet legally an adult, a parent, legal guardian, or other authorized representative may need to act on their behalf for certain legal or financial matters.
          </div>
        {% endif %}
      {% endif %}
    </main>
  </body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        age = request.form.get("age")
        marital_status = request.form.get("marital_status")
        if age:
            result = is_legal_age(int(age), marital_status)
    return render_template_string(HTML, result=result)


if __name__ == "__main__":
    app.run(debug=True)
