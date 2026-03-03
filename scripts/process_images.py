#!/usr/bin/env python3
"""
Blog card image generator for geekyblinder.co.uk
─────────────────────────────────────────────────
Generates consistent 728×469 card images for every post, saves them to
img/cards/ and rewrites the image: front-matter field in each post.

Usage:
    python3 scripts/process_images.py          # process all posts
    python3 scripts/process_images.py --dry    # preview without writing

Design system
─────────────
• Dark gradient background keyed to topic colour
• Per-category background texture (hex grid, dot matrix, circuit, etc.)
• Large programmatic icon centred in upper area with accent ring/halo
• Corner accent shape + secondary decoration
• Semi-transparent title banner at bottom
• Consistent branding footer
"""

import os
import re
import sys
import math
import random
import textwrap
import hashlib

from PIL import Image, ImageDraw, ImageFont

# ─────────────────────────────────────────────────────────────────────────────
# Global config
# ─────────────────────────────────────────────────────────────────────────────

WIDTH    = 728
HEIGHT   = 469
SITE     = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS    = os.path.join(SITE, "img", "cards")
POSTS    = os.path.join(SITE, "_posts")
BRAND    = "geekyblinder.co.uk"
DRY      = "--dry" in sys.argv

# ─────────────────────────────────────────────────────────────────────────────
# Colour palettes  (bg, mid, accent)
# ─────────────────────────────────────────────────────────────────────────────

P = {
    "security":  ((18, 18, 38),  (45, 30,  90), (130,  70, 220)),
    "hack":      ((8,  20,  8),  (20, 65,  20), ( 50, 200,  70)),
    "redteam":   ((35, 10, 10),  (100, 25, 25), (220,  50,  50)),
    "blueteam":  ((10, 20, 50),  (25, 60, 140), ( 60, 140, 240)),
    "k8s":       ((15, 25, 55),  (30, 75, 170), ( 80, 160, 255)),
    "cloud":     ((15, 30, 50),  (30, 90, 150), ( 70, 190, 240)),
    "ai":        ((35, 10, 50),  (90, 30, 130), (200,  80, 240)),
    "devops":    ((15, 35, 45),  (30, 95, 130), ( 60, 190, 210)),
    "linux":     ((30, 22, 10),  (85, 65,  30), (195, 155,  60)),
    "data":      ((20, 35, 35),  (40, 100, 95), ( 80, 200, 185)),
    "pi":        ((45, 12, 12),  (130, 35, 35), (210,  60,  60)),
    "tool":      ((20, 30, 30),  (50, 90,  80), (100, 180, 165)),
    "people":    ((35, 25, 45),  (90, 60, 120), (180, 120, 220)),
    "mental":    ((30, 30, 50),  (70, 70, 130), (140, 140, 230)),
    "startup":   ((40, 30, 10),  (120, 85, 25), (230, 175,  50)),
    "writing":   ((25, 35, 45),  (60, 95, 130), (120, 190, 230)),
    "game":      ((30, 15, 45),  (85, 40, 130), (175,  80, 255)),
    "home":      ((30, 35, 20),  (80, 95,  50), (155, 195, 100)),
}

KEYWORD_PALETTE = [
    (["oscp", "hacker", "ctf", "phish", "social engineer", "pentest",
       "red team sim", "modern cloud hack", "hacking my way"],        "redteam"),
    (["blue team", "defend"],                                          "blueteam"),
    (["kubernetes", "k8s", "minikube", "linkerd", "helm", "scale to zero",
       "namespace", "container"],                                      "k8s"),
    (["cloud", "aws", "gcp", "s3", "cnapp", "terraform", "scheduler"], "cloud"),
    (["ai ", "aiops", "artificial", "llm", "shadow ai", "deepfake",
       "ai-assist", "ai gov", "ai hack"],                             "ai"),
    (["devops", "devsecops", "devops culture", "devops tool",
       "devsecops tool", "cicd"],                                      "devops"),
    (["linux", "distro", "tmux", "terminal"],                         "linux"),
    (["security", "cyber", "hack", "password", "auth", "oauth", "jwt",
       "zero trust", "vpn", "threat model", "harden"],                "security"),
    (["raspberry pi", "pi 5", "pi zero", "home assist", "game server"], "pi"),
    (["homelab", "home lab", "nas", "home nas"],                       "home"),
    (["startup", "ipo", "race to"],                                    "startup"),
    (["imposter", "mental", "burnout", "wellbeing", "brain"],         "mental"),
    (["empathy", "interpersonal", "soft skill", "psychological safety",
       "people ops", "boundaries"],                                   "people"),
    (["blog", "write", "obsidian", "note"],                           "writing"),
    (["game", "minecraft"],                                            "game"),
    (["gmail", "gapps", "tool", "toolbelt", "platform"],              "tool"),
    (["senior", "team lead", "lead"],                                  "people"),
    (["data", "splunk", "dynatrace", "monitoring"],                    "data"),
]

def pick_palette(title: str) -> tuple:
    tl = title.lower()
    for keywords, key in KEYWORD_PALETTE:
        if any(k in tl for k in keywords):
            return P[key]
    return P["tool"]

# ─────────────────────────────────────────────────────────────────────────────
# Background texture functions  (draw onto img RGBA layer)
# ─────────────────────────────────────────────────────────────────────────────

def _alpha_layer(w, h):
    lay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    return lay, ImageDraw.Draw(lay)

