#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Arabic pages for Al-Rouby website."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_pages import *

def gen_ar_homepage():
    print("Generating: ar/index.html")
    write_file("ar/index.html", f'''{ar_head(
        "الروبي | خدمات التخليص الجمركي والخدمات اللوجستية في مصر",
        "الروبي للتخليص الجمركي — خدمات تخليص جمركي متكاملة في جميع الموانئ المصرية. دعم كامل لمنظومة نافذة ونظام ACI. خبرة أكثر من 27 عاماً.",
        "/ar/",
        hreflang_en="/"
    )}
    <script type="application/ld+json">{org_schema()}</script>
    <script type="application/ld+json">{{
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "الروبي للتخليص الجمركي",
      "alternateName": "Al-Rouby Customs",
      "description": "خدمات التخليص الجمركي في جميع الموانئ المصرية مع دعم كامل لنظام ACI ونافذة.",
      "url": "https://al-rouby.com/ar/",
      "telephone": "+201000628855",
      "email": "info@al-rouby.com",
      "address": {{
        "@type": "PostalAddress",
        "streetAddress": "مبنى 615، تيدا",
        "addressLocality": "العين السخنة",
        "addressRegion": "السويس",
        "addressCountry": "EG"
      }},
      "sameAs": ["https://www.facebook.com/RisElRouby","https://www.linkedin.com/company/al-rouby/"],
      "image": "https://al-rouby.com/images/og-image.jpg",
      "areaServed": {{ "@type": "Country", "name": "Egypt" }}
    }}</script>
  </head>
  <body id="top">
    <a class="skip-link" href="#main">انتقل إلى المحتوى</a>
{ar_nav("home")}
    <main id="main">
      <section class="container hero">
        <div class="hero-content reveal">
          <h1>تخليص جمركي في جميع موانئ مصر — سرعة، التزام، وثقة</h1>
          <p>شريكك الموثوق لحلول جمركية ولوجستية خالية من المتاعب. نضمن تحرك شحناتك بسلاسة عبر الموانئ المصرية مع دعم كامل لمنظومة نافذة.</p>
          <p class="service-summary">شركة الروبي متخصصة في التخليص الجمركي، والامتثال التنظيمي، وتجهيز المستندات، ودعم عمليات الموانئ، وتنسيق النقل البري الداخلي عبر جميع الموانئ المصرية الرئيسية.</p>
          <div class="hero-buttons">
            <a href="#quote" class="btn btn-primary">اطلب عرض سعر</a>
            <a href="https://wa.me/201000628855?text=مرحباً%20شركة%20الروبي،%20أرغب%20في%20الاستفسار%20عن%20تخليص%20شحنة." target="_blank" rel="noopener noreferrer" class="btn btn-secondary">تواصل عبر واتساب</a>
          </div>
        </div>
        <div class="hero-card reveal">
          <h3>لمحة سريعة</h3>
          <ul>
            <li><span class="check-icon" aria-hidden="true">&#10004;</span> دعم كامل لنظام ACI ونافذة</li>
            <li><span class="check-icon" aria-hidden="true">&#10004;</span> تغطية: جميع موانئ مصر</li>
            <li><span class="check-icon" aria-hidden="true">&#10004;</span> متوسط التخليص: ٣–٥ أيام</li>
            <li><span class="check-icon" aria-hidden="true">&#10004;</span> شفافية تامة في الأسعار</li>
          </ul>
        </div>
      </section>

      <section class="trust"><div class="container">
        <div class="trust-grid reveal-stagger">
          <div class="trust-item"><h3>+27</h3><p>سنة خبرة</p></div>
          <div class="trust-item"><h3>12,000+</h3><p>شحنة تم تخليصها</p></div>
          <div class="trust-item"><h3>100%</h3><p>توافق مع ACI</p></div>
          <div class="trust-item"><h3>24/7</h3><p>دعم للعملاء</p></div>
        </div>
      </div></section>

      <section id="services" class="services"><div class="container">
        <div class="section-header reveal"><h2>خدماتنا الأساسية</h2><p>حلول لوجستية شاملة مصممة خصيصاً للمستوردين وأصحاب المصانع.</p></div>
        <div class="services-grid reveal-stagger">
          <article class="service-card">
            <div class="service-icon" aria-hidden="true">&#128674;</div>
            <h3>التخليص الجمركي</h3>
            <p>تعامل احترافي مع إجراءات الاستيراد والتصدير، نضمن السرعة والامتثال الكامل للقوانين المصرية.</p>
            <a href="/ar/services/customs-clearance.html" class="service-link">اعرف المزيد &larr;</a>
          </article>
          <article class="service-card">
            <div class="service-icon" aria-hidden="true">&#128667;</div>
            <h3>الشحن والتوصيل</h3>
            <p>نقل سلس من الميناء إلى مستودعك. نحن ندير العملية اللوجستية بالكامل.</p>
            <a href="/ar/services/freight-forwarding.html" class="service-link">اعرف المزيد &larr;</a>
          </article>
          <article class="service-card">
            <div class="service-icon" aria-hidden="true">&#128228;</div>
            <h3>الشحن البحري</h3>
            <p>شحن دولي بحاويات كاملة أو جزئية مع تخليص جمركي متكامل.</p>
            <a href="/ar/services/shipping.html" class="service-link">اعرف المزيد &larr;</a>
          </article>
          <article class="service-card">
            <div class="service-icon" aria-hidden="true">&#128230;</div>
            <h3>الخدمات اللوجستية</h3>
            <p>حلول لوجستية متكاملة من عمليات الموانئ والتخزين إلى النقل الداخلي.</p>
            <a href="/ar/services/logistics.html" class="service-link">اعرف المزيد &larr;</a>
          </article>
          <article class="service-card">
            <div class="service-icon" aria-hidden="true">&#128196;</div>
            <h3>خدمة ACI ونافذة</h3>
            <p>دعم كامل في التسجيل المسبق (ACI)، وتكويد الأصناف، والمستندات البنكية.</p>
            <a href="/ar/services/aci-nafeza.html" class="service-link">اعرف المزيد &larr;</a>
          </article>
        </div>
      </div></section>

      <section class="services" style="background: var(--bg-body);"><div class="container">
        <div class="section-header reveal"><h2>تغطية الموانئ</h2><p>نعمل في جميع الموانئ المصرية الرئيسية بخبرة ميدانية مباشرة.</p></div>
        <div class="ports-grid reveal-stagger">
          <article class="port-card"><h3>&#9875; ميناء العين السخنة</h3><p>مقرنا الرئيسي في منطقة تيدا مع أسرع أوقات تخليص.</p><a href="/ar/ports/ain-sokhna.html" class="service-link">اعرف المزيد &larr;</a></article>
          <article class="port-card"><h3>&#9875; الإسكندرية والدخيلة</h3><p>أكبر ميناء متوسطي في مصر. خدمات استيراد وتصدير كاملة.</p><a href="/ar/ports/alexandria.html" class="service-link">اعرف المزيد &larr;</a></article>
          <article class="port-card"><h3>&#9875; المنطقة الاقتصادية</h3><p>المنطقة الاقتصادية لقناة السويس. مرخصون للمناطق الحرة وقانون الاستثمار.</p><a href="/ar/ports/sczone.html" class="service-link">اعرف المزيد &larr;</a></article>
        </div>
      </div></section>

      <section id="process" class="process"><div class="container">
        <h2 class="reveal">٣ خطوات بسيطة</h2>
        <div class="process-steps reveal-stagger">
          <article class="step"><div class="step-number" aria-hidden="true">1</div><h3>إرسال المستندات</h3><p>أرسل لنا الفاتورة وقائمة التعبئة. نقوم بمراجعة كل شيء لضمان المطابقة.</p></article>
          <article class="step"><div class="step-number" aria-hidden="true">2</div><h3>التجهيز والتقديم</h3><p>نتعامل مع ملف ACI وندرج الشهادات والرسوم عبر منصة نافذة فوراً.</p></article>
          <article class="step"><div class="step-number" aria-hidden="true">3</div><h3>التخليص والتسليم</h3><p>يتم الإفراج عن الشحنة ونقلها مباشرة إلى الموقع الذي تحدده.</p></article>
        </div>
      </div></section>

      <section class="testimonials"><div class="container">
        <div class="section-header reveal"><h2>ماذا يقول عملاؤنا</h2></div>
        <div class="testimonial-grid reveal-stagger">
          <article class="review-card"><p>"الروبي أنقذنا من غرامات أرضيات ضخمة. سرعة واحترافية عالية."</p><div class="client-info"><h4>أ. أحمد عاطف</h4><span>صاحب مصنع كواليتي</span></div></article>
          <article class="review-card"><p>"أفضل تجربة في التسجيل المسبق ACI. تعاملوا مع كل شيء بسلاسة."</p><div class="client-info"><h4>أ. هاني عبيد</h4><span>صاحب ذا بوينت</span></div></article>
          <article class="review-card"><p>"أسعار واضحة ومتابعة يومية. أنصح بهم بشدة لميناء السخنة."</p><div class="client-info"><h4>أ. محمد صلاح</h4><span>مستورد منسوجات</span></div></article>
        </div>
      </div></section>

      <section id="faq"><div class="container faq-container reveal">
        <div class="section-header"><h2>الأسئلة الشائعة</h2></div>
        <div class="faq-item"><button class="faq-question" type="button">كم يستغرق التخليص الجمركي؟ <span aria-hidden="true">+</span></button><div class="faq-answer"><p>عادةً يستغرق التخليص من ٣ إلى ٥ أيام عمل من لحظة تفريغ الباخرة، بشرط صحة جميع المستندات.</p></div></div>
        <div class="faq-item"><button class="faq-question" type="button">هل تتعاملون مع نظام ACI؟ <span aria-hidden="true">+</span></button><div class="faq-answer"><p>نعم، نوفر دعم كامل لنظام التسجيل المسبق للشحنات (ACI) واستخراج رقم ACID.</p></div></div>
        <div class="faq-item"><button class="faq-question" type="button">ما المستندات المطلوبة؟ <span aria-hidden="true">+</span></button><div class="faq-answer"><p>المستندات الأساسية تشمل الفاتورة التجارية، قائمة التعبئة، بوليصة الشحن، وشهادة المنشأ.</p></div></div>
        <div class="faq-item"><button class="faq-question" type="button">ما الموانئ التي تغطونها؟ <span aria-hidden="true">+</span></button><div class="faq-answer"><p>نعمل في جميع الموانئ المصرية الرئيسية بما فيها العين السخنة، الإسكندرية، الدخيلة، دمياط، بورسعيد، الأدبية، بورتوفيق، والمنطقة الاقتصادية لقناة السويس.</p></div></div>
        <div class="faq-item"><button class="faq-question" type="button">هل توفرون تخليص في المنطقة الاقتصادية؟ <span aria-hidden="true">+</span></button><div class="faq-answer"><p>نعم، نحن مرخصون ولدينا خبرة في التعامل مع التخليص داخل المنطقة الاقتصادية لقناة السويس.</p></div></div>
      </div></section>

      <section id="quote" class="quote"><div class="container quote-grid">
        <div class="quote-info reveal">
          <h2>اطلب عرض سعر</h2>
          <p>أرسل تفاصيل شحنتك وسنرد عليك بعرض سعر واضح وشفاف.</p>
          <ul class="quote-points">
            <li><span class="check-icon" aria-hidden="true">&#10004;</span> رد سريع خلال ساعات</li>
            <li><span class="check-icon" aria-hidden="true">&#10004;</span> أسعار شفافة بدون رسوم مخفية</li>
            <li><span class="check-icon" aria-hidden="true">&#10004;</span> دعم كامل لنظام ACI / نافذة</li>
          </ul>
        </div>
        <form class="quote-form reveal" action="https://formspree.io/f/mreapbqn" method="post" novalidate>
          <div class="form-row">
            <label>الاسم الكامل <input type="text" name="name" placeholder="اسمك" required autocomplete="name" minlength="2" maxlength="100"></label>
            <label>الهاتف / واتساب <input type="tel" name="phone" placeholder="+20 ..." required autocomplete="tel" pattern="[\\+]?[0-9\\s]{{10,20}}"></label>
          </div>
          <label>البريد الإلكتروني (اختياري) <input type="email" name="email" placeholder="you@email.com" autocomplete="email" maxlength="100"></label>
          <div class="form-row">
            <label>نوع الخدمة<select name="service_type" required><option value="" selected disabled>اختر نوع الخدمة...</option><option value="import_final">وارد نهائي</option><option value="export">تصدير</option><option value="transit">ترانزيت</option><option value="temporary_admission">إفراج مؤقت</option><option value="sczone">المنطقة الاقتصادية</option></select></label>
            <label>الميناء<select name="port" required><option value="" selected disabled>اختر الميناء...</option><option value="ain-sokhna">العين السخنة</option><option value="alexandria">الإسكندرية / الدخيلة</option><option value="damietta">دمياط</option><option value="port-said">بورسعيد</option><option value="adabiya">الأدبية</option></select></label>
          </div>
          <div class="shipment-mode-box">
            <label class="shipment-label">طبيعة الشحن</label>
            <div class="radio-group">
              <label class="radio-item"><input type="radio" name="shipment_mode" value="FCL"> حاوية كاملة (FCL)</label>
              <label class="radio-item"><input type="radio" name="shipment_mode" value="LCL"> بضائع مشتركة (LCL)</label>
            </div>
            <div id="fcl-details">
              <div class="container-input-col"><label>عدد حاويات 20 قدم</label><input type="number" name="containers_20ft" placeholder="0" min="0"></div>
              <div class="container-input-col"><label>عدد حاويات 40 قدم</label><input type="number" name="containers_40ft" placeholder="0" min="0"></div>
            </div>
          </div>
          <label>تفاصيل الرسالة <textarea name="message" rows="4" placeholder="وصف البضاعة، موعد الوصول المتوقع..." required maxlength="1000"></textarea></label>
          <button type="submit" class="btn btn-accent btn-submit">إرسال الطلب</button>
          <p class="form-note">بإرسال هذا النموذج، أنت توافق على أن نقوم بالتواصل معك بخصوص طلبك.</p>
        </form>
      </div></section>

      <section class="final-cta">
        <h2 class="reveal">جاهز لتسهيل أعمالك اللوجستية؟</h2>
        <p class="reveal">احصل على عرض سعر دقيق وسريع لشحنتك القادمة اليوم.</p>
        <div class="cta-buttons reveal">
          <a href="#quote" class="btn btn-accent">اطلب عرض سعر</a>
          <a href="https://wa.me/201000628855?text=مرحباً،%20أود%20الاستفسار%20عن%20عرض%20سعر." target="_blank" rel="noopener noreferrer" class="btn btn-white">واتساب</a>
        </div>
      </section>

      <section id="contact" class="contact"><div class="container">
        <div class="section-header reveal"><h2>اتصل بنا</h2><p>تواصل معنا في أي وقت — نرد بسرعة.</p></div>
        <div class="contact-grid reveal-stagger">
          <div class="contact-card"><h3>البريد الإلكتروني</h3><p><a href="mailto:info@al-rouby.com">info@al-rouby.com</a></p></div>
          <div class="contact-card"><h3>الهاتف / واتساب</h3><p><a href="tel:+201000628855" dir="ltr">+20 100 062 8855</a></p></div>
          <div class="contact-card"><h3>العنوان</h3><p><a href="https://maps.app.goo.gl/RsDBzG56XkLNRWNFA" target="_blank" rel="noopener noreferrer">مبنى 615، تيدا، العين السخنة، السويس، مصر</a></p></div>
        </div>
      </div></section>
    </main>
''' + ar_footer() + '''
  </body>
</html>''')

