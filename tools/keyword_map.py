"""Keyword -> page map (SEO spec steps 0.0 to 0.3).

Usage:  pip install openpyxl && python tools/keyword_map.py "Keyword_Canada.xlsx" [output.xlsx]

For every keyword in the spreadsheet it decides one of:
  EXCLUDED   targets a market we do not serve (spec 0.0.2): never turned into a page
  BRAND      is the name of another IPTV provider / unrelated site: no page (see docs/SEO.md for why)
  MAPPED     assigned to the page that targets it (existing or new), with cluster, page type and primary-keyword flag
  UNMAPPED   too vague / not worth a page: listed for review
Pages declare their own target keywords (the `keywords` list in sitegen/seo_content/*.py); this script reads those and applies
the rules below to everything not declared anywhere.
"""
import re
import sys
from collections import Counter, defaultdict

import openpyxl

sys.path.insert(0, ".")
from sitegen.pages import all_pages          # noqa: E402
from sitegen.seo_content import ALL          # noqa: E402

SRC = sys.argv[1] if len(sys.argv) > 1 else "Keyword_Canada.xlsx"
OUT = sys.argv[2] if len(sys.argv) > 2 else "docs/keyword-map.xlsx"


def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9àâçéèêëîïôûùüÿñæœ ]", "", str(s).lower())).strip()


# ----------------------------------------------------------------------------- 0.0 market exclusion (spec 0.0.2 / appendix A)
EXCLUDED = [
    ("Middle East / Arabic", r"\b(arabic|arab|arabe|arabisk|lebanese|lebanon|iraq|iran|saudi|uae|dubai|syria|kurd\w*|turk\w*|osn)\b|great bee"),
    ("Asia", r"\b(tamil\w*|desi|jio|hindi|punjabi|tashan|bangla|urdu|pakistan\w*|india\w*|cctv\d*|tfc|filipino|chinese|china|korean|japan\w*|thai|vietnam\w*|unifi|malaysia\w*|startimes)\b"),
    ("Africa", r"\b(africa\w*|dstv|gotv|nigeria\w*|ghana\w*|kenya\w*|somali\w*|ethiopia\w*|egypt\w*|morocc?o\w*|algeri\w*|tunisia\w*|supersport africa)\b"),
    ("Latin America", r"\b(latino|latin|mexic\w*|brasil|brazil\w*|colombia\w*|argentin\w*|cuba\w*|venezuela\w*)\b"),
    ("Not on the approved list (Caucasus)", r"\bge imedi\b|\bimedi\b|\biptv kanali\b"),
]

