"""Reusable page sections."""
import json
import os
import re
from html import escape

from . import config as C
from .icons import icon

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src")


def data(name):
    return json.load(open(os.path.join(SRC, "data", name + ".json"), encoding="utf-8"))


def content(slug):
    """src/content/<slug>.html -> (meta dict, html body). Meta lives in a leading <!--meta {json} --> block."""
    raw = open(os.path.join(SRC, "content", slug + ".html"), encoding="utf-8").read()
    m = re.match(r"\s*<!--meta\s*(\{.*?\})\s*-->\s*", raw, re.S)
    return (json.loads(m.group(1)), raw[m.end():]) if m else ({}, raw)


PLANS = data("plans")
FEATURES = PLANS["features"]


def plan_label(months):
    return {1: "1 Month", 6: "6 Months", 12: "12 Months"}[months]


def devices_label(n):
    return f"{n} {'device' if n == 1 else 'devices'}"


def all_plans():
    for c in PLANS["connections"]:
        for p in c["plans"]:
            yield c["devices"], p


def per_month(p):
    return f"≈ ${p['price'] / p['months']:.2f}/mo" if p["months"] > 1 else "Billed monthly"


# ------------------------------------------------------------------ small pieces
def aurora():
    return '<div class="aurora" aria-hidden="true"><i></i><i></i><i></i></div>'


def section_head(kicker, title, sub="", left=False):
    k = f'<span class="kicker">{kicker}</span>' if kicker else ""
    s = f"<p>{sub}</p>" if sub else ""
    return f'<div class="section-head{" section-head--left" if left else ""} reveal">{k}<h2 class="h2">{title}</h2>{s}</div>'


def checks(items):
    return '<ul class="checks">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def crumbs(items):
    parts = []
    for i, (label, href) in enumerate(items):
        if i:
            parts.append('<span aria-hidden="true">/</span>')
        parts.append(f'<a href="{href}">{label}</a>' if href else f"<span>{label}</span>")
    return f'<nav class="crumbs" aria-label="Breadcrumb">{"".join(parts)}</nav>'


def breadcrumb_ld(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": label, **({"item": C.SITE_URL + href} if href else {})}
        for i, (label, href) in enumerate(items)]}


def page_hero(title, lead="", kicker="", crumb=None, extra=""):
    return f"""<section class="page-hero">
  {aurora()}<div class="grid-bg" aria-hidden="true"></div>
  <div class="container z">
    {crumbs(crumb) if crumb else ""}
    {f'<span class="kicker">{kicker}</span>' if kicker else ""}
    <h1>{title}</h1>
    {f'<p class="lead">{lead}</p>' if lead else ""}
    {extra}
  </div>
</section>"""


def trust_row():
    return f"""<div class="pricing-foot">
  <span>{icon("refund")} 7-day money-back guarantee</span>
  <span>{icon("bolt")} Ready within 5 minutes</span>
  <span>{icon("headset")} 24/7 live support</span>
  <span>{icon("lock")} Secure &amp; private</span>
</div>"""


# ------------------------------------------------------------------ pricing
def pricing(default_devices=1, heading=True):
    conn = next(c for c in PLANS["connections"] if c["devices"] == default_devices)
    tabs = "".join(
        f'<button type="button" role="tab" data-devices="{c["devices"]}" aria-selected="{str(c["devices"] == default_devices).lower()}">'
        f'<b>{c["devices"]}</b><span>{"Device" if c["devices"] == 1 else "Devices"}</span></button>'
        for c in PLANS["connections"])
    cards = []
    for p in conn["plans"]:
        best = p["months"] == 12
        n = default_devices
        feats = [f'<span class="js-conn">{n} {"device" if n == 1 else "devices"} at the same time</span>'] + FEATURES
        cards.append(f"""<article class="plan{' plan--best' if best else ''} reveal" style="--d:{.08 * len(cards)}s">
  {'<span class="plan-badge">Best value</span>' if best else ''}
  <div class="plan-name">{plan_label(p["months"])}</div>
  <div class="plan-sub">{n} simultaneous {"connection" if n == 1 else "connections"}</div>
  <div class="price"><span class="cur">$</span><span class="amt">{p["price"]}</span><span class="per">/ {plan_label(p["months"]).lower()}</span></div>
  <div class="price-meta"><s>${p["original"]}</s><span class="save">Save 50%</span><span class="per-month">{per_month(p)}</span></div>
  {checks(feats)}
  <a class="btn {'btn--primary' if best else 'btn--ghost'} btn--block" href="/{p['slug']}/">Get {plan_label(p['months'])}</a>
  <div class="plan-foot">Ready within 5 minutes</div>
</article>""")
    payload = json.dumps([{"devices": c["devices"], "plans": [{k: q[k] for k in ("months", "price", "original", "slug")} for q in c["plans"]]}
                          for c in PLANS["connections"]], separators=(",", ":"))
    head = section_head("Pricing", 'Simple plans. <span class="grad-text">Half the price.</span>',
                        "Every plan includes every channel, every movie and every feature. Pick how many screens you need and how long you want to save.") if heading else ""
    return f"""<div data-pricing>
  {head}
  <div class="seg-wrap reveal"><p class="seg-note">How many devices will watch at the same time?</p>
  <div class="seg" role="tablist" aria-label="Number of devices">{tabs}</div></div>
  <div class="plans">{"".join(cards)}</div>
  {trust_row()}
  <p class="center muted" style="font-size:13.5px;margin-top:14px">Prices in US dollars. Paying in CAD? Your bank converts automatically.</p>
  <script type="application/json">{payload}</script>
</div>"""