def gen_ar_service_page(filename, title, desc, canonical, en_canonical, h1, intro, services_html):
    print(f"Generating: ar/services/{filename}")
    write_file(f"ar/services/{filename}", f'''{ar_head(title, desc, canonical, hreflang_en=en_canonical)}
    <script type="application/ld+json">{org_schema()}</script>
    <script type="application/ld+json">{breadcrumb_schema([("الرئيسية", "/ar/"), ("خدماتنا", "/ar/services/customs-clearance.html"), (h1, "")])}</script>
  </head>
  <body>
    <a class="skip-link" href="#main">انتقل إلى المحتوى</a>
{ar_nav("services")}
{ar_breadcrumb_html([("الرئيسية", "/ar/"), ("خدماتنا", "/ar/services/customs-clearance.html"), (h1,)])}
    <main id="main">
      <section class="page-hero"><div class="container reveal"><h1>{h1}</h1><p>{intro}</p></div></section>
      <section class="content-section"><div class="container">
        <!-- TODO: Expand Arabic content -->
        {services_html}
        <div class="cta-box reveal"><h3>اطلب عرض سعر</h3><p>أرسل تفاصيل شحنتك واحصل على عرض سعر شفاف.</p><a href="/ar/#quote" class="btn btn-accent">اطلب عرض سعر</a></div>
      </div></section>
    </main>
''' + ar_footer() + '''
  </body>
</html>''')

