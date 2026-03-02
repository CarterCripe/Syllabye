/*
 * Get the DOM object correlated with the given string
 * 
 * Param: screenName {str} - the name of the screen
 * 
 * Return {DOM obj - screen div} - the corresponding screen
 */
function getScreenObj(screenName){
  let screen;
  switch(screenName){
    case "home": screen = "scrHome"; break;
    case "add": screen = "scrAddSyl"; break;
    case "raw": screen = "scrSeeSyl"; break;
    case "quick": screen = "scrQuickInfo"; break;
    case "search": screen = "scrSearchResults"; break;
    default:
      console.log("Error: Not supported screen");
      screen = "scrHome";
  }

  return document.getElementById(screen);
}

/*
 * switch the visible screen
 * 
 * Params:
 *   origin {str} - the currently visible screen
 *   dest {str} - the string to switch to
 */
function switchScreen(origin, dest){
  let originScreen = getScreenObj(origin);
  let destScreen = getScreenObj(dest);

  if(originScreen === destScreen){
    console.log("Error: Origin & Destination screens are the same.");
    return;
  }

  originScreen.classList.add("hidden");
  destScreen.classList.remove("hidden"); 
}

/*
 * process a .pdf file into raw text using the PDF.js library
 *
 * Param: file {file obj}: the file from the input
 * 
 * Return {str}: the raw text from the pdf
 */
async function processPDF(file){
  //call the library and process the file
  const arrayBuffer = await file.arrayBuffer();
  const pdf = await pdfjsLib.getDocument({ data: arrayBuffer }).promise;

  let fullText = "";

  //concat the text from each page together into a single string
  for (let i = 1; i <= pdf.numPages; i++) {
    const page = await pdf.getPage(i);
    const content = await page.getTextContent();

    const strings = content.items.map(item => item.str);
    fullText += strings.join(" ") + "\n\n";

  }

  return fullText;
}

/*
 * record error when adding syllabus to console and display on process btn
 *
 * Param: errorMessage {str} - the error message to log in console & dispaly to user
 */
function addSyllabusError(errorMessage){
  console.log(errorMessage);
  let btnProcessSyllabus = document.getElementById("btnProcessSyllabus");
  btnProcessSyllabus.textContent = errorMessage;
}

/*
 * Save a processed syllabus object to chrome.storage.local under a given course name
 *
 * Param: courseName {str} - the key to store the syllabus under a user entered course name
 *        syllabusData {obj} - the process JSON object that returned from the backend
 */
async function saveSyllabus(courseName, syllabusData){
  return new Promise((resolve, reject) => {
    //Load already saved syllabi to not overwrite them
    chrome.storage.local.get("syllabi", function(result){
      const syllabi = result.syllabi || {};
      //Add or overwrite the entry for this coruse name
      syllabi[courseName] = syllabusData;
      //Write the updated syllabi back into local storage
      chrome.storage.local.set({ syllabi: syllabi }, function(){
        if(chrome.runtime.lastError){
          reject(chrome.runtime.lastError);
        } else {
          resolve();
        }
      });
    });
  });
}


/*
 * processes the file input into raw text if needed, and send to backend
 */
async function addSyllabus(){
  const inputObj = document.getElementById("fileInput");
  const file = inputObj.files[0];
  const courseName = document.getElementById("courseInput").value.trim();
  
  if(!file){
    addSyllabusError("Error! No file found.");
    return;
  }

  if(!courseName){
    addSyllabusError("Error! No course name entered.");
    return;
  }

  let text;

  //if the file is a pdf
  if(file.type == "application/pdf"){
    text = await processPDF(file);
  //if the file is a txt
  }else if(file.type == "text/plain"){
    text = await file.text();
  }else{
    addSyllabusError("Error! No valid file selected!");
    return;
  }

  //Make sure the file actually has content
  if (!text || text.trim().length === 0) {
    addSyllabusError("Error! No file content found!");
    return;
  }

  //Let user know that the LLM is working 
  let btnProcessSyllabus = document.getElementById("btnProcessSyllabus");
  btnProcessSyllabus.textContent = "Processing...";

  try {
    //POST raw text to the Flask backend
    const response = await fetch("http://localhost:6767/api/process", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ text: text })
    });

    if (!response.ok) {
      addSyllabusError("Error! Backend procsssing failed.");
      return;
    }

    //Parse returned processed JSON and attach user given courseName
    const processed = await response.json();
    processed.course_name = courseName;
    await saveSyllabus(courseName, processed);

    btnProcessSyllabus.textContent = "Added " + courseName + " Syllabus!";

  } catch (err) {
    console.error(err);
    addSyllabusError("Error! Could not reach backend.");
  }
}

/*
 * displays the chosen file & entered course on the process/"Add Syllabus" btn
 *
 * Param: fileInput {DOM obj - file input}
 */
function displayChosenFile(fileInput){
  //substring is reqd because file paths are obscured behind "C:\fakepath\"
  let fileName = fileInput.value.substring(12, fileInput.value.length);
  
  let courseName = document.getElementById("courseInput").value;

  let btnProcessSyllabus = document.getElementById("btnProcessSyllabus");

  //"Add CS 362: syllabus.pdf"
  btnProcessSyllabus.textContent = "Add " + courseName + ": " + fileName;
}

/*
* Load and return all saved syllabi from chrome.storage.local
* Return {obj} - Dictionary of {courseName : syllabusData, ...}
*/
async function getAllSyllabi(){
  return new Promise((resolve) => {
    chrome.storage.local.get("syllabi", function(result){
      resolve(result.syllabi || {});
    });
  });
}

