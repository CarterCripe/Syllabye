# Installing Syllabye

Follow the instructions laid out in USER\_MANUAL.md.

This guide may be updated in the future to point to a page on the Chrome WebStore.

The TL;DR of USER\_MANUAL.md

Prerequisites: Have Python (v3.11 or higher) and Google Chrome (v88 or higher) installed, and get a free Gemini API key ([https://aistudio.google.com](https://aistudio.google.com)) 

Warning: The following instructions are a brief form of USER\_MANUAL.md. Please follow the more detailed instructions in USER\_MANUAL.md.

1. Download repo as a .zip file  
2. Extract .zip file to folder (referred to from now on as `syllabye`)  
3. In a terminal/command line window, navigate to `syllabye/src/backend` (or `syllabye\src\backend` on Windows)  
4. Use pip to install the packages in requirements.txt (`pip \-r requirements.txt`)  
5. In Google Chrome, open chrome://extensions. Enable developer mode.  
6. Select “Load unpacked”, and in the file dialog window select `syllabye/`.  
7. In `syllabye/src/backend`, create a file titled `.env`, and insert your Gemini key into it.  
8. In the terminal/command line window (still in `syllabye/src/backend`), type `python app.py`  
9. Click the Syllabye icon (a multi-coloured magnifying glass) in the Chrome extension menu, and have fun!