def bg_hex_grid(img, mid, accent, seed):
    """Flat-top hexagonal grid — k8s / cloud / security."""
    lay, d = _alpha_layer(WIDTH, HEIGHT)
    rng = random.Random(seed)
    col = (*[min(255, x + 25) for x in mid], 28)
    hex_r = 38
    w_step = hex_r * math.sqrt(3)
    h_step = hex_r * 1.5
    rows = int(HEIGHT / h_step) + 2
    cols = int(WIDTH  / w_step) + 2
    for row in range(-1, rows):
        for col in range(-1, cols):
            ox = (col * w_step) + (w_step / 2 if row % 2 else 0)
            oy = row * h_step
            pts = []
            for i in range(6):
                a = math.radians(30 + 60 * i)
                pts.append((ox + hex_r * math.cos(a), oy + hex_r * math.sin(a)))
            # randomly vary some hex fill opacity for depth
            a = 18 if rng.random() > 0.85 else 0
            if a:
                d.polygon(pts, fill=(*[min(255, x + 15) for x in mid], a))
            d.polygon(pts, outline=col, width=1)
    img.paste(lay, (0, 0), lay)

def bg_dot_matrix(img, mid, accent, seed):
    """Dot grid — data / tool / devops."""
    lay, d = _alpha_layer(WIDTH, HEIGHT)
    rng = random.Random(seed)
    col = (*[min(255, x + 40) for x in mid], 55)
    big = (*[min(255, x + 70) for x in accent], 70)
    spacing = 28
    for y in range(0, HEIGHT, spacing):
        for x in range(0, WIDTH, spacing):
            r = 2 if rng.random() > 0.92 else 1
            c = big if rng.random() > 0.97 else col
            d.ellipse([x - r, y - r, x + r, y + r], fill=c)
    img.paste(lay, (0, 0), lay)

def bg_scanlines(img, mid, accent, seed):
    """Horizontal scanlines — retro hacker / terminal feel."""
    lay, d = _alpha_layer(WIDTH, HEIGHT)
    col = (0, 0, 0, 35)
    for y in range(0, HEIGHT, 3):
        d.line([(0, y), (WIDTH, y)], fill=col, width=1)
    # faint hex chars scattered
    rng = random.Random(seed)
    chars = "0123456789ABCDEF"
    col2 = (*[min(255, x + 55) for x in mid], 30)
    try:
        fnt = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 11)
    except Exception:
        fnt = ImageFont.load_default()
    for _ in range(120):
        x = rng.randint(0, WIDTH - 20)
        y = rng.randint(0, HEIGHT - 20)
        txt = "".join(rng.choice(chars) for _ in range(rng.randint(2, 6)))
        d.text((x, y), txt, fill=col2, font=fnt)
    img.paste(lay, (0, 0), lay)

def bg_circuit(img, mid, accent, seed):
    """Circuit board traces — pi / homelab / hardware."""
    lay, d = _alpha_layer(WIDTH, HEIGHT)
    rng = random.Random(seed)
    col = (*[min(255, x + 35) for x in mid], 45)
    node_col = (*[min(255, x + 55) for x in accent], 60)
    grid = 32
    nodes = []
    for _ in range(28):
        x = rng.randrange(grid, WIDTH  - grid, grid)
        y = rng.randrange(grid, HEIGHT - grid, grid)
        nodes.append((x, y))
    # draw traces (horizontal/vertical L-paths)
    for i, (x1, y1) in enumerate(nodes):
        for x2, y2 in nodes[i+1:i+3]:
            if rng.random() > 0.4:
                mid_x = x1 if rng.random() > 0.5 else x2
                d.line([(x1, y1), (mid_x, y1), (mid_x, y2), (x2, y2)],
                       fill=col, width=1)
    for (x, y) in nodes:
        r = 3
        d.ellipse([x - r, y - r, x + r, y + r], fill=node_col)
    img.paste(lay, (0, 0), lay)

def bg_neural(img, mid, accent, seed):
    """Neural network nodes — AI / ML posts."""
    lay, d = _alpha_layer(WIDTH, HEIGHT)
    rng = random.Random(seed)
    layers = [
        [(100, 80 + i * 80) for i in range(4)],
        [(280, 60 + i * 70) for i in range(5)],
        [(460, 80 + i * 80) for i in range(4)],
        [(620, 100 + i * 90) for i in range(3)],
    ]
    edge_col  = (*[min(255, x + 20) for x in mid], 38)
    node_col  = (*[min(255, x + 60) for x in accent], 80)
    node_col2 = (*[min(255, x + 30) for x in mid], 100)
    for li, layer in enumerate(layers[:-1]):
        for (x1, y1) in layer:
            for (x2, y2) in layers[li + 1]:
                if rng.random() > 0.2:
                    d.line([(x1, y1), (x2, y2)], fill=edge_col, width=1)
    for layer in layers:
        for i, (x, y) in enumerate(layer):
            r = 9 if i % 2 == 0 else 7
            c = node_col if rng.random() > 0.5 else node_col2
            d.ellipse([x - r, y - r, x + r, y + r], fill=c)
            d.ellipse([x - r, y - r, x + r, y + r], outline=(*[min(255, x2 + 100) for x2 in accent], 120), width=1)
    img.paste(lay, (0, 0), lay)

def bg_code_rain(img, mid, accent, seed):
    """Faint falling code columns — redteam / hacking posts."""
    lay, d = _alpha_layer(WIDTH, HEIGHT)
    rng = random.Random(seed)
    chars = "01アイウエカキクケサシスセタチツテナニヌネ"
    try:
        fnt = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 13)
    except Exception:
        fnt = ImageFont.load_default()
    col_bright = (*[min(255, x + 100) for x in accent], 55)
    col_dim    = (*[min(255, x + 40)  for x in mid], 25)
    for col_x in range(0, WIDTH, 18):
        length = rng.randint(4, 14)
        start_y = rng.randint(-100, HEIGHT)
        for i in range(length):
            y = start_y + i * 16
            if 0 <= y < HEIGHT:
                c = col_bright if i == 0 else col_dim
                d.text((col_x, y), rng.choice(chars), fill=c, font=fnt)
    img.paste(lay, (0, 0), lay)

