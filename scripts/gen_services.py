#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate service pages for Al-Rouby website."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_pages import *

def gen_customs_clearance():
    print("Generating: services/customs-clearance.html")
    faqs = [
        ("How long does customs clearance take in Egypt?", "Typically 3-5 business days from vessel discharge, provided all documents are correct."),
        ("What documents do I need for import clearance?", "Commercial Invoice, Packing List, Bill of Lading, Certificate of Origin, and ACI registration. Some goods require additional permits."),
        ("Do you handle all types of customs regimes?", "Yes - final import, export, transit, temporary admission, drawback, and exemption clearance."),
        ("What is the cost of customs clearance in Egypt?", "Costs vary based on cargo value, HS code classification, and applicable duties. Contact us for a transparent quote."),
    ]
    write_file("services/customs-clearance.html", f'''{en_head(
        "Customs Clearance in Egypt | Fast &amp; Compliant | Al-Rouby",
        "Expert customs clearance across all Egyptian ports. ACI compliant, 3-5 day clearance. 27+ years experience. Get a free quote today.",
        "/services/customs-clearance.html",
        hreflang_ar="/ar/services/customs-clearance.html"
    )}
    <script type="application/ld+json">{org_schema()}</script>
    <script type="application/ld+json">{breadcrumb_schema([("Home", "/"), ("Services", "/services/customs-clearance.html"), ("Customs Clearance", "")])}</script>
    <script type="application/ld+json">{service_schema("Customs Clearance", "Expert customs clearance across all Egyptian ports with full ACI compliance and 3-5 day average clearance time.")}</script>
    <script type="application/ld+json">{faq_schema(faqs)}</script>
  </head>
  <body>
    <a class="skip-link" href="#main">Skip to content</a>
{en_nav("services")}
{en_breadcrumb_html([("Home", "/"), ("Services", "/services/customs-clearance.html"), ("Customs Clearance",)])}
    <main id="main">
      <section class="page-hero">
        <div class="container reveal">
          <h1>Customs Clearance in Egypt</h1>
          <p>Expert handling of import and export formalities across all Egyptian ports. Fast, compliant, and transparent customs clearance with over 27 years of experience.</p>
        </div>
      </section>

      <section class="content-section">
        <div class="container">
          <h2 class="reveal">Professional Customs Clearance Services</h2>
          <p class="reveal">Al-Rouby Customs provides comprehensive customs clearance services at every major Egyptian port. Whether you are importing raw materials for manufacturing, exporting finished goods, or managing transit shipments, our team ensures your cargo clears customs quickly and in full compliance with Egyptian regulations.</p>
          <p class="reveal">With an average clearance time of just 3 to 5 business days, we help you avoid costly demurrage charges and keep your supply chain moving. Our deep relationships with port authorities, combined with our thorough understanding of Egyptian customs law, mean fewer delays and more predictable timelines for your shipments.</p>

          <h2 class="reveal">Types of Customs Clearance We Handle</h2>
          <div class="service-features reveal-stagger">
            <div class="feature-item">
              <h3>Final Import Clearance</h3>
              <p>Complete processing for goods entering Egypt for domestic consumption. We handle duty assessment, tariff classification, and all required documentation to release your goods from customs.</p>
            </div>
            <div class="feature-item">
              <h3>Export Clearance</h3>
              <p>Streamlined export procedures including documentation preparation, customs declarations, and coordination with shipping lines to ensure your goods depart on schedule.</p>
            </div>
            <div class="feature-item">
              <h3>Transit &amp; Re-Export</h3>
              <p>Efficient handling of goods passing through Egyptian ports in transit to other destinations, with proper bonding and customs documentation.</p>
            </div>
            <div class="feature-item">
              <h3>Temporary Admission</h3>
              <p>Specialized clearance for goods entering Egypt temporarily for exhibitions, processing, or assembly, with full compliance under temporary admission regulations.</p>
            </div>
            <div class="feature-item">
              <h3>Drawback Procedures</h3>
              <p>Recovery of customs duties on imported materials used in the manufacture of exported goods. We manage the entire drawback process from documentation to refund.</p>
            </div>
            <div class="feature-item">
              <h3>Exemption Clearance</h3>
              <p>Handling of duty-exempt imports under investment law, diplomatic privileges, or other exemption schemes. We ensure all requirements are met for approved exemptions.</p>
            </div>
          </div>

          <h2 class="reveal">Documents Required for Customs Clearance</h2>
          <p class="reveal">Proper documentation is essential for smooth customs clearance. The basic documents you will need include:</p>
          <ul class="reveal">
            <li><strong>Commercial Invoice</strong> &mdash; detailing goods, quantities, and values</li>
            <li><strong>Packing List</strong> &mdash; itemized list of package contents and weights</li>
            <li><strong>Bill of Lading (B/L)</strong> &mdash; shipping document from the carrier</li>
            <li><strong>Certificate of Origin</strong> &mdash; verifying the country of manufacture</li>
            <li><strong>ACI Registration (ACID Number)</strong> &mdash; mandatory pre-registration via the Nafeza system</li>
          </ul>
          <p class="reveal">Depending on your cargo type, additional documents may be required such as health certificates, conformity certificates, or special import permits. Our team will guide you through exactly what is needed for your specific shipment.</p>

          <h2 class="reveal">Ports We Cover</h2>
          <p class="reveal">Our customs clearance services are available at all major Egyptian ports:</p>
          <ul class="reveal">
            <li><a href="/ports/ain-sokhna.html">Ain Sokhna Port</a> (our home base in the TEDA zone)</li>
            <li><a href="/ports/alexandria.html">Alexandria &amp; Dekheila Ports</a></li>
            <li><a href="/ports/sczone.html">Suez Canal Economic Zone (SCZone)</a></li>
            <li>Damietta Port</li>
            <li>Port Said (East &amp; West)</li>
            <li>Adabiya &amp; Port Tawfiq</li>
            <li>Cairo Airport (air cargo clearance)</li>
          </ul>

          <h2 class="reveal">Why Choose Al-Rouby for Customs Clearance</h2>
          <p class="reveal">With over 27 years of experience and more than 12,000 shipments successfully cleared, Al-Rouby Customs has built a reputation for reliability, speed, and transparency. Our dedicated team provides daily updates on your shipment status, transparent pricing with no hidden fees, and full ACI and Nafeza compliance to keep your imports moving smoothly.</p>

          <div class="cta-box reveal">
            <h3>Get a Free Customs Clearance Quote</h3>
            <p>Send us your shipment details and receive a transparent, detailed quote within hours.</p>
            <a href="/#quote" class="btn btn-accent">Request a Quote</a>
          </div>

          <h2 class="reveal">Frequently Asked Questions</h2>
          <div class="faq-container reveal">''' + ''.join([f'''
            <div class="faq-item">
              <button class="faq-question" type="button">{q} <span aria-hidden="true">+</span></button>
              <div class="faq-answer"><p>{a}</p></div>
            </div>''' for q, a in faqs]) + '''
          </div>
        </div>
      </section>

      <section class="related-services">
        <div class="container">
          <div class="section-header reveal"><h2>Related Services</h2></div>
          <div class="related-grid reveal-stagger">
            <div class="related-card"><h3>Freight Forwarding</h3><p>Port-to-door transportation for your cleared goods.</p><a href="/services/freight-forwarding.html">Learn More &rarr;</a></div>
            <div class="related-card"><h3>ACI &amp; Nafeza</h3><p>Pre-shipment registration and Nafeza platform support.</p><a href="/services/aci-nafeza.html">Learn More &rarr;</a></div>
            <div class="related-card"><h3>Shipping to Egypt</h3><p>International container shipping with customs clearance included.</p><a href="/services/shipping.html">Learn More &rarr;</a></div>
          </div>
        </div>
      </section>
    </main>
''' + en_footer() + '''
  </body>
</html>''')

