# NBCS website (nbcs-envi.com)

Static site for N. Aguirre Business Consultancy Services. Plain HTML, CSS and a little JavaScript, no build step.
Hosted on GitHub Pages (see `CNAME`); pushing to `main` deploys to production.

> Not a developer? Read `docs/RUNBOOK.md` instead.

## Layout

| Path | What it is |
|---|---|
| `index.html`, `about.html`, `services.html`, `projects.html`, `review.html`, `contact-form.html` | Main pages |
| `stories/` | Blog-style articles; `stories/all-stories.html` lists them |
| `games/` | Two standalone mini-games (own styling, not part of the main design) |
| `includes/footer.html` | Footer, loaded into every page by JavaScript |
| `assets/css/site.css` | The new stylesheet (design tokens at the top). Pages migrate to it one by one |
| `assets/css/main.css` | Legacy template stylesheet, still used by pages not yet migrated. **Edit directly**; the old Sass sources were removed because they had drifted out of date |
| `assets/fonts/` | Self-hosted WOFF2 fonts (see `assets/fonts/README.md`) |
| `assets/js/` | jQuery plus small plugins and `main.js` (nav highlighting, smooth scroll) |
| `images/` | Photos, logo, partner logos |
| `scripts/check_site.py` | Automated checks (run locally and in CI) |

## Working on it

```bash
python3 -m http.server 8000      # preview at http://localhost:8000
pip install beautifulsoup4
python3 scripts/check_site.py    # must pass before merging
```

Work on a branch and open a pull request instead of pushing straight to `main`. CI runs the same check.

## Conventions

- Tabs for indentation, LF line endings (`.editorconfig`, `.gitattributes`).
- Images: longest side 1800 px or less, under 1 MB each (the check enforces the 1 MB limit). Always write `alt` text; use `alt=""` only for purely decorative images.
- One `<h1>` per page; every page needs `lang`, a `<title>`, a meta description and a canonical link.
- Do not add new jQuery code. Prefer plain JavaScript and CSS.

## Where dynamic data lives

- **Reviews**: Firebase Firestore (project `nbcs-review-page`), collection `reviews`. The page only shows documents with `status == "approved"`; new submissions are saved as `pending`. The Firestore security rules are **not** in this repository; export them from the Firebase console and store them here.
- **Service inquiries**: an embedded Google Form (`contact-form.html`).
- **Analytics**: Google Analytics 4 (`G-0HM8RZLQFF`).
- **Story list, project list, partner logos**: hand-edited arrays/markup in `index.html`, `stories/all-stories.html`, `projects.html`, `about.html`.

## Known issues / pending decisions

- The design is based on the HTML5 UP "Stellar" template (CC BY 3.0, credit required). The footer currently carries no credit; either restore it or finish replacing the template before relying on that.
- `main.css` still has the template's grid system and many unused rules.
- The home page video is hotlinked from Wikimedia Commons (a drone flyover of Okinawa).
- The footer, the featured story and the project list are rendered by JavaScript.
