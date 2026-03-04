#!/usr/bin/env python3
"""Replace inline theme script with external theme-init.js across all HTML files."""
import os, sys, re, glob

sys.stdout.reconfigure(encoding='utf-8')

base = os.path.join(os.path.dirname(__file__), 'public_html')

# Patterns to match the inline theme script block
# Pattern 1: The full script block with various formatting
patterns = [
    # Multiline pattern for the inline script
    re.compile(
        r'<script>\s*\(function\s*\(\)\s*\{[\s\S]*?localStorage\.getItem\("theme"\)[\s\S]*?\}\)\(\);\s*</script>',
        re.MULTILINE
    ),
]

replacement = '<script src="/js/theme-init.js"></script>'

html_files = glob.glob(os.path.join(base, '**', '*.html'), recursive=True)

count = 0
for filepath in sorted(html_files):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    for pattern in patterns:
        content = pattern.sub(replacement, content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        relpath = os.path.relpath(filepath, base)
        print(f"  Updated: {relpath}")
        count += 1

print(f"\nDone. Updated {count} files.")
