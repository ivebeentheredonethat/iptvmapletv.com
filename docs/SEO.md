# SEO guide — iptvmapletv.com

## How the site is built
- `build.py` renders `src/` + `sitegen/` into `public/` (pure-stdlib Python 3.12). Cloudflare Pages deploys on every push to `main` (`.github/workflows/deploy.yml`).
- SEO pages are dicts in `sitegen/seo_content/*.py` (one per page). Keys: `slug, hub, lang, title, description, kicker, h1, lead, crumb, blurb, answer, body, faq, related, keywords, alternates, published, updated, noindex, og_image`.
- `seo_content/deep*.py` append sections/FAQs to existing pages without editing them.
- Every page gets automatically: canonical, hreflang (EN↔FR pairs in `PAIRS`), OG/Twitter tags, JSON-LD graph (Organization, WebSite, WebPage, BreadcrumbList, Article/Service, FAQPage from the visible FAQ), table of contents on long articles, contextual auto-links, image width/height.
- `sitemap.xml` (with `lastmod` and hreflang alternates), `robots.txt`, `llms.txt`, and `404.html` are generated.

## Adding a page
1. Add a dict to the right module (or a new one imported in `seo_content/__init__.py`).
2. Title 50–60 chars, description 150–160, 3+ FAQs, `related` links.
3. Add it to a hub (`hub`) so it is linked from the hub page and footer/ring links.
4. `python3.12 build.py && python3.12 tools/seo_audit.py` — must report 0 critical / 0 important.
5. Redirect aliases go in `src/static/_redirects`; the build fails if a redirect source is a real page.

## Keyword map
`python3.12 tools/keyword_map.py <Keyword_Canada.xlsx> docs/keyword-map.xlsx` — assigns each keyword to a page, or to an exclusion bucket (excluded markets per spec 0.0.2; other providers' brand names). Result: 651 keywords (519k searches/mo) mapped, 22 excluded-market, 406 other-brand. Review the "Working list" sheet; a few borderline assignments (e.g. English app queries sent to French pages) can be corrected in `MAP_RULES`.

## Deliberately not built
- Pages named after competitor IPTV brands (406 keywords): we can't truthfully write about them, and it risks trademark/misleading-content issues.
- Excluded markets (Arabic, Asian, African, Caucasus content).
- A reseller page.

## Open items for the owner
- **Legal page** (`/is-iptv-legal-in-canada/`, `/iptv-legal-canada/`): add your actual licensing statement; it currently stays general.
- Legacy testimonials and the adult-content claim on `/landing/`, `/landing3/` (now `noindex`) should be verified or removed.
- Location pages are templated; keep them unique and useful (doorway-page risk if spammed further).
- `channels-list` includes channels from excluded markets.
- Submit `https://iptvmapletv.com/sitemap.xml` in Google Search Console and Bing Webmaster Tools.
- Revoke the GitHub and Cloudflare tokens that were pasted in chat; use repo secrets instead.
- No one can guarantee #1 rankings. This work removes technical blockers and covers the topics; results depend on links, competition and time.

## Coverage check
`python3 tools/coverage.py docs/keyword-map.xlsx` lists mapped keywords whose exact phrase is missing from the assigned page (`ABSENT` = words missing, `tokens-only` = words present but not as a phrase). The gap pass cut the list from 540 to about 215, mostly word-order variants of the same query.
Gap-pass content lives in `sitegen/seo_content/deep_gap1-4.py`; the new pages `iptv-lifetime`, `iptv-resellers` and `iptv-for-beginners` are in `gaps.py`.

## Deep audit (`tools/seo_audit_deep.py`)
Second-level checks run after `tools/seo_audit.py`: heading outline, H1 keywords in the intro and body, density, dead links, authority links, CTAs and trust signals, JSON-LD vs visible content (prices, breadcrumbs, Article fields), near-duplicate content, and city-page overlap. Known false positives: H1 keyword in a different word order, the home page's hero images, and legal pages with no CTA by design.

Decisions from the audit:
- The 15 order pages (`/6-month-iptv-3-devices/` and siblings) were 90% identical, so they now carry a canonical to `/iptv-plans-canada/` and are out of the sitemap. Each still has its own price table and Product schema. If you want any of them to rank on its own, give it unique content and remove the canonical (`canonical=` in `product_pages()`).
- `/iptv-plans-canada/` now has a static all-plans table (the cards only showed 1 screen without JavaScript) and Product schema with one Offer per plan.
- Headings that skipped a level are fixed at render time (`fix_heading_levels`), keeping the same visual size.
- City pages in the same metro now carry a factual local paragraph (`geo_local.py`). Overlap among the worst pairs dropped, but these pages are still templated: check Search Console for "Crawled, not indexed" and consolidate if needed.

## Final audit (2026-10-02)
- Live crawl of all 361 sitemap URLs: all 200, no redirects, canonical matches, one H1 and valid JSON-LD on every page. Redirects verified (http, www, missing trailing slash).
- Channels list: only Americas, Europe and Australia are published (the other regions stay in `src/data/channels.json`). Page weight fell from 590 KB to 385 KB.
- Added HSTS; softened three unverifiable claims ("thousands of customers", "Join thousands", "Verified reviews").
- Every city is now linked from the `/canada/` and `/usa/` hubs; 3 single-city pages still have 2 inbound links.
- Open: the "50,000+ channels" claim vs the 10k listed names; legality statement; templated city pages; legacy testimonials.
