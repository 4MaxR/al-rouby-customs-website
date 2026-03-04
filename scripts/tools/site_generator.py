#!/usr/bin/env python3
from __future__ import annotations

import json
from html import escape
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parents[1]
DOMAIN = "https://al-rouby.com"
OG_IMAGE = f"{DOMAIN}/images/og-image.jpg"
LASTMOD = "2026-02-28"
FORM_ACTION = "https://formspree.io/f/mreapbqn"
HOME_ALIAS = {"en": "/index.html", "ar": "/ar/index.html", "zh": "/zh/index.html"}
HOME_CANON = {"en": f"{DOMAIN}/", "ar": f"{DOMAIN}/ar/", "zh": f"{DOMAIN}/zh/"}
PREFIX = {"en": "", "ar": "/ar", "zh": "/zh"}
ROUTE_OVERRIDES = {
    "ar": {
        "/services/customs-logistics-consulting.html": "/services/consulting.html",
    },
}
ROUTES = [
    "/",
    "/about.html",
    "/contact.html",
    "/services/customs-clearance.html",
    "/services/freight-forwarding.html",
    "/services/shipping.html",
    "/services/logistics.html",
    "/services/customs-logistics-consulting.html",
    "/services/aci-nafeza.html",
    "/ports/ain-sokhna.html",
    "/ports/alexandria.html",
    "/ports/sczone.html",
    "/blog/customs-clearance-guide-egypt.html",
    "/blog/aci-system-guide.html",
    "/blog/sea-freight-types.html",
    "/blog/egypt-port-fees.html",
    "/blog/hs-code-guide.html",
]

L = {
    "en": {
        "html_lang": "en",
        "dir": "",
        "site": "Al-Rouby Customs",
        "skip": "Skip to content",
        "nav": "Main navigation",
        "menu": "Toggle navigation menu",
        "theme": "Toggle dark mode",
        "lang": "Language",
        "lang_switch": "Switch language",
        "lang_short": "EN",
        "home": "Home",
        "about": "About",
        "services": "Services",
        "ports": "Ports",
        "blog": "Blog",
        "contact": "Contact",
        "quote": "Request Quote",
        "footer_about": "Your reliable partner in Egyptian customs clearance and logistics. Fast, transparent, and legally compliant.",
        "contact_text": "Reach us anytime for shipment planning, quotes, and customs support.",
        "top": "Back to top",
        "updated": "Updated February 2026",
        "read_more": "Learn more",
        "contact_cards": ["Email", "Phone / WhatsApp", "Location"],
        "faq": "Frequently Asked Questions",
        "related": "Related Services",
        "how": "How We Work",
        "rights": "&copy; 2026 Al-Rouby Customs. All rights reserved.",
        "credit": 'Design &amp; Development by <a href="https://alroubyds.com" target="_blank" rel="noopener noreferrer">Alrouby Digital Studio</a>',
        "error_title": "Page Not Found",
        "error_text": "The page you requested could not be found. Use the links below to continue browsing the site.",
        "error_home": "Go to Homepage",
        "error_services": "Our Services",
        "error_contact": "Contact Us",
    },
    "ar": {
        "html_lang": "ar",
        "dir": ' dir="rtl"',
        "site": "الروبي للتخليص الجمركي",
        "skip": "انتقل إلى المحتوى",
        "nav": "التنقل الرئيسي",
        "menu": "قائمة التصفح",
        "theme": "تبديل الوضع الليلي",
        "lang": "اللغة",
        "lang_switch": "تبديل اللغة",
        "lang_short": "AR",
        "home": "الرئيسية",
        "about": "من نحن",
        "services": "الخدمات",
        "ports": "الموانئ",
        "blog": "المدونة",
        "contact": "اتصل بنا",
        "quote": "اطلب عرض سعر",
        "footer_about": "شريكك الموثوق في التخليص الجمركي والخدمات اللوجستية في مصر. سرعة في التنفيذ ووضوح في الخطوات.",
        "contact_text": "تواصل معنا في أي وقت لطلب عرض سعر أو مناقشة متطلبات الشحنة.",
        "top": "العودة للأعلى",
        "updated": "آخر تحديث: فبراير 2026",
        "read_more": "اعرف المزيد",
        "contact_cards": ["البريد الإلكتروني", "الهاتف / واتساب", "العنوان"],
        "faq": "الأسئلة الشائعة",
        "related": "خدمات ذات صلة",
        "how": "كيف نعمل",
        "rights": "&copy; 2026 الروبي للتخليص الجمركي. جميع الحقوق محفوظة.",
        "credit": 'تصميم وتطوير <a href="https://alroubyds.com" target="_blank" rel="noopener noreferrer">Alrouby Digital Studio</a>',
        "error_title": "الصفحة غير موجودة",
        "error_text": "الصفحة التي تبحث عنها غير متاحة حالياً. استخدم الروابط التالية للعودة إلى الصفحات الرئيسية.",
        "error_home": "العودة للرئيسية",
        "error_services": "الخدمات",
        "error_contact": "تواصل معنا",
    },
    "zh": {
        "html_lang": "zh",
        "dir": "",
        "site": "Al-Rouby海关清关",
        "skip": "跳至主要内容",
        "nav": "主导航",
        "menu": "切换导航菜单",
        "theme": "切换深色模式",
        "lang": "语言",
        "lang_switch": "切换语言",
        "lang_short": "ZH",
        "home": "首页",
        "about": "关于我们",
        "services": "服务项目",
        "ports": "港口",
        "blog": "博客",
        "contact": "联系我们",
        "quote": "获取报价",
        "footer_about": "您在埃及值得信赖的清关与物流合作伙伴。流程透明、响应迅速，并重视合规执行。",
        "contact_text": "欢迎联系团队讨论报价、时间节点与口岸执行安排。",
        "top": "返回顶部",
        "updated": "更新于 2026年2月",
        "read_more": "了解更多",
        "contact_cards": ["电子邮箱", "电话 / WhatsApp", "位置"],
        "faq": "常见问题",
        "related": "相关服务",
        "how": "合作方式",
        "rights": "&copy; 2026 Al-Rouby Customs. 保留所有权利。",
        "credit": '设计与开发：<a href="https://alroubyds.com" target="_blank" rel="noopener noreferrer">Alrouby Digital Studio</a>',
        "error_title": "页面未找到",
        "error_text": "您访问的页面不存在或链接已失效。请使用下面的链接继续浏览网站内容。",
        "error_home": "返回首页",
        "error_services": "查看服务",
        "error_contact": "联系团队",
    },
}

CONTACT_INFO = {
    "email": "info@al-rouby.com",
    "phone": "+20 100 062 8855",
    "phone_href": "tel:+201000628855",
    "map_href": "https://maps.app.goo.gl/RsDBzG56XkLNRWNFA",
    "map": {
        "en": "Ain Sokhna, Suez, Egypt",
        "ar": "العين السخنة، السويس، مصر",
        "zh": "埃及苏伊士艾因苏赫纳 TEDA 615号楼",
    },
}

