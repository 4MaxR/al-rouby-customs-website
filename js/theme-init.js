/**
 * Al-Rouby Customs — Theme Initialization
 * Loaded synchronously in <head> to prevent flash of wrong theme.
 */
(function () {
  var t = localStorage.getItem("theme");
  if (t === "dark") document.documentElement.style.colorScheme = "dark";
  if (t) {
    if (document.body) {
      document.body.classList.add(t + "-mode");
    } else {
      document.addEventListener("DOMContentLoaded", function () {
        document.body.classList.add(t + "-mode");
      });
    }
  }
})();
