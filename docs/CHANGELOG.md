# Changelog

## Step 1: rebrand (complete)

- New design on every page: `assets/css/site.css` (colour and font tokens at the top), fonts Manrope + Inter (self-hosted; add the two files per `assets/fonts/README.md`, until then system fonts are used). No jQuery, no Font Awesome, no Stellar template code.
- All pages converted: home, About, Services, Projects, Stories (index + 3 articles), Reviews, Contact, 404. Content, JSON-LD, analytics, the Google Form, and the Firestore review flow are unchanged.
- Project and story lists are real HTML cards (visible to search engines and without JavaScript); `assets/js/filter-cards.js` only provides search and filters.
- The home page no longer embeds the hotlinked Okinawa drone video.
- Responsive card and hero images generated from the original photos.
- Navigation and footer are identical on every page and the checker enforces this; it also enforces that every story is listed in the story index and the sitemap.
- Removed: `main.css`, `noscript.css`, `review.css`, jQuery and plugins, Font Awesome and its fonts, `includes/footer.html`, `util.js`, `breakpoints`, `browser`, `main.js`.
- `sitemap.xml` now includes the reviews page.

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
