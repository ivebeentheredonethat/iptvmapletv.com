// Lists form submissions stored in the LEADS KV namespace, newest first.
// Usage: https://iptvmapletv.com/api/leads?key=<ADMIN_KEY>

export async function onRequestGet({ request, env }) {
  const key = new URL(request.url).searchParams.get("key");
  if (!env.ADMIN_KEY || key !== env.ADMIN_KEY) return new Response("Not found", { status: 404 });
  if (!env.LEADS) return new Response("LEADS KV namespace is not bound", { status: 500 });

  const leads = [];
  let cursor;
  do {
    const page = await env.LEADS.list({ prefix: "lead:", cursor });
    const values = await Promise.all(page.keys.map((k) => env.LEADS.get(k.name, "json")));
    leads.push(...values.filter(Boolean));
    cursor = page.list_complete ? undefined : page.cursor;
  } while (cursor && leads.length < 5000);

  leads.sort((a, b) => (a.at < b.at ? 1 : -1));
  return new Response(JSON.stringify(leads, null, 2), { headers: { "content-type": "application/json; charset=utf-8" } });
}
