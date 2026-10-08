# NBCS website (nbcs-envi.com)

Static site for N. Aguirre Business Consultancy Services: plain HTML, one stylesheet, a little vanilla JavaScript. No framework, no build step, no jQuery.
Hosted on GitHub Pages (see `CNAME`); a push to `main` deploys to production.

> Not a developer? Read `docs/RUNBOOK.md` instead.

## Layout

| Path | What it is |
|---|---|
| `index.html`, `about.html`, `services.html`, `projects.html`, `review.html`, `contact-form.html` | Main pages |
| `stories/` | Articles; `stories/all-stories.html` lists them with search and filters |
| `games/` | Two standalone mini-games (self-contained, not part of the site design) |
| `404.html`, `blogs.html` | Not-found page; old URL that redirects to the stories page |
| `assets/css/site.css` | The only stylesheet. Colours and fonts are variables at the top |
| `assets/js/site.js` | Mobile menu, footer year |
| `assets/js/filter-cards.js` | Search and category filters for projects and stories |
| `assets/fonts/` | Self-hosted WOFF2 fonts (see `assets/fonts/README.md`) |
| `images/` | Photos. `*-800.jpg` are card sizes, other sizes are for article/hero use |
| `scripts/check_site.py` | Automated checks (run locally and in CI) |
| `docs/` | Runbook for non-developers, changelog |

## Working on it

```bash
python -m http.server 8000      # preview at http://localhost:8000  (use `py` or `python3` if needed)
pip install beautifulsoup4
python scripts/check_site.py    # must pass before merging
```

Work on a branch and open a pull request; CI runs the same check. Never push straight to `main` for non-trivial changes.

## How the pages are built

Every page is hand-written static HTML. The **header and footer are copied into every page**; the check fails if any page's copy differs from `index.html`, so you cannot forget one. To change navigation or contact details, use find-and-replace across all `.html` files, then run the check.

The project and story cards are plain HTML (so search engines and visitors without JavaScript see them). `filter-cards.js` only hides/shows them; the markup contract is documented at the top of that file.

## Conventions

- Tabs for indentation, LF line endings (`.editorconfig`, `.gitattributes`).
- Images: under 1 MB each (enforced). Always give `alt` text (`alt=""` only for decorative images) and `width`/`height`.
- One `<h1>` per page. Every page needs `lang`, a title, a meta description and a canonical link.
- Use CSS variables from `site.css` instead of hard-coded colours.

## Where dynamic data lives

- **Reviews**: Firebase Firestore (project `nbcs-review-page`), collection `reviews`. The page shows only documents with `status == "approved"`; new submissions are saved as `pending`. The Firestore security rules are **not** in this repository; export them from the Firebase console and commit them here.
- **Service inquiries**: an embedded Google Form (`contact-form.html`).
- **Analytics**: Google Analytics 4 (`G-0HM8RZLQFF`), loaded in each page's `<head>`.

## Ideas for the next developer (not done on purpose)

- A small static-site generator (for example Eleventy) so the header, footer, and cards come from one source instead of being copied.
- A git-based editor (Decap CMS or similar) so staff can publish stories without touching code.
- Real view counts for stories (a Cloudflare Worker with KV or D1; filter bots).
- Responsive images (`srcset`/WebP) for the article photos, which are served at up to 1800 px.
- Restrict the Firebase API key to the production domain, add App Check, and review the Firestore rules.
- The Facebook link differs between the footer and the JSON-LD `sameAs` list; confirm which is correct.