def bg_wavy(img, mid, accent, seed):
    """Organic wavy lines — people / mental health / soft skills."""
    lay, d = _alpha_layer(WIDTH, HEIGHT)
    rng = random.Random(seed)
    col1 = (*[min(255, x + 30) for x in mid], 35)
    col2 = (*[min(255, x + 50) for x in accent], 25)
    for wave in range(12):
        pts = []
        base_y = (wave / 12) * HEIGHT + rng.randint(-10, 10)
        amp    = rng.randint(12, 35)
        freq   = rng.uniform(0.006, 0.014)
        phase  = rng.uniform(0, math.pi * 2)
        for x in range(0, WIDTH + 1, 4):
            y = base_y + amp * math.sin(freq * x + phase)
            pts.append((x, y))
        c = col1 if wave % 3 != 0 else col2
        if len(pts) > 1:
            d.line(pts, fill=c, width=1)
    img.paste(lay, (0, 0), lay)

def bg_starburst(img, mid, accent, seed):
    """Radiating lines from vanishing point — startup / rocket."""
    lay, d = _alpha_layer(WIDTH, HEIGHT)
    rng = random.Random(seed)
    ox = WIDTH * 0.45 + rng.randint(-40, 40)
    oy = HEIGHT * 0.38 + rng.randint(-20, 20)
    col = (*[min(255, x + 25) for x in mid], 30)
    for angle in range(0, 360, 8):
        a = math.radians(angle)
        ex = ox + math.cos(a) * max(WIDTH, HEIGHT) * 1.5
        ey = oy + math.sin(a) * max(WIDTH, HEIGHT) * 1.5
        d.line([(ox, oy), (ex, ey)], fill=col, width=1)
    img.paste(lay, (0, 0), lay)

def bg_diagonal_grid(img, mid, accent, seed):
    """Diagonal hash lines — writing / blog / general."""
    lay, d = _alpha_layer(WIDTH, HEIGHT)
    col = (*[min(255, x + 20) for x in mid], 30)
    spacing = 36
    for i in range(-HEIGHT, WIDTH + HEIGHT, spacing):
        d.line([(i, 0), (i + HEIGHT, HEIGHT)],  fill=col, width=1)
        d.line([(i + HEIGHT, 0), (i, HEIGHT)],  fill=col, width=1)
    img.paste(lay, (0, 0), lay)

# Palette → background function
BG_TEXTURES = {
    "security": bg_hex_grid,
    "hack":     bg_code_rain,
    "redteam":  bg_code_rain,
    "blueteam": bg_hex_grid,
    "k8s":      bg_hex_grid,
    "cloud":    bg_hex_grid,
    "ai":       bg_neural,
    "devops":   bg_dot_matrix,
    "linux":    bg_scanlines,
    "data":     bg_dot_matrix,
    "pi":       bg_circuit,
    "tool":     bg_dot_matrix,
    "people":   bg_wavy,
    "mental":   bg_wavy,
    "startup":  bg_starburst,
    "writing":  bg_diagonal_grid,
    "game":     bg_dot_matrix,
    "home":     bg_circuit,
}

def palette_key(palette: tuple) -> str:
    for k, v in P.items():
        if v == palette:
            return k
    return "tool"

# ─────────────────────────────────────────────────────────────────────────────
# Icon drawing library
# ─────────────────────────────────────────────────────────────────────────────

def _c(color, alpha=255):
    return (*color, alpha)

def _halo(draw, cx, cy, r, color, rings=2):
    """Soft accent rings around an icon."""
    for i in range(rings):
        a = 35 - i * 12
        rr = r + 22 + i * 16
        draw.ellipse([cx - rr, cy - rr, cx + rr, cy + rr],
                     outline=(*color, a), width=1)

def icon_shield(draw, cx, cy, r, color):
    """Shield — security / zero trust / blue team."""
    pts = [
        (cx,        cy - r),
        (cx + r,    cy - r * 0.4),
        (cx + r,    cy + r * 0.2),
        (cx,        cy + r),
        (cx - r,    cy + r * 0.2),
        (cx - r,    cy - r * 0.4),
    ]
    draw.polygon(pts, outline=color, width=3)
    # tick mark
    draw.line([(cx - r*0.35, cy + r*0.05),
               (cx - r*0.05, cy + r*0.38),
               (cx + r*0.42, cy - r*0.28)], fill=color, width=4)
    # small shield badge label
    _halo(draw, cx, cy, r, color, rings=1)

def icon_padlock(draw, cx, cy, r, color):
    """Padlock — passwords / auth."""
    bx, by = r * 0.65, r * 0.55
    draw.rectangle([cx - bx, cy, cx + bx, cy + r * 1.1], outline=color, width=3)
    draw.arc([cx - bx, cy - r, cx + bx, cy + r * 0.1],
             start=0, end=180, fill=color, width=3)
    draw.ellipse([cx - r*0.15, cy + r*0.35, cx + r*0.15, cy + r*0.65], outline=color, width=2)
    # keyhole slot
    draw.line([(cx, cy + r*0.55), (cx, cy + r*0.9)], fill=color, width=2)
    _halo(draw, cx, cy, r, color, rings=1)

def icon_skull(draw, cx, cy, r, color):
    """Skull — red team / offensive hacking."""
    draw.ellipse([cx - r, cy - r, cx + r, cy + r * 0.5], outline=color, width=3)
    draw.rectangle([cx - r*0.68, cy + r*0.28, cx + r*0.68, cy + r*0.82], outline=color, width=3)
    # teeth
    for ox in [-0.38, 0, 0.38]:
        draw.rectangle([cx + ox*r - r*0.13, cy + r*0.52,
                        cx + ox*r + r*0.13, cy + r*0.82], fill=color)
    # eyes — filled with inner highlight ring
    for ox in [-0.35, 0.35]:
        ex, ey = cx + ox*r, cy - r*0.25
        er = r * 0.22
        draw.ellipse([ex - er, ey - er, ex + er, ey + er], fill=color)
        draw.ellipse([ex - er*0.4, ey - er*0.4, ex + er*0.4, ey + er*0.4],
                     fill=tuple(max(0, x - 80) for x in color))
    # nose
    draw.polygon([(cx, cy + r*0.05), (cx - r*0.12, cy + r*0.22),
                  (cx + r*0.12, cy + r*0.22)], outline=color, width=2)

