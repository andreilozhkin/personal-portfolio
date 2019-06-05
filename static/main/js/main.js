

/* Toggle between showing and hiding the navigation menu */

function toggleMenu() {
  let nav = document.getElementsByClassName("header__nav")[0];

  if (nav.style.display === "block") {
    nav.style.display = "none";
  } else {
    nav.style.display = "block";
  };
};


/* Collapse navigation menu on link click */

function collapseMenu() {
  if (!x.matches) {
    console.log('smth');
    let nav = document.getElementsByClassName("header__nav")[0];
    nav.style.display = "none";
  }
};


/* Auto expand/collapse */

function expandMenu() {
  let nav = document.getElementsByClassName("header__nav")[0];

  if (x.matches) {
    console.log('expand');
    nav.style.display = "block";
  } else {
    console.log('collapse');
    nav.style.display = "none";
  };
}

var x = window.matchMedia("(min-width: 1000px)")
x.addListener(expandMenu)


/* zenscroll scroll duration ms */
zenscroll.setup(600)
