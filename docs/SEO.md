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
- Channels list: all regions stay listed (viewers in Canada/US watch them); no page or copy targets those markets.
- Added HSTS; softened three unverifiable claims ("thousands of customers", "Join thousands", "Verified reviews").
- Every city is now linked from the `/canada/` and `/usa/` hubs; 3 single-city pages still have 2 inbound links.
- Open: the "50,000+ channels" claim vs the 10k listed names; legality statement; templated city pages; legacy testimonials.

## Expansion pass (2026-10-04)
Ran the SEO STRUCTURE 2.0 process on the new **worldwide** keyword file (822 keywords) and re-ran the Canada file. Maps: `docs/keyword-map-worldwide.xlsx`, `docs/keyword-map.xlsx`.
- Baseline audit: 0 critical, 0 important, 3 minor (under-linked city pages). After: the same, with 13 more indexable pages (374 in the sitemap).
- New pages (`sitegen/seo_content/expansion.py`): `/ss-iptv/`, `/set-iptv/`, `/duplecast/`, `/nanomid/`, `/lazy-iptv/`, `/iptv-smart-tv/` (English pillar for every TV brand; "iptv smart tv" previously landed on a French page), `/pluto-tv-vs-iptv/`, `/iptv-vs-satellite/`, `/iptv-starlink/`, `/iptv-account/`, `/iptv-recording-catch-up/`, `/hbo-iptv/`, `/german-iptv/`.
- Third-party app facts (trial lengths, activation, supported TVs) were checked on the developers' own sites on 2026-10-04; app prices are deliberately not quoted.
- `expansion.LINK_IN` adds each new page to the "Related guides" of 1–2 relevant existing pages so none is orphaned.
- Not built: OTT Navigator (store listings conflict, facts not verifiable); separate Hisense/Philips/Panasonic/Sony pages (covered in the smart TV pillar); box model numbers (MAG, Dreamlink, TVIP, Formuler variants: existing device pages); "iptv wifi" / "isp iptv" (added to buffering and what-is-IPTV pages); 327 other-provider brand names; 19 excluded-market keywords.

## Expansion pass 2 (2026-10-04, SEO master prompt v3)
Re-ran both keyword files under the v3 rules. v3 changes vs 2.0: device, app and tool names are protected classes (never filed as "other brands"), and the Caucasus is no longer an excluded market.
- Maps: worldwide 495 mapped (was 476) / 16 excluded / 311 other-provider names; Canada 687 mapped (was 672) / 20 / 372.
- New pages (`sitegen/seo_content/expansion2.py`): `/gse-smart-iptv/`, `/iptvx/`, `/ott-navigator/`, `/purple-iptv/` (apps), `/onn-tv-box-iptv/` (device, "onn tv box" 50k/mo), `/iptv-vs-netflix/`, `/iptv-checker/` (a working M3U playlist checker; parsing runs in the browser in `site.js`, nothing is uploaded).
- Extended (`deep_gap6.py`): `/iptv-box/` box-model table (TVIP, Ugoos AM7, Homatics Box Q, Dreamlink, Xsarius, Amiko), `/ex-yu-iptv/` Balkan terms ("iptv ponuda", "iptv televizija", "iptv kanali"), `/iptv-iphone/`, `/iptv-apps/`. `deep.py` now accepts `keywords_add` and a per-entry `updated` date.
- Keyword ownership moved: "gseiptv"/"iptvx" from `/iptv-iphone/`, "iptv checker"/"m3u checker" from `/watch-iptv-online/`.
- Spelling-variant 301s for the new pages in `_redirects`.
- Third-party facts checked on 2026-10-04 on App Store / Google Play listings, the developers' sites and established reviews (onn 4K Pro specs). App prices deliberately not quoted.
- Not built, and why:
  - Pages for other IPTV providers' names (311 worldwide / 372 Canada keywords, e.g. "forevertv", "xtreme hd iptv"). v3 suggests conquest pages, but these are navigational searches for unlicensed services we can't describe truthfully; one page per name would be thin, doorway-like and a trademark risk.
  - Georgian IPTV ("iptv ge", "rustavi2", "imedi", ~25k/mo): now allowed under v3, but the channel list has only 5 Georgian channels, so a page would be thin and the searches are mostly for the iptv.ge site.
  - Albanian ("iptv iliria"): no Albanian channels in the list.
  - SoPlayer: the app is tied to a provider selling its own channel packages; facts not independently verifiable.
  - Excluded markets (16 / 20 keywords): Arabic, Asian, African.

## Gap pass 7 (2026-10-05)
Re-checked both keyword files (unchanged since expansion pass 2) against every page. Few real gaps were left; most of the remaining "not covered" list is word-order variants, misspellings ("smasters", "mu3") and other providers' names.
- New pages (`sitegen/seo_content/expansion3.py`): `/myiptv-player/` (Windows player; "my iptv", "my ip tv"), `/iptv-5g-mobile-data/` (5G home internet and phone data; "5g iptv", "iptv sim"). Spelling-variant 301s in `_redirects`.
- Extended (`deep_gap7.py`): MAG model table (520, 524, 424, 425A, 540w3/544w3, 555, 322w1), Formuler Z+ Neo and ZX, Smart STB on the STBEmu page, buying boxes on AliExpress/eBay and "fully loaded" boxes, ISP IPTV vs internet IPTV, IPTV over Wi-Fi, paid vs free IPTV, Xtream on PC, XCIPTV on Samsung, 4K OTT / 8K labels, spelling FAQs for SSIPTV, SET IP TV, GSEIPTV and IPTV X.
- Fixed: the MAG page called the MAG 424 "Android-based" (it is Linux; the Android model is the 425A) and the 524 the "current flagship" (Infomir lists it as discontinued).
- Maps: worldwide 513 mapped (was 495) / 16 excluded / 293 other-provider names; Canada 705 (was 687) / 20 / 354. Coverage: phrases absent from their page 73 → 52.
- Not built: CloudStream ("cloud stream", 500k/mo: a scraper app, not an IPTV player), "Smart IPTV" on Fire TV (not verified), MAG 420 and Amiko A6N (specs not verified), the remaining provider names.