def icon_target(draw, cx, cy, r, color):
    """Crosshair target — CTF / threat modelling."""
    for i, frac in enumerate([1.0, 0.68, 0.38]):
        draw.ellipse([cx - r*frac, cy - r*frac, cx + r*frac, cy + r*frac],
                     outline=color, width=3 if i == 2 else 2)
    # crosshairs with gap at center
    gap = r * 0.22
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        draw.line([(cx + dx*gap, cy + dy*gap),
                   (cx + dx*r*1.18, cy + dy*r*1.18)], fill=color, width=2)
    # center dot
    draw.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=color)

def icon_k8s(draw, cx, cy, r, color):
    """Kubernetes helm wheel."""
    spokes = 7
    outer, inner = r, r * 0.28
    draw.ellipse([cx - outer, cy - outer, cx + outer, cy + outer], outline=color, width=3)
    draw.ellipse([cx - inner, cy - inner, cx + inner, cy + inner], fill=color)
    for i in range(spokes):
        angle = math.radians(i * 360 / spokes - 90)
        x1 = cx + (inner + 3) * math.cos(angle)
        y1 = cy + (inner + 3) * math.sin(angle)
        x2 = cx + (outer - 3) * math.cos(angle)
        y2 = cy + (outer - 3) * math.sin(angle)
        draw.line([(x1, y1), (x2, y2)], fill=color, width=4)
    _halo(draw, cx, cy, r, color, rings=2)

def icon_cloud(draw, cx, cy, r, color):
    """Cloud shape with upload arrow."""
    for ox, oy, fr in [(-0.45, 0.15, 0.4), (0, -0.1, 0.55), (0.45, 0.1, 0.42)]:
        rr = r * fr
        draw.ellipse([cx + ox*r - rr, cy + oy*r - rr,
                      cx + ox*r + rr, cy + oy*r + rr], outline=color, width=3)
    draw.line([(cx - r*0.8, cy + r*0.45), (cx + r*0.8, cy + r*0.45)], fill=color, width=3)
    # upload arrow
    ax, ay = cx, cy + r*0.75
    draw.line([(ax, ay + r*0.5), (ax, ay - r*0.1)], fill=color, width=3)
    draw.line([(ax - r*0.2, ay + r*0.15), (ax, ay - r*0.1),
               (ax + r*0.2, ay + r*0.15)], fill=color, width=3)

def icon_terminal(draw, cx, cy, r, color):
    """Terminal window with actual prompt text."""
    bw, bh = r * 1.25, r * 0.95
    draw.rectangle([cx - bw, cy - bh, cx + bw, cy + bh], outline=color, width=3)
    # title bar
    bar_y = cy - bh + r*0.36
    draw.line([(cx - bw, bar_y), (cx + bw, bar_y)], fill=color, width=2)
    # traffic light dots in title bar
    for i, dot_col in enumerate([color, color, color]):
        dx = cx - bw + 14 + i * 18
        draw.ellipse([dx - 5, cy - bh + 10, dx + 5, cy - bh + 22], fill=color)
    # prompt lines
    try:
        mono = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", int(r * 0.42))
    except Exception:
        mono = ImageFont.load_default()
    lines = ["$ nmap -sV target", "$ gobuster dir ...", "$ ./exploit.py"]
    for i, ln in enumerate(lines):
        ly = bar_y + 12 + i * (int(r * 0.42) + 8)
        if ly < cy + bh - 8:
            draw.text((cx - bw + 10, ly), ln, fill=color, font=mono)
    # blinking cursor block
    cur_y = bar_y + 12 + len(lines) * (int(r * 0.42) + 8)
    if cur_y < cy + bh - 8:
        draw.rectangle([cx - bw + 10, cur_y, cx - bw + 18, cur_y + int(r*0.38)],
                       fill=color)

def icon_brain(draw, cx, cy, r, color):
    """Brain with circuit-like internal lines."""
    draw.arc([cx - r, cy - r*0.8, cx + r*0.05, cy + r*0.6],
             start=200, end=540, fill=color, width=3)
    draw.arc([cx - r*0.05, cy - r*0.8, cx + r, cy + r*0.6],
             start=-20, end=340, fill=color, width=3)
    draw.line([(cx, cy - r*0.8), (cx, cy + r*0.6)], fill=color, width=2)
    # internal folds
    for oy, sx in [(-0.3, -0.6), (0.0, 0.55), (0.25, -0.55)]:
        draw.arc([cx + sx*r - r*0.35, cy + oy*r - r*0.2,
                  cx + sx*r + r*0.35, cy + oy*r + r*0.2],
                 start=0, end=180, fill=color, width=2)
    _halo(draw, cx, cy, r, color, rings=1)

def icon_rocket(draw, cx, cy, r, color):
    """Rocket with flame trail."""
    # body
    draw.polygon([(cx, cy - r),
                  (cx + r*0.42, cy + r*0.42),
                  (cx - r*0.42, cy + r*0.42)], outline=color, width=3)
    # fins
    draw.polygon([(cx - r*0.42, cy + r*0.18), (cx - r*0.75, cy + r*0.85),
                  (cx - r*0.42, cy + r*0.52)], outline=color, width=2)
    draw.polygon([(cx + r*0.42, cy + r*0.18), (cx + r*0.75, cy + r*0.85),
                  (cx + r*0.42, cy + r*0.52)], outline=color, width=2)
    # porthole
    draw.ellipse([cx - r*0.2, cy - r*0.28, cx + r*0.2, cy + r*0.12],
                 outline=color, width=2)
    # flame  (3 teardrop lines)
    for ox in [-0.18, 0, 0.18]:
        flen = r * (0.55 if ox == 0 else 0.38)
        draw.line([(cx + ox*r, cy + r*0.42),
                   (cx + ox*r * 0.5, cy + r*0.42 + flen)],
                  fill=color, width=3 if ox == 0 else 2)

