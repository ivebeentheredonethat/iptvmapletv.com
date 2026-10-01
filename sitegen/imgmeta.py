"""Read image dimensions from file headers (PNG, JPEG, WebP, GIF) — stdlib only.

Used at build time to put width/height on every local <img> (prevents layout shift) and to declare og:image size.
"""
import os
import re
import struct

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC = os.path.join(ROOT, "src", "static")
_cache = {}


def _size(path):
    with open(path, "rb") as f:
        d = f.read(65536)
    if d[:8] == b"\x89PNG\r\n\x1a\n":
        return struct.unpack(">II", d[16:24])
    if d[:6] in (b"GIF87a", b"GIF89a"):
        return struct.unpack("<HH", d[6:10])
    if d[:4] == b"RIFF" and d[8:12] == b"WEBP":
        kind = d[12:16]
        if kind == b"VP8 ":
            w, h = struct.unpack("<HH", d[26:30])
            return w & 0x3FFF, h & 0x3FFF
        if kind == b"VP8L":
            b = d[21:25]
            bits = b[0] | b[1] << 8 | b[2] << 16 | b[3] << 24
            return (bits & 0x3FFF) + 1, ((bits >> 14) & 0x3FFF) + 1
        if kind == b"VP8X":
            return 1 + int.from_bytes(d[24:27], "little"), 1 + int.from_bytes(d[27:30], "little")
    if d[:2] == b"\xff\xd8":
        i = 2
        while i < len(d) - 9:
            if d[i] != 0xFF:
                i += 1
                continue
            m = d[i + 1]
            if m in (0xC0, 0xC1, 0xC2, 0xC3):
                h, w = struct.unpack(">HH", d[i + 5:i + 9])
                return w, h
            i += 2 + struct.unpack(">H", d[i + 2:i + 4])[0]
    return None


def image_size(web_path):
    """'/images/x.webp' -> (w, h) or None (missing file, SVG, unknown format)."""
    p = web_path.split("?")[0]
    if p not in _cache:
        fp = os.path.join(STATIC, p.lstrip("/"))
        try:
            _cache[p] = _size(fp) if os.path.isfile(fp) else None
        except Exception:
            _cache[p] = None
    return _cache[p]


_IMG = re.compile(r"<img\b[^>]*>")


def add_dimensions(html):
    """Add missing width/height to every local <img> (keeps ones already set)."""
    def fix(m):
        tag = m.group(0)
        src = re.search(r'\ssrc="(/[^"]+)"', tag)
        if not src:
            return tag
        has_w, has_h = re.search(r'\swidth="', tag), re.search(r'\sheight="', tag)
        if has_w and has_h:
            return tag
        size = image_size(src.group(1))
        if not size or not size[0] or not size[1]:
            return tag
        w, h = size
        if has_h and not has_w:      # e.g. height="40" only: derive the width from the aspect ratio
            hh = int(re.search(r'\sheight="(\d+)"', tag).group(1))
            return tag.replace("<img", f'<img width="{round(hh * w / h)}"', 1)
        if has_w and not has_h:
            ww = int(re.search(r'\swidth="(\d+)"', tag).group(1))
            return tag.replace("<img", f'<img height="{round(ww * h / w)}"', 1)
        return tag.replace("<img", f'<img width="{w}" height="{h}"', 1)
    return _IMG.sub(fix, html)
