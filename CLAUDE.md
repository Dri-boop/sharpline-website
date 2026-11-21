# Sharpline Renovation & Woodworks — instructions for Claude

**Read `HANDOFF.md` before touching anything.** It holds the decisions, the
setup and the traps from the project's history, and replaces session memory.
Update it when a decision changes.

## Two work streams, two sessions

| Stream | Folder(s) | Claude session |
|---|---|---|
| **Website** — pages, design, photos, suburb pages, domain | `site/`, `tools/`, `brand/` | "Sharpline website" |
| **SEO** — Google Search Console, Analytics, fortnightly reports and SEO pull requests | `seo/`, `.github/workflows/seo-*.yml`, `.claude/skills/seo-update/` | "Sharpline SEO" |

Both sessions share this folder. Stay in your own folders. The only shared
files are `site/index.html` (analytics tag in the head), `tools/build_areas.py`
(page templates) and `site/styles.css`: before editing them, check
`git status` for the other session's uncommitted work and message that session
first. Commit only your own changes.

## Hard rules

- Repo-local git identity only: `Dri-boop` / `Dri-boop@users.noreply.github.com`.
  Never the machine's global identity, never a personal email.
- The GitHub repo `Dri-boop/sharpline-website` is **public**. Never commit
  `raw/` (original photos), `docs/` (internal plans), SEO report data, keys,
  tokens or anything personal about clients.
- Never invent projects, reviews, prices or locations. A photo gets a suburb
  name only when Charles has confirmed where the job was (`KNOWN` captions in
  `site/index.html`, `real_photos` in `tools/areas_data.py`).
- Check every photo against its caption before publishing (contact sheet).
- No prices on the site: pricing is the process plus the fixed-price promise.
- Copy: short, plain, not wordy, nothing that reads as AI-written.
- Google/Meta keys go into GitHub Actions secrets by the owner, never into chat
  or files.
- Publishing = push to `main` (GitHub Pages deploys `site/`). Verify the live
  file afterwards, e.g. `curl` and compare, not just the status code.
- Show the owner changes on localhost (preview "sharpline", port 5510) when
  asked; the browser caches `main.js` and images, force a reload.
