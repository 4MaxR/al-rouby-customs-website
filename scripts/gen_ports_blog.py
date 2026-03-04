#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate port pages and blog pages."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_pages import *

def gen_ain_sokhna():
    print("Generating: ports/ain-sokhna.html")
    write_file("ports/ain-sokhna.html", f'''{en_head(
        "Ain Sokhna Port Customs Clearance | Al-Rouby",
        "Expert customs clearance at Ain Sokhna Port. Located in TEDA zone. Fast clearance, competitive rates. Your trusted Sokhna port agent.",
        "/ports/ain-sokhna.html",
        hreflang_ar="/ar/ports/ain-sokhna.html"
    )}
    <script type="application/ld+json">{org_schema()}</script>
    <script type="application/ld+json">{breadcrumb_schema([("Home", "/"), ("Ports", "/ports/ain-sokhna.html"), ("Ain Sokhna Port", "")])}</script>
  </head>
  <body>
    <a class="skip-link" href="#main">Skip to content</a>
{en_nav("ports")}
{en_breadcrumb_html([("Home", "/"), ("Ports", "/ports/ain-sokhna.html"), ("Ain Sokhna Port",)])}
    <main id="main">
      <section class="page-hero">
        <div class="container reveal">
          <h1>Ain Sokhna Port Customs Clearance</h1>
          <p>Our home base. Located directly in the TEDA zone at Ain Sokhna, we offer the fastest customs clearance times on Egypt's Red Sea coast.</p>
        </div>
      </section>
      <section class="content-section">
        <div class="container">
          <h2 class="reveal">About Ain Sokhna Port</h2>
          <p class="reveal">Ain Sokhna Port, located on the western shore of the Gulf of Suez approximately 120 km east of Cairo, is one of Egypt's fastest-growing commercial ports. Situated within the TEDA (Tianjin Economic-Technological Development Area) industrial zone, Port Sokhna serves as a major gateway for cargo arriving from Asia, the Indian subcontinent, and East Africa.</p>
          <p class="reveal">The port's strategic location at the southern entrance of the Suez Canal makes it an ideal entry point for goods destined for the greater Cairo region, Upper Egypt, and the Suez Canal Economic Zone. With modern container terminals and expanding capacity, Ain Sokhna handles an increasing share of Egypt's import and export traffic.</p>

          <h2 class="reveal">Our Services at Ain Sokhna</h2>
          <div class="service-features reveal-stagger">
            <div class="feature-item"><h3>Customs Clearance</h3><p>Fast-track customs processing with our on-site team. Average clearance time of 3-5 business days, among the fastest at any Egyptian port.</p></div>
            <div class="feature-item"><h3>ACI &amp; Nafeza Support</h3><p>Complete pre-registration and Nafeza platform operations for all shipments arriving at Ain Sokhna.</p></div>
            <div class="feature-item"><h3>Inland Transport</h3><p>Trucking coordination from Ain Sokhna to Cairo, 10th of Ramadan City, 6th of October City, and all Egyptian destinations.</p></div>
            <div class="feature-item"><h3>SCZone Clearance</h3><p>Specialized clearance for cargo entering or exiting the Suez Canal Economic Zone adjacent to Ain Sokhna.</p></div>
          </div>

          <h2 class="reveal">Why Al-Rouby at Ain Sokhna</h2>
          <p class="reveal">Our headquarters are located at Building 615 in the TEDA zone, giving us direct, daily access to Ain Sokhna Port facilities. This physical proximity means faster document processing, immediate issue resolution, and the shortest possible clearance times. With 27+ years of experience at this port, we have established relationships with all relevant authorities and terminal operators.</p>
          <!-- TODO: Client should add more port-specific content here, such as specific terminal information, typical cargo types, and seasonal considerations -->

          <div class="cta-box reveal">
            <h3>Clear Your Cargo at Ain Sokhna</h3>
            <p>Get a fast, transparent quote for customs clearance at Port Sokhna.</p>
            <a href="/#quote" class="btn btn-accent">Request a Quote</a>
          </div>
        </div>
      </section>
      <section class="related-services">
        <div class="container">
          <div class="section-header reveal"><h2>Related Pages</h2></div>
          <div class="related-grid reveal-stagger">
            <div class="related-card"><h3>Customs Clearance</h3><p>Our complete customs clearance services.</p><a href="/services/customs-clearance.html">Learn More &rarr;</a></div>
            <div class="related-card"><h3>SCZone</h3><p>Suez Canal Economic Zone clearance.</p><a href="/ports/sczone.html">Learn More &rarr;</a></div>
            <div class="related-card"><h3>ACI &amp; Nafeza</h3><p>Pre-shipment registration.</p><a href="/services/aci-nafeza.html">Learn More &rarr;</a></div>
          </div>
        </div>
      </section>
    </main>
''' + en_footer() + '''
  </body>
</html>''')

