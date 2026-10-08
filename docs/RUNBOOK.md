# NBCS website runbook

Written for whoever looks after nbcs-envi.com next. No programming knowledge is needed for sections 1 and 2.

## 1. Who owns what

Fill this in and keep it current. **The company, not an individual's personal login, should own every account.**
Store passwords in the company password manager, never in this repository.

| Service | What it does | Account / owner email | Recovery contact |
|---|---|---|---|
| Domain registrar (nbcs-envi.com) | Owns the web address | ________ | ________ |
| GitHub (organisation `nbcs-main`) | Holds the website files; publishing happens here | ________ | ________ |
| Cloudflare | Sits in front of the site (speed, security, DNS) | ________ | ________ |
| Firebase project `nbcs-review-page` | Stores customer reviews | ________ | ________ |
| Google Analytics 4 (`G-0HM8RZLQFF`) | Visitor statistics | ________ | ________ |
| Google Form (service inquiries) | Receives inquiries; responses go to the form owner's Google account | ________ | ________ |
| Facebook / LinkedIn pages | Linked from the site | ________ | ________ |

If you can only do one thing before the current developer leaves: make sure at least two trusted people are **owners** of each row above.

## 2. Everyday tasks

### Approve or hide a customer review
1. Open the Firebase console, project `nbcs-review-page`, then Firestore Database, then collection `reviews`.
2. New reviews have `status: pending`. Change it to `approved` to publish. Any other value keeps it hidden.
3. Refresh the Reviews page to confirm.

### Read service inquiries
Open the Google Form's Responses tab (see the table above for who owns it).

### Change phone numbers, email or address
These appear in the footer of **every** page, and in the structured data (`"telephone"`, `"email"`, `"address"`) of `index.html`. Use find-and-replace across all `.html` files, then run the checks.

### Change the menu
The header is copied into every page. Change it everywhere with find-and-replace; the check tells you if one page was missed.

## 3. Publishing a change (technical)

1. Create a branch, make the change, run `python scripts/check_site.py` until it reports 0 errors.
2. Open a pull request. The "Site checks" workflow must pass.
3. Merge to `main`. GitHub Pages publishes within a few minutes. If the old version still shows, purge the Cloudflare cache.
4. If something breaks: on GitHub, open the merged pull request and press **Revert**, then merge the revert.

### Add a story
1. Copy an existing article in `stories/` (for example `groundwater-supply.html`) to a new file name.
2. In the new file change: `<title>`, meta description, canonical URL, the `og:` tags, the JSON-LD block, the heading and intro in the dark banner, and the article text. Replace the images.
3. Save its photos in `images/`: one wide photo for the article (longest side 1600 px or less) and one 800 px wide card version named `<name>-800.jpg`. Each file must be under 1 MB.
4. In `stories/all-stories.html` copy one `<article class="story-card">` block and edit it. `data-category` must match a filter button (`Environmental Compliance` or `Water Resources`, or add a new button), and `data-search` is the title, category and summary in lowercase.
5. In `index.html`, update the "Stay informed" cards if it should appear on the home page (keep three).
6. Add the page to `sitemap.xml`.
7. Run the checks and publish as above. The check fails if the story is missing from the story list or the sitemap.

### Add or edit a project
In `projects.html` copy one `<article class="project-card">` block and edit it. `data-category` must match a filter button. Use a card-size photo (800 px wide). Leave the link out if the project has no detail page.

### Change colours or fonts
Edit the variables at the top of `assets/css/site.css`. Font files: see `assets/fonts/README.md`.

## 4. Things to know

- Pushing to `main` changes the live site. Prefer pull requests.
- Never put passwords or private keys in the repository. The Firebase "apiKey" in `review.html` is a public identifier by design; protection comes from the Firestore rules.
- Large photos slow the site down. The checks refuse images over 1 MB.
- The home page, stories and projects pages contain real text in the HTML (not filled in by scripts), so Google and visitors with JavaScript blocked can read them.
- Original, full-size photos are not kept in the repository. Keep the originals somewhere else (shared drive).

## 5. Printing this document
Print `docs/RUNBOOK.pdf` if it exists, or open this file on GitHub and use the browser's print function. Keep a printed copy with the company's important papers.
