#!/usr/bin/env python3
"""Fix accessibility issues across all HTML files:
1. Hero card: h3 -> h2 for "At a Glance" / Arabic/Chinese equivalents
2. Trust stats: h3 -> span.trust-number (semantic fix, not headings)
3. Testimonial client names: h4 -> h3
4. Container count label associations: wrap inputs inside labels
"""
import os, sys, re, glob

sys.stdout.reconfigure(encoding='utf-8')

base = os.path.join(os.path.dirname(__file__), 'public_html')
html_files = glob.glob(os.path.join(base, '**', '*.html'), recursive=True)

count = 0
for filepath in sorted(html_files):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Hero card: <h3>At a Glance</h3> -> <h2>At a Glance</h2>
    # Also Arabic: نظرة سريعة / Chinese: 核心优势
    content = content.replace('<h3>At a Glance</h3>', '<h2>At a Glance</h2>')
    content = content.replace('<h3>نظرة سريعة</h3>', '<h2>نظرة سريعة</h2>')
    content = content.replace('<h3>核心优势</h3>', '<h2>核心优势</h2>')

    # 2. Trust stats: Replace <h3>27+</h3>, <h3>12,000+</h3>, etc. with <span class="trust-number">
    # Match pattern: inside .trust-item div, h3 contains numbers/stats
    trust_pattern = re.compile(
        r'<div class="trust-item">\s*<h3>([^<]+)</h3>\s*<p>([^<]+)</p>',
        re.MULTILINE
    )
    content = trust_pattern.sub(
        r'<div class="trust-item">\n              <span class="trust-number" aria-hidden="true">\1</span>\n              <p>\2</p>',
        content
    )

    # 3. Testimonial client names: <h4> -> <h3>
    # Inside .client-info div
    client_pattern = re.compile(r'(<div class="client-info">\s*)<h4>([^<]+)</h4>', re.MULTILINE)
    content = client_pattern.sub(r'\1<h3>\2</h3>', content)

    # 4. Container count labels: add for/id association
    # Pattern: <label>20ft Container Count</label><input type="number" name="containers_20ft"
    content = content.replace(
        '<label>20ft Container Count</label\n                  ><input\n                    type="number"\n                    name="containers_20ft"',
        '<label for="containers_20ft">20ft Container Count</label\n                  ><input\n                    id="containers_20ft"\n                    type="number"\n                    name="containers_20ft"'
    )
    content = content.replace(
        '<label>40ft Container Count</label\n                  ><input\n                    type="number"\n                    name="containers_40ft"',
        '<label for="containers_40ft">40ft Container Count</label\n                  ><input\n                    id="containers_40ft"\n                    type="number"\n                    name="containers_40ft"'
    )

    # Arabic container labels
    content = content.replace(
        '<label>عدد حاويات 20 قدم</label><input type="number" name="containers_20ft"',
        '<label for="containers_20ft">عدد حاويات 20 قدم</label><input id="containers_20ft" type="number" name="containers_20ft"'
    )
    content = content.replace(
        '<label>عدد حاويات 40 قدم</label><input type="number" name="containers_40ft"',
        '<label for="containers_40ft">عدد حاويات 40 قدم</label><input id="containers_40ft" type="number" name="containers_40ft"'
    )

    # Chinese container labels
    content = content.replace(
        '<label>20尺柜数量</label\n                  ><input\n                    type="number"\n                    name="containers_20ft"',
        '<label for="containers_20ft">20尺柜数量</label\n                  ><input\n                    id="containers_20ft"\n                    type="number"\n                    name="containers_20ft"'
    )
    content = content.replace(
        '<label>40尺柜数量</label\n                  ><input\n                    type="number"\n                    name="containers_40ft"',
        '<label for="containers_40ft">40尺柜数量</label\n                  ><input\n                    id="containers_40ft"\n                    type="number"\n                    name="containers_40ft"'
    )

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        relpath = os.path.relpath(filepath, base)
        print(f"  Updated: {relpath}")
        count += 1

print(f"\nDone. Updated {count} files.")
