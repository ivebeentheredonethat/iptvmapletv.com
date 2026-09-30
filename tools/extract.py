"""Dump each WordPress page's SEO head + main content as ordered blocks (tools/content/*.json)."""
import glob
import json
import os
import re

from bs4 import BeautifulSoup, NavigableString

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "tools", "content")
os.makedirs(OUT, exist_ok=True)


def txt(el):
    return " ".join(el.get_text(" ", strip=True).split())


def clean_html(el):
    for bad in el.select("script, style"):
        bad.decompose()
    # unwrap ChatGPT-paste wrapper divs etc.
    for d in el.find_all(["div", "span"]):
        if not d.attrs.get("class") or any(c.startswith(("flex", "min-h", "markdown", "text-message")) for c in d.get("class", [])):
            d.unwrap()
    for t in el.find_all(True):
        for a in list(t.attrs):
            if a not in ("href", "src", "alt", "target", "rel"):
                del t.attrs[a]
    return re.sub(r"\s+", " ", el.decode_contents()).strip()


def blocks_of(main):
    out = []
    for w in main.select(".elementor-widget"):
        if w.find_parent(class_="elementor-widget") is not None and "elementor-widget-template" not in w.find_parent(class_="elementor-widget").get("class", []):
            continue
        cls = w.get("class", [])
        kind = next((c.replace("elementor-widget-", "") for c in cls if c.startswith("elementor-widget-") and c != "elementor-widget-container"), "?")
        if kind == "heading":
            h = w.find(re.compile("^h[1-6]$")) or w.find(["p", "div", "span"])
            if h and txt(h):
                out.append({"t": "h", "tag": h.name, "text": txt(h), "html": clean_html(h)})
        elif kind == "text-editor":
            c = w.select_one(".elementor-widget-container")
            if c and txt(c):
                out.append({"t": "text", "html": clean_html(c)})
        elif kind == "icon-list":
            out.append({"t": "list", "items": [txt(li) for li in w.select("li")]})
        elif kind == "button":
            a = w.find("a")
            if a:
                out.append({"t": "button", "text": txt(a), "href": a.get("href")})
        elif kind == "image":
            i = w.find("img")
            if i:
                out.append({"t": "img", "src": i.get("src"), "alt": i.get("alt", "")})
        elif kind == "image-carousel":
            out.append({"t": "carousel", "imgs": [[i.get("src"), i.get("alt", "")] for i in w.select("img")]})
        elif kind == "icon-box":
            out.append({"t": "iconbox", "title": txt(w.select_one(".elementor-icon-box-title") or w), "desc": txt(w.select_one(".elementor-icon-box-description") or w)})
        elif kind == "eael-adv-accordion" or kind == "accordion" or kind == "toggle" or kind == "n-accordion":
            qa = []
            for item in w.select(".eael-accordion-list, .elementor-accordion-item, .elementor-toggle-item, details"):
                q = item.select_one(".eael-accordion-tab-title, .elementor-tab-title, summary")
                a = item.select_one(".eael-accordion-content, .elementor-tab-content, [role=region]")
                if q and a:
                    qa.append([txt(q), clean_html(a)])
            out.append({"t": "faq", "items": qa})
        elif kind == "html":
            c = w.select_one(".elementor-widget-container")
            out.append({"t": "rawhtml", "text": txt(c)[:400], "raw": c.decode_contents()})
        elif kind == "elementskit-accordion":
            items = []
            for card in w.select(".elementskit-card"):
                title = card.select_one(".ekit-accordion-title")
                body = card.select_one(".elementskit-card-body")
                if title and body:
                    items.append([txt(title), clean_html(body)])
            out.append({"t": "accordion", "items": items})
        elif kind in ("shortcode", "forminator_forms") or w.select_one("form.forminator-ui"):
            f = w.select_one("form.forminator-ui")
            out.append({"t": "form", "id": f.get("data-form-id") if f else None, "labels": [txt(l) for l in w.select(".forminator-label")]})
        elif kind == "template":
            out.append({"t": "template", "id": (w.select_one("[data-elementor-id]") or {}).get("data-elementor-id")})
        elif kind in ("spacer", "divider"):
            continue
        else:
            out.append({"t": kind, "text": txt(w)[:300]})
    return out


def main():
    for f in sorted(glob.glob(os.path.join(ROOT, "site", "**", "index.html"), recursive=True)):
        slug = os.path.relpath(os.path.dirname(f), os.path.join(ROOT, "site")).replace(os.sep, "/")
        slug = "" if slug == "." else slug
        soup = BeautifulSoup(open(f, encoding="utf-8").read(), "html.parser")
        head = {
            "title": soup.title.get_text() if soup.title else "",
            "description": (soup.find("meta", attrs={"name": "description"}) or {}).get("content", ""),
            "robots": (soup.find("meta", attrs={"name": "robots"}) or {}).get("content", ""),
            "og_image": (soup.find("meta", attrs={"property": "og:image"}) or {}).get("content", ""),
            "published": (soup.find("meta", attrs={"property": "article:published_time"}) or {}).get("content", ""),
            "modified": (soup.find("meta", attrs={"property": "article:modified_time"}) or {}).get("content", ""),
        }
        main_el = soup.select_one("main .page-content") or soup.select_one("main") or soup.body
        json.dump({"slug": slug, "head": head, "blocks": blocks_of(main_el)}, open(os.path.join(OUT, (slug or "home") + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("ok")


if __name__ == "__main__":
    main()
