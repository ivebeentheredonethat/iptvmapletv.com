"""Mirror iptvmapletv.com (WordPress) into ./site as static files.

Usage: python tools/mirror.py
"""
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from html import unescape

HOST = "iptvmapletv.com"
ORIGIN = f"https://{HOST}"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "site")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"

SKIP = re.compile(r"^/(wp-admin|wp-json|xmlrpc\.php|wp-login\.php|feed|comments/feed|cdn-cgi|\?)|/feed/?$|/embed/?$")
ASSET_EXT = re.compile(r"\.(css|js|png|jpe?g|gif|webp|svg|ico|woff2?|ttf|eot|otf|mp4|webm|json|pdf|avif)$", re.I)


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


opener = urllib.request.build_opener(NoRedirect)
redirects = {}
failed = {}


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with opener.open(req, timeout=60) as r:
            return r.status, r.headers, r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.headers, e.read() if e.code < 300 or e.code >= 400 else b""


def norm(url, base):
    url = unescape(url.strip())
    if not url or url.startswith(("data:", "mailto:", "tel:", "javascript:", "#")):
        return None
    u = urllib.parse.urlparse(urllib.parse.urljoin(base, url))
    if u.hostname not in (HOST, "www." + HOST):
        return None
    return urllib.parse.urlunparse(("https", HOST, u.path or "/", "", "", ""))


def local_path(path, is_html):
    path = urllib.parse.unquote(path)
    if is_html:
        return os.path.join(OUT, path.strip("/"), "index.html") if path.strip("/") else os.path.join(OUT, "index.html")
    return os.path.join(OUT, path.lstrip("/"))


def save(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)


def refs_in_html(html, base):
    pages, assets = set(), set()
    for m in re.finditer(r'''\b(?:href|src|data-src|poster)\s*=\s*["']([^"']+)["']''', html):
        n = norm(m.group(1), base)
        if n:
            (assets if ASSET_EXT.search(urllib.parse.urlparse(n).path) or "/wp-content/" in n or "/wp-includes/" in n else pages).add(n)
    for m in re.finditer(r'''srcset\s*=\s*["']([^"']+)["']''', html):
        for part in m.group(1).split(","):
            n = norm(part.strip().split(" ")[0], base)
            if n:
                assets.add(n)
    # URLs inside JSON / inline scripts / styles (e.g. background images, escaped slashes)
    for m in re.finditer(r'''https?:(?:\\?/){2}(?:www\.)?iptvmapletv\.com((?:\\?/[^"'\s)<>,]*)?)''', html):
        n = norm(ORIGIN + m.group(1).replace("\\/", "/"), base)
        if n and ASSET_EXT.search(urllib.parse.urlparse(n).path):
            assets.add(n)
    for m in re.finditer(r'''url\(\s*["']?([^"')]+)["']?\s*\)''', html):
        n = norm(m.group(1), base)
        if n:
            assets.add(n)
    return pages, assets


def refs_in_css(css, base):
    out = set()
    for m in re.finditer(r'''url\(\s*["']?([^"')]+)["']?\s*\)|@import\s+["']([^"']+)["']''', css):
        n = norm(m.group(1) or m.group(2), base)
        if n:
            out.add(n)
    return out


def get_asset(url):
    path = urllib.parse.urlparse(url).path
    dest = local_path(path, False)
    if os.path.exists(dest):
        data = open(dest, "rb").read()
        status = 200
    else:
        status, headers, data = fetch(url)
        if status in (301, 302, 307, 308):
            loc = norm(headers.get("Location", ""), url)
            redirects[path] = loc
            return set([loc]) if loc else set()
        if status != 200:
            failed[url] = status
            return set()
        save(dest, data)
    if path.endswith(".css"):
        return refs_in_css(data.decode("utf-8", "replace"), url)
    return set()


def get_page(url):
    path = urllib.parse.urlparse(url).path
    status, headers, data = fetch(url)
    if status in (301, 302, 307, 308):
        loc = headers.get("Location", "")
        redirects[path] = loc
        n = norm(loc, url)
        return ({n} if n else set()), set()
    if status != 200:
        failed[url] = status
        return set(), set()
    ctype = headers.get("Content-Type", "")
    if "html" not in ctype:
        save(local_path(path, False), data)
        return set(), set()
    html = data.decode("utf-8", "replace")
    save(local_path(path, True), data)
    return refs_in_html(html, url)


def main():
    seeds = [ORIGIN + "/"]
    sm = fetch(ORIGIN + "/page-sitemap.xml")[2].decode()
    seeds += re.findall(r"<loc>([^<]+)</loc>", sm)
    seeds = [s for s in seeds if "/wp-content/" not in s]
    seen_pages, seen_assets = set(), set()
    todo_pages, todo_assets = set(norm(s, ORIGIN) for s in seeds), set()
    extra = ["/robots.txt", "/favicon.ico"]
    todo_assets |= {ORIGIN + p for p in extra}

    with ThreadPoolExecutor(12) as pool:
        while todo_pages or todo_assets:
            pages = [p for p in todo_pages if p not in seen_pages and not SKIP.search(urllib.parse.urlparse(p).path)]
            seen_pages |= todo_pages
            todo_pages = set()
            for newp, newa in pool.map(get_page, pages):
                for p in newp:
                    if ASSET_EXT.search(urllib.parse.urlparse(p).path):
                        newa.add(p)
                    else:
                        todo_pages.add(p)
                todo_assets |= newa
            assets = [a for a in todo_assets if a not in seen_assets]
            seen_assets |= todo_assets
            todo_assets = set()
            for more in pool.map(get_asset, assets):
                for m in more:
                    (todo_assets if ASSET_EXT.search(urllib.parse.urlparse(m).path) else todo_pages).add(m)
            print(f"pages={len(seen_pages)} assets={len(seen_assets)}", flush=True)

    json.dump({"redirects": redirects, "failed": failed}, open(os.path.join(os.path.dirname(OUT), "tools", "mirror-report.json"), "w"), indent=2)
    print("redirects:", len(redirects), "failed:", len(failed))


if __name__ == "__main__":
    sys.exit(main())
