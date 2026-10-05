# Recent purchase notifications

A small card at the bottom-left reads "**Michael** from Canada purchased **12 Months**", with "Confirmed order · 2 hours ago" underneath. It shows **only real orders you add yourself**. With no entries, nothing appears.

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
One notification every 7 s, each visible for 2 s (first one 7 s after load). Each real entry is shown once per page view, newest first, so with 3 entries visitors see 3 notifications on that page. Hover or keyboard focus keeps a card on screen; it pauses while the tab is in the background; it can be closed (stays closed for the session); entries older than 30 days are ignored; hidden on thank-you and landing pages.

## Preview (owner only)
Open `/sales-demo/` (noindex, unlinked) to see the design with sample names, or switch preview on there to see it on every page of your own device. Sample cards are labelled "Sample, not real" and are never shown to visitors.
