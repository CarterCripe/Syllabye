# Week 7: Project Implementation and Documentation

## Team Report (Group 13)

### Goals planned for this week:
- Complete implementation and documentation requirements of milestone 4 (USER/DEVELOPER) guidelines
- Finish backend syllabus initialization
- Complete system that saves user syllabi information locally
- Begin frontend/backend integration

### Team progress and issues:
- **What the team did:**
    - Began integration
    - Did first test in browser-extension environment
    - Created workflow tools to streamline backend workflow such as debugging toggles, processing templates, and factory methods
    - Implimented high level syllabus initialization
- **What worked:**
    - Frontend can be succesfully navigated in in extension view
    - Backend is ready for a final sprint to complete functionality
- **What team learned:**
    - Chrome renders "popups" (aka the default addon window) differently than normal webpages, requiring modifications
- **Where the team had trouble and where the team is stuck:**
    - Using GitHub workflows is a required part of the project, but there does not seem to be a match for our stack easily available. Further discussion is required prior to integration testing.

### Goals planned for next week:
- Continue integration
- Begin preperation for final presentation
- Complete syllabus backend initialization
- Impliment automated backend testing

## Contributions of Individual Team Members

### Brennan Duman:
**Goals planned for this week:**
- Finish UI implementation
- Implement .pdf text parsing
- Do UI testing

**Team progress and issues:**
- **What team member did:**
    - Completed UI & pdf conversion implementation.
    - Did first test of UI in extension environment.
- **What worked:**
    - .pdf and .txt files can be parsed into strings that can be further processed into JSON for backend processing
    - UI can succesfully load in extension view, & it is fully navigable
- **What team member learned:**
    - file types can be determined via metadata (aka MIME type) as well as file extension
        - the MIME type for .pdf files is "application/pdf", while .txt is "text/plain"
    - The extension developer panel in Chrome has an error panel that reports errors, and calls out when errors are explicitly raised by Chrome (e.g. manifest v3 preventing remote code execution)
- **Where the team member had trouble and where the team member is stuck:**
    - Class was introduced to GitHub workflows last week, but does not have any suggested workflows for HTML/CSS. More research is needed to leverage this tool
    - When opened as an extension, the viewable window is extremly narrow
    - Due to manifest v3 (the same reason leading to pivot away from react.js), Chrome won't allow the PDF.js library used for pdf parsing to be accessed. This portion must be redeveloped to do this locally.

**Goals planned for next week:**
- Fix extension view width issue
- Figure out method to parse PDFs locally

### Carter Cripe:
**Goals planned for this week:**
 - Finish implimentation the main processing unit for syllabus implimentation
 - Create implimentation plan the secondary complex-question answering system
 - Begin implimentation for automated testing of the backend

**Team progress and issues:**
- **What team member did:**
    - Implimented high level data processing
    - Created prompting format for llm access
    - Created template processed syllabus for use in testing and development
    - Created debug parameter to toggle debugging statements
- **What worked:**
    - Creating tools upfront that will make implimentation faster later in the process, such as the template syllabus and the llm agent factory method 
- **What team member learned:**
    - I learned that it is important to keep track of data types throughout my code, for example using comments and debug print statements
- **Where the team member had trouble and where the team member is stuck:**
    - I had trouble this week in determining the right balence regarding length and detail of prompt. I dont want to make prompts too long, due to processing cost and speed, but also detail is important to make sure you get exactly what you want as a response.
    - Prompt engineering took longer than expected, and also I had trouble finding time to work on project due to other obligations that occupied all my time thursday-sunday (out of state tournament)

**Goals planned for next week:**
- Create prompts for sub-processing elements of initialization
- Create implimentation plan for secondary complex-question answering system
- Further impliment automated testing of backend

### Justin Primc:
**Goals planned for this week:**
- Complete information documents: USER/DEVELOPER GUIDELINES
- Solve local data storage issue (getting user data stored through their interaction of the extension application)
- Begin working on CI style testing using the Actions section of GitHub for the backend

**Team progress and issues:**
- **What team member did:** Completed both md files for the user and developer guidelines. Edited the index.js file to include a save locally feature for users' syllabi data. Added necessary files (milestone.json) for implementation into a Chrome extension.
- **What worked:** Using outside tools when needed (Google Chrome extension developer guides)
- **What team member learned:** I learned how to start creating a Chrome extension and the specific files and permissions you need to implement these.
- **Where the team member had trouble and where the team member is stuck:** I initially had trouble figuring out what was needed to save user data locally. I later learned how this works when using a Chrome extension through the Chrome provided guidelines.

**Goals planned for next week:**
- Add CI automated tests
- Fix any new issues found through the testing process in the frontend section
- Complete automated CI tests using GitHub actions on the backend
