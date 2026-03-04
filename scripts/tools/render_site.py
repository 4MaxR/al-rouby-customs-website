#!/usr/bin/env python3
from __future__ import annotations

import json
from html import escape
from pathlib import Path
from textwrap import dedent

import site_generator as data

ROOT = data.ROOT
DOMAIN = data.DOMAIN
OG_IMAGE = data.OG_IMAGE
LASTMOD = data.LASTMOD
FORM_ACTION = data.FORM_ACTION
HOME_ALIAS = data.HOME_ALIAS
HOME_CANON = data.HOME_CANON
PREFIX = data.PREFIX
ROUTE_OVERRIDES = data.ROUTE_OVERRIDES
ROUTES = data.ROUTES
L = data.L
CONTACT_INFO = data.CONTACT_INFO
SERVICE_ORDER = data.SERVICE_ORDER
SERVICES = data.SERVICES
PORT_ORDER = data.PORT_ORDER
PORTS = data.PORTS
HOME = data.HOME
ABOUT = data.ABOUT
CONTACT = data.CONTACT
BLOGS = data.BLOGS

LOCALE_CODE = {"en": "en_US", "ar": "ar_EG", "zh": "zh_CN"}
LANGUAGE_LABELS = {"en": "English", "ar": "العربية", "zh": "中文"}
SERVICE_ICONS = {
    "customs-clearance": "&#128220;",
    "freight-forwarding": "&#128667;",
    "shipping": "&#128674;",
    "logistics": "&#128230;",
    "customs-logistics-consulting": "&#128202;",
    "aci-nafeza": "&#128196;",
}

UI = {
    "en": {
        "lang_current": "English",
        "fast_facts": "Fast Facts",
        "core_services": "Core Services",
        "core_services_text": "Practical support designed around document control, port timing, and compliant cargo movement in Egypt.",
        "port_coverage": "Port Coverage",
        "port_coverage_text": "Operational support across Egypt's main cargo gateways and zone-linked movements.",
        "testimonials": "Client Perspective",
        "quote_title": "Request a Quote",
        "quote_text": "Share the shipment profile and timing. We will review the practical route, file readiness, and next steps.",
        "quote_points": ["Review of cargo profile and port plan", "Clear communication on documents and timing", "Support aligned with customs and inland handover"],
        "name": "Full Name",
        "company": "Company",
        "phone": "Phone / WhatsApp",
        "email": "Email",
        "service_needed": "Service Needed",
        "preferred_port": "Preferred Port",
        "shipment_mode": "Shipment Mode",
        "fcl": "FCL",
        "lcl": "LCL",
        "container_count": "Container Count",
        "container_size": "Container Size",
        "message": "Shipment Details",
        "message_hint": "Share the cargo type, origin, target port, timing, and any ACI or customs questions.",
        "submit": "Send Request",
        "contact_section": "Talk to Our Team",
        "contact_cta_title": "Need a practical next step?",
        "contact_cta_text": "Send the shipment details and our team will respond with a realistic execution path.",
        "contact_cta_button": "Go to Quote Form",
        "final_cta_title": "Need customs and logistics support in Egypt?",
        "final_cta_text": "Discuss the cargo profile, document status, and port timing with a team that works around execution rather than guesswork.",
        "about_story": "Our Story",
        "about_mission": "Our Mission",
        "about_points": "Why Clients Work With Al-Rouby",
        "service_scope": "What This Service Covers",
        "service_scope_text": "Each shipment needs both the right documents and the right operating rhythm. This service helps align both.",
        "documents": "Typical Documents and Inputs",
        "faq_intro": "Common questions we receive when this service is part of the shipment workflow.",
        "port_overview": "Port Overview",
        "port_strengths": "Operational Strengths",
        "port_cargo": "Typical Cargo Profiles",
        "request_help": "Need support for this route?",
        "request_help_text": "Share the cargo profile, timing, and delivery expectations so we can outline the practical next steps.",
        "article_byline": "Published by Al-Rouby Customs | Updated February 2026",
        "article_note": "For Egypt-bound cargo, this point should be checked against the actual port, cargo profile, and document chain before shipment moves.",
        "article_cta_title": "Need practical support?",
        "article_cta_text": "Discuss your shipment, file status, or port timing with our team.",
        "article_cta_button": "Contact the Team",
    },
    "ar": {
        "lang_current": "العربية",
        "fast_facts": "لمحة سريعة",
        "core_services": "الخدمات الأساسية",
        "core_services_text": "دعم عملي مبني على ضبط المستندات والتوقيت والتنسيق التشغيلي للشحنات داخل مصر.",
        "port_coverage": "تغطية الموانئ",
        "port_coverage_text": "دعم تشغيلي عبر الموانئ المصرية الرئيسية والحركات المرتبطة بالمناطق الاقتصادية.",
        "testimonials": "انطباعات العملاء",
        "quote_title": "اطلب عرض سعر",
        "quote_text": "شارك بيانات الشحنة والتوقيت المتوقع، وسنراجع المسار العملي وجاهزية الملف والخطوات التالية.",
        "quote_points": ["مراجعة وصف البضاعة وخطة الميناء", "تواصل واضح بشأن المستندات والتوقيت", "دعم يربط التخليص بالتسليم الداخلي"],
        "name": "الاسم الكامل",
        "company": "اسم الشركة",
        "phone": "الهاتف / واتساب",
        "email": "البريد الإلكتروني",
        "service_needed": "الخدمة المطلوبة",
        "preferred_port": "الميناء المفضل",
        "shipment_mode": "نمط الشحنة",
        "fcl": "حاوية كاملة",
        "lcl": "شحنة مجمعة",
        "container_count": "عدد الحاويات",
        "container_size": "مقاس الحاوية",
        "message": "تفاصيل الشحنة",
        "message_hint": "اذكر نوع البضاعة وبلد المنشأ والميناء المستهدف والتوقيت وأي استفسارات تخص ACI أو الجمارك.",
        "submit": "إرسال الطلب",
        "contact_section": "تواصل مع فريقنا",
        "contact_cta_title": "هل تحتاج إلى خطوة عملية واضحة؟",
        "contact_cta_text": "أرسل بيانات الشحنة وسنعود إليك بمسار تنفيذ واقعي وواضح.",
        "contact_cta_button": "الانتقال إلى نموذج الطلب",
        "final_cta_title": "هل تحتاج إلى دعم جمركي ولوجستي في مصر؟",
        "final_cta_text": "ناقش معنا وصف الشحنة وحالة المستندات وتوقيت الميناء مع فريق يركز على التنفيذ العملي.",
        "about_story": "قصتنا",
        "about_mission": "مهمتنا",
        "about_points": "لماذا يعمل العملاء مع الروبي",
        "service_scope": "ماذا تغطي هذه الخدمة؟",
        "service_scope_text": "كل شحنة تحتاج إلى ملف صحيح وإيقاع تنفيذي منضبط. هذه الخدمة تساعد على ضبط الاثنين معاً.",
        "documents": "المستندات والبيانات المعتادة",
        "faq_intro": "أكثر الأسئلة التي نتلقاها عندما تكون هذه الخدمة جزءاً من مسار الشحنة.",
        "port_overview": "نظرة على الميناء",
        "port_strengths": "نقاط القوة التشغيلية",
        "port_cargo": "أنماط البضائع المعتادة",
        "request_help": "هل تحتاج إلى دعم لهذا المسار؟",
        "request_help_text": "شارك وصف البضاعة والتوقيت ومتطلبات التسليم حتى نوضح لك الخطوات العملية التالية.",
        "article_byline": "منشور بواسطة الروبي | آخر تحديث فبراير 2026",
        "article_note": "في الشحنات المتجهة إلى مصر، يجب مراجعة هذه النقطة وفق الميناء الفعلي وطبيعة البضاعة وتسلسل المستندات قبل تحرك الشحنة.",
        "article_cta_title": "هل تحتاج إلى دعم عملي؟",
        "article_cta_text": "ناقش معنا حالة الشحنة أو الملف أو توقيت الميناء مع فريقنا.",
        "article_cta_button": "تواصل مع الفريق",
    },
    "zh": {
        "lang_current": "中文",
        "fast_facts": "快速概览",
        "core_services": "核心服务",
        "core_services_text": "围绕单证、时间节点与口岸执行节奏，为进入埃及市场的货物提供务实支持。",
        "port_coverage": "港口覆盖",
        "port_coverage_text": "覆盖埃及主要港口及与经济区相关的操作场景。",
        "testimonials": "客户视角",
        "quote_title": "获取报价",
        "quote_text": "欢迎提交货物信息和时间计划，我们会先判断实务路径、文件准备程度以及下一步安排。",
        "quote_points": ["先看货物属性和目标港口", "明确文件与时点要求", "把清关与放行后的交接一起考虑"],
        "name": "联系人姓名",
        "company": "公司名称",
        "phone": "电话 / WhatsApp",
        "email": "电子邮箱",
        "service_needed": "所需服务",
        "preferred_port": "目标港口",
        "shipment_mode": "出运模式",
        "fcl": "整箱",
        "lcl": "拼箱",
        "container_count": "箱量",
        "container_size": "箱型",
        "message": "货运说明",
        "message_hint": "请说明货物类型、起运地、目标港口、时间安排，以及任何 ACI 或清关问题。",
        "submit": "发送需求",
        "contact_section": "联系执行团队",
        "contact_cta_title": "需要一个更清晰的下一步？",
        "contact_cta_text": "把货物情况发给我们，我们会根据实际操作条件给出执行建议。",
        "contact_cta_button": "前往报价表单",
        "final_cta_title": "需要埃及清关与物流支持？",
        "final_cta_text": "欢迎与团队讨论货物属性、文件状态和港口节奏，重点放在实际可执行性上。",
        "about_story": "我们的方式",
        "about_mission": "我们的目标",
        "about_points": "客户选择 Al-Rouby 的原因",
        "service_scope": "这项服务通常覆盖什么",
        "service_scope_text": "一票货既需要正确的文件，也需要合适的执行节奏。这项服务就是把两者连接起来。",
        "documents": "常见文件与输入资料",
        "faq_intro": "当这项服务进入实际项目时，客户最常提出的问题通常包括以下几类。",
        "port_overview": "港口概况",
        "port_strengths": "操作重点",
        "port_cargo": "常见货物类型",
        "request_help": "需要这条线路的支持？",
        "request_help_text": "欢迎提供货物情况、时间计划和交付要求，我们会先梳理实际可行的下一步。",
        "article_byline": "由 Al-Rouby Customs 发布 | 更新于 2026年2月",
        "article_note": "针对进入埃及的货物，这一点应结合实际港口、货物说明和文件链条逐项确认，而不是等到装运后再被动修正。",
        "article_cta_title": "需要更务实的支持？",
        "article_cta_text": "欢迎联系团队讨论货运状态、文件准备和港口时间节点。",
        "article_cta_button": "联系团队",
    },
}