def gen_alexandria():
    print("Generating: ports/alexandria.html")
    write_file("ports/alexandria.html", f'''{en_head(
        "Alexandria Port Customs Clearance | Al-Rouby",
        "Professional customs clearance at Alexandria &amp; Dekheila ports. Import/export handling, documentation, transport coordination.",
        "/ports/alexandria.html",
        hreflang_ar="/ar/ports/alexandria.html"
    )}
    <script type="application/ld+json">{org_schema()}</script>
    <script type="application/ld+json">{breadcrumb_schema([("Home", "/"), ("Ports", "/ports/ain-sokhna.html"), ("Alexandria Port", "")])}</script>
  </head>
  <body>
    <a class="skip-link" href="#main">Skip to content</a>
{en_nav("ports")}
{en_breadcrumb_html([("Home", "/"), ("Ports", "/ports/ain-sokhna.html"), ("Alexandria Port",)])}
    <main id="main">
      <section class="page-hero">
        <div class="container reveal">
          <h1>Alexandria Port Customs Clearance</h1>
          <p>Professional customs clearance at Egypt's busiest Mediterranean port. Full import/export handling at Alexandria and Dekheila.</p>
        </div>
      </section>
      <section class="content-section">
        <div class="container">
          <h2 class="reveal">About Alexandria &amp; Dekheila Ports</h2>
          <p class="reveal">Alexandria Port is Egypt's primary Mediterranean gateway and one of the oldest ports in the world. Together with the adjacent Dekheila Port, it handles the majority of Egypt's trade with Europe, North Africa, and the Americas. The port complex serves importers and exporters across northern Egypt, the Delta region, and beyond.</p>
          <p class="reveal">Al-Rouby Customs provides full customs clearance services at both Alexandria and Dekheila terminals. Our experienced team handles all types of cargo including containerized goods, bulk commodities, and breakbulk shipments.</p>

          <h2 class="reveal">Our Services at Alexandria</h2>
          <div class="service-features reveal-stagger">
            <div class="feature-item"><h3>Import Clearance</h3><p>Complete processing for goods arriving at Alexandria and Dekheila, from documentation to release and delivery.</p></div>
            <div class="feature-item"><h3>Export Procedures</h3><p>Streamlined export processing including customs declarations and coordination with shipping lines.</p></div>
            <div class="feature-item"><h3>Documentation</h3><p>Full document handling including ACI registration, banking documents, and certificates.</p></div>
            <div class="feature-item"><h3>Transport Coordination</h3><p>Inland delivery from Alexandria to Cairo, Delta cities, and Upper Egypt.</p></div>
          </div>
          <!-- TODO: Client should add more port-specific content here -->

          <div class="cta-box reveal">
            <h3>Clear Your Cargo at Alexandria</h3>
            <p>Get a quote for customs clearance at Alexandria or Dekheila port.</p>
            <a href="/#quote" class="btn btn-accent">Request a Quote</a>
          </div>
        </div>
      </section>
      <section class="related-services">
        <div class="container">
          <div class="section-header reveal"><h2>Related Pages</h2></div>
          <div class="related-grid reveal-stagger">
            <div class="related-card"><h3>Ain Sokhna Port</h3><p>Red Sea port clearance.</p><a href="/ports/ain-sokhna.html">Learn More &rarr;</a></div>
            <div class="related-card"><h3>Customs Clearance</h3><p>All ports covered.</p><a href="/services/customs-clearance.html">Learn More &rarr;</a></div>
            <div class="related-card"><h3>Freight Forwarding</h3><p>Port-to-door delivery.</p><a href="/services/freight-forwarding.html">Learn More &rarr;</a></div>
          </div>
        </div>
      </section>
    </main>
''' + en_footer() + '''
  </body>
</html>''')