def icon_server(draw, cx, cy, r, color):
    """Server rack with LEDs and drive bays."""
    unit_h = r * 0.38
    gap    = r * 0.1
    for i in range(3):
        y = cy - r + i * (unit_h + gap)
        draw.rectangle([cx - r, y, cx + r, y + unit_h], outline=color, width=2)
        # drive bay lines
        draw.line([(cx - r*0.8, y + unit_h*0.5), (cx + r*0.4, y + unit_h*0.5)],
                  fill=color, width=1)
        # LED (filled if top unit)
        led_c = color if i == 0 else tuple(max(0, x - 60) for x in color)
        draw.ellipse([cx + r*0.6, y + unit_h*0.22,
                      cx + r*0.82, y + unit_h*0.62], fill=led_c)
    _halo(draw, cx, cy, r, color, rings=1)

def icon_network(draw, cx, cy, r, color):
    """Node mesh — service mesh / devsecops."""
    nodes = [
        (cx,        cy - r),
        (cx + r,    cy - r*0.3),
        (cx + r*0.7, cy + r*0.7),
        (cx - r*0.7, cy + r*0.7),
        (cx - r,    cy - r*0.3),
        (cx,        cy),          # centre hub
    ]
    for i, (x1, y1) in enumerate(nodes):
        for j, (x2, y2) in enumerate(nodes):
            if j > i:
                draw.line([(x1, y1), (x2, y2)], fill=color, width=1)
    nr = r * 0.18
    hub_r = r * 0.26
    for k, (nx, ny) in enumerate(nodes):
        draw.ellipse([nx - nr, ny - nr, nx + nr, ny + nr], fill=color)
        if k == len(nodes) - 1:
            draw.ellipse([nx - hub_r, ny - hub_r, nx + hub_r, ny + hub_r],
                         outline=color, width=2)

def icon_key(draw, cx, cy, r, color):
    """Key — auth / JWT / OAuth."""
    kr = r * 0.44
    draw.ellipse([cx - r - kr, cy - kr, cx - r + kr, cy + kr], outline=color, width=3)
    draw.ellipse([cx - r - kr*0.36, cy - kr*0.36,
                  cx - r + kr*0.36, cy + kr*0.36], fill=color)
    draw.line([(cx - r + kr, cy), (cx + r, cy)], fill=color, width=3)
    for ox in [r*0.22, r*0.58]:
        draw.line([(cx + ox, cy), (cx + ox, cy + r*0.42)], fill=color, width=3)
    _halo(draw, cx, cy, r, color, rings=1)

def icon_infinity(draw, cx, cy, r, color):
    """Infinity loop with arrows — DevOps / CI/CD."""
    for sign in [-1, 1]:
        ox = sign * r * 0.5
        draw.arc([cx + ox - r*0.52, cy - r*0.46, cx + ox + r*0.52, cy + r*0.46],
                 start=0 if sign == 1 else 180,
                 end=360 if sign == 1 else 540,
                 fill=color, width=4)
    for angle, ax, ay in [(0, cx + r, cy), (180, cx - r, cy)]:
        for da in [30, -30]:
            da_r = math.radians(angle + da + 180)
            draw.line([(ax, ay),
                       (ax + math.cos(da_r)*r*0.24,
                        ay + math.sin(da_r)*r*0.24)],
                      fill=color, width=3)
    _halo(draw, cx, cy, r, color, rings=1)

def icon_people(draw, cx, cy, r, color):
    """Two figures facing each other — people / empathy / culture."""
    for sign, ox in [(-1, -r*0.42), (1, r*0.42)]:
        hx, hy = cx + ox, cy - r*0.5
        hr = r * 0.24
        draw.ellipse([hx - hr, hy - hr, hx + hr, hy + hr], outline=color, width=2)
        draw.arc([hx - hr*1.7, hy + hr*0.8, hx + hr*1.7, hy + r*1.1],
                 start=0, end=180, fill=color, width=2)
    # speech bubble between them
    bx1, by1, bx2, by2 = cx - r*0.28, cy + r*0.05, cx + r*0.28, cy + r*0.5
    draw.ellipse([bx1, by1, bx2, by2], outline=color, width=2)
    # tail
    draw.polygon([(cx, by2 - 3), (cx - r*0.1, by2 + r*0.18),
                  (cx + r*0.12, by2)], outline=color, width=1)

def icon_chart(draw, cx, cy, r, color):
    """Bar chart going up — data / monitoring / metrics."""
    bars = [0.4, 0.72, 0.55, 0.9, 0.65, 0.82]
    bw   = r * 0.24
    total_w = len(bars) * (bw + r*0.08) - r*0.08
    ox = cx - total_w / 2
    for i, h in enumerate(bars):
        x   = ox + i * (bw + r*0.08)
        top = cy + r - r * 2 * h
        # bar fill (subtle)
        draw.rectangle([x, top, x + bw, cy + r],
                       fill=tuple(max(0, x2 - 100) for x2 in color),
                       outline=color, width=2)
    # axes
    draw.line([(ox - bw*0.3, cy - r), (ox - bw*0.3, cy + r + 5),
               (ox + total_w + bw*0.3, cy + r + 5)], fill=color, width=2)

def icon_gear(draw, cx, cy, r, color):
    """Cog / gear — tools / ops / automation."""
    teeth = 10
    ir, or_ = r * 0.58, r
    pts = []
    for i in range(teeth * 2):
        angle = math.radians(i * 180 / teeth)
        rad = or_ if i % 2 == 0 else ir
        pts.append((cx + rad * math.cos(angle), cy + rad * math.sin(angle)))
    draw.polygon(pts, outline=color, width=2)
    inner_r = ir * 0.5
    draw.ellipse([cx - inner_r, cy - inner_r, cx + inner_r, cy + inner_r],
                 outline=color, width=3)
    # inner cross
    draw.line([(cx - inner_r*0.6, cy), (cx + inner_r*0.6, cy)], fill=color, width=2)
    draw.line([(cx, cy - inner_r*0.6), (cx, cy + inner_r*0.6)], fill=color, width=2)

