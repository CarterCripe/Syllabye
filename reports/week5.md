# Week 5: Architecture and Design

## Team Report (Group 13)

### Goals planned for this week:
- Create a rough page layout for the frontend UI, using Google Drawings
- Complete the steps of Milestone 3, improving the risk assessment, project schedule, coding guideline, and basic architecture outline of the software.
- Create a full function layout of backend, including the project filestructure and API routes

### Team progress and issues:
- **What the team did:** Completed the rough layout of the frontend UI using Google Drawings. Got the working document caught up to the requirements given in Milestone 3. Also completed the function layout, project filestructure, API routes (goal 3). Beyond that, we also implimented an Agentic AI factory structure in order to facilitate the data processing, and created a temporary webpage in order to test the API connection.
- **What worked:** We decided to switch from using the React Interface for the frontend UI to using a basic system of HTML, CSS, and JavaScript, which we are more familiar with. We also were able to make a huge amount of progress on the backend due to familiarity with the structure and processes involved.
- **What team learned:** Gained an understanding of the Chrome extension architecture and how the complexity of React would only make this project harder, so the simple use of HTML and CSS would accomplish the same task.
- **Where the team had trouble and where the team is stuck:** The team chose to pivot from React to HTML and CSS. The team is also still working on finalizing the complete structure of the working living document. We also need to decide on a specific JSON format for the processed data in order to begin working on both the data processing and also the frontend implimentation.

### Goals planned for next week:
- Implement the rough draft frontend layout, using HTML & CSS
- Create a comprehensive API documentation in order to fully understand Frontend -> API interface
- Determine a specific JSON format for the processed data
- Impliment the backend processing method for the Syllabus initialization 

## Contributions of Individual Team Members

### Brennan Duman:
**Goals planned for this week:**
- Learn React Basics
- Create frontend concept UI in Google Drawings

**Team progress and issues:**
- **What team member did:**
    - Led discussion regarding the switch from React to a more classic HTML implementation for the frontend
    - Drafted frontend layout, UI, colour scheme and flow in Google Drawings
    - Worked on expanding statements in Week 4's report, due to feedback that it wasn't detailed or specific enough.
- **What worked:**
    - Created colour theming for the primary interface options that carry through the layout, allowing a user to immediately know their location in the system.
- **What team member learned:**
    - While developing extensions is very similar to developing webpages, Chromium does impose some restrictions (especially with manifest v3, which affects user data storage and transmission). This can cause issues with React, prompting the discussion to change the frontend framework to classic HTML/CSS/JavaScript.
    - Since React is a JavaScript framework, a theoretical implementation would interact with the backend the same way a HTML/JS implementation would, meaning already created testing files and practices can be maintained.
- **Where the team member had trouble and where the team member is stuck:**
    - During research into learning React, discovered issue with React and manifest v3 that would introduce additional difficulty into development. This was resolved through team discussion and frontend framework change.
    - Week 4's report was subpar. Considerable time this week was dedicated to increasing granularity and increasing the level of detail.

**Goals planned for next week:**
- Implement the drafted frontend in Google Drawings using HTML5/CSS/JavaScript.
- Potentially begin API testing & integration with backend.

### Carter Cripe:
**Goals planned for this week:**
Create a function layout of the project backend containing input / output structure, as well as data processing plan

**Team progress and issues:**
- **What team member did:**
    - I created the project filestructure for the frontend and backend, containing the files that we would need to   begin work on the implimentation.
    - I created a Flask API routes page with several basic routes including /health, /process, /syllabus, and /complex-question, and I added basic testing functionality for each (returning a placeholder value)
    - I created a comprehensive LLM Agent factory class that when called, created a agent object of a specified model and system prompt, and said agent can then be given user prompts and context in order for data processing.
- **What worked:**
    - I am familiar with much of the backend software that we will need for this project, and so I was able to quickly impliment much of the framework  
- **What team member learned:**
    - I learned a lot about Flask APIs and how to better make a coherent functional frontend/backend system that works smoothly 
- **Where the team member had trouble and where the team member is stuck:**
    - I had trouble coming up with a concrete plan for the data processing. What exactly should the API return in order to give the frontend the most useful data? What syllabus categories should be implimented in the initialization?

**Goals planned for next week:**
- Create comprehensive API documentation in order to give the frontend designers a clear idea of how to integrate the frontend with the backend API
- Determine a processing plan for the data to maximise utility
- Impliment a basic version of the syllabus initialization containing core features in order to allow the frontend to use it for testing

### Justin Primc:
**Goals planned for this week:** Complete pieces of Milestone 3, risk assessment, and architectural assumptions.

**Team progress and issues:**
- **What team member did:** Completed the risk assessment section of Milestone 3, updated the living document and reports to reflect the shift from using the React interface to using basic HTML and CSS for the frontend. Reviewed Google Drawings UI layout created by Brennan.
- **What worked:** Following the structured approach to complete Milestone 3 and switching to an already understood language and interface of HTML and CSS.
- **What team member learned:** I gained a deeper understanding of the earlier level design process in applications/software.
- **Where the team member had trouble and where the team member is stuck:** Ensuring that the risk assessment section covers all of the potential issues in the framework.

**Goals planned for next week:**
- Implement rough draft of the UI using HTML and CSS
- Continue refining the living document based on previous milestones and any instructor feedback.
