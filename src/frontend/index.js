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
 * extracts the file name from the given path
 * SOURCE: HTML SPEC: https://html.spec.whatwg.org/multipage/input.html#fakepath-srsly
 * Param: path {str} - the file path of an inputted file
 */
function extractFilename(path) {
  if (path.substr(0, 12) == "C:\\fakepath\\")
    return path.substr(12); // modern browser
  var x;
  x = path.lastIndexOf('/');
  if (x >= 0) // Unix-based path
    return path.substr(x+1);
  x = path.lastIndexOf('\\');
  if (x >= 0) // Windows-based path
    return path.substr(x+1);
  return path; // just the filename
}

async function processFile(filePath){
  //let fileName = extractFilename(filePath);

  inputObj = document.getElementById("fileInput");
  const file = inputObj.files[0];

  if(!file){
    console.log("Error! The no file found.");
    return "Err~|~";
  }

  const arrayBuffer = await file.arrayBuffer();
  const pdf = await pdfjsLib.getDocument({ data: arrayBuffer }).promise;

  let fullText = "";

  for (let i = 1; i <= pdf.numPages; i++) {
    const page = await pdf.getPage(i);
    const content = await page.getTextContent();

    const strings = content.items.map(item => item.str);
    fullText += strings.join(" ") + "\n\n";
  }

  console.log(fullText);
}

function addSyllabus(){
  //TODO: see what kind of data has been inputted (.pdf, .txt, raw text), and
  //  process accordingly
  let inputObj = document.getElementById("fileInput");
  let filePath = inputObj.value;
  processFile(filePath);

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