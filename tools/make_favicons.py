"""Render every favicon / app icon size from src/static/favicon.svg (the single source of truth).
Requires cairosvg and Pillow. Usage: python tools/make_favicons.py"""
import io
import os

import cairosvg
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC = os.path.join(ROOT, "src", "static")
SVG = os.path.join(STATIC, "favicon.svg")
OUT = os.path.join(STATIC, "brand")


def render(size, full_bleed=False):
    svg = open(SVG, encoding="utf-8").read()
    if full_bleed:  # iOS applies their own rounding, so fill the corners
        svg = svg.replace('rx="14"', 'rx="0"')
    png = cairosvg.svg2png(bytestring=svg.encode(), output_width=size, output_height=size)
    return Image.open(io.BytesIO(png)).convert("RGBA")


for size, name in ((32, "favicon-32.png"), (192, "icon-192.png"), (512, "icon-512.png")):
    render(size).save(os.path.join(OUT, name), optimize=True)
render(180, full_bleed=True).convert("RGB").save(os.path.join(OUT, "apple-touch-icon.png"), optimize=True)

# favicon.ico: each size rendered natively rather than downscaled, so 16px stays crisp
ico = [render(s) for s in (16, 32, 48)]
ico[-1].save(os.path.join(STATIC, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)], append_images=ico[:-1])
print("ok")