BLOG_OPENING_NOTE = {
    "customs-clearance-guide-egypt": {
        "en": "In the Egyptian market, customs clearance should be treated as an operating workflow rather than a last-minute administrative task. Importers usually get better results when customs preparation starts while documents, payment references, and cargo timing can still be adjusted.",
        "ar": "في السوق المصري، من الأفضل التعامل مع التخليص الجمركي كمسار تشغيلي كامل وليس كخطوة إدارية متأخرة. كلما بدأ تجهيز الملف مبكراً، كان من الأسهل معالجة اختلافات المستندات قبل أن تتحول إلى تأخير أو تكلفة إضافية.",
        "zh": "在埃及市场，清关不应被当成最后一刻才处理的行政手续，而应当视为一条完整的执行链。越早开始准备单证、付款参考资料和到港节奏，越容易在发运前就消除会影响放行的问题。",
    },
    "aci-system-guide": {
        "en": "ACI preparation works best when importers, suppliers, and banks treat the process as part of shipment planning from the start. Most avoidable problems appear when one party assumes another party has already validated the file details.",
        "ar": "ينجح ملف ACI أكثر عندما يعتبره المستورد والمورد والبنك جزءاً من تخطيط الشحنة من البداية. كثير من المشكلات القابلة للتجنب تظهر عندما يفترض كل طرف أن الطرف الآخر راجع البيانات مسبقاً.",
        "zh": "ACI 最有效的推进方式，是让进口商、供应商和银行从一开始就把它纳入装运计划。很多本可避免的问题，都出在各方默认别人已经核对过文件细节。",
    },
    "sea-freight-types": {
        "en": "The container decision is commercial, operational, and customs-related at the same time. Importers usually make stronger decisions when they compare the full landed workflow instead of only comparing headline freight rates.",
        "ar": "قرار اختيار نمط الحاوية ليس قراراً سعرياً فقط، بل هو قرار تشغيلي وتجاري وجمركي في الوقت نفسه. وتكون النتيجة أفضل عندما يقارن المستورد المسار الكامل حتى التسليم النهائي، وليس فقط سعر الشحن البحري.",
        "zh": "整箱还是拼箱，不只是一个海运费比较题，而是同时涉及商业节奏、操作控制和清关准备。真正稳妥的判断，通常来自对完整落地流程的比较，而不只是比较运价。",
    },
    "egypt-port-fees": {
        "en": "Port cost in Egypt is usually a timing issue as much as it is a tariff or terminal issue. Importers who ask the right operational questions early are often better positioned to reduce avoidable exposure after arrival.",
        "ar": "تكلفة الميناء في مصر ترتبط غالباً بالتوقيت التنفيذي بقدر ارتباطها ببنود الرسوم أو المشغل. وكلما طرح المستورد الأسئلة التشغيلية الصحيحة مبكراً، زادت فرص تقليل التكلفة التي يمكن تجنبها بعد الوصول.",
        "zh": "埃及港口费用往往既是收费问题，也是时间管理问题。越早问清楚放行、提货、仓库接收和特殊监管要求，越有机会减少到港后的额外费用暴露。",
    },
    "hs-code-guide": {
        "en": "HS classification is one of the earliest decisions that shapes duty exposure, permit requirements, and document preparation. When importers validate coding early, the rest of the shipment plan usually becomes easier to control.",
        "ar": "تصنيف HS من أوائل القرارات التي تحدد الرسوم والمتطلبات الترخيصية وجاهزية الملف. وعندما يتم التحقق منه مبكراً، يصبح التحكم في باقي مسار الشحنة أكثر سهولة.",
        "zh": "HS 编码往往是最早影响税费、许可证要求和单证准备质量的关键判断之一。越早确认分类，后续的清关与到港安排就越容易控制。",
    },
}

