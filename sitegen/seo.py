"""SEO landing pages (apps, devices, sports, cities, guides, French Québec pages).

Every page is a plain dict in sitegen/seo_content/*.py and is rendered by the one template below, so all of
them share the same title block, quick-answer box, FAQ (with FAQPage schema), breadcrumbs and internal links.

Page dict keys
  slug         URL slug ("tivimate" -> /tivimate/)
  hub          which cluster it belongs to (key of HUBS) — sets the breadcrumb and the hub page it's listed on
  lang         "en" (default) or "fr"
  title        <title> (aim for 50–60 characters, primary keyword first)
  description  meta description (aim for 120–160 characters)
  kicker, h1, lead      the shared page title block
  crumb        short name for the breadcrumb / hub card
  blurb        one sentence for the hub card
  answer       quick-answer HTML shown at the top of the article
  body         article HTML (h2/h3/p/ul/table …)
  faq          [(question, answer_html), …] — shown on the page and in FAQPage schema
  related      [slug, …] — "Related guides" links at the end of the article
  hub_page     True on the hub itself (lists every page of its cluster as cards)
  keywords     the spreadsheet keywords this page targets (documentation only)
"""
import re
from html import escape

from . import config as C
from .components import breadcrumb_ld, cta_band, faq_ld, faq_section, page_hero
from .icons import icon
from .layout import Page
from .seo_content import ALL

UPDATED = "2026-09-30"

HUBS = {
    "apps": ("/iptv-apps/", "IPTV apps"),
    "devices": ("/iptv-devices/", "Devices"),
    "sports": ("/iptv-sports/", "Sports"),
    "cities": ("/iptv-near-me/", "Cities"),
    "guides": (None, None),
    "fr": ("/iptv-quebec/", "IPTV Québec"),
}

TEXT = {
    "en": dict(home="Home", quick="Quick answer", updated="Updated", by="By the IPTVMaple team", related="Related guides",
               explore="Explore", trial="Start free 24h trial", plans="See plans — 50% off",
               faq="Frequently asked questions", cta_title="Ready to start watching?",
               cta_text="Every plan includes 50,000+ live channels, 300,000+ movies & series and 24/7 human support. Try it free first.",
               side1=("Try IPTVMaple free", "24 hours of full access. No credit card needed.", "Start free trial"),
               side2=("Plans from $9", "50,000+ channels &amp; 300,000+ movies in 4K — 50% off.", "See pricing"),
               all_label="All {label}"),
    "fr": dict(home="Accueil", quick="Réponse rapide", updated="Mis à jour le", by="Par l’équipe IPTVMaple", related="Guides connexes",
               explore="Découvrir", trial="Essai gratuit de 24 h", plans="Voir les forfaits — 50 % de rabais",
               faq="Questions fréquentes", cta_title="Prêt à regarder?",
               cta_text="Chaque forfait inclut plus de 50 000 chaînes en direct, 300 000 films et séries et un soutien humain 24/7. Essayez-le gratuitement d’abord.",
               side1=("Essayez IPTVMaple gratuitement", "24 heures d’accès complet. Aucune carte de crédit.", "Commencer l’essai"),
               side2=("Forfaits dès 9 $", "50 000+ chaînes et 300 000+ films en 4K — 50 % de rabais.", "Voir les prix"),
               all_label="{label}"),
}


def _plain(html):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", html.replace("&amp;", "&"))).strip()


def _by_slug():
    return {p["slug"]: p for p in ALL}


def _crumbs(p, T):
    items = [(T["home"], "/")]
    hub_url, hub_label = HUBS[p["hub"]]
    if hub_url and not p.get("hub_page"):
        items.append((hub_label, hub_url))
    items.append((p["crumb"], ""))
    return items


def _aside(T):
    (t1, d1, b1), (t2, d2, b2) = T["side1"], T["side2"]
    return f"""<aside>
  <div class="card side-cta"><div class="icon" style="margin-inline:auto">{icon("play")}</div><h3>{t1}</h3><p>{d1}</p><a class="btn btn--primary btn--block" href="/try-iptv-canada/">{b1}</a></div>
  <div class="card side-cta"><h3>{t2}</h3><p>{d2}</p><a class="btn btn--ghost btn--block" href="/iptv-plans-canada/">{b2}</a></div>
</aside>"""


def _hub_cards(p, T):
    pages = [q for q in ALL if q["hub"] == p["hub"] and not q.get("hub_page")]
    cards = "".join(
        f'<a class="card card--hover link-card reveal" href="/{q["slug"]}/"><h3>{q["crumb"]}</h3><p>{q["blurb"]}</p><span class="link-arrow">{T["explore"]}</span></a>'
        for q in pages)
    return f"""<section class="section section--tight">
  <div class="container"><div class="grid grid-3 link-cards">{cards}</div></div>
</section>"""


def render(p):
    lang = p.get("lang", "en")
    T = TEXT[lang]
    by = _by_slug()
    crumb = _crumbs(p, T)
    buttons = (f'<div class="btn-row" style="justify-content:center;margin-top:28px">'
               f'<a class="btn btn--primary btn--lg" href="/try-iptv-canada/">{T["trial"]}</a>'
               f'<a class="btn btn--ghost btn--lg" href="/iptv-plans-canada/">{T["plans"]}</a></div>')
    related = "".join(f'<li><a href="/{s}/">{by[s]["crumb"]}</a> — {by[s]["blurb"]}</li>' for s in p.get("related", []))
    hub_url, hub_label = HUBS[p["hub"]]
    if hub_url and not p.get("hub_page") and hub_url.strip("/") not in p.get("related", []):
        related += f'<li><a href="{hub_url}">{T["all_label"].format(label=hub_label)}</a></li>'
    related_html = f'<h2>{T["related"]}</h2><ul class="related-list">{related}</ul>' if related else ""
    body = f"""{page_hero(p["h1"], p["lead"], p["kicker"], crumb, buttons)}
<section class="section section--after-hero">
  <div class="container page-grid">
    <article class="prose-card prose reveal">
      <div class="answer-box"><strong>{T["quick"]}</strong>{p["answer"]}</div>
      <p class="meta-line">{T["updated"]} {UPDATED} · {T["by"]}</p>
      {p["body"]}
      {related_html}
    </article>
    {_aside(T)}
  </div>
</section>
{_hub_cards(p, T) if p.get("hub_page") else ""}
{faq_section([{"q": q, "a": a} for q, a in p["faq"]], T["faq"], lang) if p.get("faq") else ""}
{cta_band(p.get("cta_title", T["cta_title"]), p.get("cta_text", T["cta_text"]), lang=lang)}"""
    url = f"/{p['slug']}/"
    ld = [breadcrumb_ld([(label, href or url) for label, href in crumb])]
    if p.get("faq"):
        ld.append(faq_ld([{"q": q, "a": a} for q, a in p["faq"]]))
    ld.append({"@type": "Article", "headline": _plain(p["h1"])[:110], "description": p["description"],
               "datePublished": UPDATED, "dateModified": UPDATED, "inLanguage": "fr-CA" if lang == "fr" else "en-CA",
               "author": {"@id": C.SITE_URL + "/#organization"}, "publisher": {"@id": C.SITE_URL + "/#organization"},
               "image": C.SITE_URL + C.DEFAULT_OG, "mainEntityOfPage": C.SITE_URL + url})
    return Page(url, p["title"], p["description"], body, og_type="article", published=UPDATED, modified=UPDATED,
                jsonld=ld, lang="fr-CA" if lang == "fr" else "en-CA")


def seo_pages():
    return [render(p) for p in ALL]
