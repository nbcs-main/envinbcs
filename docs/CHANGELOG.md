# Changelog

## Step 1: rebrand, home page (in progress)

- New design system in `assets/css/site.css` (colour/font tokens at the top; plain CSS, no framework, no jQuery). Fonts: Manrope (headings) + Inter (body), self-hosted. The two font files must be added, see `assets/fonts/README.md`; until then the site falls back to system fonts.
- New static `index.html` using only `site.css` and `assets/js/site.js`. Services, projects, partners and the three latest stories are real HTML, so crawlers and visitors without JavaScript see them. The footer is inline on this page.
- Responsive hero and card images generated from the original photos (`*-800.jpg`, `compliance-tomfisk-1440.jpg`).
- Open Graph / Twitter tags added to the home page.
- The other pages still use the legacy `main.css` + `includes/footer.html` until they are converted. Do not merge to `main` until all pages are converted, or the site will look inconsistent between pages.
- `scripts/check_site.py` now also verifies files referenced from CSS `url()`.

## Step 0: cleanup (no design change)

- Images optimized in place (same file names): 34.1 MB reduced to 4.9 MB across photos, partner logos and the logo. Two unused images deleted.
- Removed template leftovers: `elements.html`, `generic.html`, `assets/sass/` (out of date). `blogs.html` was a placeholder page listed in the sitemap; it now redirects to `stories/all-stories.html` and was removed from the sitemap.
- Project cards no longer link to the placeholder page (`url: ""` renders a plain card).
- Added `lang="en"`, canonical links, descriptions for the contact and review pages; re-enabled pinch-zoom; descriptive `title` on iframes; fixed missing/hidden references (home video poster, Vingno logo, stray "." on the home page).
- Fonts and Font Awesome now load from `<link>` tags instead of CSS `@import`, which removes a request chain. Font loading uses `display=swap`.
- Header text appears when the DOM is ready (not after every image has loaded) and fades in faster; motion respects "reduce motion".
- The featured story title is an `<h3>` (one `<h1>` per page), styled to look the same.
- Footer: tappable phone numbers, accessible names on social icons.
- Added `404.html`, `README.md`, `docs/RUNBOOK.md`, `.editorconfig`, `.gitattributes`, `scripts/check_site.py` and a CI workflow.
- Line endings normalized to LF, so the first commit shows large diffs for some files.
