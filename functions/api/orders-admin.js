// Owner-only management of the purchase-notification feed. Requires the ADMIN_KEY secret (same one as /api/leads).
//   List:    GET    /api/orders-admin?key=KEY
//   Add:     POST   /api/orders-admin?key=KEY   {"first":"Sarah","place":"Ontario","plan":"12 Months","at":"2026-10-01T15:00:00Z"}
//   Remove:  DELETE /api/orders-admin?key=KEY&id=ID
// Only add real, confirmed orders from customers who agreed to be shown (first name and region only).

const KEY = "recent-orders";
const clean = (v, n) => String(v || "").replace(/[<>&"]/g, "").trim().slice(0, n);
const out = (body, status = 200) =>
  new Response(JSON.stringify(body, null, 2), { status, headers: { "content-type": "application/json; charset=utf-8" } });

export async function onRequest({ request, env }) {
  const url = new URL(request.url);
  if (!env.ADMIN_KEY || url.searchParams.get("key") !== env.ADMIN_KEY) return new Response("Not found", { status: 404 });
  if (!env.LEADS) return out({ error: "LEADS KV namespace is not bound" }, 500);
  let items = (await env.LEADS.get(KEY, "json")) || [];

  if (request.method === "GET") return out(items);

  if (request.method === "POST") {
    let b;
    try { b = await request.json(); } catch { return out({ error: "send JSON" }, 400); }
    const item = { id: crypto.randomUUID().slice(0, 8), first: clean(b.first, 30), place: clean(b.place, 40), plan: clean(b.plan, 30),
      at: Number.isFinite(Date.parse(b.at)) ? new Date(b.at).toISOString() : new Date().toISOString() };
    if (!item.first || !item.place || !item.plan) return out({ error: "first, place and plan are required" }, 400);
    items = [item, ...items].slice(0, 100);
    await env.LEADS.put(KEY, JSON.stringify(items));
    return out(item, 201);
  }

  if (request.method === "DELETE") {
    const id = url.searchParams.get("id");
    items = items.filter((x) => x.id !== id);
    await env.LEADS.put(KEY, JSON.stringify(items));
    return out({ ok: true });
  }
  return new Response("Method not allowed", { status: 405 });
}
