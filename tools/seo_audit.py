"""SEO audit for the built site.   Usage: python build.py && python tools/seo_audit.py [--verbose]

Crawls ./public like a search engine would and checks the things in the SEO checklist:
titles, descriptions, canonicals, H1s, Open Graph / Twitter, hreflang reciprocity, JSON-LD (parses, FAQPage
matches the visible FAQ), images (alt / width / height), sitemap vs. real pages, internal links
(orphans, click depth, links to redirected URLs) and thin content.

Exit code 1 if any CRITICAL problem is found, so it can also run in CI.
"""
import json
import os
import re
import sys
from collections import Counter, defaultdict, deque
from html import unescape
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "public")
SITE = "https://iptvmapletv.com"
VERBOSE = "--verbose" in sys.argv


def read(p):
    return open(p, encoding="utf-8").read()


def load_pages():
    pages = {}
    for dp, _, fs in os.walk(OUT):
        for f in fs:
            if f == "index.html":
                rel = "/" + os.path.relpath(dp, OUT).replace(os.sep, "/") + "/"
                pages[rel.replace("/./", "/") if rel != "/./" else "/"] = read(os.path.join(dp, f))
    pages["/"] = pages.pop("/./", pages.get("/", ""))
    return pages


def redirects():
    out = {}
    for line in read(os.path.join(OUT, "_redirects")).splitlines():
        parts = line.split()
        if len(parts) >= 2 and not line.startswith("#") and "*" not in parts[0] and ":" not in parts[0]:
            out[parts[0]] = parts[1]
    return out


def text_of(html):
    body = re.search(r"<main[^>]*>(.*)</main>", html, re.S)
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", body.group(1) if body else html, flags=re.S)
    return re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", t))).strip()


