# Syllabye Developer Guidelines

## Getting the Code
```
git clone https://github.com/CarterCripe/Syllabye.git
```

---

## Directory Structure
```
Syllabye/
├── src/
│   ├── backend/        # Python Flask API
│   │   ├── agents/     # LLM agent and prompt files
│   │   ├── app.py      # Run this to start the server
│   │   ├── routes.py   # API routes
│   │   ├── processor.py# Syllabus processing
│   │   └── requirements.txt
│   └── frontend/       # Chrome extension
│       ├── index.html
│       ├── index.js
│       ├── styles.css
│       └── manifest.json
└── reports/            # Weekly progress reports
```

---

## Setup and Running
Follow the steps in the [User Manual](USER_MANUAL.md). For debug mode:
```
python app.py --debug
```
After changing frontend files, click the refresh icon on the extension at `chrome://extensions`.

---

## Testing
*(Work in Progress)* — Tests will use `pytest`.
```
cd src/backend
pytest
```
Test files go in `src/backend/tests/` named `test_<module>.py`.

---

## Branching
- `main` — stable code only
- `frontend` — active frontend development
- Don't merge your own pull requests

---

## Releases
1. Update the version in `manifest.json`
2. Make sure `.env` is not committed
3. Zip `src/frontend/` to distribute the extension
