/**
 * Al-Rouby Customs — Main JavaScript
 * Static multilingual navigation, theme, and page interactions.
 */
(function () {
  "use strict";

  var ROUTE_WHITELIST = {
    "/": true,
    "/about.html": true,
    "/contact.html": true,
    "/services/customs-clearance.html": true,
    "/services/freight-forwarding.html": true,
    "/services/shipping.html": true,
    "/services/logistics.html": true,
    "/services/customs-logistics-consulting.html": true,
    "/services/aci-nafeza.html": true,
    "/ports/ain-sokhna.html": true,
    "/ports/alexandria.html": true,
    "/ports/sczone.html": true,
    "/blog/customs-clearance-guide-egypt.html": true,
    "/blog/aci-system-guide.html": true,
    "/blog/sea-freight-types.html": true,
    "/blog/egypt-port-fees.html": true,
    "/blog/hs-code-guide.html": true,
  };

  var HOME_ALIAS = {
    en: "/index.html",
    ar: "/ar/index.html",
    zh: "/zh/index.html",
  };

  var ROUTE_ALIASES = {
    "/services/consulting.html": "/services/customs-logistics-consulting.html",
  };

  var ROUTE_OVERRIDES = {
    ar: {
      "/services/customs-logistics-consulting.html": "/ar/services/consulting.html",
    },
  };

  var $ = function (selector, root) {
    return (root || document).querySelector(selector);
  };

  var $$ = function (selector, root) {
    return Array.prototype.slice.call((root || document).querySelectorAll(selector));
  };

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

  function normalizePath(pathname) {
    var locale = "en";
    var base = pathname || "/";

    if (base === "/" || base === "/index.html") {
      return { locale: "en", base: "/" };
    }
    if (base === "/ar/" || base === "/ar/index.html") {
      return { locale: "ar", base: "/" };
    }
    if (base === "/zh/" || base === "/zh/index.html") {
      return { locale: "zh", base: "/" };
    }

    if (base.indexOf("/ar/") === 0) {
      locale = "ar";
      base = base.slice(3);
    } else if (base.indexOf("/zh/") === 0) {
      locale = "zh";
      base = base.slice(3);
    }

    if (!base) {
      base = "/";
    }
    if (base === "/index.html") {
      base = "/";
    }
    if (base.length > 1 && base.charAt(base.length - 1) === "/") {
      base = base.slice(0, -1);
    }
    if (ROUTE_ALIASES[base]) {
      base = ROUTE_ALIASES[base];
    }

    return { locale: locale, base: base };
  }

  function currentRoute() {
    var body = document.body || {};
    var normalized = normalizePath(window.location.pathname);
    return {
      locale: body.dataset && body.dataset.locale ? body.dataset.locale : normalized.locale,
      base:
        body.dataset && typeof body.dataset.routeBase === "string" && body.dataset.routeBase.length
          ? body.dataset.routeBase
          : normalized.base,
    };
  }

  function targetPath(lang, base) {
    if (!ROUTE_WHITELIST[base]) {
      return HOME_ALIAS[lang];
    }
    if (ROUTE_OVERRIDES[lang] && ROUTE_OVERRIDES[lang][base]) {
      return ROUTE_OVERRIDES[lang][base];
    }
    if (base === "/") {
      return HOME_ALIAS[lang];
    }
    return (lang === "en" ? "" : "/" + lang) + base;
  }

  var menuBtn = $("#menuBtn");
  var navLinks = $("#navLinks");
  var themeToggle = $("#themeToggle");
  var backToTop = $("#backToTop");
  var quoteForm = $(".quote-form");
  var langToggle = $("#langToggle");
  var langMenu = $("#langMenu");
  var langSwitcher = langToggle ? langToggle.closest(".language-switcher") : null;
  var langOptions = langMenu ? $$(".lang-option", langMenu) : [];

  function closeLanguageMenu(returnFocus) {
    if (!langSwitcher || !langToggle) return;
    langSwitcher.classList.remove("is-open");
    langToggle.setAttribute("aria-expanded", "false");
    if (returnFocus) {
      langToggle.focus();
    }
  }

  function focusLanguageOption(index) {
    if (!langOptions.length) return;
    var safeIndex = index;
    if (safeIndex < 0) safeIndex = langOptions.length - 1;
    if (safeIndex >= langOptions.length) safeIndex = 0;
    langOptions[safeIndex].focus();
  }

  function openLanguageMenu(focusIndex) {
    if (!langSwitcher || !langToggle) return;
    langSwitcher.classList.add("is-open");
    langToggle.setAttribute("aria-expanded", "true");
    if (typeof focusIndex === "number") {
      focusLanguageOption(focusIndex);
    }
  }

  function selectLanguage(lang) {
    var route = currentRoute();
    setStored("preferredLanguage", lang);
    closeLanguageMenu(false);
    if (navLinks && navLinks.classList.contains("nav-active")) {
      closeMenu();
    }
    window.location.href = targetPath(lang, route.base);
  }

  function closeMenu() {
    if (!navLinks || !menuBtn) return;
    navLinks.classList.remove("nav-active");
    menuBtn.setAttribute("aria-expanded", "false");
    menuBtn.textContent = "\u2630";
    $$(".nav-dropdown").forEach(function (dropdown) {
      dropdown.classList.remove("dropdown-open");
    });
  }

  function toggleMenu() {
    if (!navLinks || !menuBtn) return;
    var isActive = navLinks.classList.toggle("nav-active");
    menuBtn.setAttribute("aria-expanded", String(isActive));
    menuBtn.textContent = isActive ? "\u2715" : "\u2630";
  }

  if (menuBtn) {
    menuBtn.addEventListener("click", toggleMenu);
  }

  $$("#navLinks a").forEach(function (link) {
    if (!link.closest(".nav-dropdown") || link.closest(".dropdown-menu")) {
      link.addEventListener("click", function () {
        closeLanguageMenu(false);
        closeMenu();
      });
    }
  });

  $$(".nav-dropdown > a").forEach(function (trigger) {
    trigger.addEventListener("click", function (event) {
      if (window.innerWidth < 1024) {
        event.preventDefault();
        var parent = trigger.closest(".nav-dropdown");
        var isOpen = parent.classList.contains("dropdown-open");
        $$(".nav-dropdown").forEach(function (dropdown) {
          dropdown.classList.remove("dropdown-open");
        });
        if (!isOpen) {
          parent.classList.add("dropdown-open");
        }
      }
    });
  });

  if (langToggle) {
    langToggle.addEventListener("click", function () {
      if (langSwitcher.classList.contains("is-open")) {
        closeLanguageMenu(false);
      } else {
        openLanguageMenu();
      }
    });

    langToggle.addEventListener("keydown", function (event) {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        if (langSwitcher.classList.contains("is-open")) {
          closeLanguageMenu(false);
        } else {
          openLanguageMenu(0);
        }
      } else if (event.key === "ArrowDown") {
        event.preventDefault();
        openLanguageMenu(0);
      } else if (event.key === "ArrowUp") {
        event.preventDefault();
        openLanguageMenu(langOptions.length - 1);
      } else if (event.key === "Home") {
        event.preventDefault();
        openLanguageMenu(0);
      } else if (event.key === "End") {
        event.preventDefault();
        openLanguageMenu(langOptions.length - 1);
      } else if (event.key === "Escape") {
        closeLanguageMenu(false);
      }
    });
  }

  langOptions.forEach(function (option, index) {
    option.addEventListener("click", function () {
      selectLanguage(option.getAttribute("data-lang"));
    });

    option.addEventListener("keydown", function (event) {
      if (event.key === "ArrowDown") {
        event.preventDefault();
        focusLanguageOption(index + 1);
      } else if (event.key === "ArrowUp") {
        event.preventDefault();
        focusLanguageOption(index - 1);
      } else if (event.key === "Home") {
        event.preventDefault();
        focusLanguageOption(0);
      } else if (event.key === "End") {
        event.preventDefault();
        focusLanguageOption(langOptions.length - 1);
      } else if (event.key === "Escape") {
        event.preventDefault();
        closeLanguageMenu(true);
      } else if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        selectLanguage(option.getAttribute("data-lang"));
      }
    });
  });

  document.addEventListener("click", function (event) {
    if (langSwitcher && !langSwitcher.contains(event.target)) {
      closeLanguageMenu(false);
    }

    if (
      navLinks &&
      menuBtn &&
      navLinks.classList.contains("nav-active") &&
      !navLinks.contains(event.target) &&
      !menuBtn.contains(event.target)
    ) {
      closeMenu();
    }
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") {
      if (langSwitcher && langSwitcher.classList.contains("is-open")) {
        closeLanguageMenu(true);
      }
      if (navLinks && navLinks.classList.contains("nav-active")) {
        closeMenu();
        if (menuBtn) {
          menuBtn.focus();
        }
      }
    }
  });

  $$(".faq-item").forEach(function (item, index) {
    var question = item.querySelector(".faq-question");
    var answer = item.querySelector(".faq-answer");
    if (!question || !answer) return;
    var icon = question.querySelector("span");

    question.setAttribute("aria-expanded", "false");
    answer.id = "faq-answer-" + index;
    question.setAttribute("aria-controls", answer.id);
    answer.setAttribute("role", "region");
    if (!question.id) question.id = "faq-q-" + index;
    answer.setAttribute("aria-labelledby", question.id);
    if (icon) icon.textContent = "+";

    question.addEventListener("click", function () {
      var isOpen = question.getAttribute("aria-expanded") === "true";

      $$(".faq-item").forEach(function (other) {
        if (other !== item) {
          var otherQuestion = other.querySelector(".faq-question");
          var otherAnswer = other.querySelector(".faq-answer");
          var otherIcon = otherQuestion ? otherQuestion.querySelector("span") : null;
          if (otherQuestion) otherQuestion.setAttribute("aria-expanded", "false");
          if (otherAnswer) otherAnswer.style.maxHeight = null;
          if (otherIcon) otherIcon.textContent = "+";
        }
      });

      question.setAttribute("aria-expanded", String(!isOpen));
      answer.style.maxHeight = isOpen ? null : answer.scrollHeight + "px";
      if (icon) icon.textContent = isOpen ? "+" : "\u2212";
    });
  });

  function isDark() {
    return document.body.classList.contains("dark-mode");
  }

  function updateToggleIcon() {
    if (themeToggle) {
      themeToggle.textContent = isDark() ? "\u2600\uFE0F" : "\uD83C\uDF19";
    }
  }

  updateToggleIcon();

  if (themeToggle) {
    themeToggle.addEventListener("click", function () {
      var goingDark = !isDark();
      document.body.classList.remove("dark-mode", "light-mode");
      document.body.classList.add(goingDark ? "dark-mode" : "light-mode");
      setStored("theme", goingDark ? "dark" : "light");
      updateToggleIcon();
    });
  }

  if (window.matchMedia) {
    window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", function () {
      if (!getStored("theme")) {
        document.body.classList.remove("dark-mode", "light-mode");
        updateToggleIcon();
      }
    });
  }

  if (backToTop) {
    var scrollTicking = false;
    window.addEventListener("scroll", function () {
      if (!scrollTicking) {
        window.requestAnimationFrame(function () {
          backToTop.classList.toggle("visible", window.scrollY > 400);
          scrollTicking = false;
        });
        scrollTicking = true;
      }
    });
    backToTop.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  $$('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener("click", function (event) {
      var href = this.getAttribute("href");
      if (href === "#" || href === "#top") {
        event.preventDefault();
        window.scrollTo({ top: 0, behavior: "smooth" });
        return;
      }
      var target = $(href);
      if (target) {
        event.preventDefault();
        var header = $("header");
        var headerHeight = header ? header.offsetHeight : 0;
        var targetTop = target.getBoundingClientRect().top + window.scrollY - headerHeight - 12;
        window.scrollTo({ top: targetTop, behavior: "smooth" });
      }
    });
  });

  if (quoteForm) {
    quoteForm.addEventListener("submit", function (event) {
      event.preventDefault();

      var name = quoteForm.querySelector('[name="name"]');
      var phone = quoteForm.querySelector('[name="phone"]');
      var message = quoteForm.querySelector('[name="message"]');

      if (name && name.value.trim().length < 2) {
        name.focus();
        return;
      }
      if (phone && !phone.value.trim().match(/[\+]?[0-9\s]{10,20}/)) {
        phone.focus();
        return;
      }
      if (message && message.value.trim().length < 5) {
        message.focus();
        return;
      }

      var submitBtn = quoteForm.querySelector('button[type="submit"]');
      var originalText = submitBtn ? submitBtn.textContent : "";

      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = "Sending...";
        submitBtn.style.opacity = "0.7";
      }

      fetch(quoteForm.getAttribute("action"), {
        method: "POST",
        body: new FormData(quoteForm),
        headers: { Accept: "application/json" },
      })
        .then(function (response) {
          if (!response.ok) throw new Error("Request failed");
          if (submitBtn) {
            submitBtn.textContent = "\u2713 Sent Successfully";
            submitBtn.style.background = "#059669";
            submitBtn.style.borderColor = "#059669";
          }
          quoteForm.reset();
        })
        .catch(function () {
          try {
            quoteForm.submit();
            return;
          } catch (error) {
            if (submitBtn) submitBtn.textContent = "Failed - Try Again";
          }
        })
        .finally(function () {
          if (submitBtn) {
            setTimeout(function () {
              submitBtn.disabled = false;
              submitBtn.textContent = originalText;
              submitBtn.style.opacity = "";
              submitBtn.style.background = "";
              submitBtn.style.borderColor = "";
            }, 2500);
          }
        });
    });
  }

  var fclDetails = $("#fcl-details");
  $$('input[name="shipment_mode"]').forEach(function (radio) {
    radio.addEventListener("change", function () {
      if (fclDetails) {
        fclDetails.style.display = this.value === "FCL" ? "flex" : "none";
      }
    });
  });

  var revealEls = $$(".reveal, .reveal-stagger");
  if (revealEls.length && "IntersectionObserver" in window) {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("revealed");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );
    revealEls.forEach(function (el) {
      observer.observe(el);
    });
  } else {
    revealEls.forEach(function (el) {
      el.classList.add("revealed");
    });
  }

  var route = currentRoute();
  var activeKey = "";
  if (route.base === "/") {
    activeKey = "home";
  } else if (route.base === "/about.html") {
    activeKey = "about";
  } else if (route.base === "/contact.html") {
    activeKey = "contact";
  } else if (route.base.indexOf("/services/") === 0) {
    activeKey = "services";
  } else if (route.base.indexOf("/ports/") === 0) {
    activeKey = "ports";
  } else if (route.base.indexOf("/blog/") === 0) {
    activeKey = "blog";
  }

  $$("[data-nav-key]").forEach(function (link) {
    if (link.getAttribute("data-nav-key") === activeKey) {
      link.classList.add("nav-active-link");
    } else {
      link.classList.remove("nav-active-link");
    }
  });

  var sections = $$("section[id]");
  var navAnchors = $$('.nav-links a[href^="#"]');
  if (sections.length && navAnchors.length) {
    var anchorTicking = false;
    window.addEventListener("scroll", function () {
      if (!anchorTicking) {
        window.requestAnimationFrame(function () {
          var scrollPos = window.scrollY + 120;
          sections.forEach(function (section) {
            var top = section.offsetTop;
            var height = section.offsetHeight;
            var id = section.getAttribute("id");
            if (scrollPos >= top && scrollPos < top + height) {
              navAnchors.forEach(function (anchor) {
                anchor.classList.remove("nav-active-link");
                if (anchor.getAttribute("href") === "#" + id) {
                  anchor.classList.add("nav-active-link");
                }
              });
            }
          });
          anchorTicking = false;
        });
        anchorTicking = true;
      }
    });
  }
})();