def gen_freight_forwarding():
    print("Generating: services/freight-forwarding.html")
    faqs = [
        ("What is freight forwarding?", "Freight forwarding is the coordination and management of shipping goods from one destination to another, including transportation, documentation, and customs clearance."),
        ("Do you offer both FCL and LCL shipping?", "Yes, we handle both Full Container Load (FCL) and Less than Container Load (LCL) shipments across all Egyptian ports."),
        ("What freight modes do you support?", "We coordinate sea freight, air freight, and land transport services to and from Egypt."),
        ("How do I get a freight forwarding quote?", "Contact us with your cargo details, origin, destination, and preferred timeline. We will provide a competitive quote within hours."),
    ]
    write_file("services/freight-forwarding.html", f'''{en_head(
        "Freight Forwarding Egypt | Sea &amp; Air Cargo | Al-Rouby",
        "Reliable freight forwarding services in Egypt. FCL, LCL, sea freight. Port-to-door delivery. Contact us for competitive rates.",
        "/services/freight-forwarding.html",
        hreflang_ar="/ar/services/freight-forwarding.html"
    )}
    <script type="application/ld+json">{org_schema()}</script>
    <script type="application/ld+json">{breadcrumb_schema([("Home", "/"), ("Services", "/services/customs-clearance.html"), ("Freight Forwarding", "")])}</script>
    <script type="application/ld+json">{service_schema("Freight Forwarding", "Reliable freight forwarding services in Egypt covering FCL, LCL, sea freight, and port-to-door delivery.")}</script>
    <script type="application/ld+json">{faq_schema(faqs)}</script>
  </head>
  <body>
    <a class="skip-link" href="#main">Skip to content</a>
{en_nav("services")}
{en_breadcrumb_html([("Home", "/"), ("Services", "/services/customs-clearance.html"), ("Freight Forwarding",)])}
    <main id="main">
      <section class="page-hero">
        <div class="container reveal">
          <h1>Freight Forwarding Services in Egypt</h1>
          <p>Reliable cargo forwarding from port to door. We manage your shipments across sea, air, and land with full customs clearance support.</p>
        </div>
      </section>
      <section class="content-section">
        <div class="container">
          <h2 class="reveal">End-to-End Freight Forwarding</h2>
          <p class="reveal">Al-Rouby Customs offers comprehensive freight forwarding services that connect your suppliers to your warehouse. As experienced freight forwarders in Egypt, we handle the entire logistics chain from cargo pickup at origin to final delivery at your facility, managing documentation, customs clearance, and transportation along the way.</p>
          <p class="reveal">Whether you need a full container shipped from China to Ain Sokhna or a small LCL shipment from Europe to Alexandria, our freight forwarding team coordinates every detail to ensure timely, cost-effective delivery. We work with trusted shipping lines and transport providers to offer competitive rates without compromising service quality.</p>

          <h2 class="reveal">Our Freight Services</h2>
          <div class="service-features reveal-stagger">
            <div class="feature-item"><h3>Full Container Load (FCL)</h3><p>Dedicated container shipping for larger shipments. 20ft and 40ft containers available at competitive rates through all Egyptian ports.</p></div>
            <div class="feature-item"><h3>Less than Container Load (LCL)</h3><p>Consolidated shipping for smaller cargo volumes. Share container space to reduce costs while maintaining reliable transit times.</p></div>
            <div class="feature-item"><h3>Sea Freight</h3><p>Ocean freight coordination from any global port to Egypt. We handle booking, documentation, and customs at the destination port.</p></div>
            <div class="feature-item"><h3>Inland Transport</h3><p>Door-to-door delivery from Egyptian ports to your warehouse, factory, or distribution center anywhere in Egypt.</p></div>
          </div>

          <h2 class="reveal">Why Choose Al-Rouby as Your Freight Forwarder</h2>
          <p class="reveal">As one of Egypt's established freight forwarding companies, we bring over 27 years of logistics experience to every shipment. Our integrated approach combines freight coordination with in-house customs clearance, eliminating the need for multiple service providers and reducing your total logistics cost.</p>
          <ul class="reveal">
            <li>Integrated customs clearance and freight forwarding under one roof</li>
            <li>Competitive rates through established carrier partnerships</li>
            <li>Real-time shipment tracking and daily status updates</li>
            <li>Full ACI and Nafeza compliance for all imports</li>
            <li>Coverage at all major Egyptian ports</li>
          </ul>

          <div class="cta-box reveal">
            <h3>Get a Freight Forwarding Quote</h3>
            <p>Tell us about your shipment and receive competitive rates within hours.</p>
            <a href="/#quote" class="btn btn-accent">Request a Quote</a>
          </div>

          <h2 class="reveal">Frequently Asked Questions</h2>
          <div class="faq-container reveal">''' + ''.join([f'''
            <div class="faq-item">
              <button class="faq-question" type="button">{q} <span aria-hidden="true">+</span></button>
              <div class="faq-answer"><p>{a}</p></div>
            </div>''' for q, a in faqs]) + '''
          </div>
        </div>
      </section>
      <section class="related-services">
        <div class="container">
          <div class="section-header reveal"><h2>Related Services</h2></div>
          <div class="related-grid reveal-stagger">
            <div class="related-card"><h3>Customs Clearance</h3><p>Fast, compliant clearance at all Egyptian ports.</p><a href="/services/customs-clearance.html">Learn More &rarr;</a></div>
            <div class="related-card"><h3>Shipping to Egypt</h3><p>International container shipping solutions.</p><a href="/services/shipping.html">Learn More &rarr;</a></div>
            <div class="related-card"><h3>Logistics Solutions</h3><p>Complete supply chain management.</p><a href="/services/logistics.html">Learn More &rarr;</a></div>
          </div>
        </div>
      </section>
    </main>
''' + en_footer() + '''
  </body>
</html>''')

