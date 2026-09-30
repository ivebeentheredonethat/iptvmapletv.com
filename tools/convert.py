"""One-time conversion of the raw WordPress mirror (./site) into the static site (./public).

After the migration, edit files in ./public directly; this script is kept for reference
and to redo the import from the old WordPress site if ever needed.
"""
import json
import os
import re
import shutil
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "site")
OUT = os.path.join(ROOT, "public")
HOST = "iptvmapletv.com"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/130 Safari/537.36"


def cf_decode(hexstr):
    key = int(hexstr[:2], 16)
    return "".join(chr(int(hexstr[i:i + 2], 16) ^ key) for i in range(2, len(hexstr), 2))


# Tags whose absolute URLs must stay absolute (SEO: canonical, Open Graph, Twitter, JSON-LD).
KEEP_ABSOLUTE = re.compile(
    r'<link[^>]+rel=["\']canonical["\'][^>]*>'
    r'|<meta[^>]+(?:property|name)=["\'](?:og:|twitter:|article:)[^>]*>'
    r'|<script[^>]+application/ld\+json[^>]*>.*?</script>',
    re.S,
)

REMOVE = [
    r'<link rel="alternate"[^>]*(?:rss\+xml|oembed)[^>]*/>\s*',
    r'<link rel="https://api\.w\.org/"[^>]*/>\s*',
    r'<link rel="alternate" title="JSON"[^>]*/>\s*',
    r'<link rel="EditURI"[^>]*/>\s*',
    r"<link rel='shortlink'[^>]*/>\s*",
    r'<link rel="profile" href="https://gmpg\.org/xfn/11">\s*',
    r'<meta name="generator"[^>]*>\s*',
    r"<link rel='dns-prefetch' href='//\[www\.googletagmanager\.com\]\([^)]*\)' />\s*",
    # Cloudflare injects these itself when the matching features are enabled on the zone
    r'<script data-cfasync="false" src="/cdn-cgi/scripts/[^"]*email-decode\.min\.js"></script>',
    r'<script[^>]+static\.cloudflareinsights\.com/beacon[^>]*></script>\s*',
]


def convert_html(html):
    for pat in REMOVE:
        html = re.sub(pat, "", html)

    # Cloudflare email obfuscation -> plain mailto links / text
    html = re.sub(
        r'<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="([0-9a-f]+)">\[email&#160;protected\]</a>',
        lambda m: f'<a href="mailto:{cf_decode(m.group(1))}">{cf_decode(m.group(1))}</a>',
        html,
    )
    html = re.sub(r'/cdn-cgi/l/email-protection#([0-9a-f]+)', lambda m: "mailto:" + cf_decode(m.group(1)), html)
    html = re.sub(
        r'<span class="__cf_email__" data-cfemail="([0-9a-f]+)">\[email&#160;protected\]</span>',
        lambda m: cf_decode(m.group(1)), html,
    )

    # WordPress AJAX endpoint -> Cloudflare Pages Function
    html = re.sub(r'https?:(\\?/){2}(www\.)?iptvmapletv\.com(\\?/)wp-admin(\\?/)admin-ajax\.php',
                  lambda m: (m.group(3) + "api" + m.group(3) + "ajax"), html)

    # Absolute same-site URLs -> root-relative, except in SEO tags
    kept = []

    def stash(m):
        kept.append(m.group(0).replace("http://" + HOST, "https://" + HOST))
        return f"\x00KEEP{len(kept) - 1}\x00"

    html = KEEP_ABSOLUTE.sub(stash, html)
    html = re.sub(r'https?:\\/\\/(?:www\.)?iptvmapletv\.com(?=\\/|["\'])', "", html)
    html = re.sub(r'https?://(?:www\.)?iptvmapletv\.com(?=[/"\'?#\s)]|$)', "", html)
    # an emptied href (link to the homepage) must still point somewhere
    html = re.sub(r'(href|action)=(["\'])\2', r'\1=\2/\2', html)
    html = re.sub(r"\x00KEEP(\d+)\x00", lambda m: kept[int(m.group(1))], html)
    return html


def convert_css_js(text):
    text = re.sub(r'https?:\\/\\/(?:www\.)?iptvmapletv\.com(?=\\/)', "", text)
    return re.sub(r'https?://(?:www\.)?iptvmapletv\.com(?=/)', "", text)


def fetch(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=60).read().decode()


def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    shutil.copytree(SRC, OUT, ignore=shutil.ignore_patterns("cdn-cgi"))

    for dirpath, _, files in os.walk(OUT):
        for name in files:
            p = os.path.join(dirpath, name)
            if name.endswith(".html"):
                conv = convert_html
            elif name.endswith((".css", ".js")):
                conv = convert_css_js
            else:
                continue
            with open(p, encoding="utf-8", errors="surrogateescape") as f:
                s = f.read()
            n = conv(s)
            if n != s:
                with open(p, "w", encoding="utf-8", errors="surrogateescape", newline="") as f:
                    f.write(n)

    # Sitemaps (static copies; drop the XSL stylesheet that only exists in WordPress)
    for sm in ("sitemap_index.xml", "page-sitemap.xml"):
        xml = fetch(f"https://{HOST}/{sm}")
        xml = re.sub(r"<\?xml-stylesheet[^>]*\?>\s*", "", xml)
        open(os.path.join(OUT, sm), "w", encoding="utf-8", newline="\n").write(xml)

    with open(os.path.join(OUT, "robots.txt"), "w", newline="\n") as f:
        f.write("User-agent: *\nAllow: /\n\nSitemap: https://iptvmapletv.com/sitemap_index.xml\n")

    report = json.load(open(os.path.join(ROOT, "tools", "mirror-report.json")))
    lines = ["# Old WordPress URLs -> current pages (301 = permanent)"]
    for old, new in sorted(report["redirects"].items()):
        lines.append(f"{old} {new.replace('https://' + HOST, '')} 301")
    lines += [
        "/referral/ /refer-a-friend/ 301",
        "/sitemap.xml /sitemap_index.xml 301",
        "/wp-sitemap.xml /sitemap_index.xml 301",
        "/feed/ / 301",
        "/comments/feed/ / 301",
        "/wp-login.php / 302",
        "/wp-admin/* / 302",
    ]
    with open(os.path.join(OUT, "_redirects"), "w", newline="\n") as f:
        f.write("\n".join(lines) + "\n")

    with open(os.path.join(OUT, "_headers"), "w", newline="\n") as f:
        f.write(
            "/wp-content/uploads/20*\n  Cache-Control: public, max-age=2592000\n"
            "/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n"
        )
    print("done")


if __name__ == "__main__":
    main()
