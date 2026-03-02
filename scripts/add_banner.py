#!/usr/bin/env python3
"""
Add a fading dark banner with title text to an existing photo.

The source image is cropped to 728×469 (centre-crop) before the banner
is applied, so the output is always the correct card size.

Usage
─────
    # Basic — source + title (saves alongside source with _card suffix)
    python3 scripts/add_banner.py img/posts/photo.jpg "My Post Title"

    # Custom output path
    python3 scripts/add_banner.py img/posts/photo.jpg "My Post Title" --out img/cards/result.jpg

    # Adjust banner darkness (0.0 = transparent … 1.0 = solid black)
    python3 scripts/add_banner.py img/posts/photo.jpg "My Post Title" --opacity 0.75

    # Skip the branding footer
    python3 scripts/add_banner.py img/posts/photo.jpg "My Post Title" --no-brand

    # Preview sizing only — no file written
    python3 scripts/add_banner.py img/posts/photo.jpg "My Post Title" --dry
"""

import argparse
import os
import sys
import textwrap

from PIL import Image, ImageDraw, ImageFont

# ─────────────────────────────────────────────────────────────────────────────
# Constants
# ─────────────────────────────────────────────────────────────────────────────

WIDTH  = 728
HEIGHT = 469
BRAND  = "geekyblinder.co.uk"

_repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ─────────────────────────────────────────────────────────────────────────────
# Font loader
# ─────────────────────────────────────────────────────────────────────────────

def _load_fonts() -> tuple:
    for path in [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFNSText.ttf",
        "/System/Library/Fonts/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]:
        try:
            return (
                ImageFont.truetype(path, 26),
                ImageFont.truetype(path, 15),
            )
        except (OSError, IOError):
            pass
    d = ImageFont.load_default()
    return d, d


# ─────────────────────────────────────────────────────────────────────────────
# Core function
# ─────────────────────────────────────────────────────────────────────────────

def apply_banner(
    src_path:  str,
    title:     str,
    out_path:  str,
    opacity:   float = 0.85,
    brand:     bool  = True,
) -> None:
    """
    Crop-resize *src_path* to 728×469 and add a fading dark banner at the
    bottom containing *title* text.  Saves to *out_path* as JPEG.
    """
    img = Image.open(src_path).convert("RGB")

    # ── centre-crop to target aspect ratio ───────────────────────────────────
    src_ratio = img.width / img.height
    tgt_ratio = WIDTH / HEIGHT

    if src_ratio > tgt_ratio:
        # wider → crop left/right
        new_w = int(img.height * tgt_ratio)
        left  = (img.width - new_w) // 2
        img   = img.crop((left, 0, left + new_w, img.height))
    else:
        # taller → crop top/bottom
        new_h = int(img.width / tgt_ratio)
        top   = (img.height - new_h) // 2
        img   = img.crop((0, top, img.width, top + new_h))

    img = img.resize((WIDTH, HEIGHT), Image.LANCZOS)

    # ── gradient dark overlay at the bottom ──────────────────────────────────
    banner_h = 165
    overlay  = Image.new("RGBA", (WIDTH, banner_h), (0, 0, 0, 0))
    ov       = ImageDraw.Draw(overlay)
    for y in range(banner_h):
        a = int(255 * opacity * (y / banner_h))
        ov.line([(0, y), (WIDTH, y)], fill=(0, 0, 0, a))

    img = img.convert("RGBA")
    img.paste(overlay, (0, HEIGHT - banner_h), overlay)
    img = img.convert("RGB")

    draw = ImageDraw.Draw(img)
    font, font_sm = _load_fonts()

    # ── title text ────────────────────────────────────────────────────────────
    lines = textwrap.fill(title, width=40).split("\n")[:3]
    ty = HEIGHT - 148
    for line in lines:
        draw.text((28, ty), line, fill=(255, 255, 255), font=font)
        ty += 34

    # ── branding ─────────────────────────────────────────────────────────────
    if brand:
        draw.text((28, HEIGHT - 26), BRAND, fill=(170, 170, 195), font=font_sm)

    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    img.save(out_path, "JPEG", quality=88)


# ─────────────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────────────

def _default_out(src: str) -> str:
    """Derive a sensible default output path from the source path."""
    base, ext = os.path.splitext(src)
    # If source is in img/posts/, put output in img/cards/
    norm = src.replace("\\", "/")
    if "img/posts/" in norm:
        fname = os.path.basename(base)
        return os.path.join(_repo_root, "img", "cards", fname + ".jpg")
    return base + "_card.jpg"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Crop-resize a photo to 728×469 and add a title banner.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("image",  help="Source image path")
    parser.add_argument("title",  help="Title text to render on the banner")
    parser.add_argument(
        "--out", metavar="PATH",
        help="Output path (default: <source>_card.jpg or img/cards/<name>.jpg)",
    )
    parser.add_argument(
        "--opacity", type=float, default=0.85, metavar="0.0-1.0",
        help="Banner darkness — 0 = transparent, 1 = solid black (default: 0.85)",
    )
    parser.add_argument(
        "--no-brand", action="store_true",
        help="Omit the geekyblinder.co.uk branding line",
    )
    parser.add_argument(
        "--dry", action="store_true",
        help="Show what would happen without writing any files",
    )

    args = parser.parse_args()

    # Resolve paths relative to repo root if not absolute
    src = args.image if os.path.isabs(args.image) else os.path.join(_repo_root, args.image)
    if not os.path.isfile(src):
        sys.exit(f"Error: source image not found: {src}")

    out = args.out or _default_out(args.image)
    if not os.path.isabs(out):
        out = os.path.join(_repo_root, out)

    print(f"\n  Source  : {os.path.relpath(src, _repo_root)}")
    print(f"  Title   : {args.title}")
    print(f"  Output  : {os.path.relpath(out, _repo_root)}")
    print(f"  Opacity : {args.opacity}")
    print(f"  Brand   : {'no' if args.no_brand else 'yes'}")

    if args.dry:
        print("\n  [dry run] — no file written.\n")
        return

    apply_banner(
        src_path = src,
        title    = args.title,
        out_path = out,
        opacity  = args.opacity,
        brand    = not args.no_brand,
    )

    sz = os.path.getsize(out) // 1024
    print(f"\n  Saved {sz} KB → {os.path.relpath(out, _repo_root)}\n")


if __name__ == "__main__":
    main()
