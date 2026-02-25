# Syllabye User Manual

## What is Syllabye?
Syllabye is a browser extension that lets students upload their course syllabi and quickly look up information like late work policies and grading breakdowns, all in one place instead of digging through Canvas.

---

## What You Need
- Google Chrome (version 88 or later)
- Python 3.10 or later — https://www.python.org/downloads/

---

## Setup

**1. Download the project**
Go to https://github.com/CarterCripe/Syllabye, click **Code → Download ZIP**, and extract it.

**2. Install backend dependencies**
```
cd path/to/Syllabye/src/backend
pip install -r requirements.txt
```
**3. Load the extension**
1. Go to `chrome://extensions`
2. Turn on **Developer mode**
3. Click **Load unpacked** and select the root folder (`Syllabye`). Wait until Syllabye appears in your extensions list; this may take several seconds.

---

## Running the App
Start the backend before using the extension:
```
cd path/to/Syllabye/src/backend
python app.py
```
Stop it with `Ctrl+C` when done.

---

## Using Syllabye

**Add Syllabus** — Enter a course name, select a `.pdf` or `.txt` file, and click Add Syllabus.

**See Syllabus** — Pick a course from the dropdown to view its full text.

**Quick Info** — Pick a course and a topic to see that specific section.

**Search** — Not yet available.

---

## Reporting a Bug
Submit bugs at: https://github.com/CarterCripe/Syllabye/issues

Include what you were doing, what you expected, what happened, and any error messages.

---

## Known Limitations
- Search is not yet functional
- The backend must be started manually each time
- Only `.pdf` and `.txt` files are supported
