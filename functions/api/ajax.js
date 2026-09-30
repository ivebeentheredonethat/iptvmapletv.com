// Replaces WordPress's /wp-admin/admin-ajax.php for the Forminator order, free-trial and
// referral forms. Each submission is:
//   1. saved in the LEADS KV namespace (if bound),
//   2. sent to Telegram (if TELEGRAM_BOT_TOKEN + TELEGRAM_CHAT_ID are set),
//   3. POSTed as JSON to NOTIFY_WEBHOOK_URL (if set),
//   4. always written to the function log.
// The response mimics Forminator's so its front-end script behaves exactly as before.

const REFERRAL_FORM = "3995";

const LABELS = {
  default: {
    "name-1": "First name",
    "email-1": "Email",
    "address-1-country": "Country",
    "phone-1": "WhatsApp",
  },
  [REFERRAL_FORM]: {
    "name-1": "First name",
    "phone-1": "WhatsApp",
    "name-2": "Friend's first name",
    "phone-2": "Friend's WhatsApp",
  },
};

const json = (body) =>
  new Response(JSON.stringify(body), { headers: { "content-type": "application/json; charset=utf-8" } });

export async function onRequestPost({ request, env, waitUntil }) {
  let form;
  try {
    form = await request.formData();
  } catch {
    return json({ success: false, data: "bad request" });
  }
  const action = form.get("action");

  // Forminator refreshes its nonce on cached pages; nonces are meaningless here.
  if (action === "forminator_get_nonce") return json({ success: true, data: "static" });

  if (action !== "forminator_submit_form_custom-forms") return json({ success: false, data: "unsupported" });

  const formId = String(form.get("form_id") || "");
  const labels = LABELS[formId] || LABELS.default;
  const fields = {};
  for (const [key, label] of Object.entries(labels)) {
    const v = String(form.get(key) || "").trim().slice(0, 300);
    if (v) fields[label] = v;
  }
  if (!Object.keys(fields).length) {
    return json({ success: true, data: { success: false, message: "Please fill in the form.", errors: [] } });
  }

  const page = new URL(String(form.get("current_url") || form.get("_wp_http_referer") || "/"), request.url).pathname;
  const lead = {
    type: formId === REFERRAL_FORM ? "referral" : page.includes("try-iptv") || page.includes("landing") ? "free-trial" : "order",
    page,
    form_id: formId,
    fields,
    country: request.cf?.country,
    at: new Date().toISOString(),
  };

  console.log("LEAD", JSON.stringify(lead));
  waitUntil(deliver(lead, env));

  if (formId === REFERRAL_FORM) {
    return json({
      success: true,
      data: { success: true, message: "Thank you! We received your referral and will contact you on WhatsApp shortly.", behav: "behaviour-thankyou" },
    });
  }
  return json({
    success: true,
    data: { success: true, message: "Order received! Redirecting…", url: "/thank-you/", newtab: "sametab", behav: "behaviour-redirect" },
  });
}

async function deliver(lead, env) {
  const jobs = [];
  if (env.LEADS) {
    jobs.push(env.LEADS.put(`lead:${lead.at}:${crypto.randomUUID().slice(0, 8)}`, JSON.stringify(lead)));
  }
  if (env.TELEGRAM_BOT_TOKEN && env.TELEGRAM_CHAT_ID) {
    const text =
      `New ${lead.type} — ${lead.page}\n` +
      Object.entries(lead.fields).map(([k, v]) => `${k}: ${v}`).join("\n") +
      (lead.country ? `\n(IP country: ${lead.country})` : "");
    jobs.push(
      fetch(`https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/sendMessage`, {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ chat_id: env.TELEGRAM_CHAT_ID, text }),
      })
    );
  }
  if (env.NOTIFY_WEBHOOK_URL) {
    jobs.push(
      fetch(env.NOTIFY_WEBHOOK_URL, { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(lead) })
    );
  }
  const results = await Promise.allSettled(jobs);
  for (const r of results) if (r.status === "rejected") console.error("lead delivery failed", r.reason);
}

export const onRequestGet = () => json({ success: false, data: "method not allowed" });
