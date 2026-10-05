"""Second-level SEO audit: on-page, schema-vs-content, content quality and performance checks that
seo_audit.py does not cover.   Usage: python build.py && python tools/seo_audit_deep.py [--verbose]
"""
import json, os, re, sys
from collections import Counter, defaultdict
from html import unescape
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seo_audit import OUT, SITE, load_pages, read, text_of, redirects

pages = load_pages()
reds = redirects()
V = "--verbose" in sys.argv
issues = defaultdict(list)
def add(k, p, extra=""): issues[k].append(f"{p} {extra}".strip())

ASSETS = {"/" + os.path.relpath(os.path.join(d, f), OUT).replace(os.sep, "/") for d, _, fs in os.walk(OUT) for f in fs}
STOP = set("the a an of in on for to and or with your you is are how what best canada canadian 2026 guide".split())
shingles = {}

for path, html in pages.items():
    head = html[: html.index("</head>")]
    noindex = "noindex" in head.split('name="robots"')[1][:80] if 'name="robots"' in head else False
    noindex = noindex or f'<link rel="canonical" href="{SITE}{path}"' not in head  # canonical variants are not indexed on their own
    body = re.search(r"<main[^>]*>(.*)</main>", html, re.S)
    main = body.group(1) if body else html
    txt = text_of(html)
    wc = len(txt.split())
    h1s = re.findall(r"<h1[^>]*>(.*?)</h1>", main, re.S)
    h1 = unescape(re.sub(r"<[^>]+>", "", h1s[0])).strip() if h1s else ""
    title = unescape((re.search(r"<title>(.*?)</title>", head, re.S) or [0, ""])[1])
    # ---------- technical
    if '<html lang="' not in html[:200]: add("html lang missing", path)
    if 'name="viewport"' not in head: add("viewport missing", path)
    if not noindex and "x-default" not in head and "hreflang" in head: add("hreflang without x-default", path)
    if "hreflang" in head and not re.search(r'hreflang="%s"' % ("fr-CA" if path.startswith("/fr") else "en-CA"), head) and not path.startswith("/fr"):
        pass
    blocking = re.findall(r"<script\b(?![^>]*(?:defer|async|type=\"application/ld\+json\"|type=\"module\"))[^>]*\bsrc=", head)
    if blocking: add("render-blocking script in <head>", path, str(len(blocking)))
    if len(re.findall(r'<link rel="stylesheet"', head)) > 2: add("more than 2 stylesheets", path)
    for im in re.findall(r"<img\b[^>]*>", main)[3:]:
        if "loading=" not in im and "fetchpriority" not in im: add("below-fold img without loading=lazy", path); break
    # ---------- on-page
    heads = [(int(m[0]), m[1]) for m in re.findall(r"<h([1-6])[^>]*>(.*?)</h\1>", main, re.S)]
    last = 0
    for lvl, _ in heads:
        if last and lvl > last + 1: add("heading level skipped (h%d -> h%d)" % (last, lvl), path); break
        last = lvl
    if heads and heads[0][0] != 1: add("first heading is not H1", path)
    kw_tokens = [w for w in re.findall(r"[a-zà-ÿ0-9]+", h1.lower()) if w not in STOP and len(w) > 2]
    first_p = re.search(r"<p[^>]*>(.*?)</p>", re.sub(r"<(nav|header)[^>]*>.*?</\1>", "", main, flags=re.S), re.S)
    fp = unescape(re.sub(r"<[^>]+>", "", first_p.group(1))).lower() if first_p else ""
    ans = re.search(r'class="[^"]*answer[^"]*"[^>]*>(.*?)</div>', main, re.S)
    first_block = (fp + " " + (unescape(re.sub(r"<[^>]+>", "", ans.group(1))).lower() if ans else ""))
    if kw_tokens and not noindex:
        hit = sum(t in first_block for t in kw_tokens) / len(kw_tokens)
        if hit < 0.5: add("H1 keywords missing from intro", path, f"({hit:.0%})")
        if hit < 0.5 or not set(kw_tokens) & set(re.findall(r"[a-zà-ÿ0-9]+", title.lower())): 
            if not set(kw_tokens) & set(re.findall(r"[a-zà-ÿ0-9]+", title.lower())): add("title shares no keyword with H1", path)
    # density of the 2-word core phrase of the title
    words = re.findall(r"[a-zà-ÿ0-9]+", txt.lower())
    if wc and not noindex and kw_tokens:
        miss = [t for t in kw_tokens if t not in set(words)]
        if miss: add("H1 keyword missing from body text", path, str(miss))
        core = " ".join(kw_tokens[:2])
        d = txt.lower().count(core) / max(wc, 1) * 100
        if d > 4: add("keyword density above 4%", path, f"'{core}' {d:.1f}%")
    internal = re.findall(r'<a [^>]*href=["\'](/[^"\'#?]*)', main)
    ext = re.findall(r'<a [^>]*href="(https?://(?!iptvmapletv)[^"]+)"', main)
    if not noindex and len(set(internal)) < 5 and path != "/thank-you/": add("fewer than 5 distinct internal links in content", path, str(len(set(internal))))
    for l in set(internal):
        l = unescape(l)
        if l.startswith(("/go/",)): continue
        if l in reds: add("link to redirect", path, l)
        elif l not in pages and l not in ASSETS and l.rstrip("/") + "/" not in pages: add("dead internal link", path, l)
    # authority links only on explanatory/legal guides
    needs_auth = path in ("/what-is-iptv/", "/is-iptv-legal-in-canada/", "/iptv-legal-canada/", "/m3u-playlist/", "/xtream-codes-iptv/", "/cord-cutting-guide/", "/iptv-buffering-fix/")
    if needs_auth and not ext: add("no outbound authority link", path)
    for e in re.findall(r'<a [^>]*href="https?://(?!iptvmapletv)[^"]+"[^>]*>', main):
        if "rel=" not in e: add("external link without rel", path); break
    # ---------- content
    money = path in ("/", "/iptv-plans-canada/", "/try-iptv-canada/", "/iptv-price/", "/best-iptv-canada/") 
    guide_like = not re.match(r"^/(fr/)?(canada|usa)/.+/.+/", path) and path not in ("/thank-you/", "/404.html", "/landing/", "/landing2/", "/landing3/", "/refer-a-friend/", "/contact/")
    if not noindex and guide_like and wc < 600 and not path.startswith(("/canada/", "/usa/", "/fr/canada", "/fr/usa", "/privacy", "/terms", "/refund")): add("under 600 words", path, f"({wc})")
    if not noindex and path not in ("/thank-you/",):
        if not re.search(r'href="/(try-iptv-canada|iptv-plans-canada|go/wa)', main): add("no conversion CTA (trial/plans/WhatsApp)", path)
        if not re.search(r"(free trial|essai gratuit|money-back|refund|remboursement|WhatsApp|support)", txt, re.I): add("no trust signal (trial/refund/support)", path)
    # near-duplicate detection on 8-word shingles of the main text
    ws = txt.lower().split()
    sh = {" ".join(ws[i:i + 8]) for i in range(0, max(len(ws) - 8, 0), 4)}
    shingles[path] = sh
    # ---------- schema vs content
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', head, re.S)
    graph = []
    for b in blocks:
        try: d = json.loads(b); graph += d.get("@graph", [d])
        except Exception: pass
    by = {n.get("@type"): n for n in graph if isinstance(n.get("@type"), str)}
    for n in graph:
        if n.get("@type") == "Article":
            for k in ("headline", "datePublished", "dateModified", "author", "publisher", "mainEntityOfPage"):
                if k not in n: add(f"Article missing {k}", path)
            if n.get("headline") and unescape(n["headline"]).strip() != h1 and h1 and unescape(re.sub(r"<[^>]+>", "", n["headline"])).strip() not in (h1, title.split(" | ")[0]):
                add("Article headline differs from H1/title", path)
        if n.get("@type") in ("Product", "Service", "Offer", "AggregateOffer"):
            pass
        if n.get("@type") == "WebPage" and n.get("url") != SITE + path: add("WebPage url != page url", path)
        if n.get("@type") == "BreadcrumbList":
            items = n.get("itemListElement", [])
            if [i.get("position") for i in items] != list(range(1, len(items) + 1)): add("breadcrumb positions not sequential", path)
            if items and items[-1].get("item") and not str(items[-1]["item"]).endswith(path) and path != "/": add("last breadcrumb != page", path)
    if path in ("/iptv-plans-canada/", "/") and not any(n.get("@type") in ("Product", "Offer", "AggregateOffer") or "offers" in n for n in graph): add("pricing page without Product/Offer schema", path)
    if path in ("/", ) and "WebSite" not in by: add("home without WebSite", path)
    if not noindex and path not in ("/", "/thank-you/") and not any(t in by for t in ("Article", "Service", "Product", "CollectionPage", "AboutPage", "ContactPage", "WebPage")): add("no WebPage/Article/Service schema", path)
    # visible price vs schema price
    for n in graph:
        offs = n.get("offers")
        if offs:
            offs = offs if isinstance(offs, list) else [offs]
            for o in offs:
                for pr in (o.get("price"), o.get("lowPrice"), o.get("highPrice")):
                    if pr and f"{float(pr):g}" not in txt.replace(",", "") and f"{float(pr):.2f}" not in txt and path != "/": add("schema price not visible on page", path, str(pr))

