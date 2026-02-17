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
 * -------------------------
 * Button Listen Events
 * -------------------------
 */

// Home Screen

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

// Back (to home)

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