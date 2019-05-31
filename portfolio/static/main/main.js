

/* Toggle between showing and hiding the navigation menu */
function toggleMenu() {
  var x = document.getElementsByClassName("header__nav")[0];
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}