# near duplicates
paths = [p for p in pages if shingles[p] and 'noindex' not in pages[p][:3000] and f'rel="canonical" href="{SITE}{p}"' in pages[p][:4000]]
pairs = []
for i, a in enumerate(paths):
    for b in paths[i + 1:]:
        if re.match(r"^/(fr/)?(canada|usa)/", a) and re.match(r"^/(fr/)?(canada|usa)/", b): continue
        inter = len(shingles[a] & shingles[b]); u = min(len(shingles[a]), len(shingles[b]))
        if u > 30 and inter / u > 0.35: pairs.append((inter / u, a, b))
for r, a, b in sorted(pairs, reverse=True)[:25]: add("near-duplicate content", f"{a} <> {b}", f"{r:.0%}")

# location pages: share of text unique vs sibling pages
loc = [p for p in paths if re.match(r"^/(fr/)?(canada|usa)/[^/]+/[^/]+/$", p)]
sims = []
for i, a in enumerate(loc):
    best = max((len(shingles[a] & shingles[b]) / max(len(shingles[a]), 1) for b in loc if b != a), default=0)
    sims.append((best, a))
hi = [s for s in sims if s[0] > 0.6]
if hi: add("city pages > 60% shared text with a sibling", f"{len(hi)} of {len(loc)}", f"worst {max(hi)[1]} {max(hi)[0]:.0%}")

total = 0
for k, v in sorted(issues.items(), key=lambda kv: -len(kv[1])):
    total += len(v)
    print(f"{len(v):4d}  {k}")
    for x in v[: (len(v) if V else 5)]: print("        ", x)
print("total findings:", total, "| pages:", len(pages))
