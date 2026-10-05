"""Render every favicon / app icon size from src/static/favicon.svg (the single source of truth).
The browser favicon is the bare mark; app icons put it on the site's dark tile.
Requires cairosvg and Pillow. Usage: python tools/make_favicons.py"""
import io
import os

import cairosvg
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC = os.path.join(ROOT, "src", "static")
SVG = os.path.join(STATIC, "favicon.svg")
OUT = os.path.join(STATIC, "brand")
TILE = "#0e1119"


def render(size, tile=False, full_bleed=False):
    svg = open(SVG, encoding="utf-8").read()
    if tile:  # mark at ~78% on a rounded dark tile; iOS rounds its own corners, so fill them
        rx = 0 if full_bleed else 14
        svg = svg.replace('<g transform="translate(32 32.4) scale(.0152)">',
                          f'<rect width="64" height="64" rx="{rx}" fill="{TILE}"/>'
                          '<g transform="translate(32 32.4) scale(.0119)">')
    png = cairosvg.svg2png(bytestring=svg.encode(), output_width=size, output_height=size)
    return Image.open(io.BytesIO(png)).convert("RGBA")


render(32).save(os.path.join(OUT, "favicon-32.png"), optimize=True)
for size, name in ((192, "icon-192.png"), (512, "icon-512.png")):
    render(size, tile=True).save(os.path.join(OUT, name), optimize=True)
render(180, tile=True, full_bleed=True).convert("RGB").save(os.path.join(OUT, "apple-touch-icon.png"), optimize=True)

# favicon.ico: each size rendered natively rather than downscaled, so 16px stays crisp
ico = [render(s) for s in (16, 32, 48)]
ico[-1].save(os.path.join(STATIC, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)], append_images=ico[:-1])
print("ok")