# ----------------------------------------------------------------------------- known apps / devices / platforms / topics (these are NOT "other brands")
KNOWN = (r"tivimate|tivi mate|smarters?|smasters?|smarter|ib ?o|implayer|xc ?iptv|xciptv|stb ?emu|stbemu|mytvonline|siptv|sip tv|smart iptv|smartone|flix|iplay|iplaytv|"
         r"kodi|vlc|plex|emby|jellyfin|stremio|gse|lxtream|xtream|duplecast|nanomid|ott navigator|ottnavigator|ott pro|ott tv|ottiptv|net iptv|iptvx|myiptv|"
         r"formuler|mag ?\d*|infomir|buzztv|dreamlink|tvip|onn|homatics|ugoos|tanggula|dlta|nvidia|shield|xiaomi|mi box|amazon|fire ?(stick|tv)?|firestick|"
         r"chromecast|roku|apple|samsung|tizen|lg|webos|sony|hisense|vidaa|android|google|pc|mac|macbook|laptop|windows|iphone|ipad|ps5|browser|web|chrome|"
         r"m3u8?|mu3|playlist|list|liste|epg|vod|stb|box|server|portal|player|app|apps|downloader|checker|tester|connect|control|installer|enigma2|satellite|receiver|device|"
         r"tv|ip|iptv|ip tv|television|channel|channels|canal|kanali|live|online|stream|streaming|streamer|streamers|service|services|provider|providers|supplier|reseller|resellers|resale|"
         r"subscription|subscribe|sub|plans|plan|packages|price|prix|cost|cheap|deals|promo|promotions|premium|pro|lite|max|free|trial|buy|shop|store|best|top|meilleur|meilleure|"
         r"les meilleurs|the best|good|great|fast|stable|legal|legale|légal|légale|reviews|review|reddit|trustpilot|ebay|aliexpress|alibaba|netflix|hbo|hbo max|bein|espn|sky sports|"
         r"eurosport|nba|nhl|ufc|f1|champions league|premier league|world cup|soccer|sport|sports|4k|8k|hd|full hd|canada|canadian|quebec|québec|near me|local|area|areas|world|worldwide|"
         r"global|euro|europe|uk|france|english|french|italian|portuguese|polish|greek|romanian|ukrainian|romanesti|canale|sur|pour|a vie|lifetime|1 mois|12 mois|12 months|24|24h|24 7|"
         r"customer service|account|com|site|website|forum|iptvforum|hub|now|today|wifi|mobile|dvr|series|rive nord|orange|freebox|soccer|dazn|pluto|jio|ctv|cbc|tnt|tvzon|strymtv|"
         r"for beginners|what is it|areas|sim|formula|extra|plus|one|digital|media|local|secured|lite|lecteur|comparatif|sans coupure|fiable|bloqué|bloque|ne fonctionne plus|"
         r"cle|cle amazon|cle iptv amazon|stick|set|set top|top box|private|paid|new|real|hot|full|all")

