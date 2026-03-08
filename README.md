# Syllabye: (Group 13)
Say goodbye to syllabi

## Team Info:
- **Carter Cripe** – Team Lead / Visionary / Full Stack Developer
- **Justin Primc** – Full Stack Developer
- **Brennan Duman** – Full Stack Developer

## Project Description
Syllabye is a browser extension that helps students easily access and search their course syllabi. Students can upload all their syllabi to the extension and quickly search across them to find specific information like late work policies, grading breakdowns, or citation guidelines without navigating through Canvas or hunting through downloaded files.

## Guidelines/Documentation
- [User Manual](USER_MANUAL.md) - Setup and usage instructions for users
- [Developer Guidelines](DEVELOPER_GUIDELINES.md) - Instructions for contributors and developers
- [Team Document](Syllabye.md) - Team documentation with information corresponding to project milestones

## Repository Layout
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
├── reports/                 # Weekly progress reports
├── USER_MANUAL.md           # Guideline for user to run application themselves
├── DEVELOPER_GUIDELINE.md   # Guideline for any developer that wants to add to code 
├── Syllabye.md              # Team working document
└── README.md                # This file
```

## Operational Use Cases
- **Add Syllabus** - Upload a `.pdf` or `.txt` syllabus, processed by Google Gemini AI
- **See Syllabus** - View full raw text of any uploaded syllabus
- **Quick Info** - Look up specific topics found in most syllabi (Late policy, Grading Scale, etc.)
- **Search** - Ask a question into the search bar about any of your added courses

**Course**: CS 362 - Software Engineering II (Winter 2026)