SERVICE_ORDER = [
    "customs-clearance",
    "freight-forwarding",
    "shipping",
    "logistics",
    "customs-logistics-consulting",
    "aci-nafeza",
]
SERVICES = {
    "customs-clearance": {
        "en": {
            "name": "Customs Clearance",
            "title": "Customs Clearance in Egypt | Al-Rouby Customs",
            "meta": "Professional customs clearance for imports, exports, temporary admission, and special regimes across Egyptian ports.",
            "hero": "Fast, compliant customs clearance for imports, exports, and regulated cargo in Egypt.",
            "summary": "We manage document review, customs preparation, inspection follow-up, and release coordination so shipments move with fewer avoidable delays.",
            "features": ["Document review", "Tariff and procedure alignment", "Inspection follow-up", "Release and handover coordination"],
            "bullets": ["Commercial invoice", "Packing list", "Bill of lading or airway bill", "Origin certificate when required", "Cargo-specific permits or approvals"],
            "faq": [("When should preparation begin?", "Ideally before the shipment arrives so documents and approvals can be reviewed early."), ("Do you support special regimes?", "Yes. We support final import, export, temporary admission, and other practical customs workflows."), ("What causes delay most often?", "Document mismatch, late ACI work, missing permits, and unclear classification or valuation details.")],
        },
        "ar": {
            "name": "التخليص الجمركي",
            "title": "التخليص الجمركي في مصر | الروبي",
            "meta": "خدمات تخليص جمركي احترافية للواردات والصادرات والإفراج المؤقت والأنظمة الخاصة في الموانئ المصرية.",
            "hero": "تخليص جمركي سريع ومتوافق للواردات والصادرات والشحنات ذات المتطلبات التنظيمية في مصر.",
            "summary": "نتولى مراجعة المستندات وتجهيز الملف ومتابعة الفحص والتنسيق مع الجهات المعنية حتى تتحرك الشحنة دون تأخير يمكن تجنبه.",
            "features": ["مراجعة المستندات", "تنسيق البند والإجراء", "متابعة الفحص", "تنسيق الإفراج والتسليم"],
            "bullets": ["الفاتورة التجارية", "قائمة التعبئة", "بوليصة الشحن أو بوليصة الطيران", "شهادة المنشأ عند الحاجة", "أي تصاريح أو موافقات خاصة بالبضاعة"],
            "faq": [("متى يجب البدء في التجهيز؟", "من الأفضل البدء قبل وصول الشحنة حتى تتم مراجعة المستندات والموافقات مبكراً."), ("هل تدعمون الأنظمة الخاصة؟", "نعم. ندعم الوارد النهائي والتصدير والإفراج المؤقت ومسارات جمركية عملية أخرى."), ("ما أكثر أسباب التأخير شيوعاً؟", "اختلاف المستندات، وتأخر ACI، ونقص التصاريح، وعدم وضوح التصنيف أو القيمة.")],
        },
        "zh": {
            "name": "海关清关",
            "title": "埃及海关清关服务 | Al-Rouby",
            "meta": "为进口、出口、暂时准入及特殊监管业务提供专业埃及清关服务，覆盖主要港口。",
            "hero": "为进入埃及的进口、出口和监管货物提供高效、合规的清关支持。",
            "summary": "我们负责单证审核、申报准备、查验跟进以及放行后的交接协调，帮助客户减少本可避免的延误。",
            "features": ["单证审核", "税则与流程衔接", "查验跟进", "放行与交接协调"],
            "bullets": ["商业发票", "装箱单", "提单或空运单", "需要时的原产地证明", "按货物性质所需的许可证或审批"],
            "faq": [("什么时候开始准备最好？", "最好在货物到港前启动，这样可以提前核对文件和审批要求。"), ("能否支持特殊监管或暂时准入？", "可以。我们可配合一般进口、出口、暂时准入及其他实务流程。"), ("最常见的延误原因是什么？", "单证不一致、ACI 过晚、许可证缺失以及编码或价格信息不清晰。")]},
    },
    "freight-forwarding": {
        "en": {"name": "Freight Forwarding", "title": "Freight Forwarding in Egypt | Al-Rouby Customs", "meta": "Coordinated freight forwarding support connecting shipment planning, port timing, and customs readiness.", "hero": "Freight forwarding support that keeps bookings, arrival planning, and customs readiness aligned.", "summary": "We help connect supplier, carrier, port, and inland handover steps so cargo moves with clearer timing and fewer coordination gaps.", "features": ["Booking coordination", "Arrival planning", "Port-to-warehouse handover", "Issue escalation"], "bullets": ["Booking confirmation", "Commercial documents", "Consignee details", "ETA updates", "Delivery requirements"], "faq": [("Do you handle only sea freight?", "Sea freight is the core focus here, but we support wider coordination when required."), ("Can this be combined with customs clearance?", "Yes. Combining both usually improves timing and visibility."), ("What should the shipper provide early?", "Supplier details, shipment mode, cargo dimensions, and expected timing.")]},
        "ar": {"name": "الشحن والتوصيل", "title": "خدمات الشحن والتوصيل في مصر | الروبي", "meta": "تنسيق متكامل لعمليات الشحن الوارد والصادر مع ربطها بالتخليص والتسليم.", "hero": "خدمة شحن وتوصيل تربط بين الحجز والوصول والتسليم النهائي بمتابعة تشغيلية واضحة.", "summary": "نساعد العميل على تنسيق حركة الشحنة بين المورد والناقل والميناء والمستلم النهائي بما يقلل فجوات التنفيذ.", "features": ["تنسيق الحجز", "تخطيط الوصول", "التسليم من الميناء للمخزن", "التعامل مع المشكلات"], "bullets": ["تأكيد الحجز", "المستندات التجارية", "بيانات المستورد", "إشعارات الوصول", "متطلبات التسليم"], "faq": [("هل الخدمة تقتصر على الشحن البحري؟", "الشحن البحري هو الأساس هنا، لكننا ندعم تنسيق الشحنة بشكل أوسع عند الحاجة."), ("هل يمكن دمجها مع التخليص؟", "نعم، وهذا غالباً يحقق أفضل نتيجة تشغيلية."), ("ما المعلومات المطلوبة مبكراً؟", "بيانات المورد، ونمط الشحن، وأبعاد البضاعة، والتوقيت المتوقع.")]},
        "zh": {"name": "货运代理", "title": "埃及货运代理服务 | Al-Rouby", "meta": "围绕订舱、到港计划、交接与清关衔接提供协调型货运代理支持。", "hero": "把订舱、到港与清关准备连接起来的货运代理支持。", "summary": "我们帮助客户在供应商、承运人、港口和仓库之间保持节奏一致，减少交接断点带来的风险。", "features": ["订舱协调", "到港计划管理", "港口到仓库交接", "异常升级处理"], "bullets": ["订舱确认", "商业文件", "收货人资料", "ETA 更新", "交货要求"], "faq": [("是否只处理海运？", "本网站重点展示海运相关业务，但也可配合更广泛的运输协调。"), ("能否与清关一起安排？", "可以。把货代与清关放在同一执行链条里通常更稳。"), ("发货人应提前提供什么？", "供应商信息、运输方式、货物尺寸与时间要求。")]},
    },
    "shipping": {
        "en": {"name": "Shipping to Egypt", "title": "Shipping to Egypt | Sea Freight Support | Al-Rouby Customs", "meta": "Support for FCL, LCL, and sea freight planning into Egypt with customs readiness built into the workflow.", "hero": "Sea freight support for shipping to Egypt with practical planning around arrival, documents, and import readiness.", "summary": "We help clients choose the right container model, time document submission, and prepare for Egyptian port operations before cargo lands.", "features": ["Mode selection", "Pre-shipment readiness", "Arrival monitoring", "Egypt-focused coordination"], "bullets": ["Container or volume estimate", "Origin and supplier schedule", "Document cut-off dates", "ACI or banking requirements", "Target port and final delivery preference"], "faq": [("When is FCL better than LCL?", "FCL is often better when volume is high, timing is strict, or handling risk must be reduced."), ("How early should shipping documents be prepared?", "As early as possible before loading, especially when ACI or banking paperwork is involved."), ("Can shipping and customs be planned together?", "Yes. That is usually the most practical approach.")]},
        "ar": {"name": "الشحن إلى مصر", "title": "الشحن إلى مصر | دعم الشحن البحري | الروبي", "meta": "دعم عملي لشحنات FCL وLCL إلى مصر مع ربط التخطيط البحري بمتطلبات التخليص والوصول.", "hero": "دعم للشحن البحري إلى مصر مع تخطيط واضح للوصول والمستندات وجاهزية الاستيراد.", "summary": "نساعد العميل على اختيار نمط الحاوية المناسب وضبط توقيت المستندات والاستعداد لتشغيل الميناء المصري قبل وصول البضاعة.", "features": ["اختيار نمط الشحن", "الجاهزية قبل الشحن", "متابعة الوصول", "تنسيق يراعي السوق المصري"], "bullets": ["تقدير حجم الشحنة", "بلد المنشأ وجدول المورد", "مواعيد إغلاق المستندات", "متطلبات ACI أو البنك", "الميناء المستهدف والتسليم النهائي"], "faq": [("متى يكون FCL أفضل من LCL؟", "عندما يكون الحجم كبيراً أو الوقت حساساً أو يجب تقليل مخاطر المناولة."), ("متى يجب تجهيز مستندات الشحن؟", "كلما كان ذلك مبكراً كان أفضل، خاصة عند وجود متطلبات ACI أو بنك."), ("هل يمكن تنسيق الشحن والتخليص معاً؟", "نعم، وهذا غالباً يحقق أفضل انضباط تشغيلي.")]},
        "zh": {"name": "海运服务", "title": "发运至埃及的海运支持 | Al-Rouby", "meta": "为整箱、拼箱及到埃及的海运计划提供支持，并将清关准备纳入发运流程。", "hero": "围绕到港时间、文件准备与进口节奏，为发运至埃及的海运业务提供支持。", "summary": "我们帮助客户选择合适的箱型或拼箱方案，安排好文件时间，并在货物到港前完成进口准备。", "features": ["运输模式判断", "装运前准备", "到港动态跟进", "贴合埃及进口流程"], "bullets": ["箱量或体积预估", "起运地与供应商排期", "截单时间", "ACI 或银行要求", "目标港口与最终交付偏好"], "faq": [("什么时候整箱更合适？", "当货量较大、交期更紧或需要降低多次搬运风险时，整箱通常更合适。"), ("海运单证何时准备？", "越早越好，尤其是涉及 ACI 或银行资料时。"), ("能否把海运和清关一起规划？", "可以，这通常更有利于控制整体节奏。")]}},
    "logistics": {
        "en": {"name": "Logistics Solutions", "title": "Logistics Solutions in Egypt | Al-Rouby Customs", "meta": "Integrated logistics support around port handling, inland transport coordination, and operational timing in Egypt.", "hero": "Integrated logistics support for cargo moving through Egyptian ports, inland handover points, and warehouse schedules.", "summary": "We help importers align customs milestones with inland transport, receiving windows, and operational planning inside Egypt.", "features": ["Operational timing", "Port-side coordination", "Visibility for stakeholders", "Flexible support model"], "bullets": ["Final delivery point", "Receiving window restrictions", "Required truck or handling type", "Equipment or labor constraints", "Key commercial deadlines"], "faq": [("Is logistics support separate from customs clearance?", "It can be, but the best results usually come from coordinating both together."), ("Can you support recurring cargo programs?", "Yes. Repeated shipment patterns benefit from standardized planning and communication."), ("What matters most for inland execution?", "Delivery address, access limitations, equipment needs, and warehouse timing.")]},
        "ar": {"name": "الخدمات اللوجستية", "title": "حلول لوجستية في مصر | الروبي", "meta": "حلول لوجستية متكاملة تشمل تشغيل الميناء والتنسيق مع النقل الداخلي وضبط التوقيتات التشغيلية.", "hero": "دعم لوجستي متكامل للشحنات التي تتحرك عبر الموانئ المصرية ونقاط التسليم والمخازن.", "summary": "نساعد المستوردين والمصنعين على ربط مراحل التخليص بتوقيت النقل والاستلام والتشغيل الداخلي داخل مصر.", "features": ["ضبط التوقيت التشغيلي", "تنسيق داخل الميناء", "رؤية أوضح للأطراف المعنية", "نموذج دعم مرن"], "bullets": ["مكان التسليم النهائي", "قيود الاستلام بالمخزن", "نوع السيارة أو المناولة المطلوبة", "قيود المعدات أو العمالة", "المواعيد التجارية الحرجة"], "faq": [("هل الدعم اللوجستي منفصل عن التخليص؟", "يمكن أن يكون منفصلاً، لكن أفضل النتائج تأتي غالباً عند تنسيق المسارين معاً."), ("هل يمكن دعم برامج شحن متكررة؟", "نعم، فالشحنات المتكررة تستفيد من التخطيط والتواصل المعياري."), ("ما أهم المعلومات للتنفيذ الداخلي؟", "عنوان التسليم، وقيود الوصول، واحتياجات المعدات، ومواعيد المخزن.")]},
        "zh": {"name": "物流解决方案", "title": "埃及物流解决方案 | Al-Rouby", "meta": "围绕港口操作、内陆运输衔接、时间窗口和货物流转可视化提供一体化物流支持。", "hero": "为经过埃及港口、内陆交接点和仓库的货物提供一体化物流支持。", "summary": "我们帮助进口商和制造企业把清关节点与内陆运输、收货时间和现场操作安排连接起来。", "features": ["操作时间协调", "港口侧交接管理", "相关方可视化", "灵活支持模式"], "bullets": ["最终交付地点", "仓库收货时间窗口", "所需车辆或装卸方式", "设备或人工限制", "关键商务时限"], "faq": [("物流支持必须和清关一起做吗？", "可以分开，但把两者放在同一执行链条里通常更容易控制结果。"), ("能否支持重复性货运项目？", "可以。重复项目尤其适合通过标准化计划提升稳定性。"), ("内陆执行最关键的信息是什么？", "交付地址、进场限制、设备需求、仓库时间和特殊装卸说明。")]},
    },
    "customs-logistics-consulting": {
        "en": {
            "name": "Customs & Logistics Consulting",
            "title": "Customs & Logistics Consulting in Egypt | Al-Rouby Customs",
            "meta": "Professional customs and logistics consulting in Egypt—HS code guidance, ACI/NAFEZA support, documentation review, cost optimization, and compliance risk reduction.",
            "hero": "Practical customs and logistics consulting for Egypt-focused imports, document readiness, and compliance planning.",
            "summary": "We advise importers on HS classification, ACI/NAFEZA preparation, document readiness, landed-cost decisions, and compliance risks before those issues slow clearance.",
            "card_summary": "HS code guidance, ACI/NAFEZA support, document review, and compliance-focused cost optimization for Egypt-bound shipments.",
            "sections": {
                "help": {
                    "title": "What we help with",
                    "intro": "This service is designed for shipments or import programs that need a practical review before costs, timing, or compliance issues become harder to correct.",
                    "cards": [
                        ("HS code guidance", "We review product descriptions and supporting details so classification decisions are clearer before filing or supplier document finalization."),
                        ("ACI / NAFEZA support", "We help check whether the ACI file, ACID references, and pre-shipment timing are aligned with the actual cargo plan."),
                        ("Documentation review", "We compare invoice, packing list, transport details, and supporting documents to identify mismatches before they affect clearance."),
                        ("Cost and compliance review", "We highlight avoidable landed-cost exposure, weak handoff points, and risks that could lead to delay, rework, or compliance questions."),
                    ],
                },
                "who": {
                    "title": "Who it’s for",
                    "intro": "The consulting scope is useful when a team needs Egypt-specific guidance before shipment, before filing, or before repeating the same operational mistake.",
                    "bullets": [
                        "First-time importers into Egypt that need a practical review of the process and document chain",
                        "Recurring import programs that want to reduce repeated delays, extra fees, or compliance friction",
                        "Suppliers or exporters that need their documents aligned with Egyptian importer requirements",
                        "Commercial or operations teams trying to improve landed cost visibility and reduce avoidable customs risk",
                    ],
                },
                "how": {
                    "title": "How it works",
                    "cards": [
                        ("1. Intake review", "You share the shipment profile, product details, target port, and the main issue you want reviewed."),
                        ("2. Consultation pass", "We assess the documents, classification points, ACI / NAFEZA readiness, and operational risks tied to timing or compliance."),
                        ("3. Practical recommendations", "You receive a clear action list covering what to fix, what to prepare, and what to watch before the shipment moves further."),
                    ],
                },
                "provide": {
                    "title": "What you need to provide",
                    "items": [
                        "Product description, specifications, catalogue, or datasheet where available",
                        "Draft or final commercial invoice and packing list",
                        "ACI / NAFEZA details or ACID reference if already started",
                        "Target port, shipment timing, and delivery expectations",
                        "The specific issue you want reviewed, such as HS code, document mismatch, or cost exposure",
                    ],
                },
                "cta": {
                    "title": "Request a consultation",
                    "text": "Send the cargo profile, draft documents, and the issue you want reviewed. We will outline the next practical steps for Egypt-focused execution.",
                },
            },
            "faq": [
                ("When should customs and logistics consulting start?", "Ideally before documents are finalized or cargo is too close to loading, so corrections can still be made with less cost and pressure."),
                ("Can you review HS code or documents as a standalone consultation?", "Yes. We can review a specific issue such as classification, ACI readiness, or document consistency without requiring full shipment handling."),
                ("What do we receive after the consultation?", "You receive practical guidance on the issues identified, the missing inputs, and the next actions that should be completed before shipment or clearance."),
            ],
            "related": ["customs-clearance", "logistics", "aci-nafeza"],
        },
        "ar": {
            "name": "استشارات جمركية ولوجيستية",
            "title": "استشارات جمركية ولوجيستية في مصر | الروبي للتخليص",
            "meta": "استشارات احترافية في التخليص والشحن بمصر: تصنيف بنود HS، دعم ACI/نافذة، مراجعة المستندات، تقليل التكاليف، وتقليل مخاطر المخالفات.",
            "hero": "استشارة عملية للشحنات المتجهة إلى مصر قبل أن تتحول مشكلات التصنيف أو المستندات أو ACI إلى تأخير فعلي.",
            "summary": "نساعد المستوردين والشركات على مراجعة تصنيف HS، وجاهزية ACI ونافذة، والمستندات التجارية، ونقاط التكلفة والامتثال قبل أن تؤثر على مسار التخليص.",
            "card_summary": "استشارات عملية لتصنيف HS، ودعم ACI/نافذة، ومراجعة المستندات، وتقليل التكلفة ومخاطر الامتثال.",
            "sections": {
                "help": {
                    "title": "كيف نساعدك",
                    "intro": "هذه الخدمة مناسبة عندما تحتاج الشحنة أو خطة الاستيراد إلى مراجعة عملية مبكرة قبل أن تصبح المعالجة أكثر تكلفة أو تعقيداً.",
                    "cards": [
                        ("مراجعة تصنيف HS", "نراجع وصف المنتج وخصائصه والمستندات الداعمة لتقليل الغموض في البند الجمركي قبل تجهيز الملف النهائي."),
                        ("دعم ACI ونافذة", "نراجع جاهزية ملف ACI وبيانات ACID وتوقيتات نافذة بما يتوافق مع الخطة الفعلية للشحنة."),
                        ("مراجعة المستندات", "نقارن الفاتورة وقائمة التعبئة وبيانات الشحن والمستندات المساندة لاكتشاف أي اختلافات قبل أن تؤثر على التخليص."),
                        ("تقليل التكلفة ومخاطر الامتثال", "نوضح مصادر التكلفة القابلة للتجنب ونقاط الضعف التشغيلية والمخاطر التي قد تؤدي إلى تأخير أو إعادة عمل أو استفسارات جمركية."),
                    ],
                },
                "who": {
                    "title": "لمن هذه الخدمة",
                    "intro": "تفيد هذه الاستشارة الفرق التي تحتاج إلى توجيه واضح مرتبط بالسوق المصري قبل الشحن أو قبل تكرار المشكلة نفسها في كل شحنة.",
                    "bullets": [
                        "المستوردون الجدد إلى مصر الذين يحتاجون إلى قراءة عملية للمسار والمستندات",
                        "برامج الاستيراد المتكررة التي تريد خفض التأخير والرسوم الإضافية والاحتكاك التنظيمي",
                        "الموردون أو المصدرون الذين يحتاجون إلى مواءمة مستنداتهم مع متطلبات الاستيراد في مصر",
                        "فرق التجارة أو التشغيل التي تريد رؤية أوضح للتكلفة النهائية وتقليل المخاطر الجمركية القابلة للتجنب",
                    ],
                },
                "how": {
                    "title": "كيف نعمل",
                    "cards": [
                        ("1. مراجعة أولية", "تشارك معنا وصف الشحنة وتفاصيل المنتج والميناء المستهدف والنقطة التي تريد تقييمها."),
                        ("2. جلسة التقييم", "نراجع المستندات والبند الجمركي وجاهزية ACI ونافذة والمخاطر التشغيلية المرتبطة بالتوقيت أو الامتثال."),
                        ("3. توصيات عملية", "تحصل على قائمة واضحة بما يجب تصحيحه أو استكماله أو متابعته قبل أن تتحرك الشحنة إلى مرحلة أكثر حساسية."),
                    ],
                },
                "provide": {
                    "title": "ما الذي نحتاجه منك",
                    "items": [
                        "وصف المنتج والمواصفات الفنية أو الكتالوج أو الـ datasheet إن وجد",
                        "مسودة أو نسخة نهائية من الفاتورة التجارية وقائمة التعبئة",
                        "بيانات ACI ونافذة أو رقم ACID إذا كان الملف قد بدأ",
                        "الميناء المستهدف وتوقيت الشحنة ومتطلبات التسليم",
                        "المشكلة المحددة المطلوب مراجعتها مثل البند الجمركي أو اختلاف المستندات أو التعرض لتكلفة إضافية",
                    ],
                },
                "cta": {
                    "title": "اطلب استشارة أو عرض سعر",
                    "text": "أرسل وصف البضاعة والمستندات المتاحة والنقطة التي تريد مراجعتها، وسنوضح لك الخطوات العملية التالية المناسبة للسوق المصري.",
                },
            },
            "faq": [
                ("متى يفضل البدء في هذه الاستشارة؟", "كلما كان ذلك قبل تثبيت المستندات أو قبل اقتراب موعد التحميل كان أفضل، لأن مساحة التصحيح تكون أكبر والتكلفة أقل."),
                ("هل يمكن مراجعة البند الجمركي أو المستندات فقط دون إدارة الشحنة كاملة؟", "نعم، يمكن تنفيذ مراجعة مستقلة للبند الجمركي أو ملف ACI أو اتساق المستندات دون ربطها فوراً بإدارة تشغيلية كاملة."),
                ("ماذا نستفيد بعد الاستشارة؟", "تحصل على توصيات عملية توضّح نقاط الضعف وما يجب استكماله والخطوات التي ينبغي تنفيذها قبل الشحن أو التخليص."),
            ],
            "related": ["customs-clearance", "logistics", "aci-nafeza"],
        },
        "zh": {
            "name": "清关与物流咨询",
            "title": "埃及清关与物流咨询服务 | Al-Rouby Customs",
            "meta": "提供埃及清关与物流专业咨询：HS编码建议、ACI/NAFEZA支持、单证审核、成本优化与合规风险控制。",
            "hero": "面向发运至埃及项目的务实咨询，帮助团队在分类、单证或 ACI 问题演变成实际延误前先完成核查。",
            "summary": "我们协助进口商和业务团队提前审视 HS 编码、ACI / NAFEZA 准备、商业单证以及落地成本与合规风险，减少后续清关阻力。",
            "card_summary": "围绕 HS 编码、ACI/NAFEZA、单证审核、成本优化与合规风险控制提供务实咨询。",
            "sections": {
                "help": {
                    "title": "我们可协助的事项",
                    "intro": "这项服务适合在出运前、申报前或准备修正重复性问题时进行一次面向埃及实务的提前审视。",
                    "cards": [
                        ("HS 编码建议", "我们结合产品描述、规格和支持资料，帮助缩小分类判断的不确定性，避免后续文件准备反复修改。"),
                        ("ACI / NAFEZA 支持", "我们核对 ACI 文件、ACID 信息以及装运前时间安排是否与实际货运计划一致。"),
                        ("单证审核", "我们比对发票、装箱单、运输信息及相关附件，提前识别会影响清关的内容不一致问题。"),
                        ("成本与合规风险控制", "我们指出可避免的落地成本暴露、操作交接薄弱点，以及可能引发延误或合规疑问的风险。"),
                    ],
                },
                "who": {
                    "title": "适用对象",
                    "intro": "当团队需要一份贴近埃及进口实际流程的判断，而不是泛泛建议时，这项咨询会更有价值。",
                    "bullets": [
                        "首次进口至埃及、希望先把流程和单证链看清楚的企业",
                        "希望减少重复延误、额外费用和合规摩擦的常规进口项目",
                        "需要让供应商或出口方文件对齐埃及进口要求的业务团队",
                        "希望提升落地成本可视性并降低可避免清关风险的商务或运营团队",
                    ],
                },
                "how": {
                    "title": "合作流程",
                    "cards": [
                        ("1. 初步了解", "您提供货物情况、产品信息、目标港口以及希望重点评估的问题。"),
                        ("2. 咨询评估", "我们检查单证、分类点、ACI / NAFEZA 准备情况，以及与时间或合规相关的实际风险。"),
                        ("3. 可执行建议", "您会拿到明确的行动建议，知道哪些内容需要修正、补充或在发运前重点关注。"),
                    ],
                },
                "provide": {
                    "title": "您需要提供的资料",
                    "items": [
                        "产品描述、技术规格、目录或 datasheet（如有）",
                        "商业发票和装箱单草稿或定稿",
                        "已启动时的 ACI / NAFEZA 信息或 ACID 编号",
                        "目标港口、时间计划和交付要求",
                        "希望重点评估的问题，例如 HS 编码、单证不一致或成本风险",
                    ],
                },
                "cta": {
                    "title": "申请咨询或报价",
                    "text": "欢迎提交货物情况、现有单证和希望重点评估的问题，我们会先说明面向埃及执行的实际下一步。",
                },
            },
            "faq": [
                ("这类咨询最好什么时候开始？", "最好在单证最终定稿前或装运时间过于紧张前启动，这样修正空间更大，成本和压力也更可控。"),
                ("可以只做 HS 编码或单证审核吗？", "可以。我们可以围绕单一问题提供独立咨询，例如分类判断、ACI 准备或单证一致性检查。"),
                ("咨询结束后会得到什么？", "您会得到面向实际执行的建议，明确当前问题、缺失资料，以及发运或清关前应完成的下一步。"),
            ],
            "related": ["customs-clearance", "logistics", "aci-nafeza"],
        },
    },
    "aci-nafeza": {
        "en": {"name": "ACI & Nafeza Support", "title": "ACI & Nafeza Support in Egypt | Al-Rouby Customs", "meta": "Practical support for Egypt's ACI workflow, ACID preparation, Nafeza coordination, and pre-shipment document timing.", "hero": "ACI and Nafeza support that helps importers prepare the file correctly before cargo moves toward Egypt.", "summary": "We help clients coordinate supplier documents, importer-side registration work, and timeline discipline so ACI preparation supports clearance instead of delaying it.", "features": ["Pre-shipment file review", "ACID readiness", "Supplier coordination", "Compliance follow-up"], "bullets": ["Importer registration status", "Supplier commercial documents", "Draft shipping details", "Bank or payment references where relevant", "Expected loading and arrival dates"], "faq": [("When should ACI work begin?", "Before loading pressure becomes critical so the file is not assembled at the last moment."), ("Can you help suppliers understand Egypt's requirements?", "Yes. We often bridge the gap between exporter documents and Egyptian import needs."), ("What happens if the file is inconsistent?", "It should be corrected before it affects loading or downstream customs work.")]},
        "ar": {"name": "دعم ACI ونافذة", "title": "خدمة ACI ونافذة في مصر | الروبي", "meta": "دعم عملي لملف ACI واستخراج ACID والتعامل مع نافذة وتوقيت المستندات قبل الشحن إلى مصر.", "hero": "دعم لنظام ACI ونافذة يساعد المستورد على تجهيز الملف بشكل صحيح قبل تحرك الشحنة إلى مصر.", "summary": "نساعد العملاء على تنسيق مستندات المورد وتجهيزات المستورد والانضباط الزمني بحيث يدعم ملف ACI عملية التخليص بدلاً من تعطيلها.", "features": ["مراجعة الملف قبل الشحن", "جاهزية ACID", "تنسيق مع المورد", "متابعة الامتثال"], "bullets": ["حالة تسجيل المستورد", "المستندات التجارية من المورد", "بيانات الشحن المبدئية", "بيانات البنك أو السداد عند الحاجة", "تواريخ التحميل والوصول المتوقعة"], "faq": [("متى يجب بدء إجراءات ACI؟", "يفضل البدء قبل أن يصبح موعد التحميل أو الحجز ضاغطاً."), ("هل يمكنكم مساعدة المورد على فهم المتطلبات المصرية؟", "نعم، ونقوم كثيراً بربط مستندات المورد بمتطلبات الاستيراد المصرية."), ("ماذا يحدث إذا كان الملف غير متسق؟", "يجب تصحيحه قبل أن يؤثر على التحميل أو التخليص اللاحق.")]},
        "zh": {"name": "ACI 与 Nafeza", "title": "埃及 ACI 与 Nafeza 支持 | Al-Rouby", "meta": "围绕埃及 ACI、ACID 准备、Nafeza 协调以及装运前文件时序提供实务支持。", "hero": "帮助进口商在货物发往埃及前把 ACI 和 Nafeza 文件准备正确的实务支持。", "summary": "我们协助客户协调供应商文件、进口方注册准备和时间节奏，使 ACI 文件成为清关助力而不是阻碍。", "features": ["装运前文件审查", "ACID 准备支持", "供应商协同", "合规修正跟进"], "bullets": ["进口商注册状态", "供应商商业文件", "预估装运资料", "相关银行或付款参考信息", "预计装货与到港日期"], "faq": [("ACI 工作应从什么时候开始？", "最好在订舱和装货压力变大前就开始。"), ("可以帮助供应商理解埃及要求吗？", "可以，我们经常协助出口方文件与埃及要求之间的衔接。"), ("如果文件前后不一致怎么办？", "应在影响装货或后续清关前完成修正。")]}},
}