def gen_shipping():
    print("Generating: services/shipping.html")
    write_file("services/shipping.html", f'''{en_head(
        "Shipping to Egypt | International Sea Freight | Al-Rouby",
        "Ship to Egypt with confidence. Container shipping, LCL &amp; FCL options. All Egyptian ports covered. Fast customs clearance included.",
        "/services/shipping.html",
        hreflang_ar="/ar/services/shipping.html"
    )}
    <script type="application/ld+json">{org_schema()}</script>
    <script type="application/ld+json">{breadcrumb_schema([("Home", "/"), ("Services", "/services/customs-clearance.html"), ("Shipping", "")])}</script>
    <script type="application/ld+json">{service_schema("International Shipping", "International container shipping to Egypt with customs clearance included. FCL and LCL options at all Egyptian ports.")}</script>
  </head>
  <body>
    <a class="skip-link" href="#main">Skip to content</a>
{en_nav("services")}
{en_breadcrumb_html([("Home", "/"), ("Services", "/services/customs-clearance.html"), ("Shipping",)])}
    <main id="main">
      <section class="page-hero">
        <div class="container reveal">
          <h1>Shipping to Egypt &mdash; International Sea Freight</h1>
          <p>Container shipping to all Egyptian ports with integrated customs clearance. FCL and LCL options for every cargo size.</p>
        </div>
      </section>
      <section class="content-section">
        <div class="container">
          <h2 class="reveal">International Shipping Solutions</h2>
          <p class="reveal">Al-Rouby Customs coordinates international shipping to Egypt from ports worldwide. We work with major shipping lines to offer competitive container shipping rates, whether you need a full container load or a smaller LCL shipment. Every shipping service includes our expert customs clearance at the destination port.</p>
          <p class="reveal">Shipping to Egypt requires careful coordination between the origin country, the shipping line, and Egyptian customs authorities. Our team manages the entire process, ensuring your cargo arrives at the right port, clears customs efficiently, and reaches your doorstep without unnecessary delays or costs.</p>

          <h2 class="reveal">Container Shipping Options</h2>
          <div class="service-features reveal-stagger">
            <div class="feature-item"><h3>FCL &mdash; Full Container Load</h3><p>Dedicated containers for larger shipments. Choose from 20ft standard, 40ft standard, or 40ft high-cube containers. Ideal for regular importers with sufficient cargo volume.</p></div>
            <div class="feature-item"><h3>LCL &mdash; Less than Container Load</h3><p>Share container space with other shippers to reduce costs on smaller shipments. Perfect for first-time importers, sample shipments, or lower-volume cargo.</p></div>
            <div class="feature-item"><h3>Specialized Containers</h3><p>Refrigerated (reefer), open-top, flat-rack, and tank containers available for special cargo requirements.</p></div>
            <div class="feature-item"><h3>Door-to-Door Service</h3><p>Complete shipping from your supplier's door to your warehouse in Egypt, including pickup, ocean freight, customs clearance, and inland delivery.</p></div>
          </div>

          <h2 class="reveal">Egyptian Ports We Ship To</h2>
          <ul class="reveal">
            <li><a href="/ports/ain-sokhna.html">Ain Sokhna Port</a> &mdash; ideal for cargo from Asia, India, and the Far East</li>
            <li><a href="/ports/alexandria.html">Alexandria Port</a> &mdash; main hub for European and Mediterranean shipments</li>
            <li>Damietta Port &mdash; specialized in grain and bulk cargo</li>
            <li>Port Said &mdash; strategic Suez Canal location for transshipment</li>
          </ul>

          <p class="reveal">Need help choosing the right port? Our team can recommend the most cost-effective routing based on your cargo origin, type, and final destination within Egypt.</p>

          <div class="cta-box reveal">
            <h3>Get a Shipping Quote</h3>
            <p>Tell us your cargo details and we will find the best shipping solution for you.</p>
            <a href="/#quote" class="btn btn-accent">Request a Quote</a>
          </div>
        </div>
      </section>
      <section class="related-services">
        <div class="container">
          <div class="section-header reveal"><h2>Related Services</h2></div>
          <div class="related-grid reveal-stagger">
            <div class="related-card"><h3>Customs Clearance</h3><p>Fast clearance at all Egyptian ports.</p><a href="/services/customs-clearance.html">Learn More &rarr;</a></div>
            <div class="related-card"><h3>Freight Forwarding</h3><p>Port-to-door transportation.</p><a href="/services/freight-forwarding.html">Learn More &rarr;</a></div>
            <div class="related-card"><h3>ACI &amp; Nafeza</h3><p>Required pre-shipment registration.</p><a href="/services/aci-nafeza.html">Learn More &rarr;</a></div>
          </div>
        </div>
      </section>
    </main>
''' + en_footer() + '''
  </body>
</html>''')