BLOG_CLOSING_NOTE = {
    "en": "A more reliable import workflow starts with earlier review, clearer ownership of each document, and realistic timing assumptions before cargo reaches the port.",
    "ar": "المسار الأكثر استقراراً يبدأ دائماً بمراجعة مبكرة وبتحديد واضح لمسؤولية كل مستند وبافتراضات زمنية واقعية قبل وصول الشحنة إلى الميناء.",
    "zh": "更稳定的进口流程，通常始于更早的文件复核、更清晰的责任分工，以及在货物到港前就建立起符合现实的时间假设。",
}


def html(text: str) -> str:
    return escape(str(text), quote=True)


def localized_base_path(lang: str, base_path: str) -> str:
    return ROUTE_OVERRIDES.get(lang, {}).get(base_path, base_path)


def path_for(lang: str, base_path: str) -> str:
    if base_path == "/":
        return HOME_ALIAS[lang]
    return f"{PREFIX[lang]}{localized_base_path(lang, base_path)}"


def canon_url(lang: str, base_path: str) -> str:
    if base_path == "/":
        return HOME_CANON[lang]
    return f"{DOMAIN}{PREFIX[lang]}{localized_base_path(lang, base_path)}"


def file_path(lang: str, base_path: str) -> Path:
    if base_path == "/":
        return ROOT / ("index.html" if lang == "en" else Path(PREFIX[lang].lstrip("/")) / "index.html")
    rel = Path(localized_base_path(lang, base_path).lstrip("/"))
    return ROOT / rel if lang == "en" else ROOT / PREFIX[lang].lstrip("/") / rel


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def json_ld(data_obj: dict) -> str:
    return '<script type="application/ld+json">\n' + json.dumps(data_obj, ensure_ascii=False, indent=2) + "\n</script>"


def favicon_links() -> str:
    return dedent(
        """
        <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png" />
        <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png" />
        <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
        <link rel="manifest" href="/site.webmanifest" />
        """
    ).strip()


def fonts_block() -> str:
    return dedent(
        """
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
        <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&family=Noto+Sans+SC:wght@400;500;700&display=swap" rel="stylesheet" />
        """
    ).strip()


def organization_schema(lang: str) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": L[lang]["site"],
        "url": HOME_CANON[lang],
        "logo": OG_IMAGE,
        "contactPoint": {
            "@type": "ContactPoint",
            "telephone": "+201000628855",
            "contactType": "customer service",
            "availableLanguage": ["English", "Arabic", "Chinese"],
        },
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Building 615, TEDA",
            "addressLocality": "Ain Sokhna",
            "addressRegion": "Suez",
            "addressCountry": "EG",
        },
        "sameAs": [
            "https://www.facebook.com/RisElRouby",
            "https://www.linkedin.com/company/al-rouby/",
        ],
    }


def local_business_schema(lang: str, description: str) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": L[lang]["site"],
        "alternateName": "Al-Rouby Customs" if lang != "en" else "الروبي للتخليص الجمركي",
        "description": description,
        "url": HOME_CANON[lang],
        "telephone": "+201000628855",
        "email": CONTACT_INFO["email"],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Building 615, TEDA",
            "addressLocality": "Ain Sokhna",
            "addressRegion": "Suez",
            "addressCountry": "EG",
        },
        "image": OG_IMAGE,
        "areaServed": {"@type": "Country", "name": "Egypt"},
        "sameAs": [
            "https://www.facebook.com/RisElRouby",
            "https://www.linkedin.com/company/al-rouby/",
        ],
    }


def breadcrumb_schema(crumbs: list[tuple[str, str]]) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": index,
                "name": name,
                "item": url,
            }
            for index, (name, url) in enumerate(crumbs, start=1)
        ],
    }


def faq_schema(faqs: list[tuple[str, str]]) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": question,
                "acceptedAnswer": {"@type": "Answer", "text": answer},
            }
            for question, answer in faqs
        ],
    }


def service_schema(lang: str, name: str, description: str) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": name,
        "provider": {"@type": "Organization", "name": L[lang]["site"]},
        "areaServed": {"@type": "Country", "name": "Egypt"},
        "description": description,
    }


def article_schema(lang: str, title: str, description: str, url: str) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": description,
        "datePublished": LASTMOD,
        "dateModified": LASTMOD,
        "mainEntityOfPage": url,
        "inLanguage": L[lang]["html_lang"],
        "image": OG_IMAGE,
        "author": {"@type": "Organization", "name": L[lang]["site"]},
        "publisher": {
            "@type": "Organization",
            "name": L[lang]["site"],
            "logo": {"@type": "ImageObject", "url": OG_IMAGE},
        },
    }


def alternate_links(base_path: str) -> str:
    links = [
        f'<link rel="alternate" hreflang="{lang}" href="{canon_url(lang, base_path)}" />'
        for lang in ("en", "ar", "zh")
    ]
    links.append(f'<link rel="alternate" hreflang="x-default" href="{canon_url("en", base_path)}" />')
    return "\n".join(links)


