"""One-time: build the transparent logo mark and the social share image from the
original logo. Requires Pillow. Usage: python tools/make_brand_assets.py [path/to/Sora-800.ttf path/to/Inter-500.ttf]"""
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC = os.path.join(ROOT, "src", "static")
LOGO = os.path.join(STATIC, "images", "2024", "12", "Untitled-design-6-png.webp")
OUT = os.path.join(STATIC, "brand")
os.makedirs(OUT, exist_ok=True)


def knock_out_black(im):
    """The source logo sits on pure black: turn darkness into transparency."""
    im = im.convert("RGBA")
    px = im.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b, _ = px[x, y]
            a = max(r, g, b)
            a = 0 if a < 18 else min(255, int((a - 18) * 1.6))
            if a == 0:
                px[x, y] = (0, 0, 0, 0)
            else:
                k = 255 / max(a, 1)
                px[x, y] = (min(255, int(r * k)), min(255, int(g * k)), min(255, int(b * k)), a)
    return im


src = Image.open(LOGO)
leaf = knock_out_black(src.crop((130, 30, 894, 800)))
leaf = leaf.crop(leaf.getbbox())
side = max(leaf.size)
sq = Image.new("RGBA", (side, side), (0, 0, 0, 0))
sq.paste(leaf, ((side - leaf.width) // 2, (side - leaf.height) // 2), leaf)
sq.resize((256, 256), Image.LANCZOS).save(os.path.join(OUT, "mark.png"), optimize=True)
sq.resize((128, 128), Image.LANCZOS).save(os.path.join(OUT, "mark-128.webp"), quality=92)

# favicons and app icons are rendered from src/static/favicon.svg by tools/make_favicons.py

# 1200x630 social share image
W, H = 1200, 630
og = Image.new("RGB", (W, H), (6, 7, 11))
glow = Image.new("RGB", (W, H), (0, 0, 0))
d = ImageDraw.Draw(glow)
d.ellipse((-200, -250, 600, 450), fill=(150, 20, 45))
d.ellipse((700, 250, 1400, 900), fill=(70, 30, 150))
d.ellipse((850, -200, 1350, 250), fill=(10, 90, 120))
glow = glow.filter(ImageFilter.GaussianBlur(160))
og = Image.blend(og, glow, 0.9)
m = sq.resize((300, 300), Image.LANCZOS)
og.paste(m, (820, 165), m)
dr = ImageDraw.Draw(og)
bold = ImageFont.truetype(sys.argv[1], 92) if len(sys.argv) > 1 else ImageFont.load_default()
body = ImageFont.truetype(sys.argv[2], 34) if len(sys.argv) > 2 else ImageFont.load_default()
dr.text((80, 150), "IPTV", font=bold, fill=(255, 45, 74))
w = dr.textlength("IPTV", font=bold)
dr.text((80 + w, 150), "Maple", font=bold, fill=(34, 211, 238))
dr.text((80, 270), "The best IPTV service", font=body, fill=(245, 246, 250))
dr.text((80, 318), "in Canada for 2026", font=body, fill=(245, 246, 250))
dr.text((80, 410), "50,000+ channels · 120,000+ movies & series · 4K", font=ImageFont.truetype(sys.argv[2], 26) if len(sys.argv) > 2 else body, fill=(163, 169, 184))
og.save(os.path.join(OUT, "og-default.jpg"), quality=88, optimize=True)
print("ok")