def icon_diamond(draw, cx, cy, r, color):
    """Gem — Obsidian / notes / knowledge base."""
    pts = [(cx, cy - r), (cx + r*0.7, cy - r*0.2),
           (cx + r*0.7, cy + r*0.2), (cx, cy + r),
           (cx - r*0.7, cy + r*0.2), (cx - r*0.7, cy - r*0.2)]
    draw.polygon(pts, outline=color, width=3)
    # facet lines for that gem look
    draw.line([(cx - r*0.7, cy - r*0.2), (cx, cy - r), (cx + r*0.7, cy - r*0.2)],
              fill=color, width=2)
    draw.line([(cx - r*0.7, cy - r*0.2), (cx, cy + r*0.1), (cx + r*0.7, cy - r*0.2)],
              fill=color, width=1)
    draw.line([(cx, cy - r), (cx, cy + r*0.1)], fill=color, width=1)
    draw.line([(cx - r*0.7, cy + r*0.2), (cx, cy + r*0.1), (cx + r*0.7, cy + r*0.2)],
              fill=color, width=1)

def icon_pen(draw, cx, cy, r, color):
    """Pen / quill — blog / writing."""
    draw.polygon([(cx, cy - r), (cx + r*0.28, cy), (cx, cy + r), (cx - r*0.28, cy)],
                 outline=color, width=3)
    draw.line([(cx, cy + r), (cx - r*0.55, cy + r*1.45)], fill=color, width=3)
    draw.line([(cx - r*0.55, cy + r*1.45), (cx - r*0.3, cy + r*0.95)], fill=color, width=2)
    # nib lines
    draw.line([(cx - r*0.15, cy + r*0.3), (cx + r*0.15, cy - r*0.3)],
              fill=color, width=1)
    _halo(draw, cx, cy, r, color, rings=1)

def icon_gamepad(draw, cx, cy, r, color):
    """Game controller with more detail."""
    draw.ellipse([cx - r, cy - r*0.55, cx + r, cy + r*0.55], outline=color, width=3)
    # handles
    draw.ellipse([cx - r - r*0.2, cy + r*0.1, cx - r + r*0.35, cy + r*0.75],
                 outline=color, width=2)
    draw.ellipse([cx + r - r*0.35, cy + r*0.1, cx + r + r*0.2, cy + r*0.75],
                 outline=color, width=2)
    # d-pad
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        draw.rectangle([cx - r*0.52 + dx*r*0.24 - r*0.1, cy + dy*r*0.24 - r*0.1,
                         cx - r*0.52 + dx*r*0.24 + r*0.1, cy + dy*r*0.24 + r*0.1],
                       fill=color)
    # ABXY buttons
    for bx, by, lbl in [(r*0.42, -r*0.18, "A"), (r*0.58, r*0.04, "B"),
                         (r*0.26,  r*0.04, "X"), (r*0.42, r*0.25, "Y")]:
        ex, ey = cx + bx, cy + by
        draw.ellipse([ex - r*0.1, ey - r*0.1, ex + r*0.1, ey + r*0.1], outline=color, width=2)

def icon_torch(draw, cx, cy, r, color):
    """Torch / lightbulb — learning."""
    draw.arc([cx - r*0.58, cy - r, cx + r*0.58, cy + r*0.28],
             start=30, end=150, fill=color, width=3)
    draw.line([(cx - r*0.58, cy + r*0.28), (cx - r*0.38, cy + r*0.72)],
              fill=color, width=3)
    draw.line([(cx + r*0.58, cy + r*0.28), (cx + r*0.38, cy + r*0.72)],
              fill=color, width=3)
    draw.line([(cx - r*0.38, cy + r*0.72), (cx + r*0.38, cy + r*0.72)],
              fill=color, width=3)
    # cross-hatch in bulb for filament look
    for oy in [-0.1, 0.05]:
        draw.line([(cx - r*0.3, cy + oy*r), (cx + r*0.3, cy + oy*r)],
                  fill=color, width=1)
    # rays
    for angle in range(-75, 76, 25):
        a = math.radians(angle - 90)
        x1 = cx + r * 0.7 * math.cos(a)
        y1 = cy + r * 0.7 * math.sin(a) - r*0.38
        x2 = cx + r * 1.1 * math.cos(a)
        y2 = cy + r * 1.1 * math.sin(a) - r*0.38
        draw.line([(x1, y1), (x2, y2)], fill=color, width=2)

def icon_pi(draw, cx, cy, r, color):
    """Raspberry Pi — π symbol."""
    draw.line([(cx - r, cy - r*0.4), (cx + r, cy - r*0.4)], fill=color, width=3)
    draw.arc([cx - r, cy - r*0.4, cx, cy + r], start=0, end=270, fill=color, width=3)
    draw.line([(cx + r*0.5, cy - r*0.4), (cx + r*0.5, cy + r)], fill=color, width=3)
    # decorative dots (GPIO pins feel)
    for i in range(4):
        px = cx - r + i * (r*0.65)
        draw.ellipse([px - 4, cy + r + 12, px + 4, cy + r + 22],
                     fill=color)

