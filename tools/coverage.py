"""Check how well each mapped keyword is covered by its assigned page's text. Usage: coverage.py keyword-map.xlsx"""
import re, sys, html, openpyxl
from pathlib import Path
wb = openpyxl.load_workbook(sys.argv[1]); rows = list(wb["Working list"].iter_rows(values_only=True))[1:]
def text(url):
    p = Path("public")/url.strip("/")/"index.html" if url != "/" else Path("public/index.html")
    if not p.exists(): return None
    h = p.read_text(); h = re.sub(r"<script.*?</script>|<style.*?</style>", " ", h, flags=re.S)
    return re.sub(r"[^a-z0-9à-ÿ ]+", " ", html.unescape(re.sub(r"<[^>]+>", " ", h)).lower())
def title(url):
    p = Path("public")/url.strip("/")/"index.html" if url != "/" else Path("public/index.html")
    m = re.search(r"<title>(.*?)</title>", p.read_text()); return (m.group(1) if m else "").lower()
cache = {}; out = []
for r in rows:
    kw, vol, url = r[0], r[1], r[3]
    if not url: continue
    if url not in cache: cache[url] = (text(url), title(url))
    t, ti = cache[url]
    if t is None: out.append((vol, kw, url, "MISSING PAGE")); continue
    k = re.sub(r"[^a-z0-9à-ÿ ]+", " ", kw.lower()); k = " ".join(k.split())
    n = len(re.findall(r"\b"+re.escape(k)+r"\b", t))
    toks = k.split(); allt = all(w in t.split() for w in toks)
    if n == 0: out.append((vol, kw, url, "tokens-only" if allt else "ABSENT"))
for v, k, u, s in sorted(out, key=lambda x: -x[0]): print(v, k, u, s, sep="\t")
