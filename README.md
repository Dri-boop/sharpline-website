# Sharpline Renovation & Woodworks — website

Website for **Sharpline Renovation & Woodworks**, carpentry and renovation by Charles Zeka.
Workshop: Unit 4, 7th Avenue Business Park, Maitland, Cape Town · +27 67 617 7735

A plain static site (HTML, CSS, a little JavaScript). No build step is needed to publish it; the
`site/` folder is the website.

## Folders

| Folder | What's in it |
|---|---|
| `site/` | **The website.** Everything in here is published. |
| `site/index.html` | Home page |
| `site/areas/` | One page per Cape Town suburb (generated, see below) and the "Areas we serve" page |
| `site/img/` | Optimised photos and video clips used on the site |
| `site/styles.css` | All styling |
| `site/main.js` | Home page script (WhatsApp links, gallery, quote form) |
| `site/area.js` | Script for the suburb pages |
| `tools/` | Small Python scripts that update the site (suburb pages, domain) |
| `.github/workflows/pages.yml` | Publishes `site/` to GitHub Pages on every push |
| `docs/` | Planning documents (strategy, competitor review, questions). **Not published**, kept local. |
| `raw/` | Original photos and videos. **Not published**, kept local. |

## Preview locally

```bash
python -m http.server 5510 -d site
```

Then open http://localhost:5510

## Common changes

**Phone / WhatsApp number** — `site/main.js` (`CONFIG.whatsapp`), `site/area.js` (`WHATSAPP`),
`tools/build_areas.py` (`PHONE`, `TEL`) and the `tel:` links in `site/index.html`.

**Suburb pages** — edit `tools/areas_data.py`, then run:

```bash
python tools/build_areas.py
```

When Charles confirms a real project in a suburb, add `real_photos=["kitchen-07", ...]` to that suburb's
entry and rebuild: the page then shows "Our work in <suburb>" with the suburb in each caption.

**Domain** — once the domain is bought:

```bash
python tools/set_domain.py yourdomain.co.za
```

This updates every page and writes `site/CNAME`. Commit and push.

## Publishing (GitHub Pages)

1. Push to the `main` branch. The workflow in `.github/workflows/pages.yml` deploys `site/`.
2. First time only: in the repository, **Settings → Pages → Build and deployment → Source: GitHub Actions**.
3. Custom domain: run `tools/set_domain.py`, push, then at your domain registrar add DNS records:
   - `A` records for the bare domain → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - `CNAME` record for `www` → `<your-github-username>.github.io`
   Then in **Settings → Pages**, enter the domain and tick **Enforce HTTPS**.

## Quote form

On GitHub Pages the quote form opens WhatsApp to Charles with the client's details filled in.
(The form also has Netlify Forms attributes, so if the site is ever moved to Netlify it saves and emails
submissions automatically.)