def head(
    lang: str,
    base_path: str,
    title: str,
    meta: str,
    schemas: list[dict],
    *,
    robots: str = "index, follow",
    og_type: str = "website",
    include_alternates: bool = True,
    include_lang_init: bool = False,
) -> str:
    canonical = canon_url(lang, base_path)
    alternates = alternate_links(base_path) if include_alternates else ""
    lang_init = '<script src="/js/lang-init.js"></script>\n' if include_lang_init else ""
    schema_block = "\n".join(json_ld(item) for item in schemas)
    return dedent(
        f"""\
        <!doctype html>
        <html lang="{L[lang]["html_lang"]}"{L[lang]["dir"]}>
          <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>{html(title)}</title>
            <meta name="description" content="{html(meta)}" />
            <meta name="author" content="{html(L[lang]["site"])}" />
            <meta name="robots" content="{html(robots)}" />
            <link rel="canonical" href="{canonical}" />
            {alternates}
            <meta property="og:site_name" content="{html(L[lang]["site"])}" />
            <meta property="og:title" content="{html(title)}" />
            <meta property="og:description" content="{html(meta)}" />
            <meta property="og:url" content="{canonical}" />
            <meta property="og:type" content="{og_type}" />
            <meta property="og:image" content="{OG_IMAGE}" />
            <meta property="og:locale" content="{LOCALE_CODE[lang]}" />
            <meta name="twitter:card" content="summary_large_image" />
            <meta name="twitter:title" content="{html(title)}" />
            <meta name="twitter:description" content="{html(meta)}" />
            <meta name="twitter:image" content="{OG_IMAGE}" />
            {favicon_links()}
            <meta name="theme-color" content="#0b1f3a" />
            {fonts_block()}
            {lang_init}<script src="/js/theme-init.js"></script>
            <link rel="stylesheet" href="/css/style.css" />
            {schema_block}
          </head>
        """
    )


def language_switcher(lang: str) -> str:
    options = "\n".join(
        f'<button type="button" class="lang-option{" is-current" if code == lang else ""}" role="menuitem" data-lang="{code}" aria-label="{html(LANGUAGE_LABELS[code])}">{html(LANGUAGE_LABELS[code])}</button>'
        for code in ("en", "ar", "zh")
    )
    return dedent(
        f"""\
        <div class="language-switcher" data-language-switcher>
          <button type="button" class="lang-toggle" id="langToggle" aria-haspopup="menu" aria-expanded="false" aria-controls="langMenu" aria-label="{html(L[lang]["lang_switch"])}">
            <span>{html(UI[lang]["lang_current"])}</span>
            <span class="dropdown-arrow" aria-hidden="true">&#9660;</span>
          </button>
          <div class="lang-menu" id="langMenu" role="menu" aria-label="{html(L[lang]["lang"])}">
            {options}
          </div>
        </div>
        """
    ).strip()


def header(lang: str) -> str:
    services_menu = "".join(
        f'<a href="{path_for(lang, f"/services/{slug}.html")}">{html(SERVICES[slug][lang]["name"])}</a>'
        for slug in SERVICE_ORDER
    )
    ports_menu = "".join(
        f'<a href="{path_for(lang, f"/ports/{slug}.html")}">{html(PORTS[slug][lang]["name"])}</a>'
        for slug in PORT_ORDER
    )
    return dedent(
        f"""\
        <header>
          <div class="nav-container">
            <a class="logo" href="{path_for(lang, "/")}">{html(L[lang]["site"])}</a>
            <button class="hamburger" id="menuBtn" aria-label="{html(L[lang]["menu"])}" aria-expanded="false" aria-controls="navLinks">&#9776;</button>
            <nav class="nav-links" id="navLinks" role="navigation" aria-label="{html(L[lang]["nav"])}">
              <a href="{path_for(lang, "/")}" data-nav-key="home">{html(L[lang]["home"])}</a>
              <a href="{path_for(lang, "/about.html")}" data-nav-key="about">{html(L[lang]["about"])}</a>
              <div class="nav-dropdown">
                <a href="{path_for(lang, "/services/customs-clearance.html")}" data-nav-key="services">{html(L[lang]["services"])} <span class="dropdown-arrow" aria-hidden="true">&#9660;</span></a>
                <div class="dropdown-menu">{services_menu}</div>
              </div>
              <div class="nav-dropdown">
                <a href="{path_for(lang, "/ports/ain-sokhna.html")}" data-nav-key="ports">{html(L[lang]["ports"])} <span class="dropdown-arrow" aria-hidden="true">&#9660;</span></a>
                <div class="dropdown-menu">{ports_menu}</div>
              </div>
              <a href="{path_for(lang, "/blog/customs-clearance-guide-egypt.html")}" data-nav-key="blog">{html(L[lang]["blog"])}</a>
              <a href="{path_for(lang, "/contact.html")}" data-nav-key="contact">{html(L[lang]["contact"])}</a>
              {language_switcher(lang)}
              <button id="themeToggle" class="theme-toggle" aria-label="{html(L[lang]["theme"])}">&#127769;</button>
              <a href="{path_for(lang, "/")}#quote" class="btn btn-primary btn-nav">{html(L[lang]["quote"])}</a>
            </nav>
          </div>
        </header>
        """
    ).strip()


def breadcrumbs(lang: str, items: list[tuple[str, str | None]]) -> str:
    nodes = []
    for name, href in items:
        if href:
            nodes.append(f'<li><a href="{href}">{html(name)}</a></li>')
        else:
            nodes.append(f'<li><span aria-current="page">{html(name)}</span></li>')
    return '<nav class="breadcrumbs" aria-label="Breadcrumb"><ol>' + "".join(nodes) + "</ol></nav>"


def footer(lang: str) -> str:
    services_links = "".join(
        f'<li><a href="{path_for(lang, f"/services/{slug}.html")}">{html(SERVICES[slug][lang]["name"])}</a></li>'
        for slug in SERVICE_ORDER
    )
    ports_links = "".join(
        f'<li><a href="{path_for(lang, f"/ports/{slug}.html")}">{html(PORTS[slug][lang]["name"])}</a></li>'
        for slug in PORT_ORDER
    )
    return dedent(
        f"""\
        <footer>
          <div class="footer-grid">
            <div class="footer-col">
              <h3>{html(L[lang]["site"])}</h3>
              <p class="footer-about">{html(L[lang]["footer_about"])}</p>
            </div>
            <div class="footer-col">
              <h4>{html(L[lang]["services"])}</h4>
              <ul>{services_links}</ul>
            </div>
            <div class="footer-col">
              <h4>{html(L[lang]["ports"])}</h4>
              <ul>{ports_links}</ul>
            </div>
            <div class="footer-col">
              <h4>{html(L[lang]["contact"])}</h4>
              <ul>
                <li><a href="mailto:{CONTACT_INFO["email"]}">{html(CONTACT_INFO["email"])}</a></li>
                <li><a href="{CONTACT_INFO["phone_href"]}">{html(CONTACT_INFO["phone"])}</a></li>
                <li><a href="{CONTACT_INFO["map_href"]}" target="_blank" rel="noopener noreferrer">{html(CONTACT_INFO["map"][lang])}</a></li>
                <li><a href="https://www.facebook.com/RisElRouby" target="_blank" rel="noopener noreferrer">Facebook</a></li>
                <li><a href="https://www.linkedin.com/company/al-rouby/" target="_blank" rel="noopener noreferrer">LinkedIn</a></li>
              </ul>
            </div>
          </div>
          <div class="footer-bottom">
            <p class="footer-copyright">{L[lang]["rights"]}</p>
            <p class="footer-credit">{L[lang]["credit"]}</p>
          </div>
        </footer>
        """
    ).strip()


