# Sharpline Renovation & Woodworks — handoff notes

Everything a fresh session needs. `README.md` covers day-to-day operation;
this file covers context, decisions and traps.

Last updated: 2026-11-21.

## 1. The business

- **Sharpline Renovation & Woodworks** (the old name "Sharpline Woodworks" is
  only the second domain and the Gmail address).
- Owner **Charles Zeka**: 15+ years, trained and ran a workshop in Malawi,
  team of 4 permanent + contractors. Selling point: trustworthy, fixed price,
  does the right job until the client is happy.
- Workshop: Unit 4, 7th Avenue Business Park, Maitland, Cape Town 7405
  (postcode assumed, not confirmed).
- Phone and WhatsApp: **+27 67 617 7735** (one number, one line on the site).
- Email shown on the site: **sharplinewoodworks1@gmail.com** (no domain mailbox yet).
- Works anywhere in South Africa; suburb pages are examples of recent work areas.

## 2. Live setup

- Live: https://sharplinerenovation.co.za (GitHub Pages, HTTPS enforced,
  certificate auto-renews). `www` redirects to the bare domain.
- `sharplinewoodworks.co.za` 301-redirects to the main domain (HOSTAFRICA
  "Domain Redirects").
- DNS at HOSTAFRICA (client area → Domains → DNS Management → Domains DNS):
  4 A records `@` → 185.199.108–111.153, CNAME `www` → `dri-boop.github.io.`.
  Leave the mail/ftp/NS/spf records alone.
- Repo: `Dri-boop/sharpline-website` (public), same GitHub account as GridPulse.
  `.github/workflows/pages.yml` deploys `site/` on every push to `main`.
- GitHub auth on this PC: Git Credential Manager (token has repo + workflow).
  GitHub CLI is not installed; the REST API with the GCM token works.
- Domain change: `python tools/set_domain.py <domain>` (also needs the Pages
  custom domain set through the API or repo settings).
- This PC prints `nslookup` output in French ("Nom", "Adresses").

## 3. Website structure (website session)

- `site/index.html` home page; `site/main.js` home script (WhatsApp links,
  gallery filters/lightbox, quote form → WhatsApp, areas toggle);
  `site/area.js` suburb-page script; `site/styles.css` all styles.
- `tools/build_areas.py` generates `site/areas/<slug>/`, the areas hub, the
  home "Recent work areas" box (half shown, "Show all" toggle) and
  `sitemap.xml` from `tools/areas_data.py`. Far areas (`far=True`, region
  "Beyond Cape Town") show no drive time.
- `brand/` logo PNGs (Gmail profile, signature, white). `google-business-photos/`
  (gitignored) is the drag-and-drop set for the Business Profile.
- Design: brutalist concrete × timber; fonts Unbounded (headlines, labels) and
  Manrope (body); colours ink #1b1a18, timber #b47a43, crayon #e0531c,
  sawdust #ece2cc; saw-tooth motif. Headline alternates "wood" (brown) /
  "renovation" (grey).

## 4. Photos

- Originals in `raw/` (gitignored): WhatsApp zips, `new pic/`, `newpic2/`,
  `shots/` = Charles's WhatsApp screenshots that label each job's location.
- Site copies: `site/img/<category>-NN.jpg` (1400px) + `-sm.jpg` (640px).
  Categories: kitchen, wardrobe, doors, furniture, tv, floor, outdoor, reno, site.
- Caption format: `<figcaption class="mono">Caption <span>· Suburb</span></figcaption>`;
  no span when the location isn't confirmed.
- **Trap:** contact-sheet numbering once mislabelled 8 photos. Always render
  an audit sheet (image + filename + caption) before publishing.
- Gallery shows 16 hand-picked lead photos first (hot-tub surround is 3rd).

## 5. Decisions

- No prices; "How pricing works" + "Our price is our price. Fixed once you say yes."
- Quotes 24/7; payment split 50/40/10 and 12-month guarantee are still
  placeholders until Charles confirms.
