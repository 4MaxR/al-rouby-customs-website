#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate all HTML pages for Al-Rouby multi-page website."""
import os, sys

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public_html")

def ensure_dir(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

def write_file(rel_path, content):
    full = os.path.join(BASE, rel_path)
    ensure_dir(full)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Created: {rel_path}")

# ─── Shared HTML fragments ───

THEME_SCRIPT = '''    <script>
      (function(){
        var t = localStorage.getItem("theme");
        if (t === "dark") document.documentElement.style.colorScheme = "dark";
        if (t) document.body ? document.body.classList.add(t + "-mode") : document.addEventListener("DOMContentLoaded", function(){ document.body.classList.add(t + "-mode"); });
      })();
    </script>'''

def org_schema():
    return '''{
      "@context": "https://schema.org",
      "@type": "Organization",
      "name": "Al-Rouby Customs",
      "url": "https://al-rouby.com",
      "logo": "https://al-rouby.com/images/og-image.jpg",
      "contactPoint": {
        "@type": "ContactPoint",
        "telephone": "+201000628855",
        "contactType": "customer service",
        "availableLanguage": ["English", "Arabic"]
      },
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Building 615, TEDA",
        "addressLocality": "Ain Sokhna",
        "addressRegion": "Suez",
        "addressCountry": "EG"
      },
      "sameAs": [
        "https://www.facebook.com/RisElRouby",
        "https://www.linkedin.com/company/al-rouby/"
      ]
    }'''

def breadcrumb_schema(items):
    """items = [(name, url), ...] last item has no url"""
    parts = []
    for i, item in enumerate(items, 1):
        if i < len(items):
            parts.append(f'{{"@type":"ListItem","position":{i},"name":"{item[0]}","item":"https://al-rouby.com{item[1]}"}}')
        else:
            parts.append(f'{{"@type":"ListItem","position":{i},"name":"{item[0]}"}}')
    return f'{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{",".join(parts)}]}}'

def service_schema(service_type, description):
    return f'''{{"@context":"https://schema.org","@type":"Service","serviceType":"{service_type}","provider":{{"@type":"Organization","name":"Al-Rouby Customs"}},"areaServed":{{"@type":"Country","name":"Egypt"}},"description":"{description}"}}'''

def faq_schema(faqs):
    """faqs = [(q, a), ...]"""
    items = []
    for q, a in faqs:
        items.append(f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}')
    return f'{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{",".join(items)}]}}'

def en_nav(active=""):
    act = lambda name: ' class="nav-active-link"' if name == active else ""
    return f'''    <header>
      <div class="nav-container">
        <a class="logo" href="/">Al-Rouby Customs</a>
        <button class="hamburger" id="menuBtn" aria-label="Toggle navigation menu" aria-expanded="false" aria-controls="navLinks">&#9776;</button>
        <nav class="nav-links" id="navLinks" role="navigation" aria-label="Main navigation">
          <a href="/"{act("home")}>Home</a>
          <div class="nav-dropdown">
            <a href="/services/customs-clearance.html"{act("services")}>Services <span class="dropdown-arrow" aria-hidden="true">&#9660;</span></a>
            <div class="dropdown-menu">
              <a href="/services/customs-clearance.html">Customs Clearance</a>
              <a href="/services/freight-forwarding.html">Freight Forwarding</a>
              <a href="/services/shipping.html">Shipping</a>
              <a href="/services/logistics.html">Logistics</a>
              <a href="/services/aci-nafeza.html">ACI &amp; Nafeza</a>
            </div>
          </div>
          <div class="nav-dropdown">
            <a href="/ports/ain-sokhna.html"{act("ports")}>Ports <span class="dropdown-arrow" aria-hidden="true">&#9660;</span></a>
            <div class="dropdown-menu">
              <a href="/ports/ain-sokhna.html">Ain Sokhna</a>
              <a href="/ports/alexandria.html">Alexandria</a>
              <a href="/ports/sczone.html">SCZone</a>
            </div>
          </div>
          <a href="/blog/customs-clearance-guide-egypt.html"{act("blog")}>Blog</a>
          <a href="/contact.html"{act("contact")}>Contact</a>
          <a href="/ar/" class="lang-switch" aria-label="Switch to Arabic">&#1593;&#1585;&#1576;&#1610;</a>
          <a href="/zh/" class="lang-switch" aria-label="Switch to Chinese">&#20013;&#25991;</a>
          <button id="themeToggle" class="theme-toggle" aria-label="Toggle dark mode">&#127769;</button>
          <a href="/#quote" class="btn btn-primary btn-nav">Request Quote</a>
        </nav>
      </div>
    </header>'''

def en_footer():
    return '''    <footer>
      <div class="footer-grid">
        <div class="footer-col">
          <h3>Al-Rouby Customs</h3>
          <p class="footer-about">Your reliable partner in Egyptian customs clearance and logistics. Fast, transparent, and legally compliant.</p>
        </div>
        <div class="footer-col">
          <h4>Services</h4>
          <ul>
            <li><a href="/services/customs-clearance.html">Customs Clearance</a></li>
            <li><a href="/services/freight-forwarding.html">Freight Forwarding</a></li>
            <li><a href="/services/shipping.html">Shipping</a></li>
            <li><a href="/services/logistics.html">Logistics</a></li>
            <li><a href="/services/aci-nafeza.html">ACI &amp; Nafeza</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Ports</h4>
          <ul>
            <li><a href="/ports/ain-sokhna.html">Ain Sokhna Port</a></li>
            <li><a href="/ports/alexandria.html">Alexandria Port</a></li>
            <li><a href="/ports/sczone.html">SCZone</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Contact</h4>
          <ul>
            <li><a href="mailto:info@al-rouby.com">info@al-rouby.com</a></li>
            <li><a href="tel:+201000628855">+20 100 062 8855</a></li>
            <li><a href="https://maps.app.goo.gl/RsDBzG56XkLNRWNFA" target="_blank" rel="noopener noreferrer">Ain Sokhna, Suez, Egypt</a></li>
            <li><a href="https://www.facebook.com/RisElRouby" target="_blank" rel="noopener noreferrer">Facebook</a></li>
            <li><a href="https://www.linkedin.com/company/al-rouby/" target="_blank" rel="noopener noreferrer">LinkedIn</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p class="footer-copyright">&copy; 2026 Al-Rouby Customs. All rights reserved.</p>
        <p class="footer-credit">Design &amp; Development by <a href="https://alroubyds.com" target="_blank" rel="noopener noreferrer">Alrouby Digital Studio</a></p>
      </div>
    </footer>
    <button id="backToTop" class="back-to-top" aria-label="Back to top">&uarr;</button>
    <script src="/js/main.js" defer></script>'''

def en_head(title, desc, canonical, og_title=None, hreflang_ar=None):
    og_t = og_title or title
    hreflang = f'''    <link rel="alternate" hreflang="en" href="https://al-rouby.com{canonical}"> <!-- CANONICAL_DOMAIN -->
    <link rel="alternate" hreflang="x-default" href="https://al-rouby.com{canonical}"> <!-- CANONICAL_DOMAIN -->'''
    if hreflang_ar:
        hreflang += f'\n    <link rel="alternate" hreflang="ar" href="https://al-rouby.com{hreflang_ar}"> <!-- CANONICAL_DOMAIN -->'
    return f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <meta name="author" content="Al-Rouby Customs">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://al-rouby.com{canonical}"> <!-- CANONICAL_DOMAIN -->
{hreflang}
    <meta property="og:site_name" content="Al-Rouby Customs">
    <meta property="og:title" content="{og_t}">
    <meta property="og:description" content="{desc}">
    <meta property="og:url" content="https://al-rouby.com{canonical}"> <!-- CANONICAL_DOMAIN -->
    <meta property="og:type" content="website">
    <meta property="og:image" content="https://al-rouby.com/images/og-image.jpg"> <!-- CANONICAL_DOMAIN -->
    <meta property="og:locale" content="en_US">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{og_t}">
    <meta name="twitter:description" content="{desc}">
    <meta name="twitter:image" content="https://al-rouby.com/images/og-image.jpg"> <!-- CANONICAL_DOMAIN -->
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
    <meta name="theme-color" content="#0b1f3a">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap" rel="stylesheet">
{THEME_SCRIPT}
    <link rel="stylesheet" href="/css/style.css">'''

def en_breadcrumb_html(items):
    """items = [(label, url), ...] last has no link"""
    html = '    <nav class="breadcrumbs" aria-label="Breadcrumb"><ol>'
    for i, item in enumerate(items):
        if i < len(items) - 1:
            html += f'<li><a href="{item[1]}">{item[0]}</a></li>'
        else:
            html += f'<li><span aria-current="page">{item[0]}</span></li>'
    html += '</ol></nav>'
    return html

# ─── Arabic fragments ───

def ar_nav(active=""):
    act = lambda name: ' class="nav-active-link"' if name == active else ""
    return f'''    <header>
      <div class="nav-container">
        <a class="logo" href="/ar/">الروبي للتخليص الجمركي</a>
        <button class="hamburger" id="menuBtn" aria-label="قائمة التصفح" aria-expanded="false" aria-controls="navLinks">&#9776;</button>
        <nav class="nav-links" id="navLinks" role="navigation" aria-label="التنقل الرئيسي">
          <a href="/ar/"{act("home")}>الرئيسية</a>
          <div class="nav-dropdown">
            <a href="/ar/services/customs-clearance.html"{act("services")}>خدماتنا <span class="dropdown-arrow" aria-hidden="true">&#9660;</span></a>
            <div class="dropdown-menu">
              <a href="/ar/services/customs-clearance.html">التخليص الجمركي</a>
              <a href="/ar/services/freight-forwarding.html">الشحن والتوصيل</a>
              <a href="/ar/services/shipping.html">الشحن البحري</a>
              <a href="/ar/services/logistics.html">الخدمات اللوجستية</a>
              <a href="/ar/services/aci-nafeza.html">ACI ونافذة</a>
            </div>
          </div>
          <div class="nav-dropdown">
            <a href="/ar/ports/ain-sokhna.html"{act("ports")}>الموانئ <span class="dropdown-arrow" aria-hidden="true">&#9660;</span></a>
            <div class="dropdown-menu">
              <a href="/ar/ports/ain-sokhna.html">ميناء العين السخنة</a>
              <a href="/ar/ports/alexandria.html">ميناء الإسكندرية</a>
              <a href="/ar/ports/sczone.html">المنطقة الاقتصادية</a>
            </div>
          </div>
          <a href="/ar/#contact"{act("contact")}>اتصل بنا</a>
          <a href="/" class="lang-switch" aria-label="Switch to English">En</a>
          <a href="/zh/" class="lang-switch" aria-label="Switch to Chinese">中文</a>
          <button id="themeToggle" class="theme-toggle" aria-label="تبديل الوضع الليلي">&#127769;</button>
          <a href="/ar/#quote" class="btn btn-primary btn-nav">اطلب عرض سعر</a>
        </nav>
      </div>
    </header>'''

def ar_footer():
    return '''    <footer>
      <div class="footer-grid">
        <div class="footer-col">
          <h3>الروبي للتخليص الجمركي</h3>
          <p class="footer-about">شريكك الموثوق في التخليص الجمركي واللوجستيات في مصر. سرعة، شفافية، والتزام قانوني تام.</p>
        </div>
        <div class="footer-col">
          <h4>خدمات</h4>
          <ul>
            <li><a href="/ar/services/customs-clearance.html">تخليص جمركي</a></li>
            <li><a href="/ar/services/freight-forwarding.html">الشحن والتوصيل</a></li>
            <li><a href="/ar/services/shipping.html">الشحن البحري</a></li>
            <li><a href="/ar/services/logistics.html">الخدمات اللوجستية</a></li>
            <li><a href="/ar/services/aci-nafeza.html">ACI ونافذة</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>الموانئ</h4>
          <ul>
            <li><a href="/ar/ports/ain-sokhna.html">ميناء العين السخنة</a></li>
            <li><a href="/ar/ports/alexandria.html">ميناء الإسكندرية</a></li>
            <li><a href="/ar/ports/sczone.html">المنطقة الاقتصادية</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>تواصل</h4>
          <ul>
            <li><a href="mailto:info@al-rouby.com">info@al-rouby.com</a></li>
            <li><a href="tel:+201000628855" dir="ltr">+20 100 062 8855</a></li>
            <li><a href="https://maps.app.goo.gl/RsDBzG56XkLNRWNFA" target="_blank" rel="noopener noreferrer">العين السخنة، السويس، مصر</a></li>
            <li><a href="https://www.facebook.com/RisElRouby" target="_blank" rel="noopener noreferrer">Facebook</a></li>
            <li><a href="https://www.linkedin.com/company/al-rouby/" target="_blank" rel="noopener noreferrer">LinkedIn</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p class="footer-copyright">&copy; 2026 الروبي للتخليص الجمركي. جميع الحقوق محفوظة.</p>
        <p class="footer-credit">تصميم وتطوير <a href="https://alroubyds.com" target="_blank" rel="noopener noreferrer">Alrouby Digital Studio</a></p>
      </div>
    </footer>
    <button id="backToTop" class="back-to-top" aria-label="العودة للأعلى">&uarr;</button>
    <script src="/js/main.js" defer></script>'''

def ar_head(title, desc, canonical, hreflang_en=None):
    hreflang = f'''    <link rel="alternate" hreflang="ar" href="https://al-rouby.com{canonical}"> <!-- CANONICAL_DOMAIN -->'''
    if hreflang_en:
        hreflang += f'\n    <link rel="alternate" hreflang="en" href="https://al-rouby.com{hreflang_en}"> <!-- CANONICAL_DOMAIN -->'
        hreflang += f'\n    <link rel="alternate" hreflang="x-default" href="https://al-rouby.com{hreflang_en}"> <!-- CANONICAL_DOMAIN -->'
    return f'''<!doctype html>
<html lang="ar" dir="rtl">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <meta name="author" content="الروبي للتخليص الجمركي">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://al-rouby.com{canonical}"> <!-- CANONICAL_DOMAIN -->
{hreflang}
    <meta property="og:site_name" content="الروبي للتخليص الجمركي">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:url" content="https://al-rouby.com{canonical}"> <!-- CANONICAL_DOMAIN -->
    <meta property="og:type" content="website">
    <meta property="og:image" content="https://al-rouby.com/images/og-image.jpg"> <!-- CANONICAL_DOMAIN -->
    <meta property="og:locale" content="ar_EG">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{desc}">
    <meta name="twitter:image" content="https://al-rouby.com/images/og-image.jpg"> <!-- CANONICAL_DOMAIN -->
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
    <meta name="theme-color" content="#0b1f3a">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap" rel="stylesheet">
{THEME_SCRIPT}
    <link rel="stylesheet" href="/css/style.css">'''

def ar_breadcrumb_html(items):
    html = '    <nav class="breadcrumbs" aria-label="مسار التصفح"><ol>'
    for i, item in enumerate(items):
        if i < len(items) - 1:
            html += f'<li><a href="{item[1]}">{item[0]}</a></li>'
        else:
            html += f'<li><span aria-current="page">{item[0]}</span></li>'
    html += '</ol></nav>'
    return html

# ════════════════════════════════════════════
# PAGE GENERATORS
# ════════════════════════════════════════════

def gen_homepage():
    print("Generating: index.html")
    write_file("index.html", f'''{en_head(
        "Al-Rouby Customs | Customs Clearance &amp; Logistics in Egypt",
        "Al-Rouby Customs provides expert customs clearance, freight forwarding, and logistics across all Egyptian ports including Ain Sokhna, Alexandria, and SCZone. 27+ years experience. Get a free quote.",
        "/",
        hreflang_ar="/ar/"
    )}
    <script type="application/ld+json">{org_schema()}</script>
    <script type="application/ld+json">{{
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "Al-Rouby Customs",
      "alternateName": "الروبي للتخليص الجمركي",
      "description": "Customs clearance services across all Egyptian ports with full ACI & Nafeza support.",
      "url": "https://al-rouby.com",
      "telephone": "+201000628855",
      "email": "info@al-rouby.com",
      "address": {{
        "@type": "PostalAddress",
        "streetAddress": "Building 615, TEDA",
        "addressLocality": "Ain Sokhna",
        "addressRegion": "Suez",
        "addressCountry": "EG"
      }},
      "geo": {{ "@type": "GeoCoordinates", "latitude": 29.5944, "longitude": 32.3296 }},
      "openingHoursSpecification": {{
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Sunday","Monday","Tuesday","Wednesday","Thursday"],
        "opens": "08:00", "closes": "17:00"
      }},
      "sameAs": ["https://www.facebook.com/RisElRouby","https://www.linkedin.com/company/al-rouby/"],
      "image": "https://al-rouby.com/images/og-image.jpg",
      "priceRange": "$$",
      "areaServed": {{ "@type": "Country", "name": "Egypt" }},
      "serviceType": ["Customs Clearance","Freight Forwarding","Logistics","ACI Filing"]
    }}</script>
    <script type="application/ld+json">{faq_schema([
        ("How long does customs clearance take in Egypt?", "Typically 3-5 business days from vessel discharge, provided all documents are correct and complete."),
        ("Do you handle ACI submissions?", "Yes, we provide full support for ACI system registration and ACID number generation."),
        ("What documents are required for customs clearance?", "Commercial Invoice, Packing List, Bill of Lading, and Certificate of Origin. Additional permits may be needed depending on cargo type."),
        ("Which Egyptian ports do you cover?", "All major ports including Ain Sokhna, Alexandria, Dekheila, Damietta, Port Said, Adabiya, Port Tawfiq, and SCZone."),
        ("Do you offer SCZone clearance?", "Yes, we are fully licensed for clearance within the Suez Canal Economic Zone including free zone and investment law procedures.")
    ])}</script>
  </head>
  <body id="top">
    <a class="skip-link" href="#main">Skip to content</a>
{en_nav("home")}
    <main id="main">
      <section class="container hero">
        <div class="hero-content reveal">
          <h1>Customs Clearance Across Egypt's Ports &mdash; Fast, Compliant, Reliable</h1>
          <p>Your trusted partner for hassle-free customs clearance and logistics solutions. We ensure your shipments move smoothly through Egyptian ports.</p>
          <p class="service-summary">Al-Rouby Customs specializes in customs clearance, regulatory compliance, documentation handling, port operations support, and inland logistics coordination across all major Egyptian ports &mdash; helping importers, exporters, and manufacturers move cargo with accuracy and speed.</p>
          <div class="hero-buttons">
            <a href="#quote" class="btn btn-primary">Request a Quote</a>
            <a href="https://wa.me/201000628855?text=Hello%20Al-Rouby%20Customs%2C%20I%27d%20like%20to%20request%20a%20quote%20for%20a%20shipment." target="_blank" rel="noopener noreferrer" class="btn btn-secondary">WhatsApp Us</a>
          </div>
        </div>
        <div class="hero-card reveal">
          <h3>At a Glance</h3>
          <ul>
            <li><span class="check-icon" aria-hidden="true">&#10004;</span> Full ACI &amp; Nafeza Support</li>
            <li><span class="check-icon" aria-hidden="true">&#10004;</span> Coverage: All Egyptian Ports</li>
            <li><span class="check-icon" aria-hidden="true">&#10004;</span> Avg. Clearance: 3&ndash;5 Days</li>
            <li><span class="check-icon" aria-hidden="true">&#10004;</span> Transparent Pricing</li>
          </ul>
        </div>
      </section>

      <section class="trust">
        <div class="container">
          <div class="trust-grid reveal-stagger">
            <div class="trust-item"><h3>+27</h3><p>Years Experience</p></div>
            <div class="trust-item"><h3>12,000+</h3><p>Shipments Handled</p></div>
            <div class="trust-item"><h3>100%</h3><p>ACI Compliant</p></div>
            <div class="trust-item"><h3>24/7</h3><p>Client Support</p></div>
          </div>
        </div>
      </section>

      <section id="services" class="services">
        <div class="container">
          <div class="section-header reveal">
            <h2>Our Core Services</h2>
            <p>Comprehensive logistics solutions tailored for importers and factory owners.</p>
          </div>
          <div class="services-grid reveal-stagger">
            <article class="service-card">
              <div class="service-icon" aria-hidden="true">&#128674;</div>
              <h3>Customs Clearance</h3>
              <p>Expert handling of import/export formalities, ensuring speed and compliance with Egyptian laws.</p>
              <a href="/services/customs-clearance.html" class="service-link">Learn More &rarr;</a>
            </article>
            <article class="service-card">
              <div class="service-icon" aria-hidden="true">&#128667;</div>
              <h3>Freight Forwarding</h3>
              <p>Seamless transportation from the port to your warehouse. We manage the logistics so you don't have to.</p>
              <a href="/services/freight-forwarding.html" class="service-link">Learn More &rarr;</a>
            </article>
            <article class="service-card">
              <div class="service-icon" aria-hidden="true">&#128228;</div>
              <h3>Shipping to Egypt</h3>
              <p>International container shipping, LCL and FCL options, with full customs clearance included.</p>
              <a href="/services/shipping.html" class="service-link">Learn More &rarr;</a>
            </article>
            <article class="service-card">
              <div class="service-icon" aria-hidden="true">&#128230;</div>
              <h3>Logistics Solutions</h3>
              <p>End-to-end logistics from port operations and warehousing to inland transport coordination.</p>
              <a href="/services/logistics.html" class="service-link">Learn More &rarr;</a>
            </article>
            <article class="service-card">
              <div class="service-icon" aria-hidden="true">&#128196;</div>
              <h3>ACI &amp; Nafeza</h3>
              <p>Full support with ACI filing, ACID number generation, HS Code classification, and Nafeza platform operations.</p>
              <a href="/services/aci-nafeza.html" class="service-link">Learn More &rarr;</a>
            </article>
          </div>
        </div>
      </section>

      <section class="services" style="background: var(--bg-body);">
        <div class="container">
          <div class="section-header reveal">
            <h2>Port Coverage</h2>
            <p>We operate across all major Egyptian ports with on-the-ground expertise.</p>
          </div>
          <div class="ports-grid reveal-stagger">
            <article class="port-card">
              <h3>&#9875; Ain Sokhna Port</h3>
              <p>Our home base. Located in the TEDA zone with the fastest clearance times.</p>
              <a href="/ports/ain-sokhna.html" class="service-link">Learn More &rarr;</a>
            </article>
            <article class="port-card">
              <h3>&#9875; Alexandria &amp; Dekheila</h3>
              <p>Egypt's busiest Mediterranean port. Full import/export handling available.</p>
              <a href="/ports/alexandria.html" class="service-link">Learn More &rarr;</a>
            </article>
            <article class="port-card">
              <h3>&#9875; SCZone</h3>
              <p>Suez Canal Economic Zone. Licensed for free zone and investment law procedures.</p>
              <a href="/ports/sczone.html" class="service-link">Learn More &rarr;</a>
            </article>
          </div>
        </div>
      </section>

      <section id="process" class="process">
        <div class="container">
          <h2 class="reveal">Simple 3-Step Process</h2>
          <div class="process-steps reveal-stagger">
            <article class="step">
              <div class="step-number" aria-hidden="true">1</div>
              <h3>Send Documents</h3>
              <p>Provide us with your invoice and packing list. We review everything for compliance.</p>
            </article>
            <article class="step">
              <div class="step-number" aria-hidden="true">2</div>
              <h3>We Prepare &amp; Submit</h3>
              <p>We handle ACI filing and submit duties via the Nafeza platform immediately.</p>
            </article>
            <article class="step">
              <div class="step-number" aria-hidden="true">3</div>
              <h3>Clearance &amp; Delivery</h3>
              <p>Shipment is released and trucked directly to your specified location.</p>
            </article>
          </div>
        </div>
      </section>

      <section class="testimonials">
        <div class="container">
          <div class="section-header reveal"><h2>What Our Clients Say</h2></div>
          <div class="testimonial-grid reveal-stagger">
            <article class="review-card">
              <p>"Al-Rouby Customs saved us from huge demurrage fees. Fast and very professional."</p>
              <div class="client-info"><h4>Mr. Ahmed Atef</h4><span>Quality's Factory Owner</span></div>
            </article>
            <article class="review-card">
              <p>"The best experience regarding ACI filing. They handled everything seamlessly."</p>
              <div class="client-info"><h4>Mr. Hany Obeid</h4><span>The Point's Owner</span></div>
            </article>
            <article class="review-card">
              <p>"Transparent pricing and daily updates. Highly recommended for Sokhna port."</p>
              <div class="client-info"><h4>Mr. Mohamed Salah</h4><span>Textile Importer</span></div>
            </article>
          </div>
        </div>
      </section>

      <section id="faq">
        <div class="container faq-container reveal">
          <div class="section-header"><h2>Frequently Asked Questions</h2></div>
          <div class="faq-item">
            <button class="faq-question" type="button">How long does clearance take? <span aria-hidden="true">+</span></button>
            <div class="faq-answer"><p>Typically, clearance takes 3&ndash;5 business days from the moment the vessel discharges, provided all documents are correct.</p></div>
          </div>
          <div class="faq-item">
            <button class="faq-question" type="button">Do you handle ACI submissions? <span aria-hidden="true">+</span></button>
            <div class="faq-answer"><p>Yes, we provide full support for the Advanced Cargo Information (ACI) system registration and ACID number generation.</p></div>
          </div>
          <div class="faq-item">
            <button class="faq-question" type="button">What documents are required? <span aria-hidden="true">+</span></button>
            <div class="faq-answer"><p>Basic documents include Commercial Invoice, Packing List, Bill of Lading, and Certificate of Origin. Additional permits may be needed depending on the cargo.</p></div>
          </div>
          <div class="faq-item">
            <button class="faq-question" type="button">Which ports do you cover? <span aria-hidden="true">+</span></button>
            <div class="faq-answer"><p>We operate across all major Egyptian ports including Ain Sokhna, Alexandria, Dekheila, Damietta, Port Said, Adabiya, Port Tawfiq, and the Suez Canal Economic Zone (SCZone).</p></div>
          </div>
          <div class="faq-item">
            <button class="faq-question" type="button">Do you offer SCZone clearance? <span aria-hidden="true">+</span></button>
            <div class="faq-answer"><p>Yes, we are fully licensed and experienced in handling clearance within the Suez Canal Economic Zone, including free zone and investment law procedures.</p></div>
          </div>
        </div>
      </section>

      <section id="quote" class="quote">
        <div class="container quote-grid">
          <div class="quote-info reveal">
            <h2>Request a Quote</h2>
            <p>Send your shipment details and we'll reply with a clear, transparent quote.</p>
            <ul class="quote-points">
              <li><span class="check-icon" aria-hidden="true">&#10004;</span> Fast response within hours</li>
              <li><span class="check-icon" aria-hidden="true">&#10004;</span> Transparent, no-hidden-fees pricing</li>
              <li><span class="check-icon" aria-hidden="true">&#10004;</span> Full ACI / Nafeza support</li>
            </ul>
          </div>
          <form class="quote-form reveal" action="https://formspree.io/f/mreapbqn" method="post" novalidate>
            <div class="form-row">
              <label>Full Name <input type="text" name="name" placeholder="Your name" required autocomplete="name" minlength="2" maxlength="100"></label>
              <label>Phone / WhatsApp <input type="tel" name="phone" placeholder="+20 ..." required autocomplete="tel" pattern="[\\+]?[0-9\\s]{{10,20}}"></label>
            </div>
            <label>Email (optional) <input type="email" name="email" placeholder="you@email.com" autocomplete="email" maxlength="100"></label>
            <div class="form-row">
              <label>Customs Regime / Service
                <select name="service_type" required>
                  <option value="" selected disabled>Select Service Type...</option>
                  <optgroup label="Standard Clearance">
                    <option value="import_final">Final Import</option>
                    <option value="export">Export</option>
                    <option value="transit">Transit</option>
                  </optgroup>
                  <optgroup label="Special Regimes">
                    <option value="temporary_admission">Temporary Admission</option>
                    <option value="drawback">Drawback</option>
                    <option value="exemptions">Exemptions (Investment/Diplomatic)</option>
                  </optgroup>
                  <optgroup label="Economic Zones">
                    <option value="sczone">SCZone (Suez Canal Economic Zone)</option>
                    <option value="free_zone">Free Zone</option>
                  </optgroup>
                </select>
              </label>
              <label>Port / Location
                <select name="port" required>
                  <option value="" selected disabled>Select Port...</option>
                  <optgroup label="Red Sea Ports">
                    <option value="ain-sokhna">Ain Sokhna</option>
                    <option value="adabiya">Adabiya</option>
                    <option value="port-tawfiq">Port Tawfiq</option>
                  </optgroup>
                  <optgroup label="Mediterranean Ports">
                    <option value="alexandria">Alexandria / Dekheila</option>
                    <option value="damietta">Damietta</option>
                    <option value="port-said">Port Said (East/West)</option>
                  </optgroup>
                  <optgroup label="Air Freight">
                    <option value="cairo_airport">Cairo Airport (CAI)</option>
                  </optgroup>
                </select>
              </label>
            </div>
            <div class="shipment-mode-box">
              <label class="shipment-label">Shipment Mode</label>
              <div class="radio-group">
                <label class="radio-item"><input type="radio" name="shipment_mode" value="FCL"> Full Container (FCL)</label>
                <label class="radio-item"><input type="radio" name="shipment_mode" value="LCL"> Less than Container (LCL)</label>
              </div>
              <div id="fcl-details">
                <div class="container-input-col"><label>20ft Container Count</label><input type="number" name="containers_20ft" placeholder="0" min="0"></div>
                <div class="container-input-col"><label>40ft Container Count</label><input type="number" name="containers_40ft" placeholder="0" min="0"></div>
              </div>
            </div>
            <label>Message <textarea name="message" rows="4" placeholder="Cargo description, ETA, documents..." required maxlength="1000"></textarea></label>
            <button type="submit" class="btn btn-accent btn-submit">Send Request</button>
            <p class="form-note">By submitting, you agree to be contacted regarding your request.</p>
          </form>
        </div>
      </section>

      <section class="final-cta">
        <h2 class="reveal">Ready to Simplify Your Logistics?</h2>
        <p class="reveal">Get a fast, accurate quote for your next shipment today.</p>
        <div class="cta-buttons reveal">
          <a href="#quote" class="btn btn-accent">Request Quote</a>
          <a href="https://wa.me/201000628855?text=Hello%20Al-Rouby%20Customs%2C%20I%27d%20like%20to%20request%20a%20quote%20for%20a%20shipment." target="_blank" rel="noopener noreferrer" class="btn btn-white">WhatsApp</a>
        </div>
      </section>

      <section id="contact" class="contact">
        <div class="container">
          <div class="section-header reveal"><h2>Contact Us</h2><p>Reach us anytime &mdash; we respond fast.</p></div>
          <div class="contact-grid reveal-stagger">
            <div class="contact-card"><h3>Email</h3><p><a href="mailto:info@al-rouby.com">info@al-rouby.com</a></p></div>
            <div class="contact-card"><h3>Phone / WhatsApp</h3><p><a href="tel:+201000628855">+20 100 062 8855</a></p></div>
            <div class="contact-card"><h3>Location</h3><p><a href="https://maps.app.goo.gl/RsDBzG56XkLNRWNFA" target="_blank" rel="noopener noreferrer">Building 615, TEDA, Ain Sokhna, Suez, Egypt</a></p></div>
          </div>
        </div>
      </section>
    </main>
{en_footer()}
  </body>
</html>''')

def gen_404():
    print("Generating: 404.html")
    write_file("404.html", f'''{en_head(
        "Page Not Found | Al-Rouby Customs",
        "The page you are looking for could not be found. Browse our customs clearance and logistics services.",
        "/404.html"
    )}
    <script type="application/ld+json">{org_schema()}</script>
  </head>
  <body>
    <a class="skip-link" href="#main">Skip to content</a>
{en_nav()}
    <main id="main">
      <section class="error-page">
        <div class="container">
          <h1>404</h1>
          <h2>Page Not Found</h2>
          <p>Sorry, the page you are looking for does not exist or has been moved.</p>
          <p dir="rtl" lang="ar">عذراً، الصفحة التي تبحث عنها غير موجودة.</p>
          <div class="error-links">
            <a href="/" class="btn btn-primary">Go to Homepage</a>
            <a href="/services/customs-clearance.html" class="btn btn-secondary">Our Services</a>
            <a href="/contact.html" class="btn btn-secondary">Contact Us</a>
          </div>
        </div>
      </section>
    </main>
{en_footer()}
  </body>
</html>''')

def gen_contact():
    print("Generating: contact.html")
    write_file("contact.html", f'''{en_head(
        "Contact Al-Rouby Customs | Get in Touch",
        "Contact Al-Rouby Customs for customs clearance quotes, logistics inquiries, and shipping support. Phone, email, WhatsApp available 24/7.",
        "/contact.html",
        hreflang_ar="/ar/"
    )}
    <script type="application/ld+json">{org_schema()}</script>
    <script type="application/ld+json">{breadcrumb_schema([("Home", "/"), ("Contact", "")])}</script>
  </head>
  <body>
    <a class="skip-link" href="#main">Skip to content</a>
{en_nav("contact")}
{en_breadcrumb_html([("Home", "/"), ("Contact",)])}
    <main id="main">
      <section class="page-hero">
        <div class="container reveal">
          <h1>Contact Al-Rouby Customs</h1>
          <p>Reach us anytime for quotes, inquiries, or support. We respond fast and we are available 24/7 via phone and WhatsApp.</p>
        </div>
      </section>
      <section class="contact">
        <div class="container">
          <div class="contact-grid reveal-stagger">
            <div class="contact-card"><h3>Email</h3><p><a href="mailto:info@al-rouby.com">info@al-rouby.com</a></p></div>
            <div class="contact-card"><h3>Phone / WhatsApp</h3><p><a href="tel:+201000628855">+20 100 062 8855</a></p></div>
            <div class="contact-card"><h3>Location</h3><p><a href="https://maps.app.goo.gl/RsDBzG56XkLNRWNFA" target="_blank" rel="noopener noreferrer">Building 615, TEDA, Ain Sokhna, Suez, Egypt</a></p></div>
          </div>
          <div class="cta-box reveal" style="margin-top:3rem;">
            <h3>Request a Quote</h3>
            <p>Send us your shipment details and receive a transparent quote within hours.</p>
            <a href="/#quote" class="btn btn-accent">Go to Quote Form</a>
          </div>
        </div>
      </section>
    </main>
{en_footer()}
  </body>
</html>''')

def gen_about():
    print("Generating: about.html")
    write_file("about.html", f'''{en_head(
        "About Al-Rouby Customs | 27+ Years in Egyptian Logistics",
        "Learn about Al-Rouby Customs - over 27 years of customs clearance experience across all Egyptian ports. Our mission, team, and commitment to excellence.",
        "/about.html",
        hreflang_ar="/ar/"
    )}
    <script type="application/ld+json">{org_schema()}</script>
    <script type="application/ld+json">{breadcrumb_schema([("Home", "/"), ("About", "")])}</script>
  </head>
  <body>
    <a class="skip-link" href="#main">Skip to content</a>
{en_nav()}
{en_breadcrumb_html([("Home", "/"), ("About",)])}
    <main id="main">
      <section class="page-hero">
        <div class="container reveal">
          <h1>About Al-Rouby Customs</h1>
          <p>Over 27 years of trusted customs clearance and logistics services across all Egyptian ports.</p>
        </div>
      </section>
      <section class="content-section">
        <div class="container">
          <h2 class="reveal">Our Story</h2>
          <p class="reveal">Founded in 1999, Al-Rouby Customs has grown from a single-office operation in Ain Sokhna to become one of Egypt's most trusted customs clearance providers. With over 27 years of hands-on experience and more than 12,000 shipments successfully handled, we bring deep expertise to every cargo we manage.</p>
          <p class="reveal">Our headquarters are located in the TEDA zone at Ain Sokhna Port, giving us direct access to one of Egypt's busiest Red Sea ports. From this strategic location, we coordinate clearance operations across all major Egyptian ports.</p>
          <h2 class="reveal">Our Mission</h2>
          <p class="reveal">To simplify international trade for businesses operating in Egypt by providing fast, transparent, and fully compliant customs clearance and logistics services. We believe every importer and exporter deserves a partner who communicates clearly, acts quickly, and delivers results.</p>
          <h2 class="reveal">Why Choose Al-Rouby</h2>
          <div class="service-features reveal-stagger">
            <div class="feature-item"><h3>27+ Years Experience</h3><p>Deep expertise in Egyptian customs regulations, port operations, and trade compliance.</p></div>
            <div class="feature-item"><h3>All Ports Covered</h3><p>Operations at Ain Sokhna, Alexandria, Dekheila, Damietta, Port Said, Adabiya, and SCZone.</p></div>
            <div class="feature-item"><h3>100% ACI Compliant</h3><p>Full support for Egypt's Advanced Cargo Information system and Nafeza platform.</p></div>
            <div class="feature-item"><h3>Transparent Pricing</h3><p>No hidden fees. Clear quotes with full cost breakdowns before we start.</p></div>
          </div>
          <div class="cta-box reveal">
            <h3>Ready to Work With Us?</h3>
            <p>Get a transparent quote for your next shipment.</p>
            <a href="/#quote" class="btn btn-accent">Request a Quote</a>
          </div>
        </div>
      </section>
    </main>
{en_footer()}
  </body>
</html>''')

# ─── Run all generators ───

if __name__ == "__main__":
    print("=" * 50)
    print("Generating Al-Rouby Multi-Page Website")
    print("=" * 50)
    gen_homepage()
    gen_404()
    gen_contact()
    gen_about()
    print("\nBatch 1 complete (homepage, 404, contact, about)")
