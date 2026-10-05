"""One-time: build the original transparent logo mark (mark.png, mark-128.webp) from the
original logo; no longer used on the site. Requires Pillow. Usage: python tools/make_brand_assets.py"""
import os

from PIL import Image

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

# the social share image is built from favicon.svg by tools/make_og.py
print("ok")
