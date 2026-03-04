## Project Structure Note

This repository contains both the production website and the Python automation scripts used to generate and maintain the HTML pages.

The website files are located inside:

public_html/

The automation scripts are located inside:

scripts/

The Python scripts automatically generate and update pages, including:

- services pages
- port pages
- blog content
- Arabic language pages
- accessibility fixes
- theme script refactoring

To regenerate pages:

python scripts/generate_pages.py
