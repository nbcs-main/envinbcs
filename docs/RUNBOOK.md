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
Edit `includes/footer.html`. Also check the contact details in `index.html` (the structured data near the top) and `about.html`.

## 3. Publishing a change (technical)

1. Create a branch, make the change, run `python3 scripts/check_site.py` until it reports 0 errors.
2. Open a pull request. The "Site checks" workflow must pass.
3. Merge to `main`. GitHub Pages publishes within a few minutes. If the old version still shows, purge the Cloudflare cache.
4. If something breaks: on GitHub, open the merged pull request and press **Revert**, then merge the revert.

### Add a story (current manual method)
1. Copy an existing file in `stories/` and edit the text, `<title>`, meta description and canonical link.
2. Put its image in `images/` (longest side 1800 px or less, under 1 MB).
3. Add it to the `stories` list in `stories/all-stories.html`, the `blogPosts` list in `index.html`, and `sitemap.xml`.
4. Run the checks and publish as above.

### Add or edit a project
Edit the `projects` list in `projects.html`. Leave `url: ""` if the project has no detail page (the card then is not a link).

## 4. Things to know

- Pushing to `main` changes the live site. Prefer pull requests.
- Never put passwords or private keys in the repository. The Firebase "apiKey" in `review.html` is a public identifier by design; protection comes from the Firestore rules.
- Large photos slow the site down. The checks refuse images over 1 MB.
- Original, full-size photos are not kept in the repository. Keep the originals somewhere else (shared drive).

## 5. Printing this document
Print `docs/RUNBOOK.pdf` if it exists, or open this file on GitHub and use the browser's print function. Keep a printed copy with the company's important papers.
