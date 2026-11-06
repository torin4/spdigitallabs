// Fade-and-slide reveals as content scrolls into view.
// Runs only when the page's <head> added the "motion" class, which it does only
// for visitors who haven't asked for reduced motion. Without this script the
// head's fallback removes that class, so nothing ever stays hidden.
(function () {
  var root = document.documentElement;
  window.__spMotion = true;
  if (!root.classList.contains("motion")) return;

  // Blocks that slide in on their own, and grids whose items stagger in turn.
  var BLOCKS = [
    ".home-art", ".home-intro-text > *", ".soon", ".home-contact > *",
    "main > .wrap > section > *", ".app-page > section > *", ".app-page > header > *",
    ".page > *", ".post-head > *", ".post-cta", ".post-body > *", ".post-more",
    ".blog-intro > *", ".about-side > *",
  ];
  var ITEMS = [".showcase > li", ".feature-row", ".features > *", ".plans > *", ".post-list > li", ".help-list > li"];

  var seen = new Set();
  var targets = [];
  BLOCKS.concat(ITEMS).forEach(function (sel) {
    document.querySelectorAll(sel).forEach(function (el) {
      if (!seen.has(el)) { seen.add(el); targets.push(el); }
    });
  });
  // A container whose children already animate shouldn't animate as a whole too.
  targets = targets.filter(function (el) {
    return !targets.some(function (other) { return other !== el && el.contains(other); });
  });

  function show(el, delay) {
    el.style.setProperty("--rv-delay", delay + "ms");
    el.classList.add("rv-in");
    el.addEventListener("transitionend", function done(e) {
      if (e.target !== el) return;
      el.removeEventListener("transitionend", done);
      el.classList.remove("rv", "rv-in");
      el.style.removeProperty("--rv-delay");
    });
  }

  var io = new IntersectionObserver(function (entries) {
    var batch = entries.filter(function (e) { return e.isIntersecting; }).map(function (e) { return e.target; });
    batch.sort(function (a, b) {
      return a.compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING ? -1 : 1;
    });
    batch.forEach(function (el, i) {
      io.unobserve(el);
      show(el, Math.min(i, 6) * 70);
    });
  }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });

  targets.forEach(function (el) {
    el.classList.add("rv");
    io.observe(el);
  });
  root.classList.add("motion-ready");
})();