def back_to_top(lang: str) -> str:
    return f'<button id="backToTop" class="back-to-top" aria-label="{html(L[lang]["top"])}">&uarr;</button>'


def service_cards(lang: str) -> str:
    cards = []
    arrow = "&larr;" if lang == "ar" else "&rarr;"
    for slug in SERVICE_ORDER:
        item = SERVICES[slug][lang]
        cards.append(
            f'<article class="service-card"><div class="service-icon" aria-hidden="true">{SERVICE_ICONS[slug]}</div><h3>{html(item["name"])}</h3><p>{html(item.get("card_summary", item["summary"]))}</p><a href="{path_for(lang, f"/services/{slug}.html")}" class="service-link">{html(L[lang]["read_more"])} {arrow}</a></article>'
        )
    return "".join(cards)


def port_cards(lang: str) -> str:
    cards = []
    arrow = "&larr;" if lang == "ar" else "&rarr;"
    for slug in PORT_ORDER:
        item = PORTS[slug][lang]
        cards.append(
            f'<article class="port-card"><h3>&#9875; {html(item["name"])}</h3><p>{html(item["overview"])}</p><a href="{path_for(lang, f"/ports/{slug}.html")}" class="service-link">{html(L[lang]["read_more"])} {arrow}</a></article>'
        )
    return "".join(cards)


def quote_section(lang: str) -> str:
    point_items = "".join(
        f'<li><span class="check-icon" aria-hidden="true">&#10004;</span>{html(point)}</li>'
        for point in UI[lang]["quote_points"]
    )
    service_options = "".join(
        f'<option value="{html(SERVICES[slug][lang]["name"])}">{html(SERVICES[slug][lang]["name"])}</option>'
        for slug in SERVICE_ORDER
    )
    port_options = "".join(
        f'<option value="{html(PORTS[slug][lang]["name"])}">{html(PORTS[slug][lang]["name"])}</option>'
        for slug in PORT_ORDER
    )
    return dedent(
        f"""\
        <section id="quote" class="quote">
          <div class="container quote-grid">
            <div class="quote-info reveal">
              <h2>{html(UI[lang]["quote_title"])}</h2>
              <p>{html(UI[lang]["quote_text"])}</p>
              <ul class="quote-points">{point_items}</ul>
            </div>
            <form class="quote-form reveal" action="{FORM_ACTION}" method="POST">
              <input type="hidden" name="_subject" value="{html(L[lang]["site"])} Quote Request" />
              <div class="form-row">
                <label>{html(UI[lang]["name"])}<input type="text" name="name" required minlength="2" /></label>
                <label>{html(UI[lang]["company"])}<input type="text" name="company" /></label>
              </div>
              <div class="form-row">
                <label>{html(UI[lang]["phone"])}<input type="tel" name="phone" required /></label>
                <label>{html(UI[lang]["email"])}<input type="email" name="email" /></label>
              </div>
              <div class="form-row">
                <label>{html(UI[lang]["service_needed"])}<select name="service"><option value="">-</option>{service_options}</select></label>
                <label>{html(UI[lang]["preferred_port"])}<select name="port"><option value="">-</option>{port_options}</select></label>
              </div>
              <div class="shipment-mode-box">
                <span class="shipment-label">{html(UI[lang]["shipment_mode"])}</span>
                <div class="radio-group">
                  <label class="radio-item"><input type="radio" name="shipment_mode" value="FCL" /> {html(UI[lang]["fcl"])}</label>
                  <label class="radio-item"><input type="radio" name="shipment_mode" value="LCL" /> {html(UI[lang]["lcl"])}</label>
                </div>
                <div id="fcl-details">
                  <div class="container-input-col"><label>{html(UI[lang]["container_count"])}</label><input type="number" min="1" name="container_count" /></div>
                  <div class="container-input-col"><label>{html(UI[lang]["container_size"])}</label><input type="text" name="container_size" /></div>
                </div>
              </div>
              <label>{html(UI[lang]["message"])}<textarea name="message" rows="5" required placeholder="{html(UI[lang]["message_hint"])}"></textarea></label>
              <button type="submit" class="btn btn-accent btn-submit">{html(UI[lang]["submit"])}</button>
            </form>
          </div>
        </section>
        """
    ).strip()


def contact_section(lang: str) -> str:
    cards = [
        (L[lang]["contact_cards"][0], f'<a href="mailto:{CONTACT_INFO["email"]}">{html(CONTACT_INFO["email"])}</a>'),
        (L[lang]["contact_cards"][1], f'<a href="{CONTACT_INFO["phone_href"]}">{html(CONTACT_INFO["phone"])}</a>'),
        (L[lang]["contact_cards"][2], f'<a href="{CONTACT_INFO["map_href"]}" target="_blank" rel="noopener noreferrer">{html(CONTACT_INFO["map"][lang])}</a>'),
    ]
    card_html = "".join(
        f'<div class="contact-card"><h3>{html(title)}</h3><p>{body}</p></div>'
        for title, body in cards
    )
    return dedent(
        f"""\
        <section class="contact">
          <div class="container">
            <div class="section-header reveal">
              <h2>{html(UI[lang]["contact_section"])}</h2>
              <p>{html(L[lang]["contact_text"])}</p>
            </div>
            <div class="contact-grid reveal-stagger">{card_html}</div>
          </div>
        </section>
        """
    ).strip()


def final_cta(lang: str) -> str:
    return dedent(
        f"""\
        <section class="final-cta">
          <div class="container reveal">
            <h2>{html(UI[lang]["final_cta_title"])}</h2>
            <p>{html(UI[lang]["final_cta_text"])}</p>
            <div class="cta-buttons">
              <a href="{path_for(lang, "/")}#quote" class="btn btn-white">{html(L[lang]["quote"])}</a>
              <a href="{path_for(lang, "/contact.html")}" class="btn btn-secondary">{html(L[lang]["contact"])}</a>
            </div>
          </div>
        </section>
        """
    ).strip()


def related_services(lang: str, slugs: list[str]) -> str:
    arrow = "&larr;" if lang == "ar" else "&rarr;"
    cards = []
    for slug in slugs:
        item = SERVICES[slug][lang]
        cards.append(
            f'<div class="related-card"><h3>{html(item["name"])}</h3><p>{html(item["summary"])}</p><a href="{path_for(lang, f"/services/{slug}.html")}">{html(L[lang]["read_more"])} {arrow}</a></div>'
        )
    return dedent(
        f"""\
        <section class="related-services">
          <div class="container">
            <div class="section-header reveal"><h2>{html(L[lang]["related"])}</h2></div>
            <div class="related-grid reveal-stagger">{"".join(cards)}</div>
          </div>
        </section>
        """
    ).strip()


