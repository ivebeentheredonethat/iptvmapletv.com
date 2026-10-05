"""One-time: turn the extracted WordPress content (tools/content/*.json) into editable
source files under src/ (data JSON + HTML content fragments). Kept for reference."""
import json
import os
import re
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C = os.path.join(ROOT, "tools", "content")
SRC = os.path.join(ROOT, "src")
EMAIL = "help@iptvmapletv.com"

REDIRECTS = {}
for line in open(os.path.join(ROOT, "public", "_redirects"), encoding="utf-8"):
    parts = line.split()
    if len(parts) == 3 and not line.startswith("#") and "*" not in parts[0]:
        REDIRECTS[parts[0]] = parts[1]
REDIRECTS["/best-iptv-canada-2026/"] = "/"
REDIRECTS["/channels/"] = "/channels-list/"

images = set()


def load(slug):
    return json.load(open(os.path.join(C, slug + ".json"), encoding="utf-8"))


def fix(html):
    html = re.sub(r'<a rel="noopener"><span>\[email(?:&#160;|\xa0| )protected\]</span>(?:<span>.*?</span>)?</a>',
                  f'<a href="mailto:{EMAIL}">{EMAIL}</a>', html)
    html = re.sub(r"\[email(?:&#160;|\xa0| )protected\]", EMAIL, html)
    html = re.sub(r"https?://(?:www\.)?iptvmapletv\.com", "", html)
    html = re.sub(r'href=""', 'href="/"', html)

    def img(m):
        images.add(m.group(1))
        return "/images/" + m.group(1)

    html = re.sub(r"/wp-content/uploads/([^\"' )?]+)", img, html)
    for old, new in REDIRECTS.items():
        html = html.replace(f'href="{old}"', f'href="{new}"')
    html = html.replace("<p> </p>", "").replace("<h3> </h3>", "").replace("<p>\xa0</p>", "")
    html = re.sub(r"<!--.*?-->", "", html, flags=re.S)
    html = re.sub(r"<p>\s*</p>", "", html)
    return html.strip()


def fix_url(u):
    return fix(f'href="{u}"')[6:-1] if u else u


def meta_for(d, **extra):
    h = d["head"]
    m = {"title": h["title"], "description": h["description"], "og_image": fix_url(h["og_image"]).replace("href=", ""),
         "published": h["published"], "modified": h["modified"]}
    m.update(extra)
    return m