def gen_ar_port_page(filename, title, desc, canonical, en_canonical, h1, intro, content_html):
    print(f"Generating: ar/ports/{filename}")
    write_file(f"ar/ports/{filename}", f'''{ar_head(title, desc, canonical, hreflang_en=en_canonical)}
    <script type="application/ld+json">{org_schema()}</script>
    <script type="application/ld+json">{breadcrumb_schema([("الرئيسية", "/ar/"), ("الموانئ", "/ar/ports/ain-sokhna.html"), (h1, "")])}</script>
  </head>
  <body>
    <a class="skip-link" href="#main">انتقل إلى المحتوى</a>
{ar_nav("ports")}
{ar_breadcrumb_html([("الرئيسية", "/ar/"), ("الموانئ", "/ar/ports/ain-sokhna.html"), (h1,)])}
    <main id="main">
      <section class="page-hero"><div class="container reveal"><h1>{h1}</h1><p>{intro}</p></div></section>
      <section class="content-section"><div class="container">
        <!-- TODO: Expand Arabic content -->
        {content_html}
        <div class="cta-box reveal"><h3>اطلب عرض سعر</h3><p>احصل على عرض سعر لتخليص بضائعك.</p><a href="/ar/#quote" class="btn btn-accent">اطلب عرض سعر</a></div>
      </div></section>
    </main>
''' + ar_footer() + '''
  </body>
</html>''')