def icon_flag(draw, cx, cy, r, color):
    """CTF flag on a pole."""
    # pole
    draw.line([(cx - r*0.2, cy - r), (cx - r*0.2, cy + r)], fill=color, width=3)
    # flag body
    pts = [(cx - r*0.2, cy - r),
           (cx + r*0.8, cy - r*0.6),
           (cx + r*0.8, cy - r*0.1),
           (cx - r*0.2, cy + r*0.25)]
    draw.polygon(pts, outline=color, width=2,
                 fill=tuple(max(0, x - 100) for x in color))
    draw.polygon(pts, outline=color, width=2)
    # "CTF" text on flag
    try:
        fnt = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", int(r * 0.3))
    except Exception:
        fnt = ImageFont.load_default()
    draw.text((cx, cy - r*0.72), "CTF", fill=color, font=fnt)
    # base
    draw.line([(cx - r*0.6, cy + r), (cx + r*0.2, cy + r)], fill=color, width=3)

# Map icon name → function
ICONS = {
    "shield":   icon_shield,
    "padlock":  icon_padlock,
    "skull":    icon_skull,
    "target":   icon_target,
    "k8s":      icon_k8s,
    "cloud":    icon_cloud,
    "terminal": icon_terminal,
    "brain":    icon_brain,
    "rocket":   icon_rocket,
    "server":   icon_server,
    "network":  icon_network,
    "key":      icon_key,
    "infinity": icon_infinity,
    "people":   icon_people,
    "chart":    icon_chart,
    "gear":     icon_gear,
    "diamond":  icon_diamond,
    "pen":      icon_pen,
    "gamepad":  icon_gamepad,
    "torch":    icon_torch,
    "pi":       icon_pi,
    "flag":     icon_flag,
}

# ─────────────────────────────────────────────────────────────────────────────
# Icon selection by title keywords
# ─────────────────────────────────────────────────────────────────────────────

ICON_KEYWORDS = [
    (["hacking my way", "hacker", "oscp", "red team", "pentest",
       "pwned", "modern cloud hack", "modern web hack"],               "skull"),
    (["ctf", "threat model"],                                          "flag"),
    (["phish", "social engineer", "how hackers think", "target"],      "target"),
    (["blue team", "defend"],                                          "shield"),
    (["security", "cyber hygiene", "zero trust", "harden",
       "devsecops culture", "stop teaching security"],                 "shield"),
    (["password", "auth", "oauth", "jwt", "credentials"],             "padlock"),
    (["key", "secret"],                                                "key"),
    (["kubernetes", "k8s", "minikube", "linkerd", "helm",
       "scale to zero", "namespace"],                                  "k8s"),
    (["cloud", "aws", "gcp", "s3", "cnapp", "terraform",
       "scheduler", "cloud security"],                                 "cloud"),
    (["ai ", "aiops", "shadow ai", "deepfake", "ai gov",
       "ai hack", "ai-assist", "autonomous"],                          "brain"),
    (["devops tool", "devsecops tool", "toolbelt"],                    "gear"),
    (["devops", "devsecops", "cicd", "pipeline"],                      "infinity"),
    (["linux", "distro"],                                              "terminal"),
    (["tmux", "terminal"],                                             "terminal"),
    (["obsidian", "note", "second brain"],                             "diamond"),
    (["raspberry pi", "pi 5", "pi zero", "game server",
       "home assist"],                                                  "pi"),
    (["homelab", "home lab", "home nas", "nas", "server"],             "server"),
    (["service mesh", "network", "mesh"],                              "network"),
    (["splunk", "dynatrace", "monitoring", "metric", "aiops platform"],"chart"),
    (["startup", "ipo", "race to", "gold rush", "from startup"],       "rocket"),
    (["imposter", "mental", "burnout", "wellbeing", "boundaries"],     "brain"),
    (["empathy", "interpersonal", "soft skill", "psychological",
       "people ops", "senior to", "team lead", "culture"],            "people"),
    (["blog", "create your own", "writing", "write a ctf"],           "pen"),
    (["game"],                                                         "gamepad"),
    (["gmail", "gapps", "app"],                                        "gear"),
    (["learn", "using ai to learn", "teach"],                          "torch"),
    (["all change"],                                                    "gear"),
]

def pick_icon(title: str) -> str:
    tl = title.lower()
    for keywords, icon in ICON_KEYWORDS:
        if any(k in tl for k in keywords):
            return icon
    return "gear"

# ─────────────────────────────────────────────────────────────────────────────
# Image generation
# ─────────────────────────────────────────────────────────────────────────────

def load_fonts():
    for path in ["/System/Library/Fonts/Helvetica.ttc",
                 "/System/Library/Fonts/SFNSText.ttf",
                 "/System/Library/Fonts/Arial.ttf"]:
        try:
            return (ImageFont.truetype(path, 26),
                    ImageFont.truetype(path, 15))
        except (OSError, IOError):
            pass
    d = ImageFont.load_default()
    return d, d

