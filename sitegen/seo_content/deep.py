"""Depth pass: extra sections, FAQs and related links for pages that already existed, plus one full rewrite.

Each entry of DATA (see deep_apps.py, deep_devices.py, deep_sports.py, deep_intl_fr.py) is keyed by page slug:

  replace  -> full new HTML body (used only where the old text was too thin to build on)
  add      -> HTML appended to the existing body (new sections)
  faq      -> [(question, answer_html), ...] appended to the page's FAQ
  related  -> [slug, ...] appended to the page's "Related guides"
  meta     -> {field: value} overrides for title / description / h1 / lead / answer / keywords ...
  keywords_add -> extra target keywords appended to the page's list (keyword map)
  updated  -> date shown as "Updated" (defaults to TODAY)

Pages touched here get updated="2026-10-01", which shows in "Updated …", Article schema and sitemap <lastmod>.
"""
from . import deep_apps, deep_devices, deep_gap1, deep_gap2, deep_gap3, deep_gap4, deep_gap5, deep_gap6, deep_gap7, deep_intl_fr, deep_sports

TODAY = "2026-10-01"
DATA = {}
for mod in (deep_apps, deep_devices, deep_sports, deep_intl_fr):
    for slug, entry in mod.DATA.items():
        assert slug not in DATA, f"{slug} defined twice in deep_*.py"
        DATA[slug] = entry
# The gap-pass modules (deep_gap*.py) extend entries above or add new ones: sections and lists are merged.
for mod in (deep_gap1, deep_gap2, deep_gap3, deep_gap4, deep_gap5, deep_gap6, deep_gap7):
    for slug, entry in mod.DATA.items():
        cur = DATA.setdefault(slug, {})
        for key in ("add", "replace"):
            if key in entry:
                cur[key] = (cur.get(key, "").rstrip() + "\n" + entry[key]) if key in cur else entry[key]
        for key in ("faq", "related", "keywords_add"):
            cur[key] = list(cur.get(key, [])) + list(entry.get(key, []))
        if "updated" in entry:
            cur["updated"] = entry["updated"]
        cur["meta"] = {**cur.get("meta", {}), **entry.get("meta", {})}


def apply(pages):
    by = {p["slug"]: p for p in pages}
    missing = [s for s in DATA if s not in by]
    assert not missing, f"deep.py refers to pages that do not exist: {missing}"
    for slug, d in DATA.items():
        p = by[slug]
        if "replace" in d:
            p["body"] = d["replace"]
        if "add" in d:
            p["body"] = p["body"].rstrip() + "\n" + d["add"]
        if "faq" in d:
            p["faq"] = list(p.get("faq", [])) + list(d["faq"])
        if "related" in d:
            p["related"] = list(p.get("related", [])) + [r for r in d["related"] if r not in p.get("related", [])]
        p.update(d.get("meta", {}))
        if d.get("keywords_add"):
            p["keywords"] = list(p.get("keywords", [])) + [k for k in d["keywords_add"] if k not in p.get("keywords", [])]
        p["updated"] = d.get("updated", TODAY)
    return pages
