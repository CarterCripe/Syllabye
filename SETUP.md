# Setting up Syllabye’s Development Environment

Syllabye requires Python v3.11+.

To start, simply clone the repository to your local environment.  
Navigate to `src/backend`, and run the following to install the required Python packages:  
```  
pip -r requirements.txt  
```  
If you’re testing using a Gemini API key, insert it into a file called `.env`, perhaps like so:  
```Unix  
touch .env  
echo “GEMINI_API_KEY=your_key_here" > .env  
```  
Where “your_key_here” is replaced with your personal API key.

Everything regarding direct interaction with LLM APIs and processing user data is written in 
Python using the Flask API, and is in `src/backend`. Everything regarding UI and user input is 
in `src/frontend`. Lastly, the library used to parse PDF files into readable text (`pdf.js`) has 
a local version stored in `libs/pdf-js-legacy`. 

# Release Notes: v1.0

Users can now

1. Add syllabi to the extension  
2. Access the raw text of any syllabi they’ve added  
3. Access the presorted “quick info” of any syllabi they’ve added  
4. Enter a custom search request that returns information from the saved syllabi

Primary limitations:

1. Drag-and-drop text is not currently supported.  
2. Only .pdf and .txt files are supported  
3. `app.py` must be running in the background, requiring interaction with a CLI.  
4. Errors regarding script rules are present in the Chrome developer console  
5. There has not been testing on Linux apart from a partial test using Mint where interacting with the file dialog box to add a file caused the extension to lose focus and disappear.
