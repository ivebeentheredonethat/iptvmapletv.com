# Recent activity notifications

A small card at the bottom-left reads "**Sarah** from Ontario — **12 Month Plan**", with the date ("Oct 4" or "3 hours ago") underneath when one is given. It runs automatically for **every visitor on every page** (new browsers, private/incognito windows, mobile and desktop) and needs **no API, no key, no server, no preview switch and no browser storage**: the entries live in one file, `src/data/recent-orders.json`, which the build copies into each page.

While the file is an empty list (`[]`), nothing appears. Add only real orders: a named person with a plan reads to visitors as a real customer, whatever the wording.

## Add an entry
After you confirm payment (and the customer is OK with their first name being shown), add one line to `src/data/recent-orders.json`:

```json
[
  {"first": "Sarah", "place": "Ontario", "plan": "12 Months", "date": "2026-10-04"},
  {"first": "Luc", "place": "Quebec", "plan": "6 Months", "date": "2026-10-03"}
]
```

- `first`: first name only. `place`: province, state or country (e.g. `Canada`, `USA`). `plan`: as on the site (`1 Month`, `3 Months`, `6 Months`, `12 Months`); it is shown as "1 Month Plan", "12 Month Plan" and so on.
- `date` (optional): `YYYY-MM-DD` (shows "Oct 4") or a full time like `2026-10-04T15:30:00Z` (shows "3 hours ago"). Leave it out and the card shows only the name line.
- Commit the change on GitHub (the pencil icon on the file works). The site rebuilds and the entry is live on every page after the deploy. Up to 20 entries are used.
- To remove an entry, delete its line and commit.

## Behaviour
The first card appears 10 s after the page loads. Each card stays visible for 4 s, then the next one appears 10 s later. The order is random on every visit and reshuffled when the list runs out, never showing the same entry twice in a row. Hover or keyboard focus keeps a card on screen; it pauses while the tab is in the background; the × closes it for the rest of that page view. No network request is made and nothing is stored in the browser.

The old `/sales-demo/` preview page and its on/off switch were removed on 2026-10-06; `/sales-demo/` now redirects to the home page.
