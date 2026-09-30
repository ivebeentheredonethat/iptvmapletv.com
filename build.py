"""Build the static site into ./public.   Usage: python build.py

Pure standard library (Python 3.12+). GitHub Actions runs this before every deploy.
"""
import hashlib
import json
import os
import re
import shutil
import sys
from html import unescape
from urllib.parse import unquote, urlparse

from sitegen import config as C
from sitegen import layout
from sitegen.pages import all_pages

ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC = os.path.join(ROOT, "src", "static")
OUT = os.path.join(ROOT, "public")


def write(rel, text):
    p = os.path.join(OUT, rel.lstrip("/"))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def asset_hash():
    h = hashlib.sha256()
    for rel in ("css/site.css", "js/site.js"):
        h.update(open(os.path.join(STATIC, rel), "rb").read())
    return h.hexdigest()[:10]


def sitemaps(pages):
    urls = "".join(
        f"<url><loc>{C.SITE_URL}{p.path}</loc>{f'<lastmod>{p.modified}</lastmod>' if p.modified else ''}</url>\n"
        for p in pages if p.in_sitemap and "noindex" not in p.robots)
    write("page-sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    last = max((p.modified for p in pages if p.modified), default="")
    write("sitemap_index.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                               f'<sitemap><loc>{C.SITE_URL}/page-sitemap.xml</loc><lastmod>{last}</lastmod></sitemap>\n</sitemapindex>\n')
    write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /api/\n\nSitemap: {C.SITE_URL}/sitemap_index.xml\n")


def manifest():
    write("site.webmanifest", json.dumps({
        "name": C.LEGAL_NAME, "short_name": C.NAME, "start_url": "/", "display": "standalone",
        "background_color": "#06070b", "theme_color": "#06070b",
        "icons": [{"src": "/brand/icon-192.png", "sizes": "192x192", "type": "image/png"},
                  {"src": "/brand/icon-512.png", "sizes": "512x512", "type": "image/png"}],
    }, indent=2))


def check_links():
    """Fail the build if any page links to a local file or page that doesn't exist."""
    redirects = [l.split()[0] for l in open(os.path.join(OUT, "_redirects"), encoding="utf-8") if l.strip() and not l.startswith("#")]
    bad = []
    for dirpath, _, files in os.walk(OUT):
        for f in files:
            if not f.endswith(".html"):
                continue
            html = open(os.path.join(dirpath, f), encoding="utf-8").read()
            for ref in re.findall(r'(?:href|src)="(/[^"#]*)"', html):
                path = unquote(urlparse(unescape(ref)).path)
                if path.startswith(("/api/", "/cdn-cgi/")) or path in redirects:
                    continue
                target = os.path.join(OUT, path.lstrip("/"))
                if not (os.path.isfile(target) or os.path.isfile(os.path.join(target, "index.html"))):
                    bad.append(f"{os.path.relpath(os.path.join(dirpath, f), OUT)} -> {ref}")
    return bad


def main():
    layout.ASSET_VERSION = asset_hash()
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    shutil.copytree(STATIC, OUT)

    pages = all_pages()
    seen = set()
    for p in pages:
        assert p.path not in seen, f"duplicate page {p.path}"
        seen.add(p.path)
        write(p.path + "index.html", layout.render(p))
    sitemaps(pages)
    manifest()

    bad = check_links()
    if bad:
        print("Broken internal links:\n  " + "\n  ".join(sorted(set(bad))))
        sys.exit(1)
    print(f"Built {len(pages)} pages into public/ (assets v{layout.ASSET_VERSION})")


if __name__ == "__main__":
    main()