def gen_logistics():
    print("Generating: services/logistics.html")
    write_file("services/logistics.html", f'''{en_head(
        "Logistics Company in Egypt | End-to-End Solutions | Al-Rouby",
        "Complete logistics solutions in Egypt. Port operations, warehousing, inland transport. Serving importers &amp; manufacturers since 1999.",
        "/services/logistics.html",
        hreflang_ar="/ar/services/logistics.html"
    )}
    <script type="application/ld+json">{org_schema()}</script>
    <script type="application/ld+json">{breadcrumb_schema([("Home", "/"), ("Services", "/services/customs-clearance.html"), ("Logistics", "")])}</script>
    <script type="application/ld+json">{service_schema("Logistics", "Complete logistics solutions in Egypt including port operations, inland transport, and supply chain management.")}</script>
  </head>
  <body>
    <a class="skip-link" href="#main">Skip to content</a>
{en_nav("services")}
{en_breadcrumb_html([("Home", "/"), ("Services", "/services/customs-clearance.html"), ("Logistics",)])}
    <main id="main">
      <section class="page-hero">
        <div class="container reveal">
          <h1>Logistics Company in Egypt</h1>
          <p>End-to-end logistics solutions from port to warehouse. We manage the entire supply chain so you can focus on your business.</p>
        </div>
      </section>
      <section class="content-section">
        <div class="container">
          <h2 class="reveal">Comprehensive Logistics Services</h2>
          <p class="reveal">Al-Rouby Customs is more than a customs broker. We are a full-service logistics company providing end-to-end supply chain solutions for businesses importing to and exporting from Egypt. Our integrated logistics services cover everything from port operations and customs clearance to inland transportation and delivery coordination.</p>
          <p class="reveal">Since 1999, we have been helping importers and manufacturers streamline their logistics operations. Our deep understanding of Egyptian trade infrastructure, combined with our on-the-ground presence at major ports, allows us to deliver reliable, cost-effective logistics solutions tailored to your business needs.</p>

          <h2 class="reveal">Our Logistics Services</h2>
          <div class="service-features reveal-stagger">
            <div class="feature-item"><h3>Port Operations</h3><p>On-site coordination at Egyptian ports for container handling, cargo inspection, and release procedures. We work directly with terminal operators to minimize dwell time.</p></div>
            <div class="feature-item"><h3>Inland Transport</h3><p>Trucking and delivery services from port to your facility anywhere in Egypt. We coordinate flatbed, enclosed, and refrigerated transport as needed.</p></div>
            <div class="feature-item"><h3>Supply Chain Management</h3><p>End-to-end visibility and coordination of your import supply chain from origin to final delivery, including shipment tracking and status reporting.</p></div>
            <div class="feature-item"><h3>Documentation Management</h3><p>Complete handling of trade documents including letters of credit, banking documents, ACI filings, and certificate management.</p></div>
          </div>

          <h2 class="reveal">Industries We Serve</h2>
          <p class="reveal">Our logistics services support businesses across multiple sectors including manufacturing, textiles, food and beverages, construction materials, automotive parts, chemicals, and consumer goods. Whatever your industry, we have the experience and infrastructure to handle your logistics requirements efficiently.</p>

          <div class="cta-box reveal">
            <h3>Optimize Your Logistics</h3>
            <p>Let us manage your supply chain. Get a customized logistics solution today.</p>
            <a href="/#quote" class="btn btn-accent">Request a Quote</a>
          </div>
        </div>
      </section>
      <section class="related-services">
        <div class="container">
          <div class="section-header reveal"><h2>Related Services</h2></div>
          <div class="related-grid reveal-stagger">
            <div class="related-card"><h3>Customs Clearance</h3><p>Fast, compliant clearance at all ports.</p><a href="/services/customs-clearance.html">Learn More &rarr;</a></div>
            <div class="related-card"><h3>Freight Forwarding</h3><p>International cargo coordination.</p><a href="/services/freight-forwarding.html">Learn More &rarr;</a></div>
            <div class="related-card"><h3>Shipping to Egypt</h3><p>Container shipping solutions.</p><a href="/services/shipping.html">Learn More &rarr;</a></div>
          </div>
        </div>
      </section>
    </main>
''' + en_footer() + '''
  </body>
</html>''')

