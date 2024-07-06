document.addEventListener("DOMContentLoaded", function () {
  "use strict";
  initPreLoader();
  initNavOpener();
});

function initPreLoader() {
  setTimeout(function () {
    document.getElementById("pre-loader").style.display = "none";
  }, 1200);
}

function initNavOpener() {
  function toggleClass(element, className) {
    element.classList.toggle(className);
  }

  function addClickEvent(selector, callback) {
    document.querySelectorAll(selector).forEach(function (element) {
      element.addEventListener("click", function (event) {
        event.preventDefault();
        callback(element);
      });
    });
  }

  addClickEvent(".side-close, .side-opener, .mt-side-over", function () {
    toggleClass(document.body, "side-col-active");
    document.querySelector(".side-opener").classList.toggle("active");
    document.querySelector(".mt-side-over").classList.toggle("active");
  });

  addClickEvent(".mobile-toggle", function () {
    toggleClass(document.body, "mobile-active");
    document.querySelector(".mobile-toggle").classList.toggle("active");
  });

  addClickEvent(".cart-opener, .mt-mdropover", function (element) {
    element.parentNode.classList.toggle("open");
  });

  addClickEvent(".search-close, .icon-magnifier, .fa-search", function () {
    toggleClass(document.body, "search-active");
  });

  addClickEvent(".drop-link, #nav > ul > li.drop > a", function (element) {
    element.nextElementSibling.classList.toggle("open");
  });

  addClickEvent(".mt-subopener", function (element) {
    element.parentNode.nextElementSibling.classList.toggle("open");
  });
}
