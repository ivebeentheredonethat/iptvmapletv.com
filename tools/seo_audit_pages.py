"""Page-by-page SEO audit: one row per HTML page, plus a summary of every failed check.
Complements seo_audit.py (site-level) and seo_audit_deep.py (on-page/schema). Stricter limits on titles and
descriptions, social tags, hreflang self-reference, _redirects targets/chains, anchors (#id), first-100-words
keyword placement, H2 presence, duplicate H1s, schema required fields, CTA/trust placement, asset weight.

Usage: python build.py && python tools/seo_audit_pages.py [--verbose] [--csv docs/seo-audit-pages.csv]
"""
import csv, json, os, re, sys
from collections import Counter, defaultdict
from html import unescape
from urllib.parse import urlparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seo_audit import OUT, SITE, load_pages, read, text_of

V = "--verbose" in sys.argv
CSV = sys.argv[sys.argv.index("--csv") + 1] if "--csv" in sys.argv else None
pages = load_pages()
STOP = set("the a an of in on for to and or with your you is are how what best canada canadian 2026 guide vs "
           "le la les de des du en et pour avec au aux un une est".split())
LEGAL = ("/privacy/", "/terms/", "/refund-policy/", "/thank-you/", "/fr/privacy/", "/fr/terms/")
# Conversion and utility pages: no outbound links (they would send buyers away) and no long-form depth needed.
COMMERCIAL = ("/", "/iptv-plans-canada/", "/try-iptv-canada/", "/iptv-price/", "/iptv-pas-cher/", "/best-iptv-canada/",
              "/channels-list/", "/iptv-near-me/", "/iptv-sports/")
UTILITY = ("/contact/", "/refer-a-friend/")
issues = defaultdict(list)
rows = []


def strip(h):
    return re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", h))).strip()


def redirects_full():
    out = {}
    for line in read(os.path.join(OUT, "_redirects")).splitlines():
        p = line.split()
        if len(p) >= 2 and not line.startswith("#"):
            out.setdefault(p[0], []).append((p[1], p[2] if len(p) > 2 else "302"))
    return out


