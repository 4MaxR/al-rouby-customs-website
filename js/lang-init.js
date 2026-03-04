(function () {
  "use strict";

  if (window.location.pathname !== "/index.html") {
    return;
  }

  function getStored(key) {
    try {
      return window.localStorage.getItem(key);
    } catch (error) {
      return null;
    }
  }

  function setStored(key, value) {
    try {
      window.localStorage.setItem(key, value);
    } catch (error) {
      return;
    }
  }

  var preferredLanguage = getStored("preferredLanguage");
  if (preferredLanguage === "ar") {
    window.location.replace("/ar/index.html");
    return;
  }
  if (preferredLanguage === "zh") {
    window.location.replace("/zh/index.html");
    return;
  }
  if (preferredLanguage === "en") {
    return;
  }

  if (getStored("languageAutoInitialized") === "1") {
    return;
  }

  var languages = [];
  if (Array.isArray(navigator.languages)) {
    languages = navigator.languages.slice();
  }
  if (navigator.language) {
    languages.push(navigator.language);
  }

  setStored("languageAutoInitialized", "1");

  var hasArabic = languages.some(function (value) {
    return typeof value === "string" && value.toLowerCase().indexOf("ar") === 0;
  });
  if (hasArabic) {
    window.location.replace("/ar/index.html");
    return;
  }

  var hasChinese = languages.some(function (value) {
    return typeof value === "string" && value.toLowerCase().indexOf("zh") === 0;
  });
  if (hasChinese) {
    window.location.replace("/zh/index.html");
  }
})();