PORT_ORDER = ["ain-sokhna", "alexandria", "sczone"]
PORTS = {
    "ain-sokhna": {
        "en": {"name": "Ain Sokhna Port", "title": "Customs Clearance at Ain Sokhna Port | Al-Rouby", "meta": "Operational support and customs coordination for cargo moving through Ain Sokhna and nearby industrial zones.", "hero": "Operational customs support at Ain Sokhna for import cargo, industrial projects, and time-sensitive deliveries.", "overview": "Ain Sokhna is one of Egypt's key Red Sea gateways. Good preparation here helps reduce avoidable cost exposure and supports faster inland handover.", "strengths": ["Red Sea access", "Industrial zone relevance", "Time-sensitive handover"], "cargo": ["Industrial inputs", "Project cargo", "Containerized imports", "Raw materials", "Factory shipments"]},
        "ar": {"name": "ميناء العين السخنة", "title": "التخليص الجمركي في ميناء العين السخنة | الروبي", "meta": "دعم تشغيلي وتنسيق جمركي للشحنات التي تمر عبر ميناء العين السخنة والمناطق الصناعية المحيطة به.", "hero": "دعم جمركي وتشغيلي في العين السخنة للشحنات الواردة والمشروعات الصناعية والتسليمات الحساسة زمنياً.", "overview": "يعد ميناء العين السخنة من أهم بوابات الواردات عبر البحر الأحمر. التحضير الجيد فيه يحد من التعرض لتكاليف إضافية ويساعد على ربط الإفراج بالنقل الداخلي بسرعة.", "strengths": ["ارتباط قوي بالبحر الأحمر", "قرب المناطق الصناعية", "حساسية التوقيت"], "cargo": ["مدخلات صناعية", "شحنات مشروعات", "حاويات وارد", "مواد خام", "شحنات مصانع"]},
        "zh": {"name": "艾因苏赫纳港", "title": "艾因苏赫纳港清关支持 | Al-Rouby", "meta": "为经过艾因苏赫纳港及周边工业区域的货物提供操作协调与清关支持。", "hero": "面向进口货物、工业项目与时效敏感交付计划的艾因苏赫纳港清关支持。", "overview": "艾因苏赫纳港是红海航线进入埃及的重要门户之一。若前期准备充分，能够明显降低延误和额外港口成本。", "strengths": ["红海航线枢纽", "工业区关联度高", "时效管理要求高"], "cargo": ["工业原料", "项目货", "集装箱进口货", "生产原材料", "工厂急需货物"]},
    },
    "alexandria": {
        "en": {"name": "Alexandria Port", "title": "Customs Clearance at Alexandria Port | Al-Rouby", "meta": "Customs and cargo coordination support for Alexandria and Dekheila import flows, including high-volume operations.", "hero": "Clearance support for Alexandria and Dekheila cargo programs with attention to volume, timing, and document accuracy.", "overview": "Alexandria and Dekheila handle a large share of Egypt's Mediterranean import flow. Success here depends on controlling document accuracy and execution timing.", "strengths": ["High-volume trade lane", "Document discipline", "Flexible cargo profile"], "cargo": ["Consumer goods", "Retail inventory", "Industrial supplies", "Containerized imports", "Recurring commercial cargo"]},
        "ar": {"name": "ميناء الإسكندرية", "title": "التخليص الجمركي في ميناء الإسكندرية | الروبي", "meta": "دعم تخليص وتنسيق للشحنات الواردة عبر الإسكندرية والدخيلة، خاصة في العمليات كبيرة الحجم.", "hero": "دعم تخليص في الإسكندرية والدخيلة مع تركيز واضح على الحجم والتوقيت ودقة المستندات.", "overview": "تتعامل الإسكندرية والدخيلة مع نسبة كبيرة من حركة الواردات عبر البحر المتوسط. ويعتمد النجاح هنا على التحكم في التعقيد ودقة الملف.", "strengths": ["حركة تجارية كبيرة", "حاجة إلى انضباط مستندي", "تنوع في أنواع البضائع"], "cargo": ["سلع استهلاكية", "مخزون تجزئة", "مستلزمات صناعية", "واردات حاويات", "شحنات تجارية متكررة"]},
        "zh": {"name": "亚历山大港", "title": "亚历山大港清关支持 | Al-Rouby", "meta": "为亚历山大港和德赫拉港的高频进口业务提供清关与货运衔接支持。", "hero": "针对亚历山大及德赫拉进口项目提供重视体量、时效和单证准确性的清关支持。", "overview": "亚历山大港及德赫拉港承担了埃及地中海方向的大量进口流量。这里的关键是控制规模化操作中的复杂度和准确性。", "strengths": ["高流量贸易口岸", "重视文件纪律", "货类覆盖广"], "cargo": ["消费品", "零售库存", "工业物料", "集装箱进口货", "重复性商业货物"]},
    },
    "sczone": {
        "en": {"name": "Suez Canal Economic Zone", "title": "Customs Support in SCZone | Al-Rouby", "meta": "Operational customs support for shipments connected to the Suez Canal Economic Zone and zone-specific procedures.", "hero": "Clearance support for businesses operating in or shipping through the Suez Canal Economic Zone.", "overview": "SCZone-related cargo often involves additional procedural awareness and timing considerations compared with a standard import file.", "strengths": ["Zone-specific awareness", "Industrial and investment focus", "Integrated planning"], "cargo": ["Industrial equipment", "Factory inputs", "Project materials", "Zone-linked imports", "Investment-related cargo"]},
        "ar": {"name": "المنطقة الاقتصادية لقناة السويس", "title": "الدعم الجمركي في المنطقة الاقتصادية لقناة السويس | الروبي", "meta": "دعم جمركي وتشغيلي للشحنات المرتبطة بالمنطقة الاقتصادية لقناة السويس والإجراءات الخاصة بها.", "hero": "دعم تخليص للشركات العاملة داخل أو من خلال المنطقة الاقتصادية لقناة السويس.", "overview": "الشحنات المرتبطة بالمنطقة الاقتصادية تحتاج غالباً إلى وعي إجرائي وتجاري إضافي مقارنة بملف الاستيراد التقليدي.", "strengths": ["فهم متطلبات المنطقة", "تركيز صناعي واستثماري", "تخطيط متكامل"], "cargo": ["معدات صناعية", "مدخلات مصانع", "مواد مشروعات", "واردات مرتبطة بالمنطقة", "شحنات استثمارية"]},
        "zh": {"name": "苏伊士运河经济区", "title": "苏伊士运河经济区清关支持 | Al-Rouby", "meta": "为涉及苏伊士运河经济区、区内企业及相关特殊程序的货物提供操作与清关支持。", "hero": "为在苏伊士运河经济区内运营或经由该区域发运的企业提供清关支持。", "overview": "与苏伊士运河经济区相关的货物，往往比普通进口文件更需要了解特定程序、商业结构和时间安排。", "strengths": ["了解园区程序", "工业与投资属性强", "强调一体化计划"], "cargo": ["工业设备", "工厂投入品", "项目材料", "园区相关进口货", "投资类货物"]},
    },
}

