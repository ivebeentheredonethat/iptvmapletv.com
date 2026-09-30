"""Download the webpack chunks Elementor / Pro Elements load on demand (carousels, tabs,
animations...). They are never referenced in the HTML, so the crawler can't find them.

Usage: python tools/fetch_chunks.py   (after mirror.py; writes into ./site and ./public)
"""
import os
import re
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/130 Safari/537.36"


def main():
    base = os.path.join(ROOT, "site")
    for dirpath, _, files in os.walk(base):
        for name in files:
            if "runtime" not in name or not name.endswith(".js"):
                continue
            src = open(os.path.join(dirpath, name), encoding="utf-8").read()
            rel_dir = os.path.relpath(dirpath, base).replace(os.sep, "/")
            for chunk in sorted(set(re.findall(r'"([\w.-]+\.bundle(?:\.min)?\.(?:js|css))"', src))):
                data = urllib.request.urlopen(
                    urllib.request.Request(f"https://iptvmapletv.com/{rel_dir}/{chunk}", headers={"User-Agent": UA}),
                    timeout=60,
                ).read()
                for out in ("site", "public"):
                    path = os.path.join(ROOT, out, rel_dir, chunk)
                    os.makedirs(os.path.dirname(path), exist_ok=True)
                    with open(path, "wb") as f:
                        f.write(data)
                print(rel_dir + "/" + chunk)


if __name__ == "__main__":
    main()
