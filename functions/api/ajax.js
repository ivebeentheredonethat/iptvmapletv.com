// Replaces WordPress's /wp-admin/admin-ajax.php for the Forminator order, free-trial and
// referral forms. Each submission is:
//   1. saved in the LEADS KV namespace (if bound),
//   2. POSTed as JSON to NOTIFY_WEBHOOK_URL (if set),
//   3. always written to the function log.
// Free-trial submissions also go through the automatic trial (functions/_lib/trial.js): the login is
// created and emailed straight away, and the lead falls back to the manual flow if that isn't possible.
// Field names and the response shape are the ones the old Forminator forms used.

import { createTrial, notifyTrial } from "../_lib/trial.js";

const REFERRAL_FORM = "3995";
const TRIAL_FORM = "1570";

const LABELS = {
  default: {
    plan: "Plan",
    "name-1": "First name",
    "email-1": "Email",
    "address-1-country": "Country",
    "phone-1": "WhatsApp",
  },
  [REFERRAL_FORM]: {
    "name-1": "Name",
    "phone-1": "Phone",
    "email-1": "Email",
    "name-2": "Friend's name",
    "phone-2": "Friend's phone",
    "email-2": "Friend's email",
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
  // Honeypot: real visitors never see or fill the "website" field; pretend success for bots.
  if (form.get("website")) return json({ success: true, data: { success: true, message: "Thanks!" } });
  const labels = LABELS[formId] || LABELS.default;
  const fields = {};
  for (const [key, label] of Object.entries(labels)) {
    const v = String(form.get(key) || "").trim().slice(0, 300);
    if (v) fields[label] = v;
  }
  if (!Object.keys(fields).some((k) => k !== "Plan")) {
    return json({ success: true, data: { success: false, message: "Please fill in the form.", errors: [] } });
  }

  const page = new URL(String(form.get("current_url") || form.get("_wp_http_referer") || "/"), request.url).pathname;
  const lead = {
    type: formId === REFERRAL_FORM ? "referral" : formId === TRIAL_FORM ? "free-trial" : "order",
    page,
    form_id: formId,
    fields,
    country: request.cf?.country,
    at: new Date().toISOString(),
  };

  if (formId === TRIAL_FORM) return trial(form, lead, request, env, waitUntil);

  console.log("LEAD", JSON.stringify(lead));
  waitUntil(deliver(lead, env));

  if (formId === REFERRAL_FORM) {
    return json({
      success: true,
      data: { success: true, message: "Thank you! We received your referral and will be in touch shortly.", behav: "behaviour-thankyou" },
    });
  }
  return json({
    success: true,
    data: { success: true, message: "Order received! Redirecting…", url: "/thank-you/", newtab: "sametab", behav: "behaviour-redirect" },
  });
}

async function trial(form, lead, request, env, waitUntil) {
  const get = (k) => String(form.get(k) || "").trim().slice(0, 120);
  const name = get("name-1"), email = get("email-1"), whatsapp = get("phone-1"), country = get("address-1-country");
  const fail = (message) => json({ success: true, data: { success: false, message, errors: [] } });
  if (!name || !email || whatsapp.replace(/\D/g, "").length < 7) return fail("Please fill in your first name, email and WhatsApp number.");

  let result;
  try {
    result = await createTrial({ name, email, country, whatsapp, ip: request.headers.get("CF-Connecting-IP"), env });
  } catch (err) {
    result = { status: "manual", reason: `error: ${err.message}` };
  }
  if (result.status === "invalid") return fail(result.message);
  if (result.status === "duplicate") {
    return fail("A free trial was already sent to this email or WhatsApp number. Check your inbox and spam folder, or message us on WhatsApp for help.");
  }
  if (result.status === "rate_limited") {
    return fail("Too many trial requests from your connection today. Please message us on WhatsApp and we’ll help you right away.");
  }

  lead.trial = result.status === "sent" ? "sent automatically" : `manual (${result.reason})`;
  console.log("LEAD", JSON.stringify(lead));
  waitUntil(deliver(lead, env));
  if (result.trial) {
    waitUntil(notifyTrial(env, result.trial, { page: lead.page, ipCountry: lead.country, emailed: result.status === "sent", reason: result.reason }));
  }

  if (result.status === "sent") {
    return json({ success: true, data: { success: true, message: "Your free trial login is on its way to your inbox.", email, behav: "behaviour-thankyou" } });
  }
  // Not automated (not configured, panel or email failure): the lead is saved and the team sends it by hand.
  return json({
    success: true,
    data: { success: true, message: "Request received! Redirecting…", url: "/thank-you/", newtab: "sametab", behav: "behaviour-redirect" },
  });
}

async function deliver(lead, env) {
  const jobs = [];
  if (env.LEADS) {
    jobs.push(env.LEADS.put(`lead:${lead.at}:${crypto.randomUUID().slice(0, 8)}`, JSON.stringify(lead)));
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
