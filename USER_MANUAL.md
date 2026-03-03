# Syllabye User Manual

## What is Syllabye?
Syllabye is a browser extension that lets students upload their course syllabi and quickly look up information like late work policies and grading breakdowns, all in one place, instead of digging through Canvas.

---

## What You Need
- Google Chrome (version 88 or later)
- Python 3.11 or later
- An Anthropic Key
> **Note:** This guide was written and tested on **Windows 11 using PowerShell**. If you are on Mac or Linux, and the commands don't work, try the same command except use forward slashes `/` in paths instead of backslashes `\`, and use your Terminal app instead of PowerShell.


---

## Setup

### 1. Check if Python is Already Installed/Install Python
Before downloading Python, check if you already have it installed. Open PowerShell and run:
```
python --version
```
- If you see something like `Python 3.11.x`, then you already have it. (3.11 and higher works)
- If you don't see that or it is a lower version, you will need to update/install.
    - Go to https://www.python.org/downloads/release/python-3143/ and scroll down to the bottom of the page to the **Files** section, not the install manager, but in the version column select the appropriate download for your machine. (e.g `Windows installer (64-bit)`)
    - **Before clicking Install**, make sure to check the "Add Python to PATH" at the bottom of the first screen.
    - After installing, verify it worked: (You should see `Python 3.14.3`)
```
python --version
```

### 2. Get Free Gemini API Key
Syllabye uses Google's Gemini AI to read and summarize syllabi.
- Go to the Gemini AI studio: https://aistudio.google.com
- Sign in with your Google account if not already
- Click the "Get API Key" in the left sidebar near the bottom
- Click "Create API Key"
    - If prompted to select a project, just leave it on "Default Gemini Project"
    - You can either leave the name the default or name it what you want (does not affect the key)
- Google will create your key, which should start with "Alza..."
> **Note:** Do NOT share this API key

### 3. Download the Project to your Local Machine
- Go to https://github.com/CarterCripe/Syllabye, click **Code → Download ZIP**, and extract it to wherever you want

### 4. Install backend dependencies
- Open PowerShell. Navigate to the backend folder inside the project:
- Replace `path/to` with the path of the extracted file
```
cd path/to/Syllabye/src/backend
```
- Then, while inside backend, install the required packages:
```
pip install -r requirements.txt
```
- Wait for the list of packages to finish downloading

### 5. Create Your API Key File
- While still inside `src/backend/` in PowerShell, run:
```
New-Item -Name ".env" -ItemType "file" -Value "GEMINI_API_KEY=your_key_here"
```
- Replace `your_key_here` with your Gemini API key from Step 3
- Verify key is correctly saved:
```
cat .env
```
- You should see your key printed back.
> **Note:** The .env file is intentionally not included in the repository in order to keep API key security.

### 6. Load the Extension in Chrome
- Go to `chrome://extensions`
- Turn on **Developer mode**
- Click **Load unpacked** and select the root folder (`Syllabye`). Wait until Syllabye appears in your extensions list; this may take several seconds.

---

## Running the App
Start the backend before using the extension:
```
cd path/to/Syllabye/src/backend
python app.py
```
- Leave this PowerShell window open the entire time while using Syllabye
- Stop it with `Ctrl+C` when done.
---

## Using Syllabye

**Add Syllabus** — Go to Canvas and select any of your current courses and download a syllabus as a `.pdf` or `.txt` file, then from the home screen click `Add Syllabus`, enter a course name (e.g `CS 362`). Then click the file selector and choose your downloaded syllabus, and finally click `Add Syllabus` at the bottom of the page.

**See Syllabus** — Select the `See Syllabus` button from the home screen after adding a syllabus, from there, pick a course from the dropdown to view its full text.

**Quick Info** — Pick a course and a topic to see that specific section. Buttons do have some basic functions that work but information is not yet correctly processed. All information will show the default `Not specified.` message.

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
- API to LLM connection with processing data fully 