MAP_RULES = [  # (regex, target url). First match wins. Applied to keywords no page declares.
    (r"tivimate|tivi mate", "/tivimate/"),
    (r"smart ?iptv|siptv|sip ?tv|my sip", "/smart-iptv/"),
    (r"smarters? ?player ?lite|smasters? ?player ?lite|smarters? lite", "/smarters-player-lite/"),
    (r"smarters?|smasters?|smarter|ip smart|iptv smart pro|ip tv smart", "/iptv-smarters-pro/"),
    (r"smartone", "/smartone-iptv/"), (r"flix", "/flix-iptv/"), (r"iplay", "/iplaytv/"), (r"implayer", "/implayer/"),
    (r"xc ?iptv|xciptv", "/xciptv/"), (r"stb ?emu|stbemu|\bstb\b", "/stbemu/"), (r"mytvonline", "/mytvonline/"),
    (r"kodi", "/kodi-iptv/"), (r"\bvlc\b", "/vlc-iptv/"), (r"plex", "/plex-iptv/"), (r"jellyfin|emby", "/jellyfin-iptv/"), (r"stremio", "/stremio-iptv/"),
    (r"xtream|lxtream", "/xtream-codes-iptv/"), (r"m3u|mu3|playlist|play list|liste|\blist\b", "/m3u-playlist/"),
    (r"formuler", "/formuler-iptv/"), (r"\bmag\b|mag ?\d{3}|infomir", "/mag-box-iptv/"),
    (r"\bbox\b|set top|dreamlink|buzztv|tvip|homatics|ugoos|tanggula|dlta|\bonn\b", "/iptv-box/"),
    (r"nvidia|shield|xiaomi|mi box|android tv|google tv|hisense|sony|vidaa", "/iptv-android-tv/"),
    (r"samsung|tizen", "/iptv-samsung-tv/"), (r"\blg\b|webos", "/iptv-lg-tv/"), (r"apple", "/iptv-apple-tv/"), (r"roku", "/iptv-roku/"),
    (r"fire ?stick|fire tv|amazon|\bstick\b", "/iptv-firestick/"), (r"chromecast", "/iptv-chromecast/"),
    (r"iphone|ipad|mobile", "/iptv-iphone/"), (r"\bpc\b|\bmac\b|macbook|laptop|windows", "/iptv-pc-mac/"),
    (r"nhl|hockey", "/nhl-iptv/"), (r"ufc", "/ufc-iptv/"), (r"nba", "/nba-iptv/"), (r"\bf1\b|formula", "/f1-iptv/"),
    (r"premier league|sky sports", "/premier-league-iptv/"), (r"champions league|world cup|eurosport", "/champions-league-iptv/"),
    (r"bein|dazn", "/bein-sports-iptv/"), (r"espn", "/espn-iptv/"), (r"soccer|sport", "/iptv-sports/"),
    (r"4k|8k|\bhd\b|full hd|premium", "/4k-iptv/"),
    (r"free trial|trial|essai", "/try-iptv-canada/"), (r"subscri|buy|\bplans?\b|packages|abonnement", "/iptv-plans-canada/"),
    (r"price|prix|cost|cheap|deal|promo|pas cher|lifetime|a vie", "/iptv-price/"),
    (r"provider|supplier|reseller|resale|top|best|meilleur|service|shop|store", "/best-iptv-canada/"),
    (r"legal|légal|legale", "/is-iptv-legal-in-canada/"), (r"reddit|trustpilot|forum|review", "/iptv-reddit/"),
    (r"server|portal|line|connect|control", "/iptv-server/"), (r"online|web|browser|chrome|site|checker|tester|viewer", "/watch-iptv-online/"),
    (r"player|app|downloader", "/iptv-apps/"), (r"near me|local|area", "/iptv-near-me/"),
    (r"world|global|euro|international", "/iptv-international/"), (r"what is|for beginners|ip television|television", "/what-is-iptv/"),
]
FR_URL = {"/m3u-playlist/": "/liste-iptv-m3u/", "/iptv-plans-canada/": "/abonnement-iptv/", "/best-iptv-canada/": "/meilleur-iptv/",
          "/iptv-price/": "/iptv-pas-cher/", "/is-iptv-legal-in-canada/": "/iptv-legal-canada/", "/iptv-apps/": "/lecteur-iptv/",
          "/iptv-buffering-fix/": "/iptv-ne-fonctionne-plus/", "/iptv-samsung-tv/": "/iptv-sur-samsung/", "/iptv-lg-tv/": "/iptv-sur-samsung/",
          "/iptv-apple-tv/": "/iptv-sur-apple-tv-iphone/", "/iptv-iphone/": "/iptv-sur-apple-tv-iphone/", "/iptv-pc-mac/": "/iptv-sur-pc-mac/",
          "/iptv-firestick/": "/iptv-sur-firestick/", "/tivimate/": "/tivimate-en-francais/", "/iptv-smarters-pro/": "/iptv-smarters-pro-francais/"}
FR_MARK = re.compile(r"\b(meilleur\w*|sur|pour|liste|légal\w*|legale|fiable|prix|pas cher|abonnement\w*|ne fonctionne plus|bloqué|sans coupure|lecteur|comparatif|"
                     r"télécharger|introuvable|ordinateur|mois|à vie|a vie|les meilleurs|le meilleur|rive nord|canale|televizija)\b")

TYPE_OF = {  # page type letters from the spec (step 3)
    "/": "D homepage", "/iptv-plans-canada/": "A subscription landing", "/try-iptv-canada/": "A subscription landing",
    "/best-iptv-canada/": "B comparison / best-of", "/iptv-providers/": "B comparison / best-of", "/iptv-near-me/": "E geo hub",
    "/canada/": "E geo hub", "/usa/": "E geo hub", "/iptv-international/": "F community hub", "/iptv-guides/": "hub",
}


def page_type(url, hub):
    if url in TYPE_OF:
        return TYPE_OF[url]
    if hub in ("usa", "canada") or url.startswith(("/usa/", "/canada/", "/fr/canada/")):
        return "E geo landing"
    if hub == "intl":
        return "F community"
    if hub in ("apps", "devices"):
        return "G device / app guide"
    if hub == "sports":
        return "C informational (sports)"
    if hub == "fr":
        return "C informational (fr-CA)"
    return "C informational / guide"


