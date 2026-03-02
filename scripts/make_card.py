#!/usr/bin/env python3
"""
Generate a single themed blog card image from a title.

Usage
─────
    # Auto-theme and auto-name from title (saves to img/cards/)
    python3 scripts/make_card.py "Zero Trust Architecture"

    # Custom output path
    python3 scripts/make_card.py "Zero Trust Architecture" --out img/cards/zero-trust.jpg

    # Override the auto-selected icon
    python3 scripts/make_card.py "My Post" --icon shield

    # Override the colour palette
    python3 scripts/make_card.py "My Post" --palette redteam

    # Both overrides
    python3 scripts/make_card.py "My Post" --icon skull --palette redteam

    # Preview what icon / palette would be chosen (no file written)
    python3 scripts/make_card.py "My Post" --dry

    # List all available icons
    python3 scripts/make_card.py --list-icons

    # List all available palettes
    python3 scripts/make_card.py --list-palettes
"""

import argparse
import os
import sys

# ── locate repo root & add scripts/ to path so we can import process_images ──
_scripts_dir = os.path.dirname(os.path.abspath(__file__))
_repo_root   = os.path.dirname(_scripts_dir)
sys.path.insert(0, _scripts_dir)

import process_images as _pi  # noqa: E402


# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────

def _resolve_output(title: str, out_arg: str | None) -> str:
    if out_arg:
        return os.path.join(_repo_root, out_arg) if not os.path.isabs(out_arg) else out_arg
    stem = _pi.safe_stem(title)
    return os.path.join(_pi.CARDS, f"{stem}.jpg")


def _palette_name(title: str) -> str:
    """Return the palette key that would be selected for this title."""
    tl = title.lower()
    for keywords, key in _pi.KEYWORD_PALETTE:
        if any(k in tl for k in keywords):
            return key
    return "tool"


def _icon_name(title: str) -> str:
    """Return the icon key that would be selected for this title."""
    tl = title.lower()
    for keywords, icon in _pi.ICON_KEYWORDS:
        if any(k in tl for k in keywords):
            return icon
    return "gear"


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a themed 728×469 card image from a blog post title.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    parser.add_argument(
        "title", nargs="?",
        help="Post title (quotes recommended for multi-word titles)",
    )
    parser.add_argument(
        "--out", metavar="PATH",
        help="Output path (default: img/cards/<title-stem>.jpg)",
    )
    parser.add_argument(
        "--icon", choices=sorted(_pi.ICONS.keys()), metavar="ICON",
        help="Override auto-selected icon. See --list-icons for choices.",
    )
    parser.add_argument(
        "--palette", choices=sorted(_pi.P.keys()), metavar="PALETTE",
        help="Override auto-selected colour palette. See --list-palettes.",
    )
    parser.add_argument(
        "--dry", action="store_true",
        help="Print what would be generated without writing any files.",
    )
    parser.add_argument(
        "--list-icons", action="store_true",
        help="Print all available icon names and exit.",
    )
    parser.add_argument(
        "--list-palettes", action="store_true",
        help="Print all available palette names and exit.",
    )

    args = parser.parse_args()

    # ── info commands ─────────────────────────────────────────────────────────
    if args.list_icons:
        print("Available icons:\n")
        for name in sorted(_pi.ICONS.keys()):
            print(f"  {name}")
        print()
        return

    if args.list_palettes:
        print("Available palettes:\n")
        for name in sorted(_pi.P.keys()):
            bg, mid, acc = _pi.P[name]
            print(f"  {name:12s}  bg={bg}  mid={mid}  accent={acc}")
        print()
        return

    if not args.title:
        parser.error("title is required (or use --list-icons / --list-palettes)")

    title    = args.title
    out_path = _resolve_output(title, args.out)

    chosen_icon    = args.icon    or _icon_name(title)
    chosen_palette = args.palette or _palette_name(title)

    print(f"\n  Title   : {title}")
    print(f"  Icon    : {chosen_icon}")
    print(f"  Palette : {chosen_palette}")
    print(f"  Output  : {os.path.relpath(out_path, _repo_root)}")

    if args.dry:
        print("\n  [dry run] — no file written.\n")
        return

    # ── apply overrides by monkey-patching module globals temporarily ─────────
    _saved_icon    = _pi.pick_icon
    _saved_palette = _pi.pick_palette
    _saved_dry     = _pi.DRY

    try:
        if args.icon:
            _pi.pick_icon = lambda _t: args.icon
        if args.palette:
            _pi.pick_palette = lambda _t: _pi.P[args.palette]
        _pi.DRY = False

        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        _pi.make_card_image(title, out_path)
    finally:
        _pi.pick_icon    = _saved_icon
        _pi.pick_palette = _saved_palette
        _pi.DRY          = _saved_dry

    sz = os.path.getsize(out_path) // 1024
    print(f"\n  Saved {sz} KB → {os.path.relpath(out_path, _repo_root)}\n")


if __name__ == "__main__":
    main()