/*
* Load saved syllabi from storage and populate the See Syllabus screen, gets called everytime user navigates to this screen
*/
async function populateSeeSyllabus(){
  const syllabi = await getAllSyllabi();
  const screen = document.getElementById("scrSeeSyl");
  const select = screen.querySelector("select");
  const display = screen.querySelector("div");

  select.innerHTML = "";
  display.innerHTML = "";

  const courseNames = Object.keys(syllabi);

  if(courseNames.length === 0){
    display.textContent = "No syllabi added yet.";
    return;
  }

  //Add a blank default option so the drop down doesn't auto select the first course
  const defaultOpt = document.createElement("option");
  defaultOpt.textContent = "-- Select a Course --";
  defaultOpt.value = "";
  select.appendChild(defaultOpt);

  //Add +1 option per saved course
  courseNames.forEach(name => {
    const opt = document.createElement("option");
    opt.value = name;
    opt.textContent = name;
    select.appendChild(opt);
  });

  select.addEventListener("change", function(){
    const chosen = syllabi[this.value];
    if(chosen){
      display.textContent = chosen.raw_text;
    } else {
      display.textContent = "";
    }
  });
}

/*
* Load saved sylalbi from storage and populate the Quick Info screen.
*/
async function populateQuickInfo(){
  const syllabi = await getAllSyllabi();
  const screen = document.getElementById("scrQuickInfo");
  const selects = screen.querySelectorAll("select");
  const courseSelect = selects[0];
  const topicSelect = selects[1];
  const display = screen.querySelector("div");
  
  courseSelect.innerHTML = "";
  topicSelect.innerHTML = "";
  display.innerHTML = "";

  const courseNames = Object.keys(syllabi);

  if(courseNames.length === 0){
    display.textContent = "No syllabi added yet.";
    return;
  }

  //Add blank default options
  const defaultCourse = document.createElement("option");
  defaultCourse.textContent = "-- Select a course --";
  defaultCourse.value = "";
  courseSelect.appendChild(defaultCourse);

  //Add an option for each saved course
  courseNames.forEach(name => {
    const opt = document.createElement("option");
    opt.value = name;
    opt.textContent = name;
    courseSelect.appendChild(opt);
  });

  //Some labels and values (Must match section keys returned by the backend).
  //Subject to change, just a rough outline of some possible options
  const topics = [
    ["-- Select a topic --", ""],
    ["Course Info",          "course_info"],
    ["Late Policy",          "late_policy"],
    ["Grading Scale",        "grading_scale"],
    ["Grading Categories",   "grading_categories"],
    ["Assignments",          "assignments"],
    ["Exam Policy",          "exam_policy"],
    ["AI Policy",            "ai_policy"],
    ["Academic Integrity",   "academic_integrity"],
    ["Prerequisites",        "prerequisites"],
    ["Materials",            "materials"],
    ["Support Info",         "support_info"],
  ];

  //Build the topic dropdown from list above
  topics.forEach(([label, value]) => {
    const opt = document.createElement("option");
    opt.textContent = label;
    opt.value = value;
    topicSelect.appendChild(opt);
  });

  function updateDisplay(){
    const course = courseSelect.value;
    const topic = topicSelect.value;
    if(course && topic){
      const info = syllabi[course]?.sections?.[topic];
      display.textContent = info || "Not specified.";
    } else {
      display.textContent = "";
    }
  }

  courseSelect.addEventListener("change", updateDisplay);
  topicSelect.addEventListener("change", updateDisplay);
}


/*
 * -------------------------
 * Listen Events
 * -------------------------
 */

// Add Syllabus
let btnProcessSyllabus = document.getElementById("btnProcessSyllabus");
btnProcessSyllabus.addEventListener("click", function(){
  addSyllabus();
});

// File has been changed
let fileInput = document.getElementById("fileInput");
fileInput.addEventListener("change", function(){
  displayChosenFile(this);
});

// Home Screen Screen Switching Buttons

let btnAddSyllabus = document.getElementById("btnAddSyllabus");
btnAddSyllabus.addEventListener("click", function(){
  switchScreen("home", "add");
});

let btnSeeSyllabus = document.getElementById("btnSeeSyllabus");
btnSeeSyllabus.addEventListener("click", function(){
  switchScreen("home", "raw");
  populateSeeSyllabus();
});

let btnQuickInfo = document.getElementById("btnQuickInfo");
btnQuickInfo.addEventListener("click", function(){
  switchScreen("home", "quick");
  populateQuickInfo();
});

let btnSearch = document.getElementById("btnSearch");
btnSearch.addEventListener("click", function(){
  switchScreen("home", "search");
});

// Back (to home) screen switching buttons

let btnAddSylBack = document.getElementById("btnAddSylBack");
btnAddSylBack.addEventListener("click", function(){
  switchScreen("add", "home");
});

let btnSeeSylBack = document.getElementById("btnSeeSylBack");
btnSeeSylBack.addEventListener("click", function(){
  switchScreen("raw", "home");
});

let btnQuickInfoBack = document.getElementById("btnQuickInfoBack");
btnQuickInfoBack.addEventListener("click", function(){
  switchScreen("quick", "home");
});

let btnSearchBack = document.getElementById("btnSearchBack");
btnSearchBack.addEventListener("click", function(){
  switchScreen("search", "home");
});