# Recent purchase notifications

A small card at the bottom-left reads "**Sarah** from Ontario purchased **12 Months** · 2 hours ago". It shows **only real orders you add yourself**. With no entries, nothing appears.

## One-time setup
Cloudflare Pages, Settings, Variables and Secrets: add `ADMIN_KEY` (any long random string; it already protects `/api/leads`). The `LEADS` KV binding is already configured.

## Add an order (after you confirm payment)
```
curl -X POST "https://iptvmapletv.com/api/orders-admin?key=YOUR_KEY" \
  -H "content-type: application/json" \
  -d '{"first":"Sarah","place":"Ontario","plan":"12 Months"}'
```
`at` is optional (ISO time; defaults to now). Use the customer's first name and region only, and only with their OK.

List: `GET /api/orders-admin?key=YOUR_KEY`. Remove: `DELETE /api/orders-admin?key=YOUR_KEY&id=ID`.

## Behaviour
Appears 7 s after load, stays 6 s, repeats every ~20 s (max 6 per visit), can be closed (stays closed for the session), ignores entries older than 30 days, and is hidden on thank-you and landing pages.
