// Builds the contact address in the browser, so the page source never contains it in full.
(function () {
  var address = ["support", "spdigitallabs.app"].join("@");
  document.querySelectorAll("a.email").forEach(function (link) {
    var subject = link.getAttribute("data-subject");
    link.href = "mailto:" + address + (subject ? "?subject=" + encodeURIComponent(subject) : "");
    link.textContent = address;
  });
})();