# ------------------------------------------------------------------ FAQ
def faq(items, open_first=True):
    out = []
    for i, f in enumerate(items):
        out.append(f'<details{" open" if open_first and i == 0 else ""}><summary>{escape(f["q"])}</summary><div class="answer">{f["a"]}</div></details>')
    return '<div class="faq">' + "".join(out) + "</div>"


def faq_ld(items):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", " ", f["a"]).strip()}}
        for f in items]}


def faq_section(items, title="Frequently asked questions"):
    return f"""<section class="section" id="faq">
  <div class="container faq-layout">
    <div class="faq-aside reveal">
      <span class="kicker">FAQ</span>
      <h2 class="h2">{title}</h2>
      <p class="muted">Can’t find what you’re looking for? Our team replies in minutes, day and night.</p>
      <div class="btn-row" style="margin-top:22px">
        <a class="btn btn--wa" href="{C.WHATSAPP_URL}" target="_blank" rel="noopener">{icon("whatsapp")} Chat on WhatsApp</a>
      </div>
    </div>
    <div class="reveal">{faq(items)}</div>
  </div>
</section>"""


# ------------------------------------------------------------------ reviews
def reviews_section():
    r = data("reviews")

    def initials(n):
        return "".join(w[0] for w in n.split()[:2]).upper()

    stars = f'<span class="stars" aria-label="5 out of 5 stars">★★★★★</span>'
    row1 = [f"""<figure class="review">{stars}<h4>{escape(x["title"])}</h4><p>{escape(x["body"])}</p>
<figcaption class="who"><span class="avatar">{initials(x["name"])}</span><span><b style="color:#fff">{escape(x["name"])}</b> · {x["country"]}</span></figcaption></figure>"""
            for x in r["reviews"]]
    row2 = [f"""<figure class="review review--wa"><span class="wa-tag">{icon("whatsapp")} WhatsApp message</span><p>“{escape(x["text"])}”</p>
<figcaption class="who"><span class="avatar" style="background:linear-gradient(135deg,#25d366,#128c7e)">{initials(x["name"])}</span><span><b style="color:#fff">{escape(x["name"])}</b> · {x["country"]}</span></figcaption></figure>"""
            for x in r["whatsapp"]]
    a = row1 + row2[:4]
    b = row2[4:] + row1
    return f"""<section class="section" id="reviews">
  <div class="container">{section_head("Reviews", "Loved by cord-cutters <span class='grad-text'>everywhere</span>", "Real words from our customers — by review and straight from our WhatsApp support chat.")}</div>
  <div class="reviews-stack reveal">
    <div class="marquee" style="--speed:70s"><div class="marquee-track">{"".join(a + a)}</div></div>
    <div class="marquee marquee--reverse" style="--speed:80s"><div class="marquee-track">{"".join(b + b)}</div></div>
  </div>
</section>"""


# ------------------------------------------------------------------ CTA band
def cta_band(title="Ready to cut the cord?", text="Join thousands of Canadians streaming live TV, sports and blockbusters in 4K — for half the price.", img="/images/composed/mosaic.webp"):
    return f"""<section class="section section--tight">
  <div class="container">
    <div class="cta-band reveal">
      <img src="{img}" alt="" loading="lazy" width="1600" height="676">
      <span class="kicker">Start today</span>
      <h2 class="h2">{title}</h2>
      <p>{text}</p>
      <div class="btn-row">
        <a class="btn btn--primary btn--lg" href="/iptv-plans-canada/">See plans — 50% off</a>
        <a class="btn btn--ghost btn--lg" href="/try-iptv-canada/">Try free for 24 hours</a>
      </div>
    </div>
  </div>
</section>"""