HOME = {
    "en": {
        "title": "Al-Rouby Customs | Customs Clearance & Logistics in Egypt",
        "meta": "Customs clearance, freight forwarding, port coordination, and ACI support across Egypt for importers, exporters, and manufacturers.",
        "hero_title": "Customs Clearance Across Egypt's Ports - Practical, Compliant, Reliable",
        "hero_text": "Al-Rouby supports importers, exporters, and manufacturers with customs clearance, freight coordination, and port-side execution across Egypt.",
        "hero_summary": "We combine document control, operational follow-up, ACI readiness, and inland handover planning so cargo can move with fewer surprises.",
        "hero_points": ["ACI and Nafeza support", "Coverage across major Egyptian ports", "Operational follow-up from file review to release", "Clear communication on timing, cost, and next steps"],
        "stats": [("27+", "Years of practical trade support"), ("12,000+", "Shipments handled"), ("100%", "Focus on compliant execution"), ("24/7", "Client communication availability")],
        "process": [("Share the shipment profile", "Send cargo details, draft documents, and timing expectations so we can review the practical path early."), ("Prepare the file", "We align the required documents, identify missing items, and coordinate the next actions needed before arrival or loading."), ("Clear and hand over", "We follow the shipment through release and connect customs completion to the next logistics step.")],
        "reviews": [("A practical team that helped us avoid delay at a critical arrival window.", "Industrial importer"), ("They kept the document process clear and flagged the real risks early.", "Trading company"), ("Useful communication, realistic expectations, and strong follow-up after arrival.", "Factory procurement team")],
        "faq": [("How early should we contact you?", "The earlier the better, especially if the shipment still needs ACI work, document review, or delivery planning."), ("Do you only work in one port?", "No. We support cargo programs across major Egyptian ports and zone-linked operations."), ("Can you work with suppliers outside Egypt?", "Yes. We often coordinate with foreign suppliers to align documents and timing before cargo moves."), ("What information do you need first?", "A short cargo description, the expected port, shipment timing, and any available draft documents.")],
    },
    "ar": {
        "title": "الروبي | التخليص الجمركي والخدمات اللوجستية في مصر",
        "meta": "تخليص جمركي، تنسيق شحن، متابعة بالموانئ، ودعم ACI للمستوردين والمصدرين والمصنعين في مصر.",
        "hero_title": "تخليص جمركي في موانئ مصر - عملي، متوافق، ويمكن الاعتماد عليه",
        "hero_text": "تدعم شركة الروبي المستوردين والمصدرين والمصنعين من خلال التخليص الجمركي وتنسيق الشحن والتنفيذ التشغيلي داخل الموانئ المصرية.",
        "hero_summary": "نجمع بين مراجعة المستندات والمتابعة التشغيلية وجاهزية ACI وتنسيق النقل بعد الإفراج حتى تتحرك الشحنة بصورة أكثر استقراراً.",
        "hero_points": ["دعم ACI ونافذة", "تغطية الموانئ الرئيسية في مصر", "متابعة تشغيلية من مراجعة الملف حتى الإفراج", "تواصل واضح بشأن التوقيت والتكلفة والخطوات التالية"],
        "stats": [("27+", "سنة من الخبرة العملية"), ("12,000+", "شحنة تم التعامل معها"), ("100%", "تركيز على التنفيذ المتوافق"), ("24/7", "تواصل متاح مع العملاء")],
        "process": [("أرسل بيانات الشحنة", "شارك وصف البضاعة والمستندات المتاحة والتوقيت المتوقع حتى نراجع المسار مبكراً."), ("تجهيز الملف", "نرتب المستندات ونحدد المطلوب الناقص وننسق الخطوات الضرورية قبل الوصول أو التحميل."), ("التخليص والتسليم", "نتابع الشحنة حتى الإفراج ثم نربط إنهاء الجمارك بالخطوة اللوجستية التالية.")],
        "reviews": [("فريق عملي ساعدنا على تجنب تأخير في وقت وصول حساس.", "مستورد صناعي"), ("أبقوا المستندات واضحة وحددوا المخاطر الحقيقية مبكراً.", "شركة تجارة"), ("تواصل جيد وتوقعات واقعية ومتابعة قوية بعد الوصول.", "فريق مشتريات مصنع")],
        "faq": [("متى يفضّل التواصل معنا؟", "كلما كان ذلك مبكراً كان أفضل، خصوصاً إذا كانت الشحنة لا تزال بحاجة إلى ACI أو مراجعة مستندات أو تخطيط للتسليم."), ("هل تعملون في ميناء واحد فقط؟", "لا. نحن ندعم الشحنات عبر الموانئ المصرية الرئيسية والعمليات المرتبطة بالمناطق الاقتصادية."), ("هل يمكنكم التنسيق مع الموردين خارج مصر؟", "نعم. نقوم كثيراً بالتنسيق مع الموردين الأجانب لضبط المستندات والتوقيت قبل الشحن."), ("ما المعلومات الأولى التي تحتاجونها؟", "وصف مختصر للبضاعة، الميناء المتوقع، توقيت الشحنة، وأي مستندات مبدئية متاحة.")],
    },
    "zh": {
        "title": "Al-Rouby海关 | 埃及清关与物流服务",
        "meta": "面向进口商、出口商和制造企业的埃及清关、货运协调、港口操作与 ACI 支持服务。",
        "hero_title": "覆盖埃及主要港口的清关服务 - 务实、合规、可靠",
        "hero_text": "Al-Rouby 为进口商、出口商和制造企业提供清关、货运协调以及港口执行支持，覆盖埃及主要口岸。",
        "hero_summary": "我们把单证审核、操作跟进、ACI 准备与放行后的运输衔接结合在一起，帮助货物以更稳定、更可控的节奏进入埃及市场。",
        "hero_points": ["支持 ACI 与 Nafeza", "覆盖埃及主要港口与经济区", "从文件审核到放行的持续跟进", "围绕时间、费用和下一步安排进行清晰沟通"],
        "stats": [("27+", "年实务经验"), ("12,000+", "已处理货运批次"), ("100%", "以合规执行为核心"), ("24/7", "客户沟通支持")],
        "process": [("提交货物资料", "提供货物说明、已有文件和时间计划，我们先判断操作路径与潜在风险。"), ("准备清关文件", "梳理所需资料、识别缺项，并安排装运前或到港前必须完成的工作。"), ("完成放行与交接", "跟进至放行，并把清关完成与下一段物流动作衔接起来。")],
        "reviews": [("团队务实，帮助我们在关键到港窗口避免了延误。", "工业进口客户"), ("文件流程解释得很清楚，也会提前指出真正的风险点。", "贸易公司"), ("到港后跟进扎实，沟通及时，不会给出不切实际的承诺。", "制造企业采购团队")],
        "faq": [("什么时候联系你们比较合适？", "越早越好，特别是当货物还需要做 ACI、单证审核或到港后交付计划时。"), ("是否只在一个港口提供服务？", "不是。我们支持埃及主要港口以及与经济区相关的货物流转。"), ("可以与境外供应商沟通文件吗？", "可以。我们经常协助境外供应商文件与埃及进口要求保持一致。"), ("初步需要提供什么信息？", "货物简要说明、预计港口、时间计划以及任何现有的草稿文件。")]},
}

