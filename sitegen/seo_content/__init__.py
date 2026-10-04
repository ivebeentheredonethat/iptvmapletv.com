"""All SEO landing pages, one module per cluster. Order here = order of hub cards (and which page "owns" a keyword if two list it)."""
from . import apps, apps2, cities, core, devices, fr, fr2, geo, international, sports, sports2, trust, gaps, expansion

ALL = (core.PAGES + trust.PAGES + apps.PAGES + apps2.PAGES + devices.PAGES + sports.PAGES + sports2.PAGES + gaps.PAGES + expansion.PAGES + cities.PAGES + geo.PAGES
       + international.PAGES + fr.PAGES + fr2.PAGES)

# English page <-> its French twin. hreflang annotations are added to BOTH pages (self-referencing, reciprocal, x-default = English),
# so search engines serve the right language in Canada. Only pages that are true equivalents belong here.
PAIRS = [
    ("is-iptv-legal-in-canada", "iptv-legal-canada"),
    ("iptv-price", "iptv-pas-cher"),
    ("iptv-buffering-fix", "iptv-ne-fonctionne-plus"),
    ("iptv-apps", "lecteur-iptv"),
    ("m3u-playlist", "liste-iptv-m3u"),
    ("iptv-smarters-pro", "iptv-smarters-pro-francais"),
    ("iptv-samsung-tv", "iptv-sur-samsung"),
    ("iptv-apple-tv", "iptv-sur-apple-tv-iphone"),
    ("iptv-pc-mac", "iptv-sur-pc-mac"),
    ("best-iptv-canada", "meilleur-iptv"),
    ("iptv-firestick", "iptv-sur-firestick"),
    ("tivimate", "tivimate-en-francais"),
]
from . import deep
deep.apply(ALL)
expansion.link_in(ALL)

_by = {p["slug"]: p for p in ALL}
for _en, _fr in PAIRS:
    _alt = [("en-CA", f"/{_en}/"), ("fr-CA", f"/{_fr}/")]
    _by[_en]["alternates"] = _alt
    _by[_fr]["alternates"] = _alt