def write(rel, text):
    p = os.path.join(SRC, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def fragment(slug, meta, body):
    write(f"content/{slug}.html", "<!--meta\n" + json.dumps(meta, ensure_ascii=False, indent=2) + "\n-->\n" + body + "\n")


# ---------------------------------------------------------------- plans
PRODUCTS = {}
for fn in sorted(os.listdir(C)):
    d = json.load(open(os.path.join(C, fn), encoding="utf-8"))
    forms = [b for b in d["blocks"] if b["t"] == "form"]
    if not forms or forms[0]["id"] in ("1570", "3995"):
        continue
    hs = [b["text"] for b in d["blocks"] if b["t"] == "h"]
    name = hs[0]
    price = int(re.search(r"(\d+)\s*\$", [h for h in hs if "Price" in h][0]).group(1))
    months = 12 if "Year" in name or "12" in name else int(re.match(r"(\d+)", name).group(1))
    dev = re.search(r"\((\d) Devices\)", name)
    text = fix(next(b["html"] for b in d["blocks"] if b["t"] == "text"))
    img = next((b["src"] for b in d["blocks"] if b["t"] == "img"), "")
    PRODUCTS[(int(dev.group(1)) if dev else 1, months)] = {
        "slug": d["slug"], "form_id": forms[0]["id"], "price": price, "original": price * 2,
        "title": d["head"]["title"], "description": d["head"]["description"],
        "og_image": fix_url(d["head"]["og_image"]).replace("href=", ""),
        "image": fix_url(img).replace("href=", ""), "intro_html": text,
        "published": d["head"]["published"], "modified": d["head"]["modified"],
    }

plans = {
    "currency": "USD",
    "features": [
        "4K Ultra HD quality",
        "PPV, UFC, Boxing, F1 & Super Bowl",
        "NBA, NHL & NFL packages",
        "50,000+ live channels",
        "120,000+ movies & series (VOD)",
        "Movies & series updated daily",
        "Catch-up & EPG TV guide",
        "Anti-freeze technology",
        "Works on all devices",
        "100% secure & private",
        "24/7 live chat support",
    ],
    "connections": [
        {"devices": n, "plans": [dict(PRODUCTS[(n, m)], months=m) for m in (1, 6, 12)]} for n in range(1, 6)
    ],
}
write("data/plans.json", json.dumps(plans, ensure_ascii=False, indent=2) + "\n")
for (n, m), p in PRODUCTS.items():
    images.add(p["image"].replace("/images/", "")) if p["image"] else None

# ---------------------------------------------------------------- channels
d = load("channels-list")
regions, cur = [], None
for b in d["blocks"]:
    if b["t"] == "h" and b["text"].isupper() and b["text"] != "CHANNELS LIST":
        cur = {"name": b["text"].title(), "countries": []}
        regions.append(cur)
    elif b["t"] == "accordion" and cur is not None:
        for title, html in b["items"]:
            raw = re.split(r"<li>|</li>|<br\s*/?>|<p>|</p>", html)
            seen, chans = set(), []
            for piece in raw:
                t = re.sub(r"<[^>]+>", "", piece).replace("&amp;", "&").strip()
                if not t or t.startswith("#") or t.lower() == title.lower() or t in seen:
                    continue
                seen.add(t)
                chans.append(t)
            if chans:
                cur["countries"].append({"name": title.replace("​", "").strip(), "channels": chans})
write("data/channels.json", json.dumps(regions, ensure_ascii=False, indent=1) + "\n")

# ---------------------------------------------------------------- FAQ (home)
home = load("home")
faq = next(b for b in home["blocks"] if b["t"] == "faq")["items"]
faq = [{"q": q, "a": fix(a)} for q, a in faq]
for f in faq:
    f["a"] = f["a"].replace("IPTVmaple.com", "iptvmapletv.com")
write("data/faq.json", json.dumps(faq, ensure_ascii=False, indent=2) + "\n")

# ---------------------------------------------------------------- how-it-works guides
d = load("how-it-works")
guides = next(b for b in d["blocks"] if b["t"] == "accordion")["items"]
guides = [{"device": t, "html": fix(re.sub(r"<pre>(.*?)</pre>", r"<p>\1</p>", h, flags=re.S))} for t, h in guides]
write("data/setup-guides.json", json.dumps(guides, ensure_ascii=False, indent=2) + "\n")
player_html = fix(next(b for b in d["blocks"] if b["t"] == "text")["html"])
fragment("how-it-works", meta_for(d), player_html)

# ---------------------------------------------------------------- prose pages
for slug in ("about-iptvmaple", "privacy", "terms", "refund"):
    d = load(slug)
    body = fix(next(b for b in d["blocks"] if b["t"] == "text")["html"])
    heading = next(b["text"] for b in d["blocks"] if b["t"] == "h")
    fragment(slug, meta_for(d, heading=heading.title()), body)

d = load("thank-you")
fragment("thank-you", meta_for(d, robots="noindex, follow"), fix(next(b for b in d["blocks"] if b["t"] == "text")["html"]))

d = load("best-iptv-service")
fragment("best-iptv-service", meta_for(d, heading="Best IPTV Service for 2025", image="/images/2024/12/mwaretv_all_devices-min-768x461-1.webp", kind="article"),
         fix(next(b for b in d["blocks"] if b["t"] == "text")["html"]))
images.add("2024/12/mwaretv_all_devices-min-768x461-1.webp")

d = load("3-smarter-ways-to-stream-tv-without-cable-in-2025")
body = fix(next(b for b in d["blocks"] if b["t"] == "text")["html"])
body = body.replace("<p>Tired of expensive cable packages? I was too. So I tested out a few modern ways to stream live sports, movies, and shows — and here’s what I found.</p>", "", 1)
body = body.replace("<p>👉 Click here to see what I use<br/>(Works on Firestick, Smart TV, Android, and more.)</p><p>Start Watching</p>",
                    '<p>👉 <a href="/iptv-plans-canada/">See what I use</a><br/>(Works on Firestick, Smart TV, Android, and more.)</p>')
fragment("3-smarter-ways-to-stream-tv-without-cable-in-2025", meta_for(d, heading="3 Smarter Ways to Stream TV Without Cable in 2025", kind="article"), body)

d = load("cord-cutting-guide")
body = "".join(fix(b["html"]) for b in d["blocks"] if b["t"] == "text")
fragment("cord-cutting-guide", meta_for(d, heading="Cut the Cord & Stream Smarter in 2025", image="/images/2024/12/shutterstock_1921373024-1.webp", kind="landing"), body)

d = load("landing")
body = fix(d["blocks"][0]["html"])
body = re.sub(r"<p><img[^>]*/></p>", "", body)
fragment("landing", meta_for(d, heading="Cut Your Monthly Bills in 2025", image="/images/2024/12/IPTV-Smarters-Pro.jpg", kind="landing"), body.replace("<hr/><h3>Cut Your Monthly Bills in 2025 — Smarter Entertainment Awaits 🎬✨</h3>", ""))
images.add("2024/12/IPTV-Smarters-Pro.jpg")

d = load("landing3")
texts = [fix(b["html"]) for b in d["blocks"] if b["t"] == "text"]
fragment("landing3", meta_for(d, heading="The best way to Cut the Cord in 2025", subheading="Stream Live TV, Sports & Movies in 4K", image="/images/2024/12/shutterstock_1921373024-1.webp", kind="landing"), "\n".join(texts))
images.add("2024/12/shutterstock_1921373024-1.webp")

d = load("landing2")
extra = fix(d["blocks"][-1]["html"])
fragment("landing2", meta_for(d), extra)
d = load("try-iptv-canada")
fragment("try-iptv-canada", meta_for(d), fix(next(b for b in d["blocks"] if b["t"] == "text")["html"]))

# referral rules from raw html
d = load("refer-a-friend")
raw = next(b for b in d["blocks"] if b["t"] == "rawhtml")["raw"]
rules = re.findall(r"<li>(.*?)</li>", raw.split("rules-box", 1)[1], re.S)
write("data/referral.json", json.dumps({"meta": meta_for(d), "rules": [" ".join(re.sub("<[^>]+>", "", r).split()) for r in rules]}, ensure_ascii=False, indent=2) + "\n")

# page meta for hand-built pages
pm = {}
for slug in ("home", "iptv-plans-canada", "channels-list", "contact", "how-it-works", "refer-a-friend"):
    pm[slug] = meta_for(load(slug))
write("data/page-meta.json", json.dumps(pm, ensure_ascii=False, indent=2) + "\n")

# ---------------------------------------------------------------- images used anywhere in content
for b in home["blocks"]:
    for s in [b.get("src")] + [i[0] for i in b.get("imgs", [])]:
        if s and "/wp-content/uploads/" in s:
            images.add(s.split("/wp-content/uploads/")[1])
for g in guides:
    pass
images |= {
    "2024/12/Untitled-design-6-png.webp", "2024/12/Untitled-design-8-1-png.webp", "2024/12/Holiday-Gathering-iStock-1.webp",
    "2025/11/Connor-McDavid-1-png.webp", "2024/12/asset-6.png", "2025/01/Untitled-design.jpg", "2024/12/UFC.png",
    "2024/12/DAZN_Logo.svg.png", "2024/12/Peacock-logo-1536x473-1.webp", "2024/12/Logo_UEFA_Champions_League.png",
    "2024/12/TSN_Logo.svg.png", "2024/12/1-1.webp", "2024/12/5.webp", "2024/12/3.webp", "2024/12/8.webp", "2024/12/9.webp",
    "2024/12/login-1024x473-1.webp",
}
out = os.path.join(SRC, "static", "images")
missing = []
for rel in sorted(images):
    rel = rel.split("?")[0]
    s = os.path.join(ROOT, "site", "wp-content", "uploads", rel)
    if not os.path.exists(s):
        missing.append(rel)
        continue
    os.makedirs(os.path.dirname(os.path.join(out, rel)), exist_ok=True)
    shutil.copyfile(s, os.path.join(out, rel))
print("images", len(images), "missing", missing)