def make_card_image(title: str, output_path: str):
    palette   = pick_palette(title)
    icon_name = pick_icon(title)
    bg, mid, accent = palette
    h = int(hashlib.md5(title.encode()).hexdigest(), 16)

    # ── gradient background ───────────────────────────────────────────────────
    img = Image.new("RGB", (WIDTH, HEIGHT), bg)
    draw = ImageDraw.Draw(img)
    for y in range(HEIGHT):
        t = y / HEIGHT
        r2 = int(bg[0] + (mid[0] - bg[0]) * t)
        g2 = int(bg[1] + (mid[1] - bg[1]) * t)
        b2 = int(bg[2] + (mid[2] - bg[2]) * t)
        draw.line([(0, y), (WIDTH, y)], fill=(r2, g2, b2))

    # ── per-category background texture ──────────────────────────────────────
    pk = palette_key(palette)
    tex_fn = BG_TEXTURES.get(pk, bg_diagonal_grid)
    tex_fn(img, mid, accent, h)

    # ── accent corner shape (top-right) ──────────────────────────────────────
    sc   = tuple(min(255, x + 35) for x in accent)
    lay2 = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    d2   = ImageDraw.Draw(lay2)
    sx   = (h >> 36) % (WIDTH // 4) + WIDTH * 2 // 3
    shape = h % 3
    if shape == 0:
        d2.polygon([(sx, 18), (sx - 65, 140), (sx + 65, 140)],
                   outline=(*sc, 60), width=2)
        d2.polygon([(sx, 30), (sx - 38, 100), (sx + 38, 100)],
                   outline=(*sc, 35), width=1)
    elif shape == 1:
        d2.polygon([(sx, 28), (sx + 60, 95), (sx, 162), (sx - 60, 95)],
                   outline=(*sc, 60), width=2)
        d2.polygon([(sx, 48), (sx + 36, 95), (sx, 142), (sx - 36, 95)],
                   outline=(*sc, 35), width=1)
    else:
        d2.ellipse([sx - 68, 16, sx + 68, 152], outline=(*sc, 60), width=2)
        d2.ellipse([sx - 42, 40, sx + 42, 128], outline=(*sc, 30), width=1)
    img = img.convert("RGBA")
    img.paste(lay2, (0, 0), lay2)
    img = img.convert("RGB")
    draw = ImageDraw.Draw(img)

    # ── icon (slightly off-centre for composition) ────────────────────────────
    icon_cx = WIDTH  // 2 + ((h >> 12) % 40) - 20   # ±20px horizontal wander
    icon_cy = HEIGHT // 2 - 38
    icon_r  = 82
    icon_color = tuple(min(255, x + 85) for x in accent)

    # Convert draw to RGBA for alpha halo rings
    img_rgba = img.convert("RGBA")
    halo_lay, halo_d = _alpha_layer(WIDTH, HEIGHT)
    for i in range(3):
        rr = icon_r + 26 + i * 18
        a  = 30 - i * 8
        halo_d.ellipse([icon_cx - rr, icon_cy - rr, icon_cx + rr, icon_cy + rr],
                       outline=(*icon_color, a), width=1)
    img_rgba.paste(halo_lay, (0, 0), halo_lay)
    img = img_rgba.convert("RGB")
    draw = ImageDraw.Draw(img)

    ICONS[icon_name](draw, icon_cx, icon_cy, icon_r, icon_color)

    # ── bottom banner ─────────────────────────────────────────────────────────
    banner_h = 155
    overlay  = Image.new("RGBA", (WIDTH, banner_h), (0, 0, 0, 0))
    ov       = ImageDraw.Draw(overlay)
    for y in range(banner_h):
        a = int(220 * (y / banner_h))
        ov.line([(0, y), (WIDTH, y)], fill=(0, 0, 0, a))
    img = img.convert("RGBA")
    img.paste(overlay, (0, HEIGHT - banner_h), overlay)
    img = img.convert("RGB")
    draw = ImageDraw.Draw(img)

    # ── title text ────────────────────────────────────────────────────────────
    font, font_sm = load_fonts()
    lines = textwrap.fill(title, width=38).split("\n")[:3]
    ty = HEIGHT - 135
    for line in lines:
        draw.text((28, ty), line, fill=(255, 255, 255), font=font)
        ty += 34
    draw.text((28, HEIGHT - 28), BRAND, fill=(170, 170, 195), font=font_sm)

    # ── accent bar — left edge with a second thinner inner bar ───────────────
    draw.rectangle([0, 0, 5, HEIGHT], fill=accent)
    draw.rectangle([7, 0, 8, HEIGHT],
                   fill=tuple(min(255, x + 40) for x in accent))

    if not DRY:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        ext = os.path.splitext(output_path)[1].lower()
        fmt = "PNG" if ext == ".png" else "JPEG"
        img.save(output_path, fmt, quality=88)

    sz = os.path.getsize(output_path) // 1024 if not DRY else 0
    print(f"  {'[DRY]' if DRY else '[ok]':6s} {os.path.basename(output_path):55s}"
          f"  icon={icon_name:10s}  palette={pk:10s}  {sz}KB")

# ─────────────────────────────────────────────────────────────────────────────
# Post scanning & updating
# ─────────────────────────────────────────────────────────────────────────────

def safe_stem(title: str) -> str:
    s = title.lower()
    s = re.sub(r"[^a-z0-9 \-]", "", s)
    s = re.sub(r"\s+", "-", s.strip())
    s = re.sub(r"-+", "-", s)
    return s[:55].rstrip("-")

def read_fm(path: str) -> dict:
    meta, in_fm = {}, False
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.rstrip()
            if line == "---":
                if not in_fm:
                    in_fm = True; continue
                else:
                    break
            if in_fm:
                if ":" in line:
                    k, _, v = line.partition(":")
                    meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta

def update_image_fm(path: str, new_image_ref: str):
    with open(path, encoding="utf-8", errors="replace") as f:
        content = f.read()
    updated = re.sub(r'^image:.*$', f'image: "{new_image_ref}"',
                     content, count=1, flags=re.MULTILINE)
    if updated != content and not DRY:
        with open(path, "w", encoding="utf-8") as f:
            f.write(updated)

# ─────────────────────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────────────────────

def main():
    print(f"Geeky Blinder — card image generator  [{WIDTH}×{HEIGHT}]"
          f"{'  DRY RUN' if DRY else ''}\n")

    post_files = sorted(
        f for f in os.listdir(POSTS)
        if f.endswith((".markdown", ".md")) and os.path.isfile(os.path.join(POSTS, f))
    )

    count = 0
    for fname in post_files:
        fpath = os.path.join(POSTS, fname)
        meta  = read_fm(fpath)
        title = meta.get("title", "")
        if not title:
            print(f"  [skip] {fname} — no title")
            continue

        stem     = safe_stem(title)
        out_name = f"{stem}.jpg"
        out_path = os.path.join(CARDS, out_name)
        img_ref  = f"img/cards/{out_name}"

        make_card_image(title, out_path)
        update_image_fm(fpath, img_ref)
        count += 1

    print(f"\n✓ {count} images {'previewed' if DRY else 'written to img/cards/'}")

if __name__ == "__main__":
    main()
