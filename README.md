# iptvmapletv.com

Static version of the former WordPress site, hosted on **Cloudflare Pages**.
Every push to `main` deploys to production automatically (GitHub Actions → `wrangler pages deploy`).
Pull requests and other branches get their own preview URL.

## Layout

| Path | What it is |
| --- | --- |
| `public/` | The website. Each page is `public/<slug>/index.html`; the homepage is `public/index.html`. |
| `public/wp-content/`, `public/wp-includes/` | Images, CSS, JS and fonts copied from WordPress (paths kept so nothing breaks). |
| `public/_redirects` | 301 redirects for old URLs. Add a line `/old-path/ /new-path/ 301` to add one. |
| `public/_headers` | Response headers (caching). |
| `public/sitemap_index.xml`, `public/page-sitemap.xml` | Sitemaps. Add a `<url>` entry when you add a page. |
| `functions/api/ajax.js` | Replaces WordPress's form backend (order, free-trial and referral forms). |
| `functions/api/leads.js` | Lists saved form submissions. |
| `tools/` | One-time scripts used to import the site from WordPress. |

## Editing

Edit the HTML in `public/` and push to `main`. Page-level styles live in
`public/wp-content/uploads/elementor/css/post-<id>.css` (the homepage is `post-8.css`,
the header `post-751.css`, the footer `post-709.css`). When you change a CSS/JS file,
bump its `?ver=` in the HTML so browsers fetch the new copy.

The header and footer are repeated in every page, so a menu change must be made in each
`index.html` (search-and-replace across `public/**/index.html`).

## Form submissions

Orders, free-trial requests and referrals are handled by `functions/api/ajax.js`:

- saved to the Cloudflare KV namespace `iptvmapletv-com-leads` (binding `LEADS`);
- viewable at `https://iptvmapletv.com/api/leads?key=<ADMIN_KEY>` (the key is a secret
  environment variable on the Pages project);
- optionally pushed to Telegram — set `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` on the
  Pages project (Settings → Variables and Secrets) — and/or to any webhook via `NOTIFY_WEBHOOK_URL`.

## Local preview

```bash
npm install
npx wrangler pages dev
```

## Deployment secrets (GitHub → Settings → Secrets and variables → Actions)

- `CLOUDFLARE_API_TOKEN` — token with *Cloudflare Pages: Edit* permission
- `CLOUDFLARE_ACCOUNT_ID`
