---
name: seo-weekly
description: Weekly reach review for the Sharpline website. Reads the newest weekly Search Console + GA4 report in the private sharpline-seo-reports repository and adds practical, evidence-based recommendations to improve reach (website, Google Business Profile, reviews, photos) as a comment on that week's "Weekly reach report" issue. Changes nothing. Used by the "Sharpline weekly reach review" cloud routine; can also be run by hand.
---

# Sharpline weekly reach review

Business: **Sharpline Renovation & Woodworks**, carpentry and renovation, workshop in Maitland, Cape Town (owner Charles Zeka). Works anywhere in South Africa. Website: https://sharplinerenovation.co.za. Enquiries come by WhatsApp, phone and the quote form (tracked as `whatsapp_click`, `phone_click`, `quote_form_submit`).

## Where the data is

- Private repository `Dri-boop/sharpline-seo-reports` (in the cloud routine it is checked out next to the website; on the owner's PC it is the folder `seo/`).
- `reports/LATEST` = date of the newest report. In `reports/<date>/`:
  - `summary.md`: this week vs last week, plus automatic recommendations (already posted as the issue body).
  - `report.md`: last 28 days vs the 28 days before, and the "SEO opportunities" lists.
  - `data.json`: every number (`meta`, `analysis`, `data`, `data.weekly`).
- Also read the previous 2–3 report folders to spot trends.
- The website itself is the `Dri-boop/sharpline-website` checkout (read `CLAUDE.md` and `HANDOFF.md` there for the house rules).

## What to do

1. If `meta.sample` is true, or the newest report is more than 8 days old, stop and say why. Do nothing else.
2. Analyse reach: Google impressions, clicks, positions, which pages and searches bring visits, which pages and sources bring enquiry clicks, and changes vs last week and vs the previous reports.
3. Write **at most 5 recommendations**, most useful first. For each:
   - what to do, in one or two short sentences;
   - why: the number from the report that supports it (e.g. "Pinelands page: 120 impressions, position 11");
   - who does it: **Charles** (photos, reviews, Business Profile posts, telling us which suburbs he really works in), **the owner** (Google settings), or **automatic** (the fortnightly SEO pull request will handle it).
   Good topics: pages close to the top 3, searches on page 2, suburbs people search for, pages with visits but no enquiries, Google Business Profile, asking clients for Google reviews, adding real job photos. Do not repeat the automatic recommendations already in the issue body unless you add something new.
4. Post the text as a **comment on the issue titled `Weekly reach report - <date>`** in `Dri-boop/sharpline-seo-reports` (use the GitHub tools available to you). If you cannot comment, put the full text in your final message instead.

## Rules

- Plain, short English: the owner's first language is not English. No jargon (say "shown in Google" rather than "impressions" the first time).
- Every recommendation must rest on a number in the reports. If there is too little data (fewer than 100 impressions in 28 days), say so, give at most 3 general starter actions, and stop.
- Never invent reviews, projects, prices, suburbs Charles has worked in, or results. Never promise rankings.
- Change nothing: no commits, no branches, no pull requests, no edits to either repository. Website changes are the fortnightly `seo-update` routine's job.
