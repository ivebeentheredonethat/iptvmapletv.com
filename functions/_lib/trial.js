// Automatic free trial (same flow as maplestreamtv.ca's trial worker):
//   1. abuse checks: one trial per email and per WhatsApp number, a few per IP per day, a daily cap,
//   2. a 24-hour line is created on the IPTV panel (or shared demo credentials are used as a fallback),
//   3. the trial is recorded in the LEADS KV namespace,
//   4. the login is emailed to the customer through Resend, and a copy goes to the team.
// Anything that is not configured or fails returns { status: "manual" } so the lead is still saved and
// the team sends the trial by hand, exactly as before this automation existed.
//
// Secrets (Cloudflare Pages → Settings → Variables and Secrets):
//   RESEND_KEY      Resend API key (iptvmapletv.com must be a verified sending domain in Resend)
//   PANEL_API_KEY   activationpanel.ru reseller API key
//   DEMO_USERNAME / DEMO_PASSWORD   optional shared trial login used when the panel can't create a line
// Optional plain variables: TRIAL_DAILY_LIMIT (default 60), TRIAL_FROM_EMAIL, TRIAL_ADMIN_EMAIL.

const SITE = "iptvmapletv.com";
const SITE_URL = "https://iptvmapletv.com";
const PANEL_API = "https://activationpanel.ru/api/api.php";
const PANEL_HOST = "http://line.truthdaily.me";
const PANEL_PACK = "USA - All";
const FROM_EMAIL = "IPTVMaple <help@iptvmapletv.com>";
const ADMIN_EMAIL = "help@iptvmapletv.com";
const WA_NUMBER = "17828026280";
const WA_LABEL = "+1 782-802-6280";
const CENTRAL_LOG = "https://iptv-kv-reader.medmaar.workers.dev/add";

const DAY = 24 * 60 * 60;
const TRIAL_HOURS = 24;
const PER_IP_PER_DAY = 3;

const DISPOSABLE = new Set([
  "mailinator.com", "guerrillamail.com", "guerrillamail.net", "sharklasers.com", "10minutemail.com", "tempmail.com",
  "temp-mail.org", "yopmail.com", "trashmail.com", "getnada.com", "dispostable.com", "maildrop.cc", "throwawaymail.com",
  "fakeinbox.com", "mintemail.com", "mohmal.com", "emailondeck.com", "tempail.com", "burnermail.io", "moakt.com",
]);

export const EMAIL_RE = /^[^\s@<>"]+@[^\s@<>"]+\.[a-z]{2,}$/i;

// gmail ignores dots and +tags; everyone else ignores +tags. One trial per real inbox.
export function inboxKey(email) {
  let [user, domain] = email.toLowerCase().split("@");
  user = user.split("+")[0];
  if (domain === "gmail.com" || domain === "googlemail.com") { user = user.replace(/\./g, ""); domain = "gmail.com"; }
  return `${user}@${domain}`;
}

const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);
const timeout = (ms) => AbortSignal.timeout(ms);

export async function createTrial({ name, email, country, whatsapp, ip, env }) {
  const kv = env.LEADS;
  email = email.trim();
  if (!EMAIL_RE.test(email)) return { status: "invalid", message: "Please enter a valid email address." };
  const domain = email.split("@")[1].toLowerCase();
  if (DISPOSABLE.has(domain)) return { status: "invalid", message: "Please use your real email address — your login is sent there." };
  if (!kv) return { status: "manual", reason: "LEADS KV namespace not bound" };

  const inbox = inboxKey(email);
  const phone = String(whatsapp || "").replace(/\D/g, "");
  const today = new Date().toISOString().slice(0, 10);
  const [byEmail, byPhone, ipCount, dayCount] = await Promise.all([
    kv.get(`trial:${inbox}`),
    phone.length >= 7 ? kv.get(`trial-phone:${phone}`) : null,
    ip ? kv.get(`trial-ip:${ip}`) : null,
    kv.get(`trial-day:${today}`),
  ]);
  if (byEmail || byPhone) return { status: "duplicate" };
  if (+ipCount >= PER_IP_PER_DAY) return { status: "rate_limited" };
  if (+dayCount >= (+env.TRIAL_DAILY_LIMIT || 60)) return { status: "manual", reason: "daily automatic trial limit reached" };
  if (!env.RESEND_KEY) return { status: "manual", reason: "RESEND_KEY secret not set" };

  // Count the attempt before calling the panel so a burst of requests can't drain panel credits.
  await Promise.all([
    ip && kv.put(`trial-ip:${ip}`, String(+ipCount + 1), { expirationTtl: DAY }),
    kv.put(`trial-day:${today}`, String(+dayCount + 1), { expirationTtl: 2 * DAY }),
  ]);

  let creds;
  try {
    creds = await panelLine(env, email, whatsapp);
  } catch (err) {
    if (env.DEMO_USERNAME && env.DEMO_PASSWORD) {
      console.log(`trial: panel failed (${err.message}), using shared demo login`);
      creds = { username: env.DEMO_USERNAME, password: env.DEMO_PASSWORD, shared: true };
    } else {
      return { status: "manual", reason: `panel: ${err.message}` };
    }
  }

  const { username, password } = creds;
  const m3u = `${PANEL_HOST}/get.php?username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}&type=m3u_plus&output=ts`;
  const now = Date.now();
  const trial = { name, email, country, whatsapp, site: SITE, username, password, m3uUrl: m3u, expiry: now + TRIAL_HOURS * 3600e3,
                  shared_demo: !!creds.shared, created_at: now };
  // Record the trial before emailing so a retry can never create a second line.
  await Promise.all([
    kv.put(`trial:${inbox}`, JSON.stringify(trial), { expirationTtl: 180 * DAY }),
    phone.length >= 7 && kv.put(`trial-phone:${phone}`, inbox, { expirationTtl: 180 * DAY }),
  ]);

  try {
    await sendEmail(env, email, "Your IPTVMaple free trial is ready — 24h access activated ✓", welcomeEmail(name, username, password, m3u));
  } catch (err) {
    return { status: "manual", reason: `email: ${err.message}`, trial };
  }
  return { status: "sent", trial };
}