def page_shell(
    lang: str,
    base_path: str,
    title: str,
    meta: str,
    body: str,
    schemas: list[dict],
    *,
    include_alternates: bool = True,
    robots: str = "index, follow",
    og_type: str = "website",
    include_lang_init: bool = False,
) -> str:
    return (
        head(
            lang,
            base_path,
            title,
            meta,
            schemas,
            robots=robots,
            og_type=og_type,
            include_alternates=include_alternates,
            include_lang_init=include_lang_init,
        )
        + f'  <body id="top" data-locale="{lang}" data-route-base="{html("" if base_path == "/404.html" else base_path)}">\n'
        + f'    <a class="skip-link" href="#main">{html(L[lang]["skip"])}</a>\n'
        + body
        + "\n    <script src=\"/js/main.js\" defer></script>\n"
        + "  </body>\n</html>\n"
    )


def render_home(lang: str) -> str:
    data_obj = HOME[lang]
    schemas = [organization_schema(lang), local_business_schema(lang, data_obj["meta"]), faq_schema(data_obj["faq"])]
    stats = "".join(
        f'<div class="trust-item"><span class="trust-number" aria-hidden="true">{html(stat)}</span><p>{html(label)}</p></div>'
        for stat, label in data_obj["stats"]
    )
    process = "".join(
        f'<article class="step"><div class="step-number" aria-hidden="true">{index}</div><h3>{html(title)}</h3><p>{html(text)}</p></article>'
        for index, (title, text) in enumerate(data_obj["process"], start=1)
    )
    reviews = "".join(
        f'<article class="review-card"><p>{html(review)}</p><div class="client-info"><h4>{html(L[lang]["site"])}</h4><span>{html(role)}</span></div></article>'
        for review, role in data_obj["reviews"]
    )
    faq_items = "".join(
        f'<div class="faq-item"><button class="faq-question" type="button">{html(question)} <span aria-hidden="true">+</span></button><div class="faq-answer"><p>{html(answer)}</p></div></div>'
        for question, answer in data_obj["faq"]
    )
    body = dedent(
        f"""\
        {header(lang)}
        <main id="main">
          <section class="container hero">
            <div class="hero-content reveal">
              <h1>{html(data_obj["hero_title"])}</h1>
              <p>{html(data_obj["hero_text"])}</p>
              <p class="service-summary">{html(data_obj["hero_summary"])}</p>
              <div class="hero-buttons">
                <a href="{path_for(lang, "/")}#quote" class="btn btn-primary">{html(L[lang]["quote"])}</a>
                <a href="{path_for(lang, "/about.html")}" class="btn btn-secondary">{html(L[lang]["about"])}</a>
              </div>
            </div>
            <div class="hero-card reveal">
              <h3>{html(UI[lang]["fast_facts"])}</h3>
              <ul>{"".join(f'<li><span class="check-icon" aria-hidden="true">&#10004;</span>{html(point)}</li>' for point in data_obj["hero_points"])}</ul>
            </div>
          </section>
          <section class="trust"><div class="container"><div class="trust-grid reveal-stagger">{stats}</div></div></section>
          <section class="services">
            <div class="container">
              <div class="section-header reveal"><h2>{html(UI[lang]["core_services"])}</h2><p>{html(UI[lang]["core_services_text"])}</p></div>
              <div class="services-grid reveal-stagger">{service_cards(lang)}</div>
            </div>
          </section>
          <section class="services" style="background: var(--bg-body);">
            <div class="container">
              <div class="section-header reveal"><h2>{html(UI[lang]["port_coverage"])}</h2><p>{html(UI[lang]["port_coverage_text"])}</p></div>
              <div class="ports-grid reveal-stagger">{port_cards(lang)}</div>
            </div>
          </section>
          <section class="process"><div class="container"><h2 class="reveal">{html(L[lang]["how"])}</h2><div class="process-steps reveal-stagger">{process}</div></div></section>
          <section class="testimonials"><div class="container"><div class="section-header reveal"><h2>{html(UI[lang]["testimonials"])}</h2></div><div class="testimonial-grid reveal-stagger">{reviews}</div></div></section>
          <section id="faq"><div class="container faq-container reveal"><div class="section-header"><h2>{html(L[lang]["faq"])}</h2></div>{faq_items}</div></section>
          {quote_section(lang)}
          {contact_section(lang)}
          {final_cta(lang)}
        </main>
        {footer(lang)}
        {back_to_top(lang)}
        """
    ).strip()
    return page_shell(lang, "/", data_obj["title"], data_obj["meta"], body, schemas, include_lang_init=(lang == "en"))


def render_about(lang: str) -> str:
    data_obj = ABOUT[lang]
    schemas = [organization_schema(lang), breadcrumb_schema([(L[lang]["home"], HOME_CANON[lang]), (L[lang]["about"], canon_url(lang, "/about.html"))])]
    story = "".join(f'<p class="reveal">{html(paragraph)}</p>' for paragraph in data_obj["story"])
    points = "".join(f'<div class="feature-item"><h3>{html(title)}</h3><p>{html(text)}</p></div>' for title, text in data_obj["points"])
    body = dedent(
        f"""\
        {header(lang)}
        {breadcrumbs(lang, [(L[lang]["home"], path_for(lang, "/")), (L[lang]["about"], None)])}
        <main id="main">
          <section class="page-hero"><div class="container reveal"><h1>{html(L[lang]["about"])}</h1><p>{html(data_obj["hero"])}</p></div></section>
          <section class="content-section">
            <div class="container">
              <h2 class="reveal">{html(UI[lang]["about_story"])}</h2>{story}
              <h2 class="reveal">{html(UI[lang]["about_mission"])}</h2><p class="reveal">{html(data_obj["mission"])}</p>
              <h2 class="reveal">{html(UI[lang]["about_points"])}</h2><div class="service-features reveal-stagger">{points}</div>
              <div class="cta-box reveal"><h3>{html(UI[lang]["contact_cta_title"])}</h3><p>{html(UI[lang]["contact_cta_text"])}</p><a href="{path_for(lang, "/")}#quote" class="btn btn-accent">{html(L[lang]["quote"])}</a></div>
            </div>
          </section>
        </main>
        {footer(lang)}
        {back_to_top(lang)}
        """
    ).strip()
    return page_shell(lang, "/about.html", data_obj["title"], data_obj["meta"], body, schemas)


