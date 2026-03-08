# Syllabye User Manual

## What is Syllabye?
Syllabye is a browser extension that lets students upload their course syllabi and quickly look up information like late work policies and grading breakdowns, all in one place, instead of digging through Canvas.

---

## What You Need
- Google Chrome (version 88 or later)
- Python 3.11 or later
- A free Gemini API key (Instructions below)
> **Note:** This guide was written and tested on **Windows 11 using PowerShell**. If you are on Mac or Linux, and the commands don't work, try the same command except use forward slashes `/` in paths instead of backslashes `\`, and use your Terminal app instead of PowerShell.


---

## Setup

### 1. Check if Python is Already Installed/Install Python
Before downloading Python, check if you already have it installed. Open PowerShell and run:
**Windows:**
```
python --version
```
**Mac/Linux:**
```
python3 --version
```

- If you see something like `Python 3.11.x`, then you already have it. (3.11 and higher works)
- If you don't see that or it is a lower version, you will need to update/install.
    - Go to https://www.python.org/downloads/release/python-3143/ and scroll down to the bottom of the page to the **Files** section, not the install manager, but in the version column select the appropriate download for your machine. (e.g `Windows installer (64-bit)`)
    - **Before clicking Install**, make sure to check the "Add Python to PATH" at the bottom of the first screen.
    - After installing, verify it worked: (You should see `Python 3.14.3`)
**Windows:**
```
python --version
```
**Mac/Linux:**
```
python3 --version
```

### 2. Get Free Gemini API Key
Syllabye uses Google's Gemini AI to read and summarize syllabi.
- Go to the Gemini AI studio: https://aistudio.google.com
- Sign in with your Google account if not already
- Click the "Get API Key" in the left sidebar near the bottom
- Click "Create API Key"
    - If prompted to select a project, just leave it on "Default Gemini Project"
    - You can either leave the name the default or name it what you want (does not affect the key)
- Google will create your key, which should start with "AIza..."
> **Note:** Do NOT share this API key

### 3. Download the Project to your Local Machine
- Go to https://github.com/CarterCripe/Syllabye, click **Code → Download ZIP**, and extract it to wherever you want

### 4. Install backend dependencies
- Open PowerShell. Navigate to the backend folder inside the project:
- Replace `path/to` with the path of the extracted file
**Windows:**
```
cd path\to\Syllabye\src\backend
pip install -r requirements.txt
```
**Mac/Linux:**
```
cd path/to/Syllabye/src/backend
pip3 install -r requirements.txt
```
- Wait for the list of packages to finish downloading

### 5. Create Your API Key File
- While still inside `src/backend/`, you need to create a .env file that contains your API key
**Windows (Powershell):**
```
New-Item -Name ".env" -ItemType "file" -Value "GEMINI_API_KEY=your_key_here"
```
**Mac/Linux (Terminal):**
```
touch .env
echo "GEMINI_API_KEY=your_key_here" > .env
```

- Replace `your_key_here` with your Gemini API key from Step 2
- Verify key is correctly saved:
```
cat .env
```
- You should see your key printed back.
> **Note:** The .env file is intentionally not included in the repository in order to keep API key security.

### 6. Load the Extension in Chrome
- Go to `chrome://extensions`
- Turn on **Developer mode** using the toggle button in the top right
- Click **Load unpacked** and select the root folder (`Syllabye`). Wait until Syllabye appears in your extensions list; this may take several seconds.

---

## Running the App
Start the backend before using the extension:
**Windows:**
```
cd path\to\Syllabye\src\backend
python app.py
```
**Mac/Linux:**
```
cd path/to/Syllabye/src/backend
python3 app.py
```

> **Note:** At this stage, Windows Defender/Firewall might show a pop-up asking if the program should be allowed access to internal and local networks. Click `Allow`.

- Leave this PowerShell window open the entire time while using Syllabye
- Stop it with `Ctrl+C` when done.
---

## Using Syllabye

**Add Syllabus** — Go to Canvas and select any of your current courses and download a syllabus as a `.pdf` or `.txt` file, then from the home screen click `Add Syllabus`, enter a course name (e.g `CS 362`). Then click the file selector and choose your downloaded syllabus, and finally click `Add Syllabus` at the bottom of the page.

**See Syllabus** — Select the `See Syllabus` button from the home screen after adding a syllabus, from there, pick a course from the dropdown to view its full text.

**Quick Info** — Pick a course and a topic (e.g. Late Policy, Grading Scale) to see that specific sections summarized information.

**Search** — Type a question about one of your courses in the search bar and click Search. Make sure to mention which course the question is for by including its given course name. 

---
## Troubleshooting

**"Error! Could not reach backend."**
The backend is not running. Open a terminal, navigate to `src/backend/`, and run `python app.py` (or `python3 app.py` on Mac/Linux).

**"ENV NOT FOUND: PROGRAM SHUTTING DOWN"**
The `.env` file is missing or in the wrong folder. Make sure it is inside `src/backend/` and contains your API key. Redo Step 5.

**`python` is not recognized**
Python is not installed or was not added to PATH. Redo Step 1 and make sure you check "Add Python to PATH" during installation. On Mac/Linux try `python3` instead of `python`.

**`pip` is not recognized**
Same cause as above. On Mac/Linux try `pip3` instead of `pip`.

**Quick Info shows "Not specified." for everything**
Your Gemini API key is invalid or the backend hit an error. Check the terminal window for error messages. Make sure your `.env` file contains a valid key starting with `AIza`.

---

## Reporting a Bug
Submit bugs at: https://github.com/CarterCripe/Syllabye/issues

Include what you were doing, what you expected, what happened, and any error messages.

---

## Known Limitations
- The backend must be started manually each time
- Only `.pdf` and `.txt` files are supported
- Requires a free Gemini API key