// Team copy + central trial log. Best-effort: runs after the response.
export async function notifyTrial(env, trial, extra = {}) {
  const jobs = [
    sendEmail(env, env.TRIAL_ADMIN_EMAIL || ADMIN_EMAIL, `Automation / ${SITE} / trial / ${trial.name} / ${trial.email}`, adminEmail(trial, extra)),
    fetch(CENTRAL_LOG, { method: "POST", headers: { "content-type": "application/json" }, signal: timeout(8000),
      body: JSON.stringify({ name: trial.name, email: trial.email, whatsapp: trial.whatsapp, phone: trial.whatsapp, site: SITE, created_at: trial.created_at }) }),
  ];
  for (const r of await Promise.allSettled(jobs)) if (r.status === "rejected") console.error("trial notify failed", r.reason);
}

async function panelGet(env, params) {
  const qs = new URLSearchParams({ ...params, api_key: env.PANEL_API_KEY });
  const res = await fetch(`${PANEL_API}?${qs}`, { signal: timeout(12000) });
  const text = (await res.text()).trim();
  if (!text.startsWith("[") && !text.startsWith("{")) throw new Error(`non-JSON reply: ${text.slice(0, 160)}`);
  return JSON.parse(text);
}

async function panelLine(env, email, whatsapp) {
  if (!env.PANEL_API_KEY) throw new Error("PANEL_API_KEY secret not set");
  let pack = "all";
  try {
    const list = await panelGet(env, { action: "bouquet" });
    const found = (Array.isArray(list) ? list : Object.values(list)).find((b) => (b.name || "").trim().toLowerCase() === PANEL_PACK.toLowerCase());
    if (found) pack = found.id;
  } catch (err) { console.log("trial: bouquet lookup failed", err.message); }

  const data = await panelGet(env, { action: "new", type: "m3u", sub: "99", pack, notes: `Trial / ${SITE} / ${email} | ${whatsapp || ""}` });
  const item = Array.isArray(data) ? data[0] : data;
  if (!item || String(item.status) !== "true") throw new Error(item?.message || JSON.stringify(item).slice(0, 160));
  const u = new URL(item.url || "");
  const username = u.searchParams.get("username"), password = u.searchParams.get("password");
  if (!username || !password) throw new Error("no username/password in panel reply");
  return { username, password };
}

async function sendEmail(env, to, subject, html) {
  const res = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { Authorization: `Bearer ${env.RESEND_KEY}`, "content-type": "application/json" },
    body: JSON.stringify({ from: env.TRIAL_FROM_EMAIL || FROM_EMAIL, reply_to: ADMIN_EMAIL, to, subject, html }),
    signal: timeout(10000),
  });
  if (!res.ok) throw new Error(`Resend ${res.status}: ${(await res.text()).slice(0, 200)}`);
}

// ------------------------------------------------------------------ emails
const P = (html, extra = "") => `<p style="margin:0 0 14px;font-family:Arial,sans-serif;font-size:14px;line-height:1.65;color:#555555;${extra}">${html}</p>`;

function wrap(content) {
  return `<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"></head>
<body style="margin:0;padding:0;background-color:#f2f2f4;font-family:Arial,sans-serif;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#f2f2f4;padding:32px 16px;"><tr><td align="center">
  <table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;background:#ffffff;border-radius:10px;overflow:hidden;">
    <tr><td style="background-color:#06070b;padding:30px 40px;text-align:center;border-bottom:3px solid #ff2d4a;">
      <img src="${SITE_URL}/brand/icon-192.png" width="56" height="56" alt="" style="display:block;margin:0 auto 10px;border:0;">
      <h1 style="margin:0;font-family:Arial,sans-serif;font-size:26px;font-weight:bold;color:#ffffff;">IPTVMaple</h1>
      <p style="margin:6px 0 0;font-family:Arial,sans-serif;font-size:13px;color:#a4aaba;">Live TV, sports, movies &amp; series in 4K</p>
    </td></tr>
    <tr><td style="padding:36px 40px;">${content}</td></tr>
    <tr><td style="background-color:#f8f8f9;border-top:1px solid #eeeeee;padding:18px 40px;text-align:center;">
      <p style="margin:0;font-family:Arial,sans-serif;font-size:11px;color:#999999;">© ${new Date().getFullYear()} IPTVMaple · <a href="${SITE_URL}" style="color:#ff2d4a;text-decoration:none;">iptvmapletv.com</a></p>
    </td></tr>
  </table>
</td></tr></table></body></html>`;
}

