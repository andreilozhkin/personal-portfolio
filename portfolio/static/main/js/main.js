

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


// Show header on scroll up

function debounce(func, wait = 10, immediate = true) {
      let timeout;
      return function() {
        let context = this, args = arguments;
        let later = function() {
          timeout = null;
          if (!immediate) func.apply(context, args);
        };
        let callNow = immediate && !timeout;
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
        if (callNow) func.apply(context, args);
      };
    };
    let scrollPos = 0;

    const nav = document.querySelector('.header');
    function checkPosition() {

      let windowY = window.scrollY;

      if (windowY <= 200) {
        nav.classList.add('is-visible');
      }

      else if (windowY < scrollPos) {
        // Scrolling UP
        nav.classList.add('is-visible');
        nav.classList.remove('is-hidden');
      } else {
        // Scrolling DOWN
        nav.classList.add('is-hidden');
        nav.classList.remove('is-visible');
      }
      scrollPos = windowY;
    }

    window.addEventListener('scroll', debounce(checkPosition));
