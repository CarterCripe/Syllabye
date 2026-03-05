# Week 8: Testing and Continuous Integration

## Team Report (Group 13)

### Goals planned for this week:
- Continue Integration
- Begin prep for final presentation
- Complete syllabus backend intitialization
- Implement automated backend testing

### Team progress and issues:
- **What the team did:**
    - Made major steps forward in frontend/backend integration
    - Delayed final presentation prep in favour of beta testing prep
    - Implemented automated CI testing for frontend and backend
    - Completed backend syllabus initialization
- **What worked:**
    - Syllabi can be easily added and retrieved in whole
- **What team learned:**
    - Initial Gemini integration used too many tokens for the free limit
- **Where the team had trouble and where the team is stuck:**
    - CI testing for frontend had not been discussed in length, and last minute focus on implementing this was required.

### Goals planned for next week:
- Collect feedback from beta test
- Begin prep for final presentation
    - create poster
- Complete question search route
- Complete advanced question answering syllabus route
- Finalize integration

## Contributions of Individual Team Members

### Brennan Duman:
**Goals planned for this week:**
- fix extension view width issue
- figure out method to parse pdfs locally
- Added linting CI test for HTML/JS/CSS

**Team progress and issues:**
- **What team member did:**
    - set min size properties to control extension view window
    - locally imported pdf.js library
    - Created and added logo
    - Added linting CI test for frontend
- **What worked:**
    - setting min size properties prevents viewing window from shrinking
    - downloading only the needed files avoids downloading the entirety of the library
    - Kept logo simple
    - CI yaml file was easy to set up, even with few CI solutions being offered directly by Github that matches our usecase
- **What team member learned:**
    - There's nothing preventing people from downloading open source libraries like pdf.js vs using them over the web... seems obvious, but never thought about it
    - kebab-case is industry standard for CSS & HTML object names
- **Where the team member had trouble and where the team member is stuck:**
    - When adding CSS linting, it caught style issues regarding classes and ids named with camelCase rather than kebab-case, which is industry standard. Need to go through and fix all instances not caught by the linter to maintain consistent style

**Goals planned for next week:**
- Fix style issues around naming conventions
- Create the project poster

### Carter Cripe:
**Goals planned for this week:**
- Create prompts for sub-processing elements of initialization
- Create implimentation plan for secondary complex-question answering system
- Impliment automated testing of backend

**Team progress and issues:**
- **What team member did:**
    - Completed backend syllabus initialization
    - Completed prompts for initialization
    - Helped impliment full backend testing
- **What worked:**
    - I was able to use infrastructure that I spent time earlier in the term creating to greatly speed up the implimentation process
- **What team member learned:**
    - It is really important to consider volume and rate limiting when working with expensive llm apis because if you let context grow too much, the api will be expensive or not work properly
- **Where the team member had trouble and where the team member is stuck:**
    - I encountered rate limiting issues with exessive llm requests needed for original process, and I consolidated the processing to use fewer llm calls

**Goals planned for next week:**
- Impliment complex question answering route
- Implimnent search query route
- Add user input constraints

### Justin Primc:
**Goals planned for this week:**
- Add CI automated tests using the Actions section in GitHub
- Complete integration between the frontend and backend sections that allows users to query the application
- Start initial application testing with user syllabi

**Team progress and issues:**
- **What team member did:** Added basic outline and multiple tests that are run through Actions in GitHub. Created a /tests folder within the backend, which tests each corresponding .py file (test_processor.py). Completed basic integration between backend and frontend layers.
- **What worked:** Communicating plans between group members and using online resources to research problem solutions (API key issues).
- **What team member learned:** I learned how to get an API key and what they allow you to do.
- **Where the team member had trouble and where the team member is stuck:** I got stuck figuring out how to use an API key for the initial testing of the application. Also having issues with the LLM and processing the syllabus data.

**Goals planned for next week:**
- Fully fix issues with API elements
- Configure LLM to collect all information needed from the user's syllabus
