# Week 7: Project Implementation and Documentation

## Team Report (Group 13)

### Goals planned for this week:
- Complete implementation and documentation requirements of milestone 4 (USER/DEVELOPER) guidelines
- Finish backend syllabus initialization
- Complete system that saves user syllabi information locally

### Team progress and issues:
- **What the team did:**
- **What worked:**
- **What team learned:**
- **Where the team had trouble and where the team is stuck:**

### Goals planned for next week:
- 

## Contributions of Individual Team Members

### Brennan Duman:
**Goals planned for this week:**
- Finish frontend implementation
- Do UI testing

**Team progress and issues:**
- **What team member did:**
    - Completed UI & pdf conversion implementation.
    - Did first test of UI in extension environment.
- **What worked:**
    - UI navigation
    - Users can add a .txt or .pdf file
- **What team member learned:**
    - file types can be determined via metadata (aka MIME type) as well as file extension
        - the MIME type for .pdf files is "application/pdf", while .txt is "text/plain"
    - The extension developer panel in Chrome has an error panel that reports errors
- **Where the team member had trouble and where the team member is stuck:**
    - Class was introduced to GitHub workflows last week, but does not have any suggested workflows for HTML/CSS. More research is needed to leverage this tool
    - When opened as an extension, the viewable window is extremly narrow
    - Due to the same reasons we couldn't use React.js, Chrome won't allow the PDF.js library used for pdf parsing to be accessed. This portion must be redeveloped to do this locally.

**Goals planned for next week:**
- Fix extension view width issue
- Figure out method to parse PDFs locally

### Carter Cripe:
**Goals planned for this week:**

**Team progress and issues:**
- **What team member did:**
- **What worked:**
- **What team member learned:**
- **Where the team member had trouble and where the team member is stuck:** 

**Goals planned for next week:**
- 

### Justin Primc:
**Goals planned for this week:**
- Complete information documents: USER/DEVELOPER GUIDELINES
- Solve local data storage issue

**Team progress and issues:**
- **What team member did:** Completed both md files for the user and developer guidelines. Edited the index.js file to include a save locally feature for users' syllabi data. Added necessary files (milestone.json) for implementation into a Chrome extension.
- **What worked:** Using outside tools when needed (Google Chrome extension developer guides)
- **What team member learned:** I learned how to start creating a Chrome extension and the specific files and permissions you need to implement these.
- **Where the team member had trouble and where the team member is stuck:** I initially had trouble figuring out what was needed to save user data locally. I later learned how this works when using a Chrome extension through the Chrome provided guidelines.

**Goals planned for next week:**
- Add CI automated tests
- Fix any new issues found through the testing process in the frontend section
- 