- Quote form opens WhatsApp with the details (no email backend on GitHub Pages).
- Facebook/Instagram links removed; footer shows WhatsApp only.

## 6. SEO stream (SEO session)

- `seo/` = local clone of the **private** repo `Dri-boop/sharpline-seo-reports`
  (ignored by the website's git; report data never goes into the public repo,
  whose files, Actions logs and artifacts anyone can read).
  - `seo/scripts/pull_reports.py`: Search Console + GA4 Data API, last 28 days vs
    previous 28, plus last 7 days vs previous 7 and plain-English recommendations;
    writes `reports/<date>/report.md`, `summary.md`, `data.json`, `reports/LATEST`.
    Test offline: `python seo/scripts/pull_reports.py --sample --out seo/sample`.
  - `seo/.github/workflows/seo-pull-reports.yml`: every Monday 04:00 UTC; commits
    the report and opens issue "Weekly reach report - <date>" (GitHub emails it). Needs secret `GOOGLE_SERVICE_ACCOUNT_JSON` and
    variable `GA4_PROPERTY_ID` (property number, not the G- ID) there.
- `.claude/skills/seo-update/SKILL.md` (website repo): instructions for the
  Claude routine **"Sharpline fortnightly SEO review"**
  (`trig_019Xo8eBPhYvBhbUwXzCg2Vf`, 2nd + 16th, 06:00 UTC). It opens one PR on a
  `claude/seo-<date>` branch, never pushes to main.
- `.claude/skills/seo-weekly/SKILL.md`: routine **"Sharpline weekly reach review"**
  (`trig_01ND7eRyteMeL6BRGMZojAck`, Monday 07:00 UTC) comments up to 5
  recommendations on the weekly issue; changes nothing.
- Both routines are **paused** until the owner
  adds the Claude GitHub App to `sharpline-seo-reports`; then add that repo as a
  routine source and enable it.
- Analytics: `site/analytics.js` (GA4, Consent Mode, cookie notice; `GA_ID` = `G-QT5TJW291V`, live since
  2026-11-21; the owner's GTM container GTM-NVCR8Z3L points to the same ID but is NOT
  loaded, to avoid double counting); events `whatsapp_click`, `phone_click`,
  `quote_form_submit`. Privacy page generated by `privacy_page()` in
  `tools/build_areas.py`. Per-suburb `title`/`description` overrides in
  `areas_data.py`.
- Search Console: Domain property `sc-domain:sharplinerenovation.co.za`, TXT at
  HOSTAFRICA next to the existing spf TXT.
- Owner's step-by-step guide: `docs/GOOGLE-SETUP.md`.

## 7. Open items

- Confirm postcode, payment split, guarantee, languages.
- Google Business Profile: verification pending (video likely).
- More suburb confirmations from Charles → add `real_photos` and rebuild.

## 8. Website status (2026-11-21, end of the first build session)

- Confirmed by the owner: payment split 50/40/10, 12-month workmanship
  guarantee, site-work hours Mon–Fri 07:30–17:00 / Sat 08:00–13:00,
  postcode 7405. Do not mention languages.
- Google Business Profile: https://maps.app.goo.gl/niwRVW97kVKSbcyAA (contact
  line, workshop "Get directions", JSON-LD `sameAs`/`hasMap` on all pages).
- "References from past clients available on request" is on the site
  (Who we are, contact section).
- Copy was tightened site-wide on request; keep new copy short.
- No Facebook page yet (later).
- Waiting on files from the owner (to be saved in `raw/new3/`):
  1. Charles selfie with glove + timber frame → founder card photo.
  2. Team photos (two men in a roof, Charles with glove, measuring) →
     team carousel in "Who we are" (same style as the jobs viewer).
  3. Floor framing over insulation, office partition wall, white/pine tables
     and benches, Durban 2021 pool project tray.
  4. Charles's Google Drive videos (`VID_2025…`) from the email.
- Photos pasted into chat while Claude is mid-turn are NOT saved to disk;
  ask the owner to save files into `raw/` instead.
