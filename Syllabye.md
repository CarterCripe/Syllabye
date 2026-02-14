# Syllabye

## Say Goodbye to Syllabi

# Abstract

Nearly every class has a different set of rules/policies, whether it’s regarding citation guidelines or late-work allowances. It can be difficult to keep track of all of the different information or navigate each class’s individual Canvas page to see where this particular instructor stores the syllabus. Syllabye is the one-stop shop to find all of your syllabi, built right inside your browser. With a single click, you can easily search through any of the documents you’ve added, providing easy access to the information you need.

# Team Info

## Team

* Carter Cripe – Team Lead / Visionary / Backend Developer  
  * Responsible for designing and implementing the backend Flask API that processes and stores syllabus data.  
* Justin Primc – Full Stack Developer  
  * Responsible for connecting the components of the frontend and backend. Handles the integration between the user interface and the API, implementing core features across both layers.  
* Brennan Duman – Front End Developer  
  * Responsible for building and designing the user interface browser extension using HTML5, CSS, and JavaScript. Responsible for creating an intuitive and accessible interface that works for a browser extension.

## Relevant Links

* [Git Repo](https://github.com/CarterCripe/Syllabye)  
* [Slideshow](https://docs.google.com/presentation/d/12o9AsrxNtalbM3esm7ppx6monv_dLKXqNAjyES7Q-0A/edit?slide=id.g3b94ffe56e8_0_164#slide=id.g3b94ffe56e8_0_164)  
* [Syllabye - Deliverable 2](https://docs.google.com/presentation/d/1KYD8NY-fFu3AdG_hjp32yP1MZYPcbqdz3A6_VbVPdJI/edit?usp=sharing)  
* [Final Project Examples from 2025](https://oregonstateuniversity-my.sharepoint.com/personal/motwanim_oregonstate_edu/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fmotwanim%5Foregonstate%5Fedu%2FDocuments%2FCS362%2DWinter25%2DFinalProjects%2Fall%5Fposters%2Epdf&parent=%2Fpersonal%2Fmotwanim%5Foregonstate%5Fedu%2FDocuments%2FCS362%2DWinter25%2DFinalProjects&ga=1)    
* [Project Brainstorming Doc](https://docs.google.com/document/d/1MjUYfTQYI4w3ZUw2u5MtEc1HKZmD9fqOyzJqfi-eMug/edit?usp=sharing) 

## Communication Channels:

* Discord  
* Google Docs  
* Github  
* Outlook

# Product Description

## Goal

Syllabye aims to provide students with instant access to all of their course syllabi through a browser extension. This tool will allow students to upload their syllabi at the beginning of each term for all of their courses and then quickly search across all of them or individually for specific policies. The goal of this application is to help eliminate any frustration around hunting through multiple files and links to find the class syllabus when students need urgent information.

## Current Practice

Currently, there are two different approaches to accessing a class’s syllabus.

1. Through Canvas: At OSU, every course has its syllabus linked through Canvas, but there is no standard for this, leading to each course or professor having a different location for their syllabus.  
2.  Through Downloaded Files: Students can also download the provided links from their Canvas onto their local devices.

## Novelty

Syllabye's key innovation is focused on bringing all syllabi together into a single, browser-integrated interface that enables cross-syllabus searching. Unlike Canvas's approach or traditional file downloads, Syllabye allows students to search across all of their syllabi simultaneously from one location. By keeping this functionality within the browser extension, users across the entire spectrum of technical understanding, so anyone can feel comfortable using the tool without needing to learn new software or file management systems.

## Effects

With Syllabye, students will be able to more efficiently access their course policies and information, reducing both the time spent searching and the stress associated with uncertainty about course requirements.

# Requirements

## Functional Requirements (Use Cases)

Use Case 1: Adding a New Syllabus (Justin Primc)  
Actors: Student / User  
Triggers: Student begins a new course and receives a syllabus.  
Preconditions: User has installed Syllabye and has access to a PDF of their syllabus  
Postconditions: Syllabus is stored in the extensions database, is searchable through the extension, and appears to the user.  
List of steps:

1. User opens the Syllabye extension from their browser  
2. User selects the “Add New Syllabus” button  
3. User enters course information and uploads a PDF of their syllabus  
4. Course appears in the user’s syllabus list

Extensions/variations of the success scenario:

* User pastes the direct text instead of uploading a file

Exceptions: failure conditions and scenarios: 

* File is not a valid PDF: System displays an error message  
* Duplicate course name: System displays an error and asks the user to confirm overwrite or rename course.

Use Case 2: Searching Syllabus (Brennan Duman)  
Actors: Student / User  
Triggers: Student opens Syllabye  
Preconditions: Syllabye is installed and a syllabus has been added  
Postconditions: User has desired information from syllabus.  
List of steps:

1. User selects syllabus to search from provided menu of available syllabi  
2. User is presented with a search input  
3. User searches for information, and Syllabye provides text matches (a la “Ctrl+F” find-on-page functionality)

Extensions/variations of the success scenario:

* User gets desired information from syllabus

Exceptions: failure conditions and scenarios:

* No matching text can be found; user must use different search terms to find information  
* No matching text can be found; desired information is not included within syllabus

Use Case 3: Saving Syllabus information (Carter Cripe)  
Actors: Student/ User  
Triggers: Student opens Syllabye  
Preconditions: Syllabye is installed and syllabus has been added  
Postconditions: User successfully saved information for fast access later  
List of steps (success scenario):

1. User searches for desired content from a syllabus  
2. User selects “Save information.”  
3. User then exits to the home page  
4. Information can be found via the saved information button.

Extensions/variations of the success scenario

* User can access the saved information

Exceptions: failure conditions and scenarios

* Saved information limit is reached

## Non-Functional Requirements

* Usability & Accessibility: The interface is simple enough so that a first-time user can successfully and easily add and search a syllabus within 2 minutes without external help.  
* Data Privacy: All syllabus documents and their users data must be stored on their users devices without transmission to external servers to protect student privacy.  
* Performance & Speed: The extensions search function must return a result to the user within 2 seconds for queries across all user-stored syllabi. The extensions pop-up interface must load in under 2 seconds.

## External Requirements

* Error Handling: Syllabye must handle common error scenarios, including invalid search queries and incomplete uploads. The system must validate all user inputs and provide clear error messages.  
* Installation: The extension will be packaged for ease of access through official browser extension stores (Chrome Web Store, Firefox, Microsoft Edge). User can install Syllabye with a single click from these stores.  
* Build & Development: The project’s repository will allow other developers to clone the repository and build the extension from source for themselves within 20 minutes.  
* Project Scope: Three team members working over the nine weeks of the course. Syllabye is appropriately sized with core features of (upload, storage, and search) that are all achievable as an MVP within six weeks, leaving three weeks for testing and implementation.

## Technical Approach

Our project uses a combination of HTML5, CSS, and JavaScript to build a clean, modern interface that feels like a professional app. Since it’s a Chrome Extension, it is accessible from right within the browser, so students don't have to constantly switch tabs or download files to find a due date. We will use AI as a data formatter in order to properly sort the data from syllabi. Instead of us manually coding rules for every syllabus, the AI reads the uploaded information, picks out the important stuff like late policies and point breakdowns, and saves it into a searchable format. This setup lets us handle the heavy lifting of reading documents in the background when they upload the information. When the user needs to access the information later, it can be presented effectively instantly without the need for lengthy API calls.

## Risks

One major risk for the app is syllabus variance. Many classes have different types of syllabi containing different formats of information, amounts of information, and depth of information. Our app will need to be able to handle every type of syllabus in order to properly present the information accurately.

Another major risk for the app is properly handling the more complex system of browser extensions instead of simple websites. We will need to navigate this extra added complexity in order for the project to function as it should.

## Features:

### Primary:

1. Process text & PDFs into sorted information  
2. Accessible from Chromium browser toolbar  
3. Store processed information  
4. Retrieve previously processed information

### Stretch Goals:

1. Notify user before homework/exams are due  
2. Sort assignments by importance based on grading scales and class grades

## Timeline:

Week 1:

- Form a team and begin project brainstorming

Week 2: 

- Complete project proposal and presentation  
- Set up basic environment for development (GitHub, Docs)

Week 3:

- Create Project Plan \- ADD MORE INFO

Week 4:

- Create Project Plan \- ADD MORE INFO

Week 5:

- Create project file structure  
- Implement backend data retrieval and returning  
- Create API documentation for backend/frontend synchronization  
- Create draft for frontend  
  - Layout, colour scheme

Week 6:

- Begin implementation on backend data processing functions  
- Implement automated unit testing  
- Implement frontend from draft

Week 7:

- Finish backend data processing functions

Week 8:

- Implement any stretch goals

Week 9:

- Final testing and bug fixes  
- Submit all deliverables and prepare for the final presentation

# Team Process

## Toolset

Backend: Python Flask API – Industry standard, team familiarity  
Frontend: HTML5/CSS/JavaScript – Industry standard: these tools/languages are the most common implementation methods for web-based applications.

## Team Roles & Schedule

* Carter Cripe – Visionary / Backend Developer: Came up with idea, familiar with Flask  
  * Week 5: Function Layout for flask API / API documentation \- Use Case 1  
  * Week 6: Sending and receiving data with frontend functional \- Use Case 1  
  * Week 7: Data sorting and processing functional \- Use Case 2  
  * Week 8-9 Testing and Refinement \- All Use Cases  
* Justin Primc – Full Stack Developer: Has experience with backend & frontend  
* Brennan Duman – Front End Developer: Has experience with HTML/CSS Web design  
  * Week 5: Proof of Concept (hard coded) – Use Case 2  
  * Week 7: API Integration – Use Case 1 & 3  
  * Week 8-9: Testing & Refinement – All Use Cases

## Major Risks

1. Lack of time.   
   1. Likelihood: Medium  
   2. Impact: Medium  
   3. Evidence: Due to a variety of circumstances, our timeline has been delayed significantly.  
   4. Reduction Plan: Each team member shall commit more than six hours per week to the project.  
   5. Detection Plan: Consistent updates during team meetings regarding progress.  
   6. Mitigation Plan: Consistent communication regarding scope of project  
2. Saving/retrieving information from the computer  
   1. Likelihood: Low  
   2. Impact: High  
   3. Evidence: The entire software depends on saving and retrieving information.  
   4. Reduction Plan: Use standard file access APIs and systems.  
   5. Detection Plan: Confirm data is accessible between sessions, and is accessible using traditional file system access.  
   6. Mitigation Plan: Test data persistence after major feature additions.  
3. Syllabus format variation  
   1. Likelihood: High  
   2. Impact: Medium  
   3. Evidence: Between the three team members in just this academic term, we each have at least 3 syllabi for different courses that have a difference in their format.  
   4. Reduction Steps: By building a diverse testing size of different formatted syllabi, we can design our software to focus on the semantic patterns instead of the formatting.  
   5. Detection Plan: Maintain a test coverage where the system is able to at least process 85% of the given test syllabi.  
   6. Mitigation Plan: Focus only on syllabi provided by Oregon State University courses.   
4. Agentic Prompt Engineering difficulty  
   1. Likelihood: High  
   2. Impact: Medium  
   3. Evidence: Engineering LLM prompts and prompt templates takes a lot of development time.  
   4. Reduction Steps: Dedicate time specifically for testing and developing prompts.  
   5. Detection Plan: Ensure LLM API calls result in desired parsing of syllabi into pre-selected information sections.  
   6. Mitigation Plan: Develop prompt templates that result in similar outputs from LLM  
5. Navigating extension window  
   1. Likelihood: Medium  
   2. Impact: High  
   3. Evidence: Extensions generally use small to medium windows for user interaction. Smaller windows are more difficult for users to interact with.  
   4. Reduction Steps: Consistently test user experience of user interfaces to evaluate the difficulty of interaction  
   5. Detection Plan: Through constant testing, note when difficulties arise.  
   6. Mitigation Plan: Keep interfaces as simple as possible, with a minimal number of large interaction objects (primarily buttons).

## External Feedback

Feedback is best accepted at all levels, but would be best accepted during the integration between front and back ends, as this fundamentally represents the user experience. Similarly, feedback for drafts of the frontend are important even when divorced from file access, as it determines the user’s initial interaction with the extension. 

# Software

## Software Architecture

The software is implemented in a **Layered Architecture Pattern**.  
Architectural Assumptions:

- Single-user deployment: The system is designed for individual student use on their personal device. This enables the storage of data locally without the use of an external database server.  
- Chrome Browser: The frontend assumes that execution of the software will be run within the Chromium-based browser system.

### Major Components

The software is split into two primary components: the frontend and the backend.

The frontend is responsible for interacting with the user, and is built using traditional web development tools (HTML5, CSS, JavaScript).

The backend is responsible for processing and storing syllabus information, and is built using Python to perform many different data processing operations. The backend will incorporate a Flask interface that operates as a REST API that the frontend can send and receive data from.   

### Interface

The application need to communicate in a couple of key ways:

1. Save Syllabus (Course Name) – save a syllabus  
   1. Return {Integer}: 0 if successful, non-0 for various errors.  
2. Retrieve Syllabus – retrieve the syllabus in full  
   1. Return {JSON}: The text of the syllabus  
3. Retrieve Info (Course, Specific Information) – retrieves a specific piece of information (i.e. turn in policy, grading, etc.) from a course  
   1. Return {JSON}: The text of the processed information  
4. Search (Search Term) – searches all syllabi   
   1. Return {JSON}: All instances of that match

### Data

The data that our project will be storing will be JSON objects representing information about the syllabi for each course. Each course’s information will be stored as a JSON object. Initially the user will upload their raw syllabus data to the browser extension, and the data will be sent to the backend API, where it will be processed. The backend will transform the raw information into sorted categories, and then return a sorted list of syllabus categories to the frontend browser extension. The information will be stored locally on the user’s platform, and will be accessed from there by the frontend whenever needed. If further processing is required, for example due to a complex request from the user, further backend API calls will further clarify the data. 

## Software Design

### Frontend

The frontend is responsible for interacting with the user. Its size is limited, due to the implementation being through a Chromium extension. It must be able to accept a user provided syllabus, and retrieve information within that syllabus that’s been processed by the backend.

The frontend can be further split into two different layers: the User Interface (UI) / Presentation Layer, and the Business Layer.

The Presentation Layer is everything the user sees. Upon initial loading, the user will be presented with four options:

1. Add a new Syllabus. Selecting this option will pull up a sub-interface that will allow a user to drag-and-drop a pdf file, a text file, or raw text. Users will also be able to input a course name that will be associated with the syllabus.  
2. Retrieve Syllabus. Selecting this option will allow users to select a course from a list generated from the saved syllabi. Then, the raw text of the selected course’s syllabus will be provided.   
3. Retrieve Specific Information. Selecting this option will allow a user to select a course from a list generated from the saved syllabi, as well as an information category. These information categories include but will not be limited to a) assignment deadlines, b) AI use policy, c) grade weighting, and d) attendance policy. These information categories will correspond to processed categories on the backend. Once a course and category has been selected, the user will be presented with the information that matches that category from the selected course (if any exist).  
4. Search syllabi. Selecting this option will allow users to enter information into a search bar, which will then be matched to specific information from a syllabus. If the requested information matches pre-processed data, the user will be show the pre-processed information. Otherwise, the backend API will be called and will generate a specific answer for the user.

The Business Layer handles communication with the backend API and any frontend processing required. This includes pdf to text conversion, as well as parsing information from the backend for proper display to the user.

### Backend

The backend is responsible for processing the user’s syllabus information and returning the information as a usable JSON object to the frontend for display. The backend functions as a REST API. It receives requests from the frontend containing raw data, and it processes the data before returning it to the frontend. The types of data processing are as follows:

1. Processing Raw Syllabi: When a user adds a new syllabus to the frontend, the frontend will send it to the backend to process. The backend will take the raw data and use an agentic llm system to break the information down into many relevant categories. It will then reassemble the produced information into a structured JSON object containing presentable pre-sorted information.  
2. Answering complex user questions: Most basic questions should be answerable by the frontend using the presorted data from the initial data processing, but if the user has a complex question, it will resend the backend the raw syllabus information, and the backend will use an LLM agent to answer the complex question and return the answer.

## Coding Guideline

### JavaScript

This project will use the [style guide used by W3Schools](https://www.w3schools.com/js/js_conventions.asp). W3Schools is a programming tutorial company that publishes documentation on a variety of languages with the goal to make learning to code easier. Duman, our primary frontend developer, is very familiar with their website and conventions. W3’s style guide also aligns with common industry standards for coding and JavaScript more specifically, such as the use of camelCase in variable and function naming, a line length maximum of 80 characters, and explicitly using two spaces (“  ”) for indentation purposes rather than a tab/tabulation, which is rendered differently by different text and code editors.

W3 also has a [best practices guide](https://www.w3schools.com/js/js_best_practices.asp) that will also be used.

### Python

This project will use the [style guide used in the Python standard library](https://peps.python.org/pep-0008/). This is the closest thing to an “official” style guide for the language.

### Enforcement

These guides and styles will be enforced through a pre-merge check. That is, before code is merged into the main branch of the GitHub repository, developers are responsible for confirming their code matches the appropriate style guide. Additionally, team members are not allowed to merge their own branch; a branch must be checked over by someone who is not the primary developer (and if possible, the person who did the least development work on that branch). This will allow the code to be viewed with fresh eyes, and reduce the amount of mistakes and style deviations introduced into the final product.

## Test Plan

Testing is broken up into three general sections: 1\) Frontend 2\) Backend and 3\) Integration.

### Frontend

The frontend is primarily responsible for two things: UI and converting pdfs to text for the backend.

The UI will be tested using students who aren’t on the development team, especially students outside of computer science or STEM entirely. Each test will flow like this:

1. A laptop with the extension installed will be provided to the tester. The laptop will have tabs open to Canvas pages with a syllabus.  
2. The tester will receive the following explanation of the extension: “This is a browser extension that stores and organizes class syllabi for you. It lets you add a syllabus, and search for specific information from saved syllabi.”  
3. The tester will be given some time to interact with the UI. The tester must be able to  
   1. Add a syllabus  
   2. Search information from a syllabus (note: as this test will occur prior to integration, this will be done using dummy data set up beforehand corresponding with the syllabi that are made available through the Canvas pages).  
4. The user must be able to intuit how to do these tasks without help from the developer, using only UI design and a knowledge of the extension’s purpose, therefore mimicking a user who would download the extension.

### Backend

The backend will be responsible for two main things: Processing the syllabus data using LLM agents and storing/retrieving the data on the user's local machine.

The backend will implement unit testing using Python’s pytest framework. The tests will flow like this:

1. A test syllabus (PDF or text) is provided to the backend processing function  
2. The backend will process the syllabus using LLM agents and will return a structured JSON file  
3. The test will focus on verifying   
   1. PDF text extraction works correctly  
   2. LLM parsing extracted the correct categories used in pre-processed requests (grading policy, late work, etc.)  
   3. The JSON structure is valid and contains all required fields  
   4. Outputs match the expected results for that test syllabus  
   5. The processing of a syllabus is completed within 5-7 seconds

### Integration

Integration testing will validate that the frontend and backend correctly work together through the API layer. The primary focus in ensuring that the data can be passed back and forth between the two layers.

Integration tests will verify three critical data flows.

1. Frontend → Backend (Syllabus Upload)  
   1. Frontend accurately passes syllabus text to the backend  
   2. Backend processes and stores the received data  
   3. Data is stored correctly and is retrievable  
2. Frontend → Backend → Frontend (Pre-processed Requests)  
   1. Frontend sends a request for some pre-processed request (Grading policy, late work policy)  
   2. Backend retrieves pre-processed data and returns that data to frontend  
   3. Frontend displays this data to the user correctly  
3.  Frontend → Backend → Frontend (Custom Requests)  
   1. Frontend sends a search query created by the user  
   2. Backend processes the request, may involvethe  use of LLM  
   3. Backend returns results to the frontend   
   4. Frontend displays the accurate search results to the user

## Documentation

The extension will be delivered alongside a user guide that will have the following information:

1. How to add a syllabus  
2. How to search a syllabus using the quick-info selection  
3. How to search a syllabus using the custom search option  
4. How to retrieve the original text of the syllabus

The extension will also be delivered alongside an extension overview that will explain in simple terms the capabilities of the extension, as well as its potential use cases. This matches with the standards shown by extensions on the Google Chrome Web Store.