ABOUT = {
    "en": {"title": "About Al-Rouby Customs | Egyptian Trade Support", "meta": "Learn how Al-Rouby supports Egyptian import and export operations with practical customs, shipping, and logistics execution.", "hero": "A customs and logistics partner built around practical execution in the Egyptian market.", "story": ["Al-Rouby has spent decades supporting businesses that need cargo to move through Egypt with fewer surprises and better preparation.", "Our work focuses on the operational details that usually determine whether a shipment stays on schedule: document readiness, timing discipline, port coordination, and realistic communication."], "mission": "We aim to make Egyptian import and export operations easier to manage by combining customs knowledge with practical coordination before and after cargo arrival.", "points": [("Execution before promises", "We focus on what actually needs to happen at each stage rather than relying on vague assurances."), ("Egypt-focused coordination", "Our advice is shaped by Egyptian procedures, document expectations, and port realities."), ("Commercial awareness", "We understand that every delay affects cost, inventory, production, and customer commitments."), ("Clear communication", "Clients receive realistic updates, not generic status messages.")]},
    "ar": {"title": "من نحن | الروبي للتخليص الجمركي", "meta": "تعرف على منهج الروبي في دعم عمليات الاستيراد والتصدير في مصر من خلال التنفيذ العملي والخبرة التشغيلية.", "hero": "شريك جمركي ولوجستي قائم على التنفيذ العملي داخل السوق المصري.", "story": ["على مدار سنوات طويلة، ساعدت الروبي الشركات التي تحتاج إلى تحريك بضائعها في مصر بدرجة أعلى من الجاهزية ووضوح الخطوات.", "يركز عملنا على التفاصيل التشغيلية التي تحدد عادة ما إذا كانت الشحنة ستبقى على المسار الصحيح: المستندات، التوقيت، التنسيق داخل الميناء، والتواصل الواقعي مع العميل."], "mission": "نهدف إلى جعل إدارة الاستيراد والتصدير في مصر أكثر سهولة من خلال الجمع بين المعرفة الجمركية والتنسيق العملي قبل وصول الشحنة وبعده.", "points": [("التنفيذ قبل الوعود", "نركز على ما يجب فعله فعلاً في كل مرحلة بدلاً من الوعود العامة."), ("تنسيق يراعي الواقع المصري", "نصيغ توصياتنا وفق الإجراءات المصرية ومتطلبات المستندات والواقع التشغيلي للموانئ."), ("فهم للأثر التجاري", "ندرك أن كل تأخير ينعكس على التكلفة والمخزون والإنتاج والتزامات العميل."), ("تواصل واضح", "يحصل العميل على تحديثات واقعية ومباشرة، لا رسائل عامة غير مفيدة.")]},
    "zh": {"title": "关于 Al-Rouby Customs | 埃及贸易执行支持", "meta": "了解 Al-Rouby 如何以务实方式支持埃及进口、出口、清关与物流执行工作。", "hero": "一家围绕埃及市场实务执行而建立的清关与物流合作伙伴。", "story": ["多年来，Al-Rouby 一直服务于需要在埃及市场内稳定推进货物流转的企业，重点在于提前准备和实际落地。", "我们的工作核心不是空泛承诺，而是那些真正决定项目是否顺利的细节：文件准备、时间管理、港口协同以及对客户的清晰反馈。"], "mission": "我们的目标是把埃及进出口操作变得更容易管理，通过清关经验与实际协调能力，帮助客户在货物到港前后都更有把握。", "points": [("先执行，再承诺", "先明确每一步真正要做什么，而不是用模糊说法替代执行。"), ("立足埃及市场", "我们的建议基于埃及监管要求、单证习惯和港口操作现实。"), ("理解商业影响", "我们清楚延误会直接影响成本、库存、生产和客户承诺。"), ("沟通清晰", "客户拿到的是可执行、可判断的更新，而不是泛泛而谈的状态说明。")]},
}