function row(label, value, last) {
  return `<tr><td style="padding:11px 0;${last ? "" : "border-bottom:1px solid #e8e8e8;"}">
    <p style="margin:0 0 2px;font-family:Arial,sans-serif;font-size:11px;color:#888888;text-transform:uppercase;">${label}</p>
    <p style="margin:0;font-family:Arial,sans-serif;font-size:14px;color:#222222;font-weight:bold;word-break:break-all;">${esc(value)}</p></td></tr>`;
}

function welcomeEmail(name, username, password, m3u) {
  const first = esc(String(name).trim().split(/\s+/)[0] || "there");
  const btn = (text, url, bg) => `<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 14px;"><tr><td style="background-color:${bg};border-radius:8px;padding:13px 28px;"><a href="${url}" style="font-family:Arial,sans-serif;font-size:15px;font-weight:bold;color:#ffffff;text-decoration:none;">${text}</a></td></tr></table>`;
  return wrap(`
    <p style="margin:0 0 16px;font-family:Arial,sans-serif;font-size:15px;color:#333333;">Hi ${first},</p>
    ${P("Your free trial is ready! 🎉 You have <strong>24 hours of full access</strong> to live TV, sports, movies and series.")}
    ${P("All countries and languages are unlocked so you can test everything. If the channel list feels too long, just ask us and we’ll hide the regions or categories you don’t need.", "font-size:13px;color:#777777;font-style:italic;margin-bottom:22px;")}
    <p style="margin:0 0 8px;font-family:Arial,sans-serif;font-size:13px;font-weight:bold;color:#333333;">Xtream Codes login</p>
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#f8f8f9;border:1px solid #e0e0e0;border-radius:6px;margin-bottom:18px;"><tr><td style="padding:8px 22px;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">${row("Server", PANEL_HOST)}${row("Username", username)}${row("Password", password, true)}</table>
    </td></tr></table>
    <p style="margin:0 0 8px;font-family:Arial,sans-serif;font-size:13px;font-weight:bold;color:#333333;">M3U link</p>
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#f8f8f9;border:1px solid #e0e0e0;border-radius:6px;margin-bottom:26px;"><tr><td style="padding:14px 20px;">
      <p style="margin:0;font-family:Arial,sans-serif;font-size:12px;color:#ff2d4a;word-break:break-all;">${esc(m3u)}</p>
    </td></tr></table>
    ${P(`Not sure which app to use? Our <a href="${SITE_URL}/how-it-works/" style="color:#ff2d4a;font-weight:bold;text-decoration:none;">setup guides</a> cover Firestick, Smart TVs, Android, iPhone and more.`)}
    ${btn("Set up my device →", `${SITE_URL}/how-it-works/`, "#ff2d4a")}
    ${P(`Need help? Reply to this email or message us on WhatsApp at <a href="https://wa.me/${WA_NUMBER}" style="color:#ff2d4a;font-weight:bold;text-decoration:none;">${WA_LABEL}</a>.`, "margin-top:10px;")}
    ${P(`Enjoying it? <a href="${SITE_URL}/iptv-plans-canada/" style="color:#ff2d4a;font-weight:bold;text-decoration:none;">See our plans</a> to keep watching after your trial.`)}
    <p style="margin:0;font-family:Arial,sans-serif;font-size:14px;color:#555555;">Best regards,<br><strong>The IPTVMaple Team</strong></p>`);
}

function adminEmail(t, extra) {
  const r = (k, v) => `<tr><td style="color:#888;width:120px;">${k}</td><td>${esc(v || "—")}</td></tr>`;
  return `<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"></head><body style="font-family:Arial,sans-serif;font-size:14px;color:#333;padding:20px;">
  <h2 style="color:#ff2d4a;margin-top:0;">New free trial — ${SITE}</h2>
  <table cellpadding="6" cellspacing="0" border="0">
    ${r("Name", t.name)}${r("Email", t.email)}${r("Country", t.country)}${r("WhatsApp", t.whatsapp)}${r("Page", extra.page)}${r("IP country", extra.ipCountry)}
    <tr><td colspan="2"><hr style="border:none;border-top:1px solid #eee;margin:8px 0;"></td></tr>
    ${r("Username", t.username)}${r("Password", t.password)}${r("M3U", t.m3uUrl)}
    ${r("Login type", t.shared_demo ? "Shared demo login (panel could not create a line)" : "New panel line, 24h")}
    ${r("Customer email", extra.emailed === false ? "NOT SENT — " + (extra.reason || "") : "Sent")}
  </table></body></html>`;
}