reds = redirects_full()
h1_seen = defaultdict(list)
for path, html in sorted(pages.items()):
    head = html[: html.index("</head>")]
    robots = (re.search(r'<meta name="robots" content="([^"]*)"', head) or [0, ""])[1]
    canon = (re.search(r'<link rel="canonical" href="([^"]+)"', head) or [0, ""])[1]
    indexable = "noindex" not in robots and canon == SITE + path
    m = re.search(r"<main[^>]*>(.*)</main>", html, re.S)
    main = m.group(1) if m else html
    txt = text_of(html)
    wc = len(txt.split())
    title = unescape((re.search(r"<title>(.*?)</title>", head, re.S) or [0, ""])[1])
    desc = unescape((re.search(r'<meta name="description" content="([^"]*)"', head) or [0, ""])[1])
    h1s = re.findall(r"<h1[^>]*>(.*?)</h1>", html, re.S)
    h1 = strip(h1s[0]) if h1s else ""
    found = []

    def f(k, extra=""):
        found.append(k)
        issues[k].append(f"{path} {extra}".strip())

    # ---------- technical
    if indexable:
        if not 30 <= len(title) <= 60: f("title not 30-60 chars", f"({len(title)}) {title}")
        if not 120 <= len(desc) <= 160: f("description not 120-160 chars", f"({len(desc)})")
        h1_seen[h1.lower()].append(path)
    if not canon: f("canonical missing")
    for tag in ("og:type", "og:site_name", "og:title", "og:description", "og:url", "og:image", "twitter:card",
                "twitter:title", "twitter:description", "twitter:image"):
        if f'"{tag}"' not in head: f(f"missing {tag}")
    ogurl = (re.search(r'property="og:url" content="([^"]+)"', head) or [0, ""])[1]
    if canon and ogurl and ogurl != canon: f("og:url differs from canonical", ogurl)
    alts = dict((hl, href) for hl, href in re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"', head))
    if alts:
        if canon not in alts.values() and indexable: f("hreflang set lacks self-reference")
        if "x-default" not in alts: f("hreflang without x-default")
        for hl in alts:
            if hl != "x-default" and not re.fullmatch(r"[a-z]{2}(-[A-Z]{2})?", hl): f("invalid hreflang code", hl)
    lang = (re.search(r'<html lang="([^"]+)"', html) or [0, ""])[1]
    if path.startswith("/fr/") and not lang.startswith("fr"): f("FR page without lang=fr")
    for s in re.findall(r"<script\b[^>]*\bsrc=[^>]*>", head):
        if "defer" not in s and "async" not in s and "module" not in s: f("render-blocking script in head", s[:60])
    for ln in re.findall(r'<link rel="stylesheet" href="(https?://[^"]+)"', head): f("third-party stylesheet", ln)
    # ---------- on-page
    if len(h1s) != 1: f("H1 count != 1", str(len(h1s)))
    heads = [int(x) for x in re.findall(r"<h([1-6])\b", main)]
    if indexable and 2 not in heads and path not in LEGAL: f("no H2 in content")
    last = 0
    for lvl in heads:
        if last and lvl > last + 1: f("heading level skipped", f"h{last}->h{lvl}"); break
        last = lvl
    kw = [w for w in re.findall(r"[a-zà-ÿ0-9]+", h1.lower()) if w not in STOP and len(w) > 1]
    body_no_h1 = re.sub(r"<(nav|script|style)[^>]*>.*?</\1>|<h1[^>]*>.*?</h1>", " ", main, flags=re.S)
    first100 = " ".join(strip(body_no_h1).lower().split()[:100])
    if indexable and kw and path not in LEGAL:
        hit = sum(t in first100 for t in kw) / len(kw)
        if hit < 0.5: f("primary keyword not in first 100 words", f"({hit:.0%}) {h1}")
    if indexable and path not in LEGAL + UTILITY and wc < 600 and not re.match(r"^/(fr/)?(canada|usa)/", path):
        f("under 600 words", f"({wc})")
    ids = set(re.findall(r'\bid="([^"]+)"', html))
    for a in set(re.findall(r'href="#([^"]+)"', main)):
        if a not in ids: f("in-page anchor to missing id", "#" + a)
    for ref in set(re.findall(r'<a [^>]*href=["\'](/[^"\'?]*)', main)):
        ref = unescape(ref)
        pth, _, frag = ref.partition("#")
        if frag and pth in pages and f'id="{frag}"' not in pages[pth]: f("link to missing #anchor on other page", ref)
    if indexable and path not in LEGAL:
        ext = re.findall(r'<a [^>]*href="(https?://(?!(?:www\.)?iptvmapletv)[^"]+)"', main)
        if not ext and not re.match(r"^/(fr/)?(canada|usa)/", path) and wc > 900 and path not in COMMERCIAL: f("long guide with no outbound link")
    # ---------- schema
    graph = []
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        try:
            d = json.loads(b)
            graph += d.get("@graph", [d])
        except Exception as e:
            f("JSON-LD parse error", str(e)[:60])
    types = Counter(n.get("@type") if isinstance(n.get("@type"), str) else "/".join(n.get("@type", [])) for n in graph)
    if indexable and not any(t in types for t in ("WebPage", "CollectionPage", "AboutPage", "ContactPage", "FAQPage")):
        f("no WebPage-type node")
    for n in graph:
        t = n.get("@type")
        if t == "FAQPage":
            for q in n.get("mainEntity", []):
                if not q.get("name") or not q.get("acceptedAnswer", {}).get("text"): f("FAQ question/answer empty")
            vis = {strip(x).lower() for x in re.findall(r"<summary>(.*?)</summary>", html, re.S)}
            for q in n.get("mainEntity", []):
                if strip(q["name"]).lower() not in vis: f("FAQ schema question not visible", q["name"][:50]); break
        if t == "Product":
            if "name" not in n: f("Product without name")
            offs = n.get("offers")
            offs = offs if isinstance(offs, list) else [offs] if offs else []
            if not offs: f("Product without offers")
            for o in offs:
                inner = o.get("offers", [o]) if o.get("@type") == "AggregateOffer" else [o]
                for k in ("priceCurrency",):
                    if k not in o: f(f"Offer missing {k}")
                if o.get("@type") == "Offer" and "price" not in o: f("Offer missing price")
                if "availability" not in o and o.get("@type") == "Offer": f("Offer missing availability")
            if "aggregateRating" in n or "review" in n: f("Product rating/review markup (check it is real)")
        if t == "Service":
            for k in ("provider", "areaServed", "name"):
                if k not in n: f(f"Service missing {k}")
        if t == "Article":
            if "image" not in n: f("Article missing image")
        if t == "BreadcrumbList":
            vis_crumbs = re.search(r'<nav[^>]*class="[^"]*crumb[^"]*"[^>]*>(.*?)</nav>', html, re.S)
            if indexable and path != "/" and not vis_crumbs: f("BreadcrumbList without visible breadcrumb")
        if "aggregateRating" in n and t != "Product": f("aggregateRating markup (check it is real)", t)
    # ---------- content
    if indexable and path not in LEGAL + UTILITY:
        tail = main[len(main) * 2 // 3:]
        if not re.search(r'href="/(try-iptv-canada|fr/essai-iptv-gratuit|iptv-plans-canada|fr/forfaits-iptv|go/wa)', tail):
            f("no CTA in last third of content")
    rows.append({"path": path, "indexable": indexable, "words": wc, "title_len": len(title), "desc_len": len(desc),
                 "h1": h1, "schema": ",".join(sorted(t for t in types if t)), "issues": "; ".join(found)})

for h, ps in h1_seen.items():
    if len(ps) > 1: issues["duplicate H1 across indexable pages"].append(f"{h[:50]}: {', '.join(ps)}")

# description templating: same first 60 chars on many indexable pages
starts = defaultdict(list)
for path, html in pages.items():
    d = (re.search(r'<meta name="description" content="([^"]*)"', html) or [0, ""])[1]
    if d: starts[unescape(d)[:60].lower()].append(path)
for s, ps in starts.items():
    if len(ps) > 3: issues["description opening shared by >3 pages"].append(f"({len(ps)}) {s}…")

# _redirects: destination exists, no chains, no page shadowed
for src, outs in reds.items():
    for dst, code in outs:
        if dst.startswith("http"): continue
        dpath = urlparse(dst).path
        if "*" in src or ":" in src or "*" in dst or ":" in dst: continue
        if dpath not in pages and not os.path.exists(os.path.join(OUT, dpath.lstrip("/"))): issues["redirect target is not a page"].append(f"{src} -> {dst}")
        if dpath in reds: issues["redirect chain"].append(f"{src} -> {dst} -> {reds[dpath][0][0]}")
        if code not in ("301", "302", "308", "200"): issues["unusual redirect status"].append(f"{src} {code}")
    if len(outs) > 1: issues["duplicate redirect source"].append(src)

# sitemap
sm = read(os.path.join(OUT, "sitemap.xml"))
locs = re.findall(r"<url>(.*?)</url>", sm, re.S)
for u in locs:
    if "<lastmod>" not in u: issues["sitemap entry without lastmod"].append(re.search(r"<loc>(.*?)</loc>", u).group(1))
# heavy assets
for dp, _, fs in os.walk(os.path.join(OUT, "images")):
    for fn in fs:
        p = os.path.join(dp, fn)
        if os.path.getsize(p) > 250_000 and fn.endswith((".jpg", ".jpeg", ".png", ".webp")):
            ref = "/" + os.path.relpath(p, OUT)
            if any(ref in h for h in pages.values()): issues["image over 250 KB in use"].append(f"{ref} ({os.path.getsize(p)//1024} KB)")

total = 0
for k, v in sorted(issues.items(), key=lambda kv: -len(kv[1])):
    total += len(v)
    print(f"{len(v):4d}  {k}")
    for x in v[: (len(v) if V else 4)]: print("        ", x)
print(f"total findings: {total} | pages audited: {len(pages)} | indexable: {sum(r['indexable'] for r in rows)}")
if CSV:
    with open(CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)
