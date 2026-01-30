# Syllabye

## Say Goodbye to Syllabi

# Abstract

Nearly every class has a different set of rules/policies, whether it’s regarding citation guidelines or late-work allowances. It can be difficult to keep track of all of the different information or navigate each class’s individual Canvas page to see where this particular instructor stores the syllabus. Syllabye is the one-stop shop to find all of your syllabi, built right inside your browser. With a single click, you can easily search through any of the documents you’ve added, providing easy access to the information you need.

# Team Info

## Team

* Carter Cripe – Team Lead / Visionary / Backend Developer  
* Justin Primc – Full Stack Developer  
* Brennan Duman – Front End Developer

## Relevant Links

* [Git Repo](https://github.com/CarterCripe/Syllabye)  
* [Slideshow](https://docs.google.com/presentation/d/12o9AsrxNtalbM3esm7ppx6monv_dLKXqNAjyES7Q-0A/edit?slide=id.g3b94ffe56e8_0_164#slide=id.g3b94ffe56e8_0_164)  
* [Final Project Examples from 2025](https://oregonstateuniversity-my.sharepoint.com/personal/motwanim_oregonstate_edu/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fmotwanim%5Foregonstate%5Fedu%2FDocuments%2FCS362%2DWinter25%2DFinalProjects%2Fall%5Fposters%2Epdf&parent=%2Fpersonal%2Fmotwanim%5Foregonstate%5Fedu%2FDocuments%2FCS362%2DWinter25%2DFinalProjects&ga=1)    
* [Project Brainstorming Doc](https://docs.google.com/document/d/1MjUYfTQYI4w3ZUw2u5MtEc1HKZmD9fqOyzJqfi-eMug/edit?usp=sharing) 

## Communication Channels:

* Discord  
* Google Docs  
* Github  
* Outlook

# Product Description

When a student is taking three or more courses simultaneously, it's often difficult for them to remember the specific policies of a class. Even more frustrating, it can be hard to find where the syllabus for the class is even stored — sure, it’s \*somewhere\* on Canvas, but at 11:37 pm when you’re trying to find the citation guidelines, you don’t have the time or mental energy to track down the specific page.

That’s where Syllabye comes in. Built directly into the browser, students can add a class’s syllabus at the beginning of the year, and then at any point afterward, quickly search through to find the information they need.

Currently, there are two different approaches to accessing a class’s syllabus.

1. Through Canvas  
2. Through a downloaded file

At Oregon State University, every course must make its syllabus accessible on Canvas. However, there is not a specific place where it must be, with common practices being the specific “Syllabus” tab, a module titled “Syllabus”, or a section in the “Home” tab. This means students have to go searching each time they want to access the syllabus.

Students do have the option of downloading the syllabus to a local device, but there are issues with this approach as well. Most students (especially ones outside of STEM fields) use computers to access the internet through a web browser; any extra functionality beyond that isn’t only unneeded but can be daunting to use.

By allowing access to files to stay within the browser, users across the tech-literacy spectrum can feel comfortable. Additionally, bringing all of the syllabi together presents interesting opportunities for stretch goals regarding the processing of syllabi to aid students even more.

With this tool, students will be able to more efficiently access their syllabi, simplifying the process of both locating where the syllabus is hosted as well as searching through it for the desired information.

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
* Performance & Speed: The extensions search function must return a result to the user within 2 seconds for queries across all user stored syllabi. The extensions pop-up interface must load in under 2 seconds.

## External Requirements

* Error Handling: Syllabye must handle common error scenarios, including invalid search queries and incomplete uploads. The system must validate all user inputs and provide clear error messages.  
* Installation: The extension will be packaged for ease of access through official browser extension stores (Chrome Web Store, Firefox, Microsoft Edge). User can install Syllabye with a single click from these stores.  
* Build & Development: The project’s repository will allow other developers to clone the repository and build the extension from source for themselves within 20 minutes.  
* Project Scope: Three team members working over the nine weeks of the course. Syllabye is appropriately sized with core features of (upload, storage, and search) that are all achievable as an MVP within six weeks leaving three weeks for testing and implementation.

## Technical Approach

Our project uses React to build a clean, modern interface that feels like a professional app. Since it’s a Chrome Extension, it is accessible from right within the browser, so students don't have to constantly switch tabs or download files to find a due date. We will use AI as a data formatter in order to properly sort the data from syllabi. Instead of us manually coding rules for every syllabus, the AI reads the uploaded information, picks out the important stuff like late policies and point breakdowns, and saves it into a searchable format. This setup lets us handle the heavy lifting of reading documents in the background when they upload the information. When the user needs to access the information later, it can be presented effectively instantly without the need for lengthy API calls.

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

- Build React based pop-up interface for a browser extension

Week 4:

- Integrate PDF parsing, file upload, and data storage on local devices

Week 5:

- Build the text search across all stored syllabi, and display results with highlighting

Week 6:

- Implement error handling, add editing features to syllabi (Add, Delete)

Week 7:

- Test with different syllabus formats, bug fixes

Week 8:

- Implement any stretch goals  
- Performance optimization

Week 9:

- Final testing and bug fixes  
- Submit all deliverables and prepare for the final presentation

# Team Process

## Toolset

Backend: Flask Python API – Industry standard, team familiarity  
Frontend: React – Industry standard, commonly used for web-based applications

## Team Roles & Schedule

* Carter Cripe – Supreme Leader / Visionary / Backend Developer: Came up with idea, familiar with Flask  
  * Week 5: Function Layout for flask API \- Use Case 1  
  * Week 6: Sending and receiving data with frontend functional \- Use Case 1  
  * Week 7: Data sorting and processing functional \- Use Case 2  
  * Week 8-9 Testing and Refinement \- All Use Cases  
* Justin Primc – Full Stack Developer: Has experience with backend & frontend  
* Brennan Duman – Front End Developer: Has experience with HTML/CSS Web design  
  * Week 5: Proof of Concept (hard coded) – Use Case 2  
  * Week 7: API Integration – Use Case 1 & 3  
  * Week 8-9: Testing & Refinement – All Use Cases

## Major Risks

1. Lack of time. Due to a variety of circumstances, our timeline has been delayed significantly.  
2. Backend issues.  
   1. Saving/Retrieving information from computer  
   2. Accessing LLM API  
3. Frontend issues.  
   1. Usability problems  
   2. Small user window due to being an extension

## External Feedback

Feedback is best accepted at all levels, but would be best accepted during the integration between front and back ends, as this fundamentally represents the user experience. Similarly, feedback for drafts of the frontend are important even when divorced from file access, as it determines the user’s initial interaction with the extension. 