def gen_aci_nafeza():
    print("Generating: services/aci-nafeza.html")
    faqs = [
        ("What is ACI in Egyptian customs?", "ACI (Advanced Cargo Information) is a mandatory pre-registration system for all imports to Egypt. Shippers must register cargo details before shipping to obtain an ACID number."),
        ("What is an ACID number?", "ACID (Advanced Cargo Information Declaration) number is a unique identifier assigned to each shipment registered in the ACI system. It is required for customs clearance."),
        ("What is the Nafeza platform?", "Nafeza is Egypt's single-window trade facilitation platform that connects importers, customs, and government agencies for electronic processing of trade transactions."),
        ("How long does ACI registration take?", "Registration typically takes 1-2 business days once all required information is provided. We recommend registering well before your cargo ships."),
    ]
    write_file("services/aci-nafeza.html", f'''{en_head(
        "ACI Registration &amp; Nafeza Filing | Al-Rouby Egypt",
        "Full ACI registration and Nafeza filing support. ACID number generation, document preparation. 100% compliant with Egyptian customs regulations.",
        "/services/aci-nafeza.html",
        hreflang_ar="/ar/services/aci-nafeza.html"
    )}
    <script type="application/ld+json">{org_schema()}</script>
    <script type="application/ld+json">{breadcrumb_schema([("Home", "/"), ("Services", "/services/customs-clearance.html"), ("ACI &amp; Nafeza", "")])}</script>
    <script type="application/ld+json">{service_schema("ACI Registration and Nafeza Filing", "Full ACI registration and Nafeza platform support for Egyptian imports. ACID number generation and document preparation.")}</script>
    <script type="application/ld+json">{faq_schema(faqs)}</script>
  </head>
  <body>
    <a class="skip-link" href="#main">Skip to content</a>
{en_nav("services")}
{en_breadcrumb_html([("Home", "/"), ("Services", "/services/customs-clearance.html"), ("ACI & Nafeza",)])}
    <main id="main">
      <section class="page-hero">
        <div class="container reveal">
          <h1>ACI Registration &amp; Nafeza Filing Services</h1>
          <p>Full support for Egypt's Advanced Cargo Information system and Nafeza platform. We handle registration, ACID numbers, and document preparation.</p>
        </div>
      </section>
      <section class="content-section">
        <div class="container">
          <h2 class="reveal">Understanding Egypt's ACI System</h2>
          <p class="reveal">Egypt's Advanced Cargo Information (ACI) system requires all importers to pre-register their cargo details before goods are shipped to Egypt. This mandatory system was introduced to enhance supply chain security and streamline customs processing. Every shipment arriving at an Egyptian port must have a valid ACID (Advanced Cargo Information Declaration) number, without which goods cannot clear customs.</p>
          <p class="reveal">Al-Rouby Customs provides complete ACI registration and Nafeza filing support, ensuring your shipments are properly registered and compliant before they leave the origin country. With 100% ACI compliance across all shipments we handle, we eliminate the risk of delays or penalties due to registration issues.</p>

          <h2 class="reveal">Our ACI &amp; Nafeza Services</h2>
          <div class="service-features reveal-stagger">
            <div class="feature-item"><h3>ACI Registration</h3><p>Complete registration of your cargo in the ACI system, including product details, HS code classification, and shipper information. We ensure all data is accurate and complete.</p></div>
            <div class="feature-item"><h3>ACID Number Generation</h3><p>Obtaining and managing ACID numbers for each shipment. We track validity periods and ensure numbers are active when your cargo arrives.</p></div>
            <div class="feature-item"><h3>Nafeza Platform Operations</h3><p>Filing customs declarations, submitting documents, and managing payments through the Nafeza single-window platform on your behalf.</p></div>
            <div class="feature-item"><h3>HS Code Classification</h3><p>Expert classification of your goods under the correct Harmonized System codes. Proper classification prevents delays and ensures accurate duty assessment.</p></div>
          </div>

          <h2 class="reveal">The ACI Registration Process</h2>
          <ol class="reveal">
            <li><strong>Provide cargo details</strong> &mdash; Send us your commercial invoice, packing list, and product descriptions</li>
            <li><strong>We register your shipment</strong> &mdash; Our team enters all required data into the ACI system</li>
            <li><strong>Receive your ACID number</strong> &mdash; A unique ACID number is generated for your shipment</li>
            <li><strong>Share with your shipper</strong> &mdash; The ACID number must be included on all shipping documents</li>
            <li><strong>Ship with confidence</strong> &mdash; Your cargo is pre-cleared for smooth entry at the Egyptian port</li>
          </ol>

          <h2 class="reveal">Why ACI Compliance Matters</h2>
          <p class="reveal">Shipments arriving at Egyptian ports without valid ACI registration face significant penalties, delays, and potential refusal of entry. Common issues include incorrect HS codes, missing ACID numbers, and mismatched cargo information. Our thorough review process catches these issues before they become problems, saving you time and money.</p>

          <div class="cta-box reveal">
            <h3>Need ACI Registration Help?</h3>
            <p>Let us handle your ACI filing and Nafeza operations. Contact us today.</p>
            <a href="/#quote" class="btn btn-accent">Request a Quote</a>
          </div>

          <h2 class="reveal">Frequently Asked Questions</h2>
          <div class="faq-container reveal">''' + ''.join([f'''
            <div class="faq-item">
              <button class="faq-question" type="button">{q} <span aria-hidden="true">+</span></button>
              <div class="faq-answer"><p>{a}</p></div>
            </div>''' for q, a in faqs]) + '''
          </div>
        </div>
      </section>
      <section class="related-services">
        <div class="container">
          <div class="section-header reveal"><h2>Related Services</h2></div>
          <div class="related-grid reveal-stagger">
            <div class="related-card"><h3>Customs Clearance</h3><p>Complete customs processing at all Egyptian ports.</p><a href="/services/customs-clearance.html">Learn More &rarr;</a></div>
            <div class="related-card"><h3>Shipping to Egypt</h3><p>International container shipping.</p><a href="/services/shipping.html">Learn More &rarr;</a></div>
            <div class="related-card"><h3>Freight Forwarding</h3><p>Cargo coordination and delivery.</p><a href="/services/freight-forwarding.html">Learn More &rarr;</a></div>
          </div>
        </div>
      </section>
    </main>
''' + en_footer() + '''
  </body>
</html>''')

if __name__ == "__main__":
    print("Generating service pages...")
    gen_customs_clearance()
    gen_freight_forwarding()
    gen_shipping()
    gen_logistics()
    gen_aci_nafeza()
    print("Service pages complete!")