def render_contact(lang: str) -> str:
    data_obj = CONTACT[lang]
    schemas = [organization_schema(lang), breadcrumb_schema([(L[lang]["home"], HOME_CANON[lang]), (L[lang]["contact"], canon_url(lang, "/contact.html"))])]
    body = dedent(
        f"""\
        {header(lang)}
        {breadcrumbs(lang, [(L[lang]["home"], path_for(lang, "/")), (L[lang]["contact"], None)])}
        <main id="main">
          <section class="page-hero"><div class="container reveal"><h1>{html(L[lang]["contact"])}</h1><p>{html(data_obj["hero"])}</p></div></section>
          {contact_section(lang)}
          <section class="content-section"><div class="container"><div class="cta-box reveal"><h3>{html(UI[lang]["contact_cta_title"])}</h3><p>{html(UI[lang]["contact_cta_text"])}</p><a href="{path_for(lang, "/")}#quote" class="btn btn-accent">{html(UI[lang]["contact_cta_button"])}</a></div></div></section>
        </main>
        {footer(lang)}
        {back_to_top(lang)}
        """
    ).strip()
    return page_shell(lang, "/contact.html", data_obj["title"], data_obj["meta"], body, schemas)


def render_service(lang: str, slug: str) -> str:
    data_obj = SERVICES[slug][lang]
    base_path = f"/services/{slug}.html"
    schemas = [
        organization_schema(lang),
        breadcrumb_schema([(L[lang]["home"], HOME_CANON[lang]), (L[lang]["services"], canon_url(lang, base_path)), (data_obj["name"], canon_url(lang, base_path))]),
        service_schema(lang, data_obj["name"], data_obj["summary"]),
        faq_schema(data_obj["faq"]),
    ]
    faq_items = "".join(f'<div class="faq-item"><button class="faq-question" type="button">{html(question)} <span aria-hidden="true">+</span></button><div class="faq-answer"><p>{html(answer)}</p></div></div>' for question, answer in data_obj["faq"])
    related = data_obj.get("related", [item for item in SERVICE_ORDER if item != slug][:3])
    if "sections" in data_obj:
        sections = data_obj["sections"]
        help_cards = "".join(
            f'<div class="feature-item"><h3>{html(title)}</h3><p>{html(text)}</p></div>'
            for title, text in sections["help"]["cards"]
        )
        who_bullets = "".join(f'<li>{html(item)}</li>' for item in sections["who"]["bullets"])
        how_cards = "".join(
            f'<div class="feature-item"><h3>{html(title)}</h3><p>{html(text)}</p></div>'
            for title, text in sections["how"]["cards"]
        )
        provide_items = "".join(f'<li>{html(item)}</li>' for item in sections["provide"]["items"])
        body = dedent(
            f"""\
            {header(lang)}
            {breadcrumbs(lang, [(L[lang]["home"], path_for(lang, "/")), (L[lang]["services"], path_for(lang, base_path)), (data_obj["name"], None)])}
            <main id="main">
              <section class="page-hero"><div class="container reveal"><h1>{html(data_obj["name"])}</h1><p>{html(data_obj["hero"])}</p></div></section>
              <section class="content-section"><div class="container"><h2 class="reveal">{html(sections["help"]["title"])}</h2><p class="reveal">{html(sections["help"]["intro"])}</p><div class="service-features reveal-stagger">{help_cards}</div><h2 class="reveal">{html(sections["who"]["title"])}</h2><p class="reveal">{html(sections["who"]["intro"])}</p><ul class="reveal">{who_bullets}</ul><h2 class="reveal">{html(sections["how"]["title"])}</h2><div class="service-features reveal-stagger">{how_cards}</div><h2 class="reveal">{html(sections["provide"]["title"])}</h2><ul class="reveal">{provide_items}</ul></div></section>
              <section id="faq"><div class="container faq-container reveal"><div class="section-header"><h2>{html(L[lang]["faq"])}</h2><p>{html(UI[lang]["faq_intro"])}</p></div>{faq_items}</div></section>
              <section class="content-section"><div class="container"><div class="cta-box reveal"><h3>{html(sections["cta"]["title"])}</h3><p>{html(sections["cta"]["text"])}</p><a href="{path_for(lang, "/")}#quote" class="btn btn-accent">{html(L[lang]["quote"])}</a></div></div></section>
              {related_services(lang, related)}
            </main>
            {footer(lang)}
            {back_to_top(lang)}
            """
        ).strip()
    else:
        feature_cards = "".join(f'<div class="feature-item"><h3>{html(feature)}</h3><p>{html(data_obj["summary"])}</p></div>' for feature in data_obj["features"])
        body = dedent(
            f"""\
            {header(lang)}
            {breadcrumbs(lang, [(L[lang]["home"], path_for(lang, "/")), (L[lang]["services"], path_for(lang, base_path)), (data_obj["name"], None)])}
            <main id="main">
              <section class="page-hero"><div class="container reveal"><h1>{html(data_obj["name"])}</h1><p>{html(data_obj["hero"])}</p></div></section>
              <section class="content-section"><div class="container"><h2 class="reveal">{html(UI[lang]["service_scope"])}</h2><p class="reveal">{html(data_obj["summary"])}</p><p class="reveal">{html(UI[lang]["service_scope_text"])}</p><div class="service-features reveal-stagger">{feature_cards}</div><h2 class="reveal">{html(UI[lang]["documents"])}</h2><ul class="reveal">{"".join(f'<li>{html(item)}</li>' for item in data_obj["bullets"])}</ul></div></section>
              <section id="faq"><div class="container faq-container reveal"><div class="section-header"><h2>{html(L[lang]["faq"])}</h2><p>{html(UI[lang]["faq_intro"])}</p></div>{faq_items}</div></section>
              <section class="content-section"><div class="container"><div class="cta-box reveal"><h3>{html(UI[lang]["request_help"])}</h3><p>{html(UI[lang]["request_help_text"])}</p><a href="{path_for(lang, "/")}#quote" class="btn btn-accent">{html(L[lang]["quote"])}</a></div></div></section>
              {related_services(lang, related)}
            </main>
            {footer(lang)}
            {back_to_top(lang)}
            """
        ).strip()
    return page_shell(lang, base_path, data_obj["title"], data_obj["meta"], body, schemas)


