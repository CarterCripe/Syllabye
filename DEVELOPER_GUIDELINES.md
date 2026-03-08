# Syllabye Developer Guidelines

## Getting the Code
```
git clone https://github.com/CarterCripe/Syllabye.git
```

---

## Directory Structure
```
syllabye/
├── .github/workflows/       # CI configuration through github actions
│   ├── frontend.yml         # CI using Lint, used to test frontned logic (html, css, js)
|   └── python.yml           # CI using python-application, used to test backend python files
├── libs/                    # Bundled PDF.js library
├── src/                     
│   ├── backend/             # Python Flask API
│   │   ├── agents/          # LLM agent and prompts
│   │   ├── tests/           # Pytest test suite
│   │   ├── testing/         # Sample syllabi
│   │   ├── app.py
│   │   ├── routes.py
│   │   ├── processor.py
│   │   └── requirements.txt
│   └── frontend/            # Chrome extension/UI code
│       ├── index.html
│       ├── index.js
│       └── styles.css
├── manifest.json            # Chrome extension manifest
└──  reports/                # Weekly progress reports
```

---

## Setup and Running
Follow the steps in the [User Manual](USER_MANUAL.md) to install python, get an API ket, install dependicies, and create your .env file.
For debug mode run:
**Windows:**
```
cd src\backend
python app.py --debug
```
**Mac/Linux:**
```
cd src/backend
python3 app.py --debug
```
After changing frontend files, click the refresh icon on the extension at `chrome://extensions`.

---

## Running Tests

**Windows:**
```
cd src\backend
pip install pytest
pytest tests/ -v
```

**Mac/Linux:**
```
cd src/backend
pip3 install pytest
pytest tests/ -v
```

All tests run without a real API key — LLM calls are mocked. New test files go in `src/backend/tests/` and must be named `test_<module>.py`.

---

## Branching
- `main` — stable code only
- `backend` - active backend development
- `frontend` — active frontend development
- Don't merge your own pull requests

---

## CI/CD
Two GitHub Actions workflows run on every push and pull request to `main`:
- `frontend.yml` — runs HTMLHint, Stylelint, and ESLint on the frontend files
- `python-app.yml` — installs dependencies and runs `pytest tests/ -v`

Both must pass before merging to `main`.

---

## Releases
1. Update the version in `manifest.json`
2. Make sure `.env` is not committed and in the `.gitignore`
3. Zip `src/frontend/` to distribute the extension
