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

function switchScreen(origin, dest){
  let originScreen;
  let destScreen;

  
}