def main():
    ws = openpyxl.load_workbook(SRC, data_only=True).active
    rows = [(str(r[0]).strip(), r[1] or 0, r[2] or "") for r in ws.iter_rows(min_row=2, values_only=True) if r[0]]
    total_vol = sum(v for _, v, _ in rows)

    # who declares what: newer pages (published 2026-10-01) win over older ones, then first in site order
    owner, pages_meta = {}, {}
    for i, p in enumerate(ALL):
        url = f"/{p['slug']}/"
        pages_meta[url] = p
        newer = p.get("published", "") >= "2026-10-01"
        for k in p.get("keywords", []):
            key = norm(k)
            if key not in owner or (newer and not owner[key][1]):
                owner[key] = (url, newer)
    # core pages built in pages.py
    core = {
        "/": ["iptv canada", "canada iptv", "iptv in canada", "iptv canadian", "canadian iptv", "iptv for canada", "iptv from canada", "iptv back canada", "best iptv for canada"],
        "/iptv-plans-canada/": ["iptv subscription", "ip tv subscription", "iptv subscribe", "iptv subscription canada", "iptv sub", "buy iptv", "buy iptv online",
                                "buy iptv subscription", "iptv plans", "iptv packages", "best iptv subscription", "iptv premium subscription", "premium iptv subscription"],
        "/try-iptv-canada/": ["free trial iptv", "iptv free trial", "trial iptv", "iptv tester", "free iptv trial"],
    }
    for url, ks in core.items():
        for k in ks:
            owner[norm(k)] = (url, True)

    out_main, out_excl, out_brand, out_unmapped = [], [], [], []
    for kw, vol, intent in rows:
        n = norm(kw)
        hit = next((cat for cat, rx in EXCLUDED if re.search(rx, n)), None)
        if hit:
            out_excl.append((kw, vol, intent, hit))
            continue
        url, how = None, ""
        if n in owner:
            url, how = owner[n][0], "declared by page"
        else:
            for rx, target in MAP_RULES:
                if re.search(rx, n):
                    url, how = target, "rule"
                    break
            if url and FR_MARK.search(n) and url in FR_URL:
                url = FR_URL[url]
        if url is None or (how == "rule" and not re.fullmatch(rf"(?:{KNOWN}|[\s])+", n) and not re.search(r"\b(iptv|ip tv)\b", n)):
            if url is None or True:
                out_brand.append((kw, vol, intent, "Name of another provider, or a site we cannot truthfully write about"))
                continue
        p = pages_meta.get(url)
        out_main.append([kw, vol, intent, url, p.get("hub", "core") if p else "core", p.get("lang", "en") if p else "en", how])

    # brand check: keywords with an unknown leading token (e.g. "diablo iptv") must not have been mapped by a generic rule
    final_main, brand2 = [], []
    for row in out_main:
        kw, vol, intent, url, hub, lang, how = row
        n = norm(kw)
        toks = [t for t in re.sub(r"\b(iptv|ip tv|tv)\b", " ", n).split() if t]
        unknown = [t for t in toks if not re.fullmatch(KNOWN, t) and t not in {"iptv"}]
        if how == "rule" and unknown and not re.search(r"\b(tivimate|smarters?|smasters?|formuler|mag|stbemu|kodi|vlc|plex|samsung|lg|apple|roku|firestick|fire|amazon|android|nhl|ufc|nba|espn|bein|dazn)\b", n):
            brand2.append((kw, vol, intent, "Name of another provider / unrecognised brand: no page (see docs/SEO.md)"))
        else:
            final_main.append(row)
    out_brand += brand2

    # primary keyword per page + cluster
    by_page = defaultdict(list)
    for r in final_main:
        by_page[r[3]].append(r)
    primary = {u: max(rs, key=lambda x: x[1])[0] for u, rs in by_page.items()}
    cluster_of = {"apps": "Apps & players", "devices": "Devices & hardware", "sports": "Sports", "guides": "Guides & trust", "intl": "International communities",
                  "fr": "Québec / French (fr-CA)", "cities": "Locations", "usa": "Locations", "canada": "Locations", "core": "Core / conversion"}

    wb = openpyxl.Workbook()
    s = wb.active
    s.title = "Summary"
    ex_by = Counter()
    ex_vol = Counter()
    for _, v, _, c in out_excl:
        ex_by[c] += 1
        ex_vol[c] += v
    mapped_vol = sum(r[1] for r in final_main)
    brand_vol = sum(v for _, v, _, _ in out_brand)
    ex_total = sum(ex_vol.values())
    lines = [
        ("SEO KEYWORD MAP — Canada", ""), ("Source file", SRC), ("", ""),
        ("Keywords in spreadsheet", len(rows)), ("Total monthly volume", total_vol), ("", ""),
        ("MAPPED to a page (working list)", len(final_main)), ("   monthly volume", mapped_vol),
        ("EXCLUDED markets (step 0.0)", len(out_excl)), ("   monthly volume", ex_total),
        ("OTHER-BRAND names (no page built)", len(out_brand)), ("   monthly volume", brand_vol),
        ("", ""), ("Excluded keywords by category", ""),
    ] + [(f"   {c}", f"{ex_by[c]} keywords / {ex_vol[c]} searches") for c in ex_by] + [
        ("", ""), ("Pages that receive keywords", len(by_page)),
        ("Pages blocked (would have targeted excluded markets)", "Arabic / Tamil / Desi / Lebanese / African / Chinese / Filipino / Indian TV pages: not built"),
    ]
    for r_ in lines:
        s.append(list(r_))
    s.column_dimensions["A"].width = 58
    s.column_dimensions["B"].width = 60

    w = wb.create_sheet("Working list")
    w.append(["Keyword", "Monthly volume", "Intent", "Assigned page", "Cluster", "Page type", "Language", "Primary keyword of that page?", "How assigned"])
    for kw, vol, intent, url, hub, lang, how in sorted(final_main, key=lambda x: (x[3], -x[1])):
        w.append([kw, vol, intent, url, cluster_of.get(hub, hub), page_type(url, hub), "fr-CA" if lang == "fr" else "en-CA", "yes" if primary[url] == kw else "", how])
    for tab, data, head in (("Excluded markets", out_excl, ["Keyword", "Monthly volume", "Intent", "Reason (step 0.0.2)"]),
                            ("Other brands (no page)", out_brand, ["Keyword", "Monthly volume", "Intent", "Why no page"])):
        t = wb.create_sheet(tab)
        t.append(head)
        for r_ in sorted(data, key=lambda x: -x[1]):
            t.append(list(r_))
    pg = wb.create_sheet("Pages")
    pg.append(["URL", "Page type", "Cluster", "Language", "Primary keyword", "Keywords assigned", "Monthly volume of those keywords", "Title"])
    titles = {p.path: p.title for p in all_pages()}
    for url, rs in sorted(by_page.items(), key=lambda x: -sum(r[1] for r in x[1])):
        meta = pages_meta.get(url)
        pg.append([url, page_type(url, meta["hub"] if meta else "core"), cluster_of.get(meta["hub"] if meta else "core", ""), "fr-CA" if meta and meta.get("lang") == "fr" else "en-CA",
                   primary[url], len(rs), sum(r[1] for r in rs), titles.get(url, "")])
    for sh in wb.worksheets[1:]:
        sh.freeze_panes = "A2"
        for col, wd in zip("ABCDEFGHI", (42, 16, 14, 44, 26, 28, 12, 26, 18)):
            sh.column_dimensions[col].width = wd
    import os
    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    wb.save(OUT)
    print(f"keywords {len(rows)} ({total_vol:,} searches/mo)")
    print(f"  mapped   {len(final_main):4}  {mapped_vol:>8,}")
    print(f"  excluded {len(out_excl):4}  {ex_total:>8,}   {dict(ex_by)}")
    print(f"  brands   {len(out_brand):4}  {brand_vol:>8,}")
    print("wrote", OUT)


if __name__ == "__main__":
    main()
