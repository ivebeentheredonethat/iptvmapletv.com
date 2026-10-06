# Recent purchase notifications

A small card at the bottom-left reads "**Sarah** from Ontario purchased **12 Months**", with "Confirmed order · Oct 4" underneath. It runs on **every page** and needs **no API, no key and no server**: the orders live in one file, `src/data/recent-orders.json`, which the build copies into each page.

It shows **only real orders you add yourself**. While the file is an empty list (`[]`), nothing appears.

## Add a real order
After you confirm payment (and the customer is OK with their first name being shown), add one line to `src/data/recent-orders.json`:

```json
[
  {"first": "Sarah", "place": "Ontario", "plan": "12 Months", "date": "2026-10-04"},
  {"first": "Luc", "place": "Quebec", "plan": "6 Months", "date": "2026-10-03"}
]
```

- `first`: customer's first name only. `place`: province, state or country. `plan`: as on the site (`1 Month`, `3 Months`, `6 Months`, `12 Months`).
- `date` (optional): the real order date, `YYYY-MM-DD` (shows "Oct 4") or a full time like `2026-10-04T15:30:00Z` (shows "3 hours ago"). Leave it out and the card just says "Confirmed order".
- Commit the change on GitHub (the pencil icon on the file works). The site rebuilds and the new entry is live on every page after the deploy. Newest first; up to 20 are used.
- To remove an entry, delete its line and commit.

## Behaviour
One notification every 7 s, each visible for 2 s (first one 7 s after the page loads), looping through the list. Hover or keyboard focus keeps a card on screen; it pauses while the tab is in the background; it can be closed (stays closed for the rest of the visit). No network request is made: the data is inside the page.

## Preview (owner only)
Open `/sales-demo/` (noindex, unlinked) to see the design with sample names, or switch preview on there to see it on every page of your own device. Sample cards show only the name line (no "Confirmed order" status) and are never shown to visitors.
