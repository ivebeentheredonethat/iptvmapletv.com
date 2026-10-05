"""Build the 1200x630 social share image (src/static/brand/og-default.jpg) from the logo mark
(src/static/favicon.svg) and the site's own fonts. Requires cairosvg, Pillow, fonttools and brotli.
Usage: python tools/make_og.py"""
import io
import os

import cairosvg
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC = os.path.join(ROOT, "src", "static")


def font(name, size, weight):
    """Load a variable woff2 from src/static/fonts at a given weight."""
    tt = TTFont(os.path.join(STATIC, "fonts", name))
    tt.flavor = None
    buf = io.BytesIO()
    tt.save(buf)
    buf.seek(0)
    f = ImageFont.truetype(buf, size)
    f.set_variation_by_axes([weight])
    return f


W, H = 1200, 630
og = Image.new("RGB", (W, H), (6, 7, 11))
glow = Image.new("RGB", (W, H), (0, 0, 0))
d = ImageDraw.Draw(glow)
d.ellipse((-200, -250, 600, 450), fill=(150, 20, 45))
d.ellipse((700, 250, 1400, 900), fill=(70, 30, 150))
d.ellipse((850, -200, 1350, 250), fill=(10, 90, 120))
glow = glow.filter(ImageFilter.GaussianBlur(160))
og = Image.blend(og, glow, 0.9)

svg = open(os.path.join(STATIC, "favicon.svg"), encoding="utf-8").read()
mark = Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(), output_width=320, output_height=320))).convert("RGBA")
og.paste(mark, (820, 155), mark)

dr = ImageDraw.Draw(og)
iptv, maple = font("sora-latin.woff2", 92, 800), font("sora-latin.woff2", 92, 600)
body, small = font("inter-latin.woff2", 34, 500), font("inter-latin.woff2", 26, 400)
# wordmark filled with the same red > pink > violet > cyan gradient as the logo and header
mask = Image.new("L", (W, H), 0)
md = ImageDraw.Draw(mask)
md.text((80, 150), "IPTV", font=iptv, fill=255)
md.text((80 + md.textlength("IPTV", font=iptv), 150), "Maple", font=maple, fill=255)
x0, _, x1, _ = mask.getbbox()
stops = [(0, (255, 45, 74)), (.3, (255, 61, 127)), (.58, (163, 91, 255)), (.86, (34, 211, 238)), (1, (34, 211, 238))]
grad = Image.new("RGB", (W, H))
gd = ImageDraw.Draw(grad)
for x in range(x0, x1 + 1):
    t = (x - x0) / max(1, x1 - x0)
    (a, ca), (b, cb) = next((stops[i], stops[i + 1]) for i in range(len(stops) - 1) if t <= stops[i + 1][0])
    k = (t - a) / (b - a)
    gd.line((x, 0, x, H), fill=tuple(round(ca[j] + (cb[j] - ca[j]) * k) for j in range(3)))
og.paste(grad, (0, 0), mask)
dr.text((80, 270), "The best IPTV service", font=body, fill=(245, 246, 250))
dr.text((80, 318), "in Canada for 2026", font=body, fill=(245, 246, 250))
dr.text((80, 410), "50,000+ channels · 120,000+ movies & series · 4K", font=small, fill=(163, 169, 184))
og.save(os.path.join(STATIC, "brand", "og-default.jpg"), quality=88, optimize=True)
print("ok")