CONTACT = {
    "en": {"title": "Contact Al-Rouby Customs | Start the Shipment Discussion", "meta": "Contact Al-Rouby for shipment planning, customs questions, and practical guidance for imports or exports involving Egypt.", "hero": "Contact our team to review your shipment, timeline, and import or export requirements."},
    "ar": {"title": "اتصل بالروبي | ابدأ مناقشة الشحنة", "meta": "تواصل مع الروبي لمناقشة التخطيط للشحنة أو الاستفسارات الجمركية أو متطلبات الاستيراد والتصدير في مصر.", "hero": "تواصل مع فريقنا لمراجعة الشحنة والتوقيت ومتطلبات الاستيراد أو التصدير."},
    "zh": {"title": "联系 Al-Rouby | 开始讨论您的货运项目", "meta": "联系 Al-Rouby 团队，讨论进口、出口、清关与到港执行问题。", "hero": "欢迎联系团队讨论货物、时间安排以及埃及进口或出口要求。"},
}

BLOGS = {
    "customs-clearance-guide-egypt": {
        "related": ["customs-clearance", "aci-nafeza", "shipping"],
        "en": {"title": "Customs Clearance in Egypt: Practical 2026 Guide | Al-Rouby", "meta": "A practical guide to customs clearance in Egypt covering core documents, ACI timing, examination flow, delay risks, and importer planning.", "hero": "Customs Clearance in Egypt: Practical 2026 Guide", "intro": "Egyptian customs clearance is an operational process, not just a paperwork event. Importers that prepare the file early usually reduce delay, cost exposure, and last-minute confusion.", "sections": [("What customs clearance covers in Egypt", "Clearance work starts before cargo is physically released. It includes document review, checking the intended customs regime, confirming whether permits apply, and preparing for questions that may appear after arrival.", []), ("Core documents every importer should review", "The basic file usually includes the commercial invoice, packing list, transport document, and certificate of origin. Many costly delays start when these documents describe the cargo differently or arrive too late for meaningful review.", ["Commercial invoice with clear buyer, seller, value, and goods description", "Packing list that matches quantities and packaging", "Bill of lading or airway bill that aligns with consignee and routing details", "Origin or supporting certificates where the cargo or bank process requires them"]), ("ACI and pre-arrival readiness", "ACI should be treated as part of the wider clearance plan because it affects supplier coordination, document timing, and importer readiness before loading and arrival.", []), ("Examination and release flow", "Once cargo arrives, customs work can involve declaration review, requests for clarification, examination or sampling, and operational follow-up with the port side. A well-prepared file shortens the time spent answering avoidable questions.", []), ("Common reasons shipments are delayed", "Importers should expect delay when documents do not match, permits are assumed but not ready, or classification and value details were never clarified before the shipment moved.", ["Invoice, packing list, and transport document do not match", "ACI or supplier-side work started too late", "Permits or certificates were not ready", "Classification, valuation, or delivery planning was left unresolved"])]},
        "ar": {"title": "التخليص الجمركي في مصر: دليل عملي 2026 | الروبي", "meta": "دليل عملي للتخليص الجمركي في مصر يشمل المستندات الأساسية وتوقيت ACI ومسار الفحص وأسباب التأخير وكيفية تجهيز المستورد للملف.", "hero": "التخليص الجمركي في مصر: دليل عملي 2026", "intro": "التخليص الجمركي في مصر عملية تشغيلية متكاملة وليست مجرد خطوة ورقية. وكلما جرى تجهيز الملف مبكراً، انخفضت احتمالات التأخير والتكلفة غير المخطط لها.", "sections": [("ماذا يشمل التخليص الجمركي في مصر؟", "العمل الجمركي يبدأ قبل أن تصبح الحاوية جاهزة للإفراج الفعلي، فهو يشمل مراجعة المستندات وربط الشحنة بالنظام المناسب والتحقق من أي تصاريح أو شهادات مطلوبة قبل الوصول.", []), ("المستندات الأساسية التي يجب مراجعتها", "عادة ما يشمل الملف الفاتورة التجارية وقائمة التعبئة ومستند النقل وشهادة المنشأ، وقد تحتاج بعض الشحنات إلى موافقات إضافية. كثير من التأخيرات تبدأ من اختلاف هذه المستندات أو من إعدادها متأخراً.", ["فاتورة تجارية واضحة", "قائمة تعبئة مطابقة", "بوليصة شحن أو بوليصة طيران متسقة", "شهادات منشأ أو شهادات داعمة عند الحاجة"]), ("ACI والجاهزية قبل الوصول", "لا ينبغي التعامل مع ACI على أنه إجراء منفصل، بل هو جزء من الخطة الكاملة لأنه يؤثر في توقيت المستندات وتنسيق المورد واستعداد المستورد قبل التحميل.", []), ("مسار الفحص والإفراج", "بعد وصول الشحنة، قد يمر العمل بمراجعة الإقرار وطلبات استيضاح ومعاينة أو سحب عينات، ثم متابعة تشغيلية مع الميناء. الملف الجيد يقلل الوقت الضائع في الرد على أسئلة كان يمكن تفاديها.", []), ("أكثر أسباب التأخير شيوعاً", "يظهر التأخير غالباً عندما تختلف بيانات المستندات أو يتأخر ملف ACI أو تغيب التصاريح أو تظل مسألة التصنيف والقيمة غير محسومة قبل تحرك الشحنة.", ["اختلاف الفاتورة وقائمة التعبئة ومستند النقل", "بدء ملف ACI متأخراً", "عدم جاهزية التصاريح", "ترك أسئلة التصنيف أو القيمة دون حسم"]) ]},
        "zh": {"title": "埃及清关实务指南 2026 | Al-Rouby", "meta": "一份面向进口商的埃及清关实务指南，涵盖核心单证、ACI 时序、查验放行流程、延误原因与到港前准备。", "hero": "埃及清关实务指南 2026", "intro": "在埃及，清关不是单纯的交文件动作，而是一整套与时间、单证和港口执行紧密相关的操作流程。准备越早，越能减少延误和额外成本。", "sections": [("埃及清关到底包括什么", "清关工作通常在货物到港前就已经开始。它不仅包括提交申报资料，还包括审查商业文件、确认进口模式、判断是否需要许可证，以及提前准备到港后可能出现的查验或补件问题。", []), ("必须先核对的核心单证", "基础文件通常包括商业发票、装箱单、提单或空运单，以及原产地证明。不同货物还可能需要技术许可或产品类别相关证书，而且这些文件必须保持一致。", ["商业发票要清楚写明买卖双方、金额和货物描述", "装箱单要与实际包装和数量结构一致", "提单或空运单要与收货人和运输路径信息匹配", "涉及产地或监管要求的证明文件要提前确认"]), ("ACI 与到港前准备的关系", "ACI 不能被视为孤立的合规动作。它直接影响装运前单证准备、供应商协同和进口方内部节奏。", []), ("查验与放行的一般流程", "货物到港后，通常会进入申报审核、资料补充、查验或抽样，以及与港口侧的现场协同等阶段。前期准备越扎实，到港后的解释和补件就越少。", []), ("最常见的延误原因", "许多延误不是因为货物本身，而是因为基础文件、ACI、许可证和分类信息在前期没有处理清楚。", ["发票、装箱单与运输单证之间描述不一致", "ACI 或供应商文件准备过晚", "许可证并未真正准备完成", "编码、价格或交付安排在前期没有确认"]) ]},
    },
    "aci-system-guide": {
        "related": ["aci-nafeza", "customs-clearance", "shipping"],
        "en": {"title": "Egypt ACI System Guide: Registration and ACID Workflow | Al-Rouby", "meta": "Understand how the Egypt ACI system fits into supplier coordination, ACID timing, Nafeza preparation, and shipment planning.", "hero": "Egypt ACI System Guide: Registration and ACID Workflow", "intro": "ACI is most useful when importers treat it as a planning discipline rather than a last-minute compliance task.", "sections": [("Who needs to think about ACI first", "The importer should take the lead because importer-side readiness determines whether supplier documents can be aligned in time. However, the exporter, bank-facing parties, and logistics partners all influence whether the file is practical and complete.", []), ("Nafeza roles and document responsibilities", "Importers should define who is responsible for commercial documents, shipping details, registration data, and any banking references. Many problems appear when each party assumes another party is handling the detail.", ["Importer-side registration and authority", "Supplier-side commercial documents", "Transport details that match the shipment plan", "Banking and supporting references where needed"]), ("Why ACID timing matters", "ACID timing matters because corrections become more disruptive once loading or sailing is near. ACI should be treated as part of the shipment launch plan, not as a document pack assembled at the last safe moment.", []), ("Supplier and bank document handoff", "Many delays occur because supplier documents were issued, but not in the format or sequence the importer and Egyptian process actually need.", []), ("Common compliance mistakes", "Importers usually struggle when they start the file too late, assume supplier documents are correct without checking them, or separate ACI work from the broader customs and delivery plan.", ["Starting the file only when loading is already close", "Leaving shipment details ambiguous", "No clear ownership between importer, supplier, and logistics parties", "Treating ACI as separate from the wider clearance plan"])]},
        "ar": {"title": "دليل نظام ACI في مصر: التسجيل ومسار ACID | الروبي", "meta": "تعرف على دور نظام ACI في تنسيق مستندات المورد وتوقيت ACID والتعامل مع نافذة والتخطيط العملي للشحنة.", "hero": "دليل نظام ACI في مصر: التسجيل ومسار ACID", "intro": "يكون نظام ACI أكثر فاعلية عندما يتعامل معه المستورد باعتباره جزءاً من التخطيط للشحنة وليس مجرد التزام متأخر.", "sections": [("من يجب أن يبدأ التفكير في ACI أولاً؟", "المستورد هو الطرف الذي يجب أن يقود الملف، لأن جاهزية المستورد تحدد ما إذا كانت مستندات المورد يمكن مواءمتها في الوقت المناسب أم لا.", []), ("أدوار نافذة ومسؤوليات المستندات", "ينبغي تحديد المسؤول عن المستندات التجارية وبيانات الشحن وبيانات التسجيل وأي مراجع مرتبطة بالبنك أو السداد، لأن كثيراً من المشكلات تظهر عندما يفترض كل طرف أن الآخر يتولى التفاصيل.", ["جاهزية بيانات وتسجيل المستورد", "مستندات المورد التجارية", "بيانات الشحن المتطابقة مع خطة التحميل", "المراجع البنكية عند الحاجة"]), ("لماذا يهم توقيت ACID؟", "أي تعديل يصبح أكثر كلفة وتعقيداً عندما يقترب التحميل أو الإبحار. لذلك يجب التعامل مع ملف ACI كجزء من خطة الشحنة نفسها.", []), ("تسليم مستندات المورد والبنك", "كثير من التأخيرات تحدث لأن المستندات لم تصدر بالصيغة أو الترتيب الذي يحتاجه المستورد والإجراء المصري.", []), ("أخطاء امتثال شائعة", "تظهر المشاكل عندما يبدأ الملف متأخراً أو تُترك تفاصيل البضاعة أو القيمة أو بيانات الشحن بصورة غير واضحة.", ["بدء الملف مع اقتراب التحميل", "الاعتماد على صحة مستندات المورد دون مراجعة", "عدم توزيع المسؤوليات بوضوح", "فصل ملف ACI عن خطة التخليص والنقل"])]},
        "zh": {"title": "埃及 ACI 系统指南：注册与 ACID 流程 | Al-Rouby", "meta": "理解埃及 ACI 如何影响供应商协同、ACID 时间、Nafeza 文件准备以及整体装运计划。", "hero": "埃及 ACI 系统指南：注册与 ACID 流程", "intro": "当进口商把 ACI 当成计划纪律而不是临近装运才处理的合规任务时，整个流程通常会更稳定。", "sections": [("谁应该最先关注 ACI", "进口商应当是文件推进的主导方，因为进口方是否准备充分，决定了供应商资料能否及时对齐。", []), ("Nafeza 相关角色与文件责任", "很多问题来自责任模糊。进口商应尽早明确商业文件、运输资料、注册数据以及银行参考资料分别由谁负责。", ["进口方的注册状态与推进权限", "供应商商业文件的格式与内容", "运输资料是否与实际装运计划一致", "涉及结算结构时的银行信息"]), ("为什么 ACID 的时间点很关键", "一旦临近装货或开船，任何修正都会更贵、更被动，因此 ACI 文件应被视为项目启动计划的一部分。", []), ("供应商与银行文件交接", "很多延误不是因为文件没有出，而是因为文件虽然出了，却不是进口方和埃及流程真正需要的版本、顺序或格式。", []), ("常见合规错误", "最常见的问题是启动过晚、默认供应商文件正确、货物描述模糊，以及把 ACI 与后续清关完全割裂开来。", ["等到装货临近才开始推进", "没有核对供应商文件是否与进口要求一致", "货物描述、金额或运输信息留有模糊空间", "没有明确责任分工"])]},
    },
    "sea-freight-types": {
        "related": ["shipping", "freight-forwarding", "customs-clearance"],
        "en": {"title": "FCL vs LCL Shipping to Egypt | Practical Comparison | Al-Rouby", "meta": "A practical comparison of FCL and LCL shipping into Egypt, including timing, handling, cost drivers, and customs implications.", "hero": "FCL vs LCL Shipping to Egypt", "intro": "Choosing between FCL and LCL is not only about volume. The right option depends on timing pressure, cargo sensitivity, cost structure, and how the shipment will move through Egyptian port procedures.", "sections": [("What FCL and LCL mean in practice", "FCL generally means one importer is using a full container movement, while LCL means goods are consolidated with other cargo. The distinction affects handling touchpoints, documentation flow, and timing control.", []), ("When FCL is usually better", "FCL is often better when cargo volume is high enough to justify the container, when timing is commercially sensitive, or when the consignee wants fewer consolidation touchpoints.", ["Better control over container timing", "Fewer third-party handling steps", "More predictable cargo separation"]), ("When LCL can make sense", "LCL can be practical for smaller shipment volumes or when the importer wants to avoid paying for unused container space, but the savings must be compared against consolidation timing and handling exposure.", []), ("Egypt-focused timing and customs considerations", "For cargo entering Egypt, shipping mode affects how importers should plan documents, release expectations, and warehouse readiness. The customs file must still be complete either way.", []), ("Decision checklist", "Importers should compare the full landed workflow, not only the ocean freight line item, before deciding on FCL or LCL.", ["How much cargo volume is moving?", "Is the shipment time-sensitive?", "How much handling risk can the cargo tolerate?", "Will consolidation timing create extra exposure in Egypt?"])]},
        "ar": {"title": "FCL مقابل LCL للشحن إلى مصر | مقارنة عملية | الروبي", "meta": "مقارنة عملية بين الشحن الكامل FCL والشحن المجمع LCL إلى مصر من حيث التوقيت والمناولة والتكلفة وأثر كل خيار على التخليص.", "hero": "FCL مقابل LCL للشحن إلى مصر", "intro": "الاختيار بين FCL وLCL لا يعتمد على الحجم فقط، بل يرتبط بحساسية التوقيت وطبيعة البضاعة وهيكل التكلفة وكيف ستتحرك الشحنة داخل الميناء المصري.", "sections": [("ماذا يعني FCL وLCL عملياً؟", "يعني FCL عادة أن الحاوية مخصصة لشحنة عميل واحد، بينما يعني LCL أن الشحنة مجمعة مع بضائع أخرى. هذا الفارق يؤثر على نقاط المناولة وتدفق المستندات ومدى سيطرة المستورد على التوقيت.", []), ("متى يكون FCL هو الخيار الأفضل؟", "يكون FCL أفضل غالباً عندما يكون حجم البضاعة كبيراً أو عندما يحتاج المستورد إلى تقليل نقاط التجميع والمناولة أو عندما تكون الحساسية الزمنية مرتفعة.", ["تحكم أكبر في توقيت الحاوية", "مراحل مناولة أقل", "وضوح أكبر في فصل الشحنة"]), ("متى يكون LCL مناسباً؟", "قد يكون LCL مناسباً عندما يكون حجم الشحنة صغيراً، لكن يجب مقارنة الوفر المتوقع مع توقيتات التجميع وفك التجميع واحتمال تأثر الشحنة بحركة أطراف أخرى.", []), ("اعتبارات مصرية مرتبطة بالتوقيت والجمارك", "بالنسبة للشحنات القادمة إلى مصر، يؤثر نمط الشحن على كيفية تجهيز المستندات وتوقعات الإفراج وجاهزية المخزن، حتى وإن كان الملف الجمركي مطلوباً في الحالتين.", []), ("قائمة قرار سريعة", "ينبغي النظر إلى المسار الكامل حتى التسليم النهائي، وليس فقط إلى بند أجرة الشحن البحري.", ["ما حجم البضاعة الحالي؟", "هل الشحنة مرتبطة بإنتاج أو موعد حساس؟", "ما مستوى المخاطر المقبول في المناولة؟", "هل يمكن أن يؤدي توقيت التجميع إلى تكلفة إضافية؟"])]},
        "zh": {"title": "整箱与拼箱发运至埃及：实务比较 | Al-Rouby", "meta": "从时间、操作环节、成本驱动与清关影响角度，对发运至埃及的整箱与拼箱进行实务比较。", "hero": "整箱与拼箱发运至埃及：实务比较", "intro": "整箱还是拼箱，不只是体积计算题。真正需要比较的是交期压力、货物敏感度、综合成本以及到埃及后的口岸执行方式。", "sections": [("整箱和拼箱在实务上的区别", "整箱通常意味着一票货以完整集装箱形式操作，拼箱则意味着与其他货物共同装运。二者在交接节点、文件节奏和时间控制上的差异非常明显。", []), ("什么时候整箱更合适", "当货量足够、交期敏感、或客户希望减少中间拆拼和多方处理时，整箱通常更合适。", ["更容易掌握集装箱时间节奏", "中间处理环节更少", "包装完整性和货物分离更可控"]), ("什么时候拼箱有意义", "当货量较小、不想承担整箱空间成本时，拼箱可能更经济，但必须比较拼箱等待时间、拆箱环节和共享流转带来的风险。", []), ("面向埃及进口的实际影响", "进入埃及市场时，运输模式会影响进口商如何准备单证、预估放行节奏以及安排仓库收货。", []), ("快速判断清单", "选择模式时要比较完整落地流程，而不只是海运费这一项。", ["当前货量有多大？", "这票货是否直接关系到生产或销售时点？", "货物对多次搬运的容忍度有多高？", "收货方更看重最低成本还是控制力？"])]},
    },
    "egypt-port-fees": {
        "related": ["customs-clearance", "logistics", "shipping"],
        "en": {"title": "Egypt Port Fees and Charges: Practical Cost Guide | Al-Rouby", "meta": "A practical guide to Egyptian port fee categories, customs-related costs, and the operational factors that affect landed cost.", "hero": "Egypt Port Fees and Charges: Practical Cost Guide", "intro": "Importers often ask for one fixed number, but port costs in Egypt are usually made up of several categories that depend on cargo, operator, timing, and how well the file was prepared.", "sections": [("Main categories of port cost", "Port-related cost is rarely a single line item. It usually includes handling, storage, release timing, transport interfaces, and the commercial structure of the shipment.", []), ("What changes the cost from one shipment to another", "Two shipments of similar value can create different landed costs because the port, operator, cargo profile, and execution timing are different.", ["Port and terminal operator", "Cargo type and packaging", "Container model and shipment size", "Document readiness after arrival"]), ("Customs-related cost drivers", "Port charges and customs-driven cost exposure are closely connected. Delays linked to document mismatch or missing approvals often increase the time cargo spends under cost-bearing conditions.", []), ("Demurrage, storage, and avoidable exposure", "Importers should pay special attention to demurrage and storage because these costs escalate when release timing, trucking, and warehouse readiness are not planned together.", []), ("How to prepare a more useful quote request", "A stronger quote request gives context, not only value. The goal is to understand which costs are predictable and which depend on execution timing.", ["Share port, cargo type, and shipment mode", "Clarify permits or special handling", "State final delivery expectations", "Ask which costs depend on timing"]) ]},
        "ar": {"title": "رسوم وتكاليف الموانئ في مصر: دليل عملي | الروبي", "meta": "دليل عملي لفئات رسوم الموانئ في مصر والتكاليف المرتبطة بالجمارك والعوامل التشغيلية التي تؤثر على التكلفة النهائية للشحنة.", "hero": "رسوم وتكاليف الموانئ في مصر: دليل عملي", "intro": "يطلب كثير من المستوردين رقماً ثابتاً واحداً، لكن التكلفة في الموانئ المصرية تتكون عادة من عدة بنود تختلف حسب نوع البضاعة والمشغل والتوقيت ومدى جاهزية الملف.", "sections": [("الفئات الرئيسية لتكلفة الميناء", "تكلفة الميناء ليست بنداً واحداً فقط. فهي تضم عادة مصروفات مرتبطة بالمناولة والتخزين وتوقيت الإفراج والتعامل مع النقل والترتيب التجاري للشحنة.", []), ("ما الذي يغيّر التكلفة من شحنة لأخرى؟", "قد تختلف التكلفة النهائية بين شحنتين متقاربتين في القيمة إذا اختلفت ظروف التنفيذ أو المشغل أو جاهزية الملف.", ["الميناء والمشغل", "نوع البضاعة وطريقة تغليفها", "نمط الحاوية أو حجم الشحنة", "مدى جاهزية الملف بعد الوصول"]), ("العوامل الجمركية المؤثرة في التكلفة", "هناك ارتباط مباشر بين رسوم الميناء والتعرض لتكلفة إضافية ناتجة عن الجمارك. فالتأخير بسبب اختلاف المستندات أو نقص الموافقات يزيد زمن بقاء الشحنة تحت بنود تكلفة إضافية.", []), ("الأرضيات والتخزين والتكلفة التي يمكن تجنبها", "ترتفع الأرضيات والتخزين عندما لا يتم تخطيط الإفراج والنقل الداخلي والاستلام معاً. لذلك فبطء التنفيذ قد يجعل الشحنة أكثر تكلفة من المتوقع.", []), ("كيف تطلب عرض تكلفة أكثر فائدة؟", "الهدف من طلب التسعير ليس رقمًا فقط، بل فهم ما هو ثابت وما الذي يتأثر بالتوقيت التنفيذي.", ["اذكر الميناء ونوع البضاعة ونمط الشحن", "وضح التصاريح أو المتطلبات الخاصة", "حدد متطلبات التسليم النهائي", "اسأل أي البنود يعتمد على التوقيت"]) ]},
        "zh": {"title": "埃及港口费用与收费：实务成本指南 | Al-Rouby", "meta": "从港口收费类别、清关相关成本到操作变量，帮助进口商更准确理解埃及落地成本结构。", "hero": "埃及港口费用与收费：实务成本指南", "intro": "很多进口商希望得到一个固定总价，但埃及港口端的实际成本通常由多类费用构成，并受到货物类型、操作时点和清关准备程度影响。", "sections": [("港口成本通常由哪些部分组成", "港口成本很少只有一个项目。它通常由装卸、堆存、放行节奏、运输衔接以及货物商业结构相关的多个费用组成。", []), ("为什么不同货物的成本差异会很大", "即使货值接近，两票货在最终落地成本上也可能出现明显差别，因为港口、操作方、货物性质和时间节点不同。", ["涉及的港口和码头不同", "货物性质和包装方式不同", "整箱、拼箱或项目货节奏不同", "到港后文件准备程度不同"]), ("与清关直接相关的成本驱动", "港口费用与清关准备相互关联。文件不一致、许可证缺失、编码不明确等问题，都会增加货物处于收费状态的时间。", []), ("滞箱、堆存与可避免的费用暴露", "如果放行、提货和仓库接收没有放在同一计划里，滞箱和堆存费用往往增长很快。", []), ("怎样提出更有价值的询价", "一个更有价值的询价，会说明港口、货物、节奏和交付要求，帮助判断哪些费用可预测，哪些要看执行时点。", ["说明目标港口和货物类型", "提前告知是否涉及许可证或特殊监管", "明确最终交付要求", "区分固定费用和时点相关费用"]) ]},
    },
    "hs-code-guide": {
        "related": ["customs-clearance", "aci-nafeza", "shipping"],
        "en": {"title": "HS Code Classification in Egypt | Practical Importer Guide | Al-Rouby", "meta": "A practical guide to HS code classification for imports into Egypt, including supporting documents, risk points, and timing advice.", "hero": "HS Code Classification in Egypt", "intro": "HS code work is not only a technical coding exercise. In practice, the classification decision affects duties, document expectations, permit requirements, and how confidently the customs file can be prepared.", "sections": [("Why HS code classification matters", "The classification decision influences duties, taxes, commercial planning, and the documents that may be requested. If the importer treats HS coding as an afterthought, the shipment is more likely to face questions later.", []), ("What information supports classification", "The more precise the supporting information, the easier it is to reduce ambiguity before customs review begins.", ["Clear product description", "Material and technical details", "Catalogues or datasheets", "Commercial context of use or sale"]), ("How importers should approach the workflow", "Classification should be reviewed early in the shipment plan, especially for new products, technically complex goods, or cargo that might require permits.", []), ("What can go wrong if the classification is weak", "An uncertain HS code can affect duty assumptions, document readiness, and how confidently the customs file can be defended.", []), ("When to validate before shipment", "Validation is especially important when a product is new, technically complex, or commercially time-sensitive.", ["When the item is new to the importer", "When multiple descriptions seem possible", "When permits or duties depend heavily on classification", "When the shipment cannot absorb delay"]) ]},
        "ar": {"title": "تصنيف HS Code في مصر | دليل عملي للمستورد | الروبي", "meta": "دليل عملي لتصنيف HS Code للواردات إلى مصر يشمل المستندات المطلوبة ونقاط المخاطرة وتوقيت المراجعة المناسب.", "hero": "تصنيف HS Code في مصر", "intro": "تصنيف HS ليس مجرد تمرين فني على اختيار كود. عملياً، يؤثر القرار على الرسوم والمتطلبات المستندية والتراخيص ومدى قوة الملف الجمركي.", "sections": [("لماذا يهم تصنيف HS Code؟", "قرار التصنيف يؤثر على الرسوم والضرائب والتخطيط التجاري والمستندات التي قد تطلب لاحقاً. وإذا تعامل المستورد مع الكود كخطوة ثانوية، فمن المرجح أن تظهر الأسئلة أثناء التخليص.", []), ("ما المعلومات التي تدعم التصنيف؟", "كلما كانت المعلومات المساندة أكثر دقة، كان من الأسهل تقليل الغموض قبل أن تبدأ المراجعة الجمركية.", ["وصف واضح للمنتج ووظيفته", "تفاصيل الخامة أو المواصفات الفنية", "كتالوجات أو Data Sheets", "سياق تجاري يوضح الاستخدام أو البيع"]), ("كيف يجب أن يتعامل المستورد مع مسار التصنيف؟", "ينبغي مراجعة التصنيف مبكراً ضمن خطة الشحنة، خصوصاً للمنتجات الجديدة أو المعقدة فنياً أو التي قد تحتاج إلى موافقات خاصة.", []), ("ماذا يحدث إذا كان التصنيف ضعيفاً؟", "التصنيف غير الواضح يؤثر على توقعات الرسوم وعلى جاهزية المستندات وعلى قوة الملف الجمركي، وقد يستهلك وقتاً وتكلفة إضافية.", []), ("متى يجب التحقق قبل الشحن؟", "التحقق المبكر يصبح أكثر أهمية كلما زادت حساسية الشحنة أو تعقد المنتج.", ["عندما يكون المنتج جديداً على المستورد", "عندما تكون البضاعة معقدة أو تحتمل أكثر من وصف", "عندما ترتبط الموافقات أو الرسوم بالتصنيف", "عندما يكون التوقيت التجاري حساساً"]) ]},
        "zh": {"title": "埃及 HS 编码分类指南 | 进口商实务参考 | Al-Rouby", "meta": "面向进口商的埃及 HS 编码实务指南，涵盖分类所需资料、风险点以及应在何时提前确认。", "hero": "埃及 HS 编码分类指南", "intro": "HS 编码不是单纯的技术编号工作。它会直接影响税费、文件准备、许可证要求以及整个清关文件的可信度。", "sections": [("为什么 HS 编码很重要", "分类结果会影响税费预估、商业决策以及后续可能需要准备的文件。如果把 HS 编码放到最后才处理，清关阶段就更容易出现解释不清和准备不足的问题。", []), ("分类通常需要哪些支持信息", "支持信息越具体，越能在清关前减少编码判断上的模糊空间。", ["清楚说明货物是什么和用途的产品描述", "材质、成分、技术规格等关键属性", "目录、技术资料或型号信息", "帮助理解货物销售或使用场景的商业背景"]), ("进口商应如何安排分类工作", "对于新产品、技术性较强的货物或可能涉及许可证的商品，最好在出运前就审查 HS 分类。", []), ("分类不稳会带来什么后果", "编码不明确不仅影响税费判断，还会削弱整份清关文件的准备质量，并增加后续解释成本。", []), ("哪些情况下必须在发运前确认", "如果产品新、技术复杂、许可证依赖分类，或项目时间敏感，就更需要提前确认。", ["该产品对进口商来说是首次操作", "产品技术属性复杂", "许可证或税负高度依赖分类结果", "项目无法承受口岸延误"]) ]},
    },
}
