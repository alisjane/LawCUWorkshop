# Thai Legal Age Checker

A simple Flask web app that checks whether a person is of legal age under Thai law.

## Rules used
- A person aged 20 or older is considered of legal age.
- A person under 20 may still be treated as an adult if they are married or divorced.

## Run locally

```bash
python3 -m pip install -r requirements.txt
python3 webapp.py
```

Then open http://127.0.0.1:5000 in your browser.