def main():
    pages = load_pages()
    reds = redirects()
    crit, imp, rec = defaultdict(list), defaultdict(list), defaultdict(list)
    titles, descs = defaultdict(list), defaultdict(list)
    links_out, inbound = {}, defaultdict(set)
    sitemap = set(re.findall(r"<loc>([^<]+)</loc>", read(os.path.join(OUT, "sitemap.xml"))))
    indexable = set()
    words = {}
    alt_of = {}

    pages_by_url = {SITE + k for k in pages}
    for path, html in pages.items():
        head = html[: html.index("</head>")]
        noindex = bool(re.search(r'<meta name="robots" content="[^"]*noindex', head))
        title = unescape((re.search(r"<title>(.*?)</title>", head, re.S) or [None, ""])[1])
        desc = unescape((re.search(r'<meta name="description" content="([^"]*)"', head) or [None, ""])[1])
        canon = (re.search(r'<link rel="canonical" href="([^"]+)"', head) or [None, ""])[1]
        if canon and canon != SITE + path:  # deliberate canonical variant (e.g. order pages): not indexable on its own
            if canon not in pages_by_url:
                crit["canonical points at a missing page"].append(f"{path} -> {canon}")
            noindex = True
            canon = SITE + path
        if not noindex:
            indexable.add(path)
            titles[title.lower()].append(path)
            descs[desc.lower()].append(path)
        if canon != SITE + path:
            crit["canonical missing/not self-referencing"].append(f"{path} -> {canon}")
        if not noindex and not 25 <= len(title) <= 65:
            imp["title length outside 25-65"].append(f"{path} ({len(title)})")
        if not noindex and not 70 <= len(desc) <= 165:
            imp["description length outside 70-165"].append(f"{path} ({len(desc)})")
        if len(re.findall(r"<h1[ >]", html)) != 1:
            crit["not exactly one H1"].append(path)
        for tag in ("og:title", "og:description", "og:url", "og:image", "og:image:width", "og:image:height", "og:locale", "twitter:card", "twitter:image"):
            if f'"{tag}"' not in head:
                imp[f"missing {tag}"].append(path)
        # JSON-LD
        ld_blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', head, re.S)
        graph = []
        for b in ld_blocks:
            try:
                d = json.loads(b)
                graph += d.get("@graph", [d])
            except Exception as e:
                crit["JSON-LD does not parse"].append(f"{path}: {e}")
        types = Counter(n.get("@type") for n in graph)
        if path != "/" and not noindex and "BreadcrumbList" not in types:
            imp["no BreadcrumbList"].append(path)
        faq_visible = len(re.findall(r'<details(?: open)?><summary>', html))
        if faq_visible and "FAQPage" not in types:
            imp["visible FAQ but no FAQPage schema"].append(path)
        if "FAQPage" in types:
            q_ld = [q["name"] for n in graph if n.get("@type") == "FAQPage" for q in n["mainEntity"]]
            if len(q_ld) != faq_visible:
                imp["FAQPage schema count != visible FAQ count"].append(f"{path} ({len(q_ld)} vs {faq_visible})")
        if not noindex and "FAQPage" not in types and path not in ("/thank-you/",):
            rec["indexable page without FAQPage"].append(path)
        # images
        for im in re.findall(r"<img\b[^>]*>", html):
            if " alt=" not in im:
                crit["img without alt"].append(path)
            if " width=" not in im or " height=" not in im:
                imp["img without width/height"].append(f"{path}: {im[:80]}")
        # links
        outs = set()
        for ref in re.findall(r'<a [^>]*href=["\'](/[^"\'#?]*)', html):
            ref = unescape(ref)
            outs.add(ref)
            inbound[ref].add(path)
        links_out[path] = outs
        words[path] = len(text_of(html).split())
        # anchor quality
        for a in re.findall(r"<a [^>]*>(.*?)</a>", html, re.S):
            if re.sub(r"<[^>]+>", "", a).strip().lower() in ("click here", "read more", "learn more", "here"):
                rec["generic anchor text"].append(path)
                break

    for t, ps in titles.items():
        if len(ps) > 1:
            crit["duplicate title"].append(f"{', '.join(ps[:4])} … ({len(ps)}) {t[:60]}")
    for d, ps in descs.items():
        if len(ps) > 1:
            crit["duplicate description"].append(f"{', '.join(ps[:4])} … ({len(ps)})")

    # hreflang reciprocity
    for path, html in pages.items():
        alts = re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"', html)
        for hl, href in alts:
            if hl == "x-default":
                continue
            other = urlparse(href).path
            ohtml = pages.get(other, "")
            if f'hreflang="{hl}" href="{SITE}{other}"' not in ohtml and other != path:
                crit["hreflang not reciprocal"].append(f"{path} -> {hl} {other}")
            if f'href="{SITE}{path}"' not in ohtml and other != path:
                crit["hreflang not reciprocal"].append(f"{other} does not link back to {path}")

    # sitemap
    smp = {urlparse(u).path for u in sitemap}
    for p in sorted(smp - set(pages)):
        crit["sitemap URL has no page"].append(p)
    for p in sorted(indexable - smp):
        imp["indexable page missing from sitemap"].append(p)
    for p in sorted(smp & (set(pages) - indexable)):
        crit["noindex page in sitemap"].append(p)

    # link graph
    for path, outs in links_out.items():
        for o in outs:
            if o in reds and o != "/go/wa":  # /go/wa is the intentional WhatsApp redirect
                imp["internal link points at a redirect"].append(f"{path} -> {o} -> {reds[o]}")
    depth = {"/": 0}
    q = deque(["/"])
    while q:
        cur = q.popleft()
        for o in links_out.get(cur, ()):
            if o in pages and o not in depth:
                depth[o] = depth[cur] + 1
                q.append(o)
    for p in sorted(indexable):
        n_in = len(inbound.get(p, set()) - {p})
        if p != "/" and n_in == 0:
            crit["orphan page (no internal links in)"].append(p)
        elif p != "/" and n_in < 3:
            rec["page with fewer than 3 inbound links"].append(f"{p} ({n_in})")
        if depth.get(p, 99) > 3:
            imp["deeper than 3 clicks from home"].append(f"{p} (depth {depth.get(p, 'unreachable')})")
    for p in sorted(indexable):
        if words[p] < 300 and p not in ("/thank-you/",):
            rec["thin page (<300 words)"].append(f"{p} ({words[p]})")

    def show(label, d, sev):
        total = sum(len(v) for v in d.values())
        print(f"\n{label}: {total}")
        for k, v in sorted(d.items(), key=lambda kv: -len(kv[1])):
            print(f"  {sev} {k}: {len(v)}")
            for x in v[: (len(v) if VERBOSE else 3)]:
                print(f"       {x}")

    n_idx = len(indexable)
    print(f"{len(pages)} pages, {n_idx} indexable, {len(smp)} in sitemap.xml, avg {sum(words[p] for p in indexable) // max(n_idx, 1)} words")
    dist = Counter(min(depth.get(p, 9), 9) for p in indexable)
    print("click depth:", dict(sorted(dist.items())))
    show("CRITICAL", crit, "❌")
    show("IMPORTANT", imp, "⚠️")
    show("RECOMMENDED", rec, "·")
    sys.exit(1 if crit else 0)


if __name__ == "__main__":
    main()