def gen_sczone():
    print("Generating: ports/sczone.html")
    write_file("ports/sczone.html", f'''{en_head(
        "SCZone Customs Clearance | Suez Canal Economic Zone | Al-Rouby",
        "Licensed customs clearance in the Suez Canal Economic Zone. Free zone &amp; investment law procedures. Expert SCZone logistics support.",
        "/ports/sczone.html",
        hreflang_ar="/ar/ports/sczone.html"
    )}
    <script type="application/ld+json">{org_schema()}</script>
    <script type="application/ld+json">{breadcrumb_schema([("Home", "/"), ("Ports", "/ports/ain-sokhna.html"), ("SCZone", "")])}</script>
  </head>
  <body>
    <a class="skip-link" href="#main">Skip to content</a>
{en_nav("ports")}
{en_breadcrumb_html([("Home", "/"), ("Ports", "/ports/ain-sokhna.html"), ("SCZone",)])}
    <main id="main">
      <section class="page-hero">
        <div class="container reveal">
          <h1>SCZone Customs Clearance</h1>
          <p>Licensed customs clearance within the Suez Canal Economic Zone. Expert handling of free zone and investment law procedures.</p>
        </div>
      </section>
      <section class="content-section">
        <div class="container">
          <h2 class="reveal">About the Suez Canal Economic Zone</h2>
          <p class="reveal">The Suez Canal Economic Zone (SCZone) is Egypt's premier economic development area, stretching along the Suez Canal corridor. It encompasses multiple industrial zones, ports, and logistics hubs designed to attract manufacturing, logistics, and trade operations. Companies operating within the SCZone benefit from special customs procedures, tax incentives, and streamlined regulatory processes.</p>
          <p class="reveal">Al-Rouby Customs is fully licensed to operate within the SCZone, providing customs clearance for goods entering and exiting the economic zone. Our team is experienced in the specific regulations and procedures that apply to SCZone operations, including free zone rules, investment law provisions, and inter-zone transfers.</p>

          <h2 class="reveal">SCZone Clearance Services</h2>
          <div class="service-features reveal-stagger">
            <div class="feature-item"><h3>Free Zone Clearance</h3><p>Specialized procedures for goods entering or leaving SCZone free zones, including duty suspension and re-export handling.</p></div>
            <div class="feature-item"><h3>Investment Law Procedures</h3><p>Clearance under Egypt's investment law provisions for manufacturing and industrial operations within the SCZone.</p></div>
            <div class="feature-item"><h3>Inter-Zone Transfers</h3><p>Documentation and customs handling for goods moving between different zones within the SCZone corridor.</p></div>
            <div class="feature-item"><h3>Raw Material Imports</h3><p>Efficient clearance of raw materials and components for SCZone-based manufacturers with duty exemption processing.</p></div>
          </div>
          <!-- TODO: Client should add more SCZone-specific content here -->

          <div class="cta-box reveal">
            <h3>SCZone Clearance Expertise</h3>
            <p>Contact us for specialized clearance within the Suez Canal Economic Zone.</p>
            <a href="/#quote" class="btn btn-accent">Request a Quote</a>
          </div>
        </div>
      </section>
      <section class="related-services">
        <div class="container">
          <div class="section-header reveal"><h2>Related Pages</h2></div>
          <div class="related-grid reveal-stagger">
            <div class="related-card"><h3>Ain Sokhna Port</h3><p>Adjacent Red Sea port.</p><a href="/ports/ain-sokhna.html">Learn More &rarr;</a></div>
            <div class="related-card"><h3>Customs Clearance</h3><p>All types of clearance.</p><a href="/services/customs-clearance.html">Learn More &rarr;</a></div>
            <div class="related-card"><h3>Logistics</h3><p>End-to-end solutions.</p><a href="/services/logistics.html">Learn More &rarr;</a></div>
          </div>
        </div>
      </section>
    </main>
''' + en_footer() + '''
  </body>
</html>''')

# ─── Blog Pages ───