def render_port(lang: str, slug: str) -> str:
    data_obj = PORTS[slug][lang]
    base_path = f"/ports/{slug}.html"
    schemas = [organization_schema(lang), breadcrumb_schema([(L[lang]["home"], HOME_CANON[lang]), (L[lang]["ports"], canon_url(lang, base_path)), (data_obj["name"], canon_url(lang, base_path))])]
    body = dedent(
        f"""\
        {header(lang)}
        {breadcrumbs(lang, [(L[lang]["home"], path_for(lang, "/")), (L[lang]["ports"], path_for(lang, base_path)), (data_obj["name"], None)])}
        <main id="main">
          <section class="page-hero"><div class="container reveal"><h1>{html(data_obj["name"])}</h1><p>{html(data_obj["hero"])}</p></div></section>
          <section class="content-section">
            <div class="container">
              <h2 class="reveal">{html(UI[lang]["port_overview"])}</h2><p class="reveal">{html(data_obj["overview"])}</p>
              <div class="service-features reveal-stagger">
                <div class="feature-item"><h3>{html(UI[lang]["port_strengths"])}</h3><ul>{"".join(f'<li>{html(item)}</li>' for item in data_obj["strengths"])}</ul></div>
                <div class="feature-item"><h3>{html(UI[lang]["port_cargo"])}</h3><ul>{"".join(f'<li>{html(item)}</li>' for item in data_obj["cargo"])}</ul></div>
              </div>
              <div class="cta-box reveal"><h3>{html(UI[lang]["request_help"])}</h3><p>{html(UI[lang]["request_help_text"])}</p><a href="{path_for(lang, "/")}#quote" class="btn btn-accent">{html(L[lang]["quote"])}</a></div>
            </div>
          </section>
          {related_services(lang, ["customs-clearance", "shipping", "logistics"])}
        </main>
        {footer(lang)}
        {back_to_top(lang)}
        """
    ).strip()
    return page_shell(lang, base_path, data_obj["title"], data_obj["meta"], body, schemas)


def render_blog(lang: str, slug: str) -> str:
    data_obj = BLOGS[slug][lang]
    base_path = f"/blog/{slug}.html"
    hero = data_obj["hero"]
    schemas = [
        organization_schema(lang),
        breadcrumb_schema([(L[lang]["home"], HOME_CANON[lang]), (hero, canon_url(lang, base_path))]),
        article_schema(lang, data_obj["title"], data_obj["meta"], canon_url(lang, base_path)),
    ]
    sections = []
    for heading, paragraph, bullets in data_obj["sections"]:
        bullet_html = ""
        if bullets:
            bullet_html = "<ul>" + "".join(f"<li>{html(item)}</li>" for item in bullets) + "</ul>"
        sections.append(f'<div class="reveal"><h2>{html(heading)}</h2><p>{html(paragraph)}</p>{bullet_html}<p>{html(UI[lang]["article_note"])}</p></div>')
    body = dedent(
        f"""\
        {header(lang)}
        {breadcrumbs(lang, [(L[lang]["home"], path_for(lang, "/")), (hero, None)])}
        <main id="main">
          <section class="page-hero"><div class="container reveal"><h1>{html(hero)}</h1><p class="article-meta">{html(UI[lang]["article_byline"])}</p></div></section>
          <section class="content-section">
            <div class="container article-content">
              <p class="reveal">{html(data_obj["intro"])}</p>
              <p class="reveal">{html(BLOG_OPENING_NOTE[slug][lang])}</p>
              {"".join(sections)}
              <p class="reveal">{html(BLOG_CLOSING_NOTE[lang])}</p>
              <div class="cta-box reveal"><h3>{html(UI[lang]["article_cta_title"])}</h3><p>{html(UI[lang]["article_cta_text"])}</p><a href="{path_for(lang, "/contact.html")}" class="btn btn-accent">{html(UI[lang]["article_cta_button"])}</a></div>
            </div>
          </section>
          {related_services(lang, BLOGS[slug]["related"])}
        </main>
        {footer(lang)}
        {back_to_top(lang)}
        """
    ).strip()
    return page_shell(lang, base_path, data_obj["title"], data_obj["meta"], body, schemas, og_type="article")


def render_404() -> str:
    lang = "en"
    schemas = [organization_schema(lang)]
    body = dedent(
        f"""\
        {header(lang)}
        <main id="main">
          <section class="error-page">
            <div class="container">
              <h1>404</h1>
              <h2>{html(L[lang]["error_title"])}</h2>
              <p>{html(L[lang]["error_text"])}</p>
              <p dir="rtl" lang="ar">{html(L["ar"]["error_text"])}</p>
              <p lang="zh">{html(L["zh"]["error_text"])}</p>
              <div class="error-links">
                <a href="{HOME_ALIAS["en"]}" class="btn btn-primary">{html(L["en"]["error_home"])}</a>
                <a href="{HOME_ALIAS["ar"]}" class="btn btn-secondary">{html(L["ar"]["error_home"])}</a>
                <a href="{HOME_ALIAS["zh"]}" class="btn btn-secondary">{html(L["zh"]["error_home"])}</a>
              </div>
            </div>
          </section>
        </main>
        {footer(lang)}
        {back_to_top(lang)}
        """
    ).strip()
    return page_shell(lang, "/404.html", "Page Not Found | Al-Rouby Customs", "The page you requested is unavailable. Continue to the English, Arabic, or Chinese homepages.", body, schemas, include_alternates=False, robots="noindex, follow")


def write_text(path: Path, content: str) -> None:
    ensure_parent(path)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def route_priority(base_path: str, lang: str) -> str:
    if base_path == "/":
        return "1.0" if lang == "en" else "0.9"
    if base_path in {"/contact.html", "/services/customs-clearance.html"}:
        return "0.9" if lang == "en" else "0.8"
    if base_path.startswith("/services/") or base_path.startswith("/ports/"):
        return "0.8" if lang == "en" else "0.7"
    if base_path.startswith("/blog/"):
        return "0.7"
    return "0.6"


def build_sitemap() -> str:
    entries = []
    for base_path in ROUTES:
        for lang in ("en", "ar", "zh"):
            alt_links = "\n".join(
                f'    <xhtml:link rel="alternate" hreflang="{alt}" href="{canon_url(alt, base_path)}" />'
                for alt in ("en", "ar", "zh")
            )
            entries.append(
                dedent(
                    f"""\
                    <url>
                      <loc>{canon_url(lang, base_path)}</loc>
                      <lastmod>{LASTMOD}</lastmod>
                      <changefreq>{"weekly" if base_path == "/" else "monthly"}</changefreq>
                      <priority>{route_priority(base_path, lang)}</priority>
                    {alt_links}
                      <xhtml:link rel="alternate" hreflang="x-default" href="{canon_url("en", base_path)}" />
                    </url>
                    """
                ).strip()
            )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n\n'
        + "\n\n".join(entries)
        + "\n</urlset>\n"
    )


def main() -> None:
    for lang in ("en", "ar", "zh"):
        write_text(file_path(lang, "/"), render_home(lang))
        write_text(file_path(lang, "/about.html"), render_about(lang))
        write_text(file_path(lang, "/contact.html"), render_contact(lang))
        for slug in SERVICE_ORDER:
            write_text(file_path(lang, f"/services/{slug}.html"), render_service(lang, slug))
        for slug in PORT_ORDER:
            write_text(file_path(lang, f"/ports/{slug}.html"), render_port(lang, slug))
        for slug in BLOGS:
            write_text(file_path(lang, f"/blog/{slug}.html"), render_blog(lang, slug))
    write_text(ROOT / "404.html", render_404())
    write_text(ROOT / "sitemap.xml", build_sitemap())


if __name__ == "__main__":
    main()
