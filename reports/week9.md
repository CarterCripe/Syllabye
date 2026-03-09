# Week 9: Project Beta Release

## Team Report (Group 13)

### Goals planned for this week:
- Complete backend, including search route and complex question route
- Create final presentation poster

### Team progress and issues:
- **What the team did:**
    - fixed frontend naming convention inconsistancy
    - recorded feedback from beta test
    - fully integrated frontend & backend, fulfilling all launch use cases
    - updated documentation
- **What worked:**
    - Integration was a success -- users can now add a syllabus, then use the quick info or search options to answer related questions
    - Beta testing was (mostly) successful
- **What team learned:**
    - how to create a poster to the specs given, including affiliation (in this case, OSU / CS 362)
    - Fixing bugs using the GitHub issue board as a guide
    - Creating bug reports on the GitHub issue board
- **Where the team had trouble and where the team is stuck:**
    - the primary piece of feedback from the beta test was some reported terminal errors. We've been unable to replicate, and we suspect that despite the report saying the user was using Powershell, the user may have been tunnelled into a linux server (such as the ENGR flip servers) due to them describing "bash" errors, and the command they had an issue with being a standard part of Powershell for twenty years

### Goals planned for next week:
- Full application testing
- Implement user input constraints
- Record demo video
- final presentation

## Contributions of Individual Team Members

### Brennan Duman:
**Goals planned for this week:**
- fix style issues around naming conventions
- create project poster

**Team progress and issues:**
- **What team member did:**
    - Went through and updated all remaining instances of camelCase naming to kebab-case
    - Created the initial layout of the poster
        - also wrote abstract & created architecture diagram
    - Tested on Linux
    - Did full integration test
- **What worked:**
    - Changed all camelCase to kebab-case
    - Did integration test using all four of current class syllabi, and confirmed that they were accurately processed
- **What team member learned:**
    - On some linux distros (ubuntu based?), python executions must be run in a virtual environment
    - Chrome on linux mint makes the popup with our UI disappear when a file is selected
- **Where the team member had trouble and where the team member is stuck:**
    - Couldn't fully test on linux due to file dialog / extension popup interaction in chrome.

**Goals planned for next week:**
- Record demo video for final presentation
- Give final presentation (Thursday 3/12)

### Carter Cripe:
**Goals planned for this week:**
- Implement complex question answering route
- Implement search query route
- Add user input constraints

**Team progress and issues:**
- **What team member did:**
    - Determined workaround for class identification issue
    - Implimented complex question answering route for backend
    - Implimented search query route for backend
    - Created plan to impliment input constraints
- **What worked:**
    - Using prebuilt framework from earlier in the project greatly sped up the process of building these routes
    - Communication with the team regarding structure made it simple to determine what was needed
- **What team member learned:**
    - I learned that it is important to keep track of variable types when working in a typeless language like python. I had a issue for a while in the code where a variable that I thought was a python dictionary was actually a plain json string, which caused issues.
- **Where the team member had trouble and where the team member is stuck:**
    - I got really sick part way through the week and was rendered unable to meet with the group or do too much to help with some of the collaborative items on the agenda.

**Goals planned for next week:**
- Finish implementing user input constraints
- Full testing for the application

### Justin Primc:
**Goals planned for this week:**
- Fix any issues with the API and LLM regarding integration
- Link the `Quick Info` & `Search` buttons/pages from frontend to backend to correctly give the user information
- Update team documentation, User/Developer guides, and README

**Team progress and issues:**
- **What team member did:** Updated the team documentation (User/Developer guides & README). Connected the search functionality from the frontend to the backend so the users' questions get correctly answered by the LLM. Fixed some issues in the routes that were causing errors.
- **What worked:** Communication between team members to explain their sections of code and what they envisioned the final product to do.
- **What team member learned:** I learned how through the use of routes to trigger the LLM to give the user either a response that has already been generated or a new response.
- **Where the team member had trouble and where the team member is stuck:** I had trouble figuring out how to connect the backend with the frontend while triggering the LLM response.

**Goals planned for next week:**
- Record demo for application
- Give final presentation