def gen_blog_page(filename, title, desc, canonical, keywords, suggested_title):
    print(f"Generating: blog/{filename}")
    write_file(f"blog/{filename}", f'''{en_head(title, desc, canonical)}
    <script type="application/ld+json">{org_schema()}</script>
    <script type="application/ld+json">{breadcrumb_schema([("Home", "/"), ("Blog", "/blog/customs-clearance-guide-egypt.html"), (suggested_title, "")])}</script>
  </head>
  <body>
    <a class="skip-link" href="#main">Skip to content</a>
{en_nav("blog")}
{en_breadcrumb_html([("Home", "/"), ("Blog", "/blog/customs-clearance-guide-egypt.html"), (suggested_title,)])}
    <main id="main">
      <section class="page-hero">
        <div class="container reveal">
          <h1>{suggested_title}</h1>
          <p class="article-meta">Published by Al-Rouby Customs | Updated February 2026</p>
        </div>
      </section>
      <section class="content-section">
        <div class="container article-content">
          <!-- TODO: Full article content needed. Target keywords: {keywords}. Suggested length: 1500+ words -->
          <p class="reveal">This comprehensive guide is coming soon. In the meantime, contact our team for expert advice on this topic.</p>

          <div class="cta-box reveal">
            <h3>Need Expert Help?</h3>
            <p>Our team has 27+ years of experience. Contact us for personalized guidance.</p>
            <a href="/#quote" class="btn btn-accent">Contact Us</a>
          </div>
        </div>
      </section>
      <section class="related-services">
        <div class="container">
          <div class="section-header reveal"><h2>Related Services</h2></div>
          <div class="related-grid reveal-stagger">
            <div class="related-card"><h3>Customs Clearance</h3><p>Professional clearance at all Egyptian ports.</p><a href="/services/customs-clearance.html">Learn More &rarr;</a></div>
            <div class="related-card"><h3>ACI &amp; Nafeza</h3><p>Pre-shipment registration support.</p><a href="/services/aci-nafeza.html">Learn More &rarr;</a></div>
            <div class="related-card"><h3>Shipping to Egypt</h3><p>International shipping solutions.</p><a href="/services/shipping.html">Learn More &rarr;</a></div>
          </div>
        </div>
      </section>
    </main>
''' + en_footer() + '''
  </body>
</html>''')

if __name__ == "__main__":
    print("Generating port pages...")
    gen_ain_sokhna()
    gen_alexandria()
    gen_sczone()
    print("Generating blog pages...")
    gen_blog_page("customs-clearance-guide-egypt.html",
        "Complete Guide to Customs Clearance in Egypt (2026)",
        "Step-by-step guide to customs clearance in Egypt. Documents required, fees, timeline, and tips from 27+ years of experience.",
        "/blog/customs-clearance-guide-egypt.html",
        "customs clearance egypt guide, import clearance egypt procedures",
        "Complete Guide to Customs Clearance in Egypt (2026)")
    gen_blog_page("aci-system-guide.html",
        "ACI System Egypt: Complete Registration Guide (2026)",
        "Everything you need to know about Egypt ACI system. Registration steps, ACID numbers, required documents, common mistakes to avoid.",
        "/blog/aci-system-guide.html",
        "aci system egypt, how to register aci, ACID number",
        "ACI System Egypt: Complete Registration Guide")
    gen_blog_page("sea-freight-types.html",
        "LCL vs FCL Shipping: Which is Right for You?",
        "Compare LCL and FCL shipping options. Cost comparison, transit times, when to use each. Expert advice from Al-Rouby logistics.",
        "/blog/sea-freight-types.html",
        "lcl vs fcl, lcl shipping, container shipping comparison",
        "LCL vs FCL Shipping: Which is Right for You?")
    gen_blog_page("egypt-port-fees.html",
        "Egypt Port Fees &amp; Customs Duties Guide (2026)",
        "Comprehensive guide to port fees and customs duties in Egypt. Updated rates for Ain Sokhna, Alexandria, and all major ports.",
        "/blog/egypt-port-fees.html",
        "egypt port fees, customs fees egypt, port charges",
        "Egypt Port Fees &amp; Customs Duties Guide (2026)")
    gen_blog_page("hs-code-guide.html",
        "HS Code Classification Guide for Egypt Imports",
        "How to find the right HS code for your imports to Egypt. Expert tips on classification to avoid delays and reduce duties.",
        "/blog/hs-code-guide.html",
        "hs code consultation egypt, tariff classification",
        "HS Code Classification Guide for Egypt Imports")
    print("Port + blog pages complete!")
