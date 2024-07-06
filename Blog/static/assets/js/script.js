"use strict";

/**
 * add event on element
 */

const addEventOnElem = function (elem, type, callback) {
  if (elem.length > 1) {
    for (let i = 0; i < elem.length; i++) {
      elem[i].addEventListener(type, callback);
    }
  } else {
    elem.addEventListener(type, callback);
  }
};

/**
 * navbar toggle
 */

const navbar = document.querySelector("[data-navbar]");
const navbarLinks = document.querySelectorAll("[data-nav-link]");
const navToggler = document.querySelector("[data-nav-toggler]");

const toggleNavbar = function () {
  navbar.classList.toggle("active");
  this.classList.toggle("active");
};

addEventOnElem(navToggler, "click", toggleNavbar);

const closeNavbar = function () {
  navbar.classList.remove("active");
  navToggler.classList.remove("active");
};

addEventOnElem(navbarLinks, "click", closeNavbar);

/**
 * search bar toggle
 */

const searchBar = document.querySelector("[data-search-bar]");
const searchTogglers = document.querySelectorAll("[data-search-toggler]");
const overlay = document.querySelector("[data-overlay]");

const toggleSearchBar = function () {
  searchBar.classList.toggle("active");
  overlay.classList.toggle("active");
  document.body.classList.toggle("active");
};

addEventOnElem(searchTogglers, "click", toggleSearchBar);

// const filterItems = document.querySelectorAll(".filter-item");
// const blogPosts = document.querySelectorAll(".blog-card");

// filterItems.forEach((item) => {
//   item.addEventListener("click", (e) => {
//     const filterValue = e.target.dataset.filter;
//     blogPosts.forEach((post) => {
//       if (filterValue === "all" || post.dataset.category === filterValue) {
//         post.style.display = "block";
//       } else {
//         post.style.display = "none";
//       }
//     });
//   });
// });

// const filterItems = document.querySelectorAll(".filter-item");
// const blogCards = document.querySelectorAll(".blog-card");

// filterItems.forEach((item) => {
//   item.addEventListener("click", (e) => {
//     const filterValue = e.target.dataset.filter;
//     const filteredCards = [];

//     blogCards.forEach((card) => {
//       if (filterValue === "all" || card.dataset.category === filterValue) {
//         filteredCards.push(card);
//       }
//     });

//     // Reorder the filtered cards
//     const gridList = document.querySelector(".grid-list");
//     gridList.innerHTML = "";
//     filteredCards.forEach((card) => {
//       gridList.appendChild(card);
//     });
//   });
// });

const filterItems = document.querySelectorAll(".filter-item");
const blogCards = document.querySelectorAll(".blog-card");

filterItems.forEach((item) => {
  item.addEventListener("click", (e) => {
    const filterValue = e.target.dataset.filter;
    const filteredCards = [];

    blogCards.forEach((card) => {
      if (filterValue === "all" || card.dataset.category === filterValue) {
        filteredCards.push(card);
      }
    });

    // Reorder the filtered cards
    const gridList = document.querySelector(".grid-list");
    gridList.innerHTML = "";
    filteredCards.forEach((card) => {
      gridList.appendChild(card);
    });

    // Remove the active class from all filter items
    filterItems.forEach((item) => {
      item.classList.remove("activte-filter");
    });

    // Add the active class to the clicked filter item
    e.target.classList.add("activte-filter");
  });
});

let slider = document.querySelector(".slider .list");
let items = document.querySelectorAll(".slider .list .item");
let next = document.getElementById("next");
let prev = document.getElementById("prev");
let dots = document.querySelectorAll(".slider .dots li");

let lengthItems = items.length - 1;
let active = 0;

next.onclick = function () {
  active = active + 1 <= lengthItems ? active + 1 : 0;
  reloadSlider();
};
prev.onclick = function () {
  active = active - 1 >= 0 ? active - 1 : lengthItems;
  reloadSlider();
};
let refreshInterval = setInterval(() => {
  next.click();
}, 3000);
function reloadSlider() {
  slider.style.left = -items[active].offsetLeft + "px";
  //
  let last_active_dot = document.querySelector(".slider .dots li.active");
  last_active_dot.classList.remove("active");
  dots[active].classList.add("active");

  clearInterval(refreshInterval);
  refreshInterval = setInterval(() => {
    next.click();
  }, 3000);
}

dots.forEach((li, key) => {
  li.addEventListener("click", () => {
    active = key;
    reloadSlider();
  });
});
window.onresize = function (event) {
  reloadSlider();
};