if __name__ == "__main__":
    print("Generating Arabic pages...")
    gen_ar_homepage()

    gen_ar_service_page("customs-clearance.html",
        "التخليص الجمركي في مصر | سريع ومتوافق | الروبي",
        "خدمات تخليص جمركي احترافية في جميع الموانئ المصرية. متوافق مع نظام ACI. تخليص في 3-5 أيام. خبرة أكثر من 27 عاماً.",
        "/ar/services/customs-clearance.html", "/services/customs-clearance.html",
        "التخليص الجمركي في مصر",
        "تعامل احترافي مع إجراءات الاستيراد والتصدير في جميع الموانئ المصرية. سرعة وامتثال كامل مع خبرة أكثر من 27 عاماً.",
        '<h2 class="reveal">خدمات التخليص الجمركي</h2><p class="reveal">شركة الروبي تقدم خدمات تخليص جمركي شاملة في جميع الموانئ المصرية الرئيسية. سواء كنت تستورد مواد خام للتصنيع أو تصدر منتجات تامة الصنع أو تدير شحنات عابرة، فريقنا يضمن تخليص بضائعك بسرعة وبما يتوافق تماماً مع اللوائح المصرية.</p><div class="service-features reveal-stagger"><div class="feature-item"><h3>الوارد النهائي</h3><p>معالجة كاملة للبضائع المستوردة للاستهلاك المحلي.</p></div><div class="feature-item"><h3>التصدير</h3><p>إجراءات تصدير مبسطة مع تجهيز المستندات.</p></div><div class="feature-item"><h3>الترانزيت</h3><p>إدارة فعالة للبضائع العابرة عبر الموانئ المصرية.</p></div><div class="feature-item"><h3>الإفراج المؤقت</h3><p>تخليص متخصص للبضائع المدخلة مؤقتاً.</p></div></div>')

    gen_ar_service_page("freight-forwarding.html",
        "الشحن والتوصيل في مصر | بحري وجوي | الروبي",
        "خدمات شحن وتوصيل موثوقة في مصر. حاويات كاملة وجزئية. توصيل من الميناء إلى الباب.",
        "/ar/services/freight-forwarding.html", "/services/freight-forwarding.html",
        "خدمات الشحن والتوصيل في مصر",
        "شحن بضائعك من الميناء إلى باب مستودعك. نحن ندير اللوجستيات بالكامل لتوفير وقتك.",
        '<h2 class="reveal">خدمات شحن متكاملة</h2><p class="reveal">شركة الروبي تقدم خدمات شحن وتوصيل شاملة تربط مورديك بمستودعك. كوكلاء شحن ذوي خبرة في مصر، نتعامل مع سلسلة اللوجستيات بالكامل.</p><div class="service-features reveal-stagger"><div class="feature-item"><h3>حاوية كاملة (FCL)</h3><p>شحن حاويات مخصصة للشحنات الكبيرة بأسعار تنافسية.</p></div><div class="feature-item"><h3>بضائع مشتركة (LCL)</h3><p>مشاركة مساحة الحاوية لتقليل التكاليف على الشحنات الأصغر.</p></div><div class="feature-item"><h3>الشحن البحري</h3><p>تنسيق الشحن البحري من أي ميناء عالمي إلى مصر.</p></div><div class="feature-item"><h3>النقل الداخلي</h3><p>توصيل من باب إلى باب من الموانئ المصرية إلى أي مكان في مصر.</p></div></div>')

    gen_ar_service_page("shipping.html",
        "الشحن إلى مصر | شحن بحري دولي | الروبي",
        "اشحن إلى مصر بثقة. شحن حاويات، خيارات LCL و FCL. تغطية جميع الموانئ المصرية مع تخليص جمركي.",
        "/ar/services/shipping.html", "/services/shipping.html",
        "الشحن البحري الدولي إلى مصر",
        "شحن حاويات إلى جميع الموانئ المصرية مع تخليص جمركي متكامل. خيارات FCL و LCL لكل حجم شحنة.",
        '<h2 class="reveal">حلول الشحن الدولي</h2><p class="reveal">شركة الروبي تنسق الشحن الدولي إلى مصر من موانئ حول العالم. نعمل مع خطوط ملاحية كبرى لتقديم أسعار شحن تنافسية.</p><div class="service-features reveal-stagger"><div class="feature-item"><h3>حاوية كاملة FCL</h3><p>حاويات مخصصة 20 قدم و40 قدم بأسعار تنافسية.</p></div><div class="feature-item"><h3>بضائع مشتركة LCL</h3><p>مشاركة مساحة الحاوية لتقليل تكاليف الشحنات الصغيرة.</p></div></div>')

    gen_ar_service_page("logistics.html",
        "شركة لوجستية في مصر | حلول شاملة | الروبي",
        "حلول لوجستية متكاملة في مصر. عمليات الموانئ، التخزين، النقل الداخلي. نخدم المستوردين والمصنعين منذ 1999.",
        "/ar/services/logistics.html", "/services/logistics.html",
        "شركة خدمات لوجستية في مصر",
        "حلول لوجستية شاملة من الميناء إلى المستودع. ندير سلسلة التوريد بالكامل لتركز أنت على أعمالك.",
        '<h2 class="reveal">خدمات لوجستية شاملة</h2><p class="reveal">شركة الروبي أكثر من مجرد مخلص جمركي. نحن شركة خدمات لوجستية متكاملة تقدم حلول سلسلة توريد شاملة للشركات المستوردة والمصدرة في مصر.</p><div class="service-features reveal-stagger"><div class="feature-item"><h3>عمليات الموانئ</h3><p>تنسيق ميداني في الموانئ المصرية لمناولة الحاويات والفحص.</p></div><div class="feature-item"><h3>النقل الداخلي</h3><p>خدمات نقل بالشاحنات من الميناء إلى منشأتك في أي مكان بمصر.</p></div></div>')

    gen_ar_service_page("aci-nafeza.html",
        "تسجيل ACI ونافذة | الروبي مصر",
        "دعم كامل لتسجيل ACI ونافذة. استخراج رقم ACID وتجهيز المستندات. 100% متوافق مع لوائح الجمارك المصرية.",
        "/ar/services/aci-nafeza.html", "/services/aci-nafeza.html",
        "خدمة تسجيل ACI ونافذة",
        "دعم كامل لنظام التسجيل المسبق للشحنات ACI ومنصة نافذة. استخراج رقم ACID وتجهيز المستندات.",
        '<h2 class="reveal">نظام ACI المصري</h2><p class="reveal">نظام المعلومات المسبقة للشحنات (ACI) يتطلب من جميع المستوردين التسجيل المسبق لتفاصيل شحناتهم قبل شحن البضائع إلى مصر. هذا النظام الإلزامي تم تقديمه لتعزيز أمن سلسلة التوريد.</p><div class="service-features reveal-stagger"><div class="feature-item"><h3>تسجيل ACI</h3><p>تسجيل كامل لشحنتك في نظام ACI بكل التفاصيل المطلوبة.</p></div><div class="feature-item"><h3>استخراج رقم ACID</h3><p>الحصول على أرقام ACID وإدارتها لكل شحنة.</p></div><div class="feature-item"><h3>عمليات نافذة</h3><p>تقديم البيانات الجمركية والمستندات عبر منصة نافذة.</p></div><div class="feature-item"><h3>تصنيف HS Code</h3><p>تصنيف دقيق لبضائعك تحت أكواد النظام المنسق الصحيحة.</p></div></div>')

    gen_ar_port_page("ain-sokhna.html",
        "تخليص جمركي في ميناء العين السخنة | الروبي",
        "تخليص جمركي متخصص في ميناء العين السخنة. موقعنا في منطقة تيدا. تخليص سريع بأسعار تنافسية.",
        "/ar/ports/ain-sokhna.html", "/ports/ain-sokhna.html",
        "تخليص جمركي في ميناء العين السخنة",
        "مقرنا الرئيسي في منطقة تيدا. نوفر أسرع أوقات تخليص على ساحل البحر الأحمر المصري.",
        '<h2 class="reveal">عن ميناء العين السخنة</h2><p class="reveal">ميناء العين السخنة يقع على الساحل الغربي لخليج السويس على بعد حوالي 120 كم شرق القاهرة. يقع الميناء ضمن المنطقة الصناعية تيدا ويعد بوابة رئيسية للبضائع القادمة من آسيا.</p><h2 class="reveal">خدماتنا في العين السخنة</h2><div class="service-features reveal-stagger"><div class="feature-item"><h3>التخليص الجمركي</h3><p>معالجة جمركية سريعة بفريقنا الميداني. متوسط تخليص 3-5 أيام عمل.</p></div><div class="feature-item"><h3>ACI ونافذة</h3><p>تسجيل مسبق كامل وعمليات نافذة لجميع الشحنات.</p></div><div class="feature-item"><h3>النقل الداخلي</h3><p>تنسيق النقل بالشاحنات من السخنة إلى القاهرة والعاشر من رمضان وجميع المحافظات.</p></div></div>')

    gen_ar_port_page("alexandria.html",
        "تخليص جمركي في ميناء الإسكندرية | الروبي",
        "تخليص جمركي احترافي في ميناء الإسكندرية والدخيلة. استيراد وتصدير وتنسيق النقل.",
        "/ar/ports/alexandria.html", "/ports/alexandria.html",
        "تخليص جمركي في ميناء الإسكندرية",
        "تخليص جمركي احترافي في أكبر ميناء متوسطي في مصر. خدمات استيراد وتصدير كاملة.",
        '<h2 class="reveal">عن ميناء الإسكندرية والدخيلة</h2><p class="reveal">ميناء الإسكندرية هو البوابة المتوسطية الرئيسية لمصر وأحد أقدم الموانئ في العالم. مع ميناء الدخيلة المجاور، يتعامل مع غالبية تجارة مصر مع أوروبا وشمال أفريقيا.</p><div class="service-features reveal-stagger"><div class="feature-item"><h3>تخليص الواردات</h3><p>معالجة كاملة للبضائع الواردة في الإسكندرية والدخيلة.</p></div><div class="feature-item"><h3>إجراءات التصدير</h3><p>معالجة تصدير مبسطة مع تنسيق خطوط الملاحة.</p></div></div>')

    gen_ar_port_page("sczone.html",
        "تخليص جمركي في المنطقة الاقتصادية لقناة السويس | الروبي",
        "تخليص جمركي مرخص في المنطقة الاقتصادية لقناة السويس. إجراءات المناطق الحرة وقانون الاستثمار.",
        "/ar/ports/sczone.html", "/ports/sczone.html",
        "تخليص جمركي في المنطقة الاقتصادية لقناة السويس",
        "مرخصون للتخليص الجمركي في المنطقة الاقتصادية. خبرة في إجراءات المناطق الحرة وقانون الاستثمار.",
        '<h2 class="reveal">عن المنطقة الاقتصادية لقناة السويس</h2><p class="reveal">المنطقة الاقتصادية لقناة السويس هي أبرز مناطق التنمية الاقتصادية في مصر. تمتد على طول ممر قناة السويس وتضم مناطق صناعية وموانئ ومراكز لوجستية متعددة.</p><div class="service-features reveal-stagger"><div class="feature-item"><h3>تخليص المناطق الحرة</h3><p>إجراءات متخصصة للبضائع الداخلة والخارجة من المناطق الحرة.</p></div><div class="feature-item"><h3>إجراءات قانون الاستثمار</h3><p>تخليص وفق أحكام قانون الاستثمار للعمليات الصناعية.</p></div></div>')

    print("Arabic pages complete!")
