"""The HTML shell shared by every page: <head> (SEO + analytics), header, footer, contact dock."""
import json
from dataclasses import dataclass, field
from html import escape

from . import config as C
from .icons import icon, payment_icons

ASSET_VERSION = "dev"  # set by build.py to a content hash


@dataclass
class Page:
    path: str                      # "/" or "/slug/"
    title: str
    description: str
    body: str
    og_image: str = C.DEFAULT_OG
    og_type: str = "website"
    robots: str = "follow, index, max-snippet:-1, max-video-preview:-1, max-image-preview:large"
    published: str = ""
    modified: str = ""
    jsonld: list = field(default_factory=list)
    in_sitemap: bool = True
    nav_active: str = ""           # which NAV href to highlight


def abs_url(u):
    return u if u.startswith("http") else C.SITE_URL + u


def _analytics():
    first = C.GOOGLE_TAGS[0]
    configs = "".join(f'gtag("config","{t}");' for t in C.GOOGLE_TAGS)
    return f"""<script async src="https://www.googletagmanager.com/gtag/js?id={first}"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag("js",new Date());gtag("set","linker",{{"domains":["iptvmapletv.com"]}});{configs}</script>
<script>!function(w,d){{if(!w.rdt){{var p=w.rdt=function(){{p.sendEvent?p.sendEvent.apply(p,arguments):p.callQueue.push(arguments)}};p.callQueue=[];var t=d.createElement("script");t.src="https://www.redditstatic.com/ads/pixel.js",t.async=!0;var s=d.getElementsByTagName("script")[0];s.parentNode.insertBefore(t,s)}}}}(window,document);rdt("init","{C.REDDIT_PIXEL}");rdt("track","PageVisit");</script>"""


def _head(p: Page):
    url = abs_url(p.path)
    img = abs_url(p.og_image)
    t, d = escape(p.title), escape(p.description)
    title_text = escape(p.title, quote=False)
    ld = [{
        "@context": "https://schema.org", "@graph": [
            {"@type": "Organization", "@id": C.SITE_URL + "/#organization", "name": C.LEGAL_NAME, "url": C.SITE_URL,
             "logo": C.SITE_URL + "/brand/icon-512.png", "email": C.EMAIL,
             "sameAs": [C.TELEGRAM_URL]},
            {"@type": "WebSite", "@id": C.SITE_URL + "/#website", "url": C.SITE_URL, "name": C.LEGAL_NAME,
             "alternateName": C.NAME, "publisher": {"@id": C.SITE_URL + "/#organization"}, "inLanguage": "en-US"},
            {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": p.title, "description": p.description,
             "isPartOf": {"@id": C.SITE_URL + "/#website"}, "inLanguage": "en-US",
             **({"datePublished": p.published} if p.published else {}), **({"dateModified": p.modified} if p.modified else {})},
        ] + p.jsonld,
    }]
    dates = ""
    if p.og_type == "article" and p.published:
        dates = f'<meta property="article:published_time" content="{p.published}">\n<meta property="article:modified_time" content="{p.modified or p.published}">\n'
    return f"""<!doctype html>
<html lang="en-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title_text}</title>
<meta name="description" content="{d}">
<meta name="robots" content="{p.robots}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#06070b">
<meta property="og:locale" content="en_US">
<meta property="og:type" content="{p.og_type}">
<meta property="og:site_name" content="{C.LEGAL_NAME}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{img}">
{dates}<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{t}">
<meta name="twitter:description" content="{d}">
<meta name="twitter:image" content="{img}">
<meta name="google-site-verification" content="{C.GOOGLE_SITE_VERIFICATION}">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/brand/icon-192.png" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="/brand/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/fonts/sora-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/css/site.css?v={ASSET_VERSION}">
<script type="application/ld+json">{json.dumps(ld[0], ensure_ascii=False, separators=(",", ":"))}</script>
{_analytics()}
</head>"""


def brand_html():
    return (f'<a class="brand" href="/" aria-label="{C.NAME} home">'
            f'<img src="/brand/mark-128.webp" width="38" height="38" alt="">'
            f'<span><span class="r">IPTV</span><span class="c">Maple</span></span></a>')


def _header(p: Page):
    def link(label, href):
        cur = ' aria-current="page"' if href == (p.nav_active or p.path) else ""
        return f'<a href="{href}"{cur}>{label}</a>'
    nav = "".join(link(l, h) for l, h in C.NAV)
    promo_text, promo_href = C.PROMO
    return f"""<a class="skip" href="#main">Skip to content</a>
<a class="promo" href="{promo_href}">{promo_text} <span>— <u>see how</u> →</span></a>
<header class="header">
  <div class="container">
    {brand_html()}
    <nav class="nav" aria-label="Main">{nav}</nav>
    <div class="header-cta">
      <a class="btn btn--ghost btn--sm" href="/try-iptv-canada/">Free trial</a>
      <a class="btn btn--primary btn--sm" href="/iptv-plans-canada/">Get started</a>
      <button class="menu-btn" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-nav"><span></span></button>
    </div>
  </div>
</header>
<nav class="mobile-nav" id="mobile-nav" aria-label="Mobile">
  {nav}
  <a class="btn btn--primary btn--lg btn--block" href="/iptv-plans-canada/">See plans — 50% off</a>
  <a class="btn btn--ghost btn--lg btn--block" href="/try-iptv-canada/">Start free 24h trial</a>
</nav>"""


def _footer():
    cols = "".join(
        f'<div><h4>{title}</h4><ul>{"".join(f"<li><a href=\"{h}\">{l}</a></li>" for l, h in links)}</ul></div>'
        for title, links in C.FOOTER
    )
    return f"""<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        {brand_html()}
        <p style="margin-top:18px">Premium IPTV for Canada — live TV, sports, movies and series in stunning 4K on every device. No contracts, no hidden fees.</p>
        <div class="pay" aria-label="Accepted payment methods">{payment_icons()}</div>
      </div>
      {cols}
      <div><h4>Get in touch</h4><ul>
        <li><a href="{C.WHATSAPP_URL}" target="_blank" rel="noopener">WhatsApp</a></li>
        <li><a href="{C.TELEGRAM_URL}" target="_blank" rel="noopener">Telegram</a></li>
        <li><a href="mailto:{C.EMAIL}">{C.EMAIL}</a></li>
      </ul></div>
    </div>
    <div class="footer-bottom">
      <span>© {C.YEAR} {C.NAME}. All rights reserved.</span>
      <span>Prices in USD · 7-day money-back guarantee</span>
    </div>
  </div>
  <div class="footer-word" aria-hidden="true">IPTVMaple</div>
</footer>
<div class="dock" aria-label="Contact us">
  <a class="wa" href="{C.WHATSAPP_URL}" target="_blank" rel="noopener" data-label="Chat on WhatsApp" aria-label="Chat on WhatsApp">{icon("whatsapp")}</a>
  <a class="tg" href="{C.TELEGRAM_URL}" target="_blank" rel="noopener" data-label="Telegram support" aria-label="Telegram support">{icon("telegram")}</a>
  <a class="em" href="{C.MAILTO}" data-label="Email us" aria-label="Email us">{icon("mail")}</a>
</div>"""


def render(p: Page):
    return f"""{_head(p)}
<body>
{_header(p)}
<main id="main">
{p.body}
</main>
{_footer()}
<script src="/js/site.js?v={ASSET_VERSION}" defer></script>
</body>
</html>
"""
