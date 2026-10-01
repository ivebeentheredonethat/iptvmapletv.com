// Public feed for the "recent purchase" notification card. It only returns entries the site owner has added
// (with the customer's consent) through /api/orders-admin. No entries -> an empty list -> nothing is shown.

const MAX_AGE_MS = 30 * 24 * 3600 * 1000;

export async function onRequestGet({ env }) {
  let items = [];
  if (env.LEADS) items = (await env.LEADS.get("recent-orders", "json")) || [];
  const now = Date.now();
  const fresh = items
    .filter((x) => now - Date.parse(x.at) < MAX_AGE_MS)
    .sort((a, b) => (a.at < b.at ? 1 : -1))
    .slice(0, 12)
    .map(({ first, place, plan, at }) => ({ first, place, plan, at }));
  return new Response(JSON.stringify(fresh), {
    headers: { "content-type": "application/json; charset=utf-8", "cache-control": "public, max-age=120" },
  });
}