# ------------------------------------------------------------------ forms
COUNTRIES = ["Canada", "United States", "United Kingdom", "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Cape Verde", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo", "Costa Rica", "Côte d’Ivoire", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "DR Congo", "Ecuador", "Egypt", "El Salvador", "Eritrea", "Estonia", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guyana", "Haiti", "Honduras", "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Mauritania", "Mauritius", "Mexico", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway", "Oman", "Pakistan", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Puerto Rico", "Qatar", "Romania", "Russia", "Rwanda", "Saint Lucia", "San Marino", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Somalia", "South Africa", "South Korea", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Uganda", "Ukraine", "United Arab Emirates", "Uruguay", "Uzbekistan", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe", "Other"]


def lead_form(form_id, kind, submit_label, value=0, plan_name=""):
    """Order / free-trial form. Field names match the old Forminator form so leads keep the same shape."""
    opts = "".join(f"<option{' selected' if c == 'Canada' else ''}>{escape(c)}</option>" for c in COUNTRIES)
    return f"""<form class="lead-form" data-lead-form="{kind}" data-value="{value}" novalidate>
  <input type="hidden" name="action" value="forminator_submit_form_custom-forms">
  <input type="hidden" name="form_id" value="{form_id}">
  <input type="hidden" name="plan" value="{escape(plan_name)}">
  <div class="hp" aria-hidden="true"><label>Website <input name="website" tabindex="-1" autocomplete="off"></label></div>
  <div class="fields">
    <div class="field"><label for="f-name">First name</label><input class="input" id="f-name" name="name-1" autocomplete="given-name" placeholder="E.g. John" required><span class="err"></span></div>
    <div class="field"><label for="f-country">Country</label><select class="input" id="f-country" name="address-1-country" autocomplete="country-name">{opts}</select><span class="err"></span></div>
    <div class="field field--full"><label for="f-email">Email address</label><input class="input" id="f-email" name="email-1" type="email" autocomplete="email" inputmode="email" placeholder="you@example.com" required><span class="err"></span></div>
    <div class="field field--full"><label for="f-phone">WhatsApp number <em>— we send your login here</em></label><input class="input" id="f-phone" name="phone-1" type="tel" autocomplete="tel" inputmode="tel" placeholder="E.g. +1 300 400 5000" required><span class="err"></span></div>
  </div>
  <button class="btn btn--primary btn--lg btn--block" type="submit" style="margin-top:22px"><span class="spinner"></span>{submit_label} {icon("arrow-right")}</button>
  <div class="form-msg" role="status" aria-live="polite"></div>
  <p class="form-note">{icon("lock")} Your details are only used to activate your service. No spam, ever.</p>
</form>"""


def referral_form():
    def person(prefix, n, who, hint, ph_name, ph_phone, ph_email):
        return f"""<fieldset class="ref-group ref-group--{prefix}">
    <legend><span class="ref-num">{n}</span><span><b>{who}</b><small>{hint}</small></span></legend>
    <div class="fields">
      <div class="field"><label for="{prefix}-name">Name</label><input class="input" id="{prefix}-name" name="name-{n}" autocomplete="{'name' if n == 1 else 'off'}" placeholder="{ph_name}" required><span class="err"></span></div>
      <div class="field"><label for="{prefix}-phone">Phone (WhatsApp)</label><input class="input" id="{prefix}-phone" name="phone-{n}" type="tel" inputmode="tel" autocomplete="{'tel' if n == 1 else 'off'}" placeholder="{ph_phone}" required><span class="err"></span></div>
      <div class="field field--full"><label for="{prefix}-email">Email</label><input class="input" id="{prefix}-email" name="email-{n}" type="email" inputmode="email" autocomplete="{'email' if n == 1 else 'off'}" placeholder="{ph_email}" required><span class="err"></span></div>
    </div>
  </fieldset>"""
    return f"""<form class="lead-form" data-lead-form="referral" novalidate>
  <input type="hidden" name="action" value="forminator_submit_form_custom-forms">
  <input type="hidden" name="form_id" value="3995">
  <div class="hp" aria-hidden="true"><label>Website <input name="website" tabindex="-1" autocomplete="off"></label></div>
  {person("r", 1, "Your details", "The person referring", "E.g. John Smith", "E.g. +1 300 400 5000", "you@example.com")}
  {person("rf", 2, "Your friend’s details", "The new customer you’re referring", "E.g. Mike Brown", "E.g. +1 245 852 4100", "friend@example.com")}
  <button class="btn btn--primary btn--lg btn--block" type="submit" style="margin-top:22px"><span class="spinner"></span>Submit referral {icon("arrow-right")}</button>
  <div class="form-msg" role="status" aria-live="polite"></div>
</form>"""


def guarantee():
    return f"""<div class="guarantee">{icon("shield")}<div><strong>7-day money-back guarantee</strong>Not satisfied? Request a full refund within 7 days of purchase.</div></div>"""
