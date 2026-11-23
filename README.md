# jadeaerospace.com

Public website for Jade Aerospace Limited (玉航天有限公司).

- `index.html`: English
- `zh/index.html`: Simplified Chinese
- `assets/style.css`: all styling (dark "satellite scene" look: jade #51BAC1 rules, peach #F6CDB4 only for planned/target items)
- `assets/site.js`: side rail and photo-frame corner marks
- `assets/contact.js`: contact form (FormSubmit → aila@alyaspace.com) and copy-email button
- `assets/`: images
- `DESIGN.md`: the design rules, if present

## Editing

**Small text change:** open the HTML file on GitHub, click the pencil, edit, and commit to `main`. The site updates in about a minute. Change the English and the Chinese page together.

**Bigger change:** all text for both languages lives in one place, `tools/build_pages.py`. Edit it there, then run `python3 tools/build_pages.py .` from this folder to regenerate both pages. If you edit the HTML directly instead, the next person running the script will overwrite your edit, so pick one way and stick to it.

## Don't put on this site

Client names (NDAs), funding numbers, applications in progress, or partners not cleared for public naming.
