"""Build the header/footer logo (src/static/brand/logo-animated.svg) from src/static/favicon.svg:
same mark, but the gradient loops red > pink > violet > cyan and back, sliding left to right
forever (SMIL, 6s, in step with the .brand .wm wordmark animation in site.css).
Usage: python tools/make_logo_anim.py"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC = os.path.join(ROOT, "src", "static")
PERIOD = 7400  # two leaf widths: the leaf always shows half the colour loop
STOPS = ("#ff2d4a", "#ec1f73", "#7c3aed", "#22d3ee", "#7c3aed", "#ec1f73", "#ff2d4a")

svg = open(os.path.join(STATIC, "favicon.svg"), encoding="utf-8").read()
stops = "".join(f'<stop offset="{i / (len(STOPS) - 1):.4g}" stop-color="{c}"/>' for i, c in enumerate(STOPS))
grad = (f'<linearGradient id="f" gradientUnits="userSpaceOnUse" spreadMethod="repeat" '
        f'x1="-1850" y1="0" x2="{PERIOD - 1850}" y2="0">{stops}'
        f'<animateTransform attributeName="gradientTransform" type="translate" from="-{PERIOD} 0" to="0 0" '
        f'dur="6s" repeatCount="indefinite"/></linearGradient>')
svg, n = re.subn(r'<linearGradient id="f".*?</linearGradient>', grad, svg)
assert n == 1
open(os.path.join(STATIC, "brand", "logo-animated.svg"), "w", encoding="utf-8").write(svg)
print("ok")
