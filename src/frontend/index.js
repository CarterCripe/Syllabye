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
 * processes the file input into raw text if needed, and send to backend
 */
async function addSyllabus(){
  const inputObj = document.getElementById("fileInput");
  const file = inputObj.files[0];
  
  if(!file){
    addSyllabusError("Error! No file found.");
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
  }
  
  if(text){
    console.log(text);
  }else{
    addSyllabusError("Error! No file content found!");
  }
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
})


// Home Screen Screen Switching Buttons

let btnAddSyllabus = document.getElementById("btnAddSyllabus");
btnAddSyllabus.addEventListener("click", function(){
  switchScreen("home", "add");
});

let btnSeeSyllabus = document.getElementById("btnSeeSyllabus");
btnSeeSyllabus.addEventListener("click", function(){
  switchScreen("home", "raw");
});

let btnQuickInfo = document.getElementById("btnQuickInfo");
btnQuickInfo.addEventListener("click", function(){
  switchScreen("home", "quick");
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