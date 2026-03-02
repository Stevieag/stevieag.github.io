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
• Geometric accent lines + shapes
• Large programmatic icon (topic-relevant) centred in upper area
• Semi-transparent title banner at the bottom
• Consistent branding footer
"""

import os
import re
import sys
import math
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
# Icon drawing library
# ─────────────────────────────────────────────────────────────────────────────

def _c(color, alpha=255):
    """Return RGBA tuple."""
    return (*color, alpha)

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
    # inner tick
    draw.line([(cx - r*0.3, cy + r*0.05), (cx - r*0.05, cy + r*0.35),
               (cx + r*0.4, cy - r*0.25)], fill=color, width=3)

def icon_padlock(draw, cx, cy, r, color):
    """Padlock — passwords / auth."""
    bx, by = r * 0.65, r * 0.55
    draw.rectangle([cx - bx, cy, cx + bx, cy + r * 1.1], outline=color, width=3)
    draw.arc([cx - bx, cy - r, cx + bx, cy + r * 0.1],
             start=0, end=180, fill=color, width=3)
    draw.ellipse([cx - r*0.15, cy + r*0.35, cx + r*0.15, cy + r*0.65], outline=color, width=2)

def icon_skull(draw, cx, cy, r, color):
    """Skull — red team / hacking offensively."""
    draw.ellipse([cx - r, cy - r, cx + r, cy + r * 0.55], outline=color, width=3)
    # jaw
    draw.rectangle([cx - r*0.7, cy + r*0.3, cx + r*0.7, cy + r*0.8], outline=color, width=3)
    # teeth
    for ox in [-0.35, 0, 0.35]:
        draw.rectangle([cx + ox*r - r*0.12, cy + r*0.55,
                        cx + ox*r + r*0.12, cy + r*0.8], fill=color)
    # eyes
    for ox in [-0.35, 0.35]:
        draw.ellipse([cx + ox*r - r*0.2, cy - r*0.3,
                      cx + ox*r + r*0.2, cy + r*0.1], fill=color)

def icon_target(draw, cx, cy, r, color):
    """Concentric rings — CTF / threat / red-team sims."""
    for i, frac in enumerate([1.0, 0.65, 0.35]):
        draw.ellipse([cx - r*frac, cy - r*frac, cx + r*frac, cy + r*frac],
                     outline=color, width=2 if i < 2 else 3)
    draw.line([(cx - r*1.1, cy), (cx + r*1.1, cy)], fill=color, width=2)
    draw.line([(cx, cy - r*1.1), (cx, cy + r*1.1)], fill=color, width=2)

def icon_k8s(draw, cx, cy, r, color):
    """Kubernetes helm wheel — 7 spokes."""
    spokes = 7
    outer, inner = r, r * 0.25
    draw.ellipse([cx - outer, cy - outer, cx + outer, cy + outer], outline=color, width=3)
    draw.ellipse([cx - inner, cy - inner, cx + inner, cy + inner], outline=color, width=2)
    for i in range(spokes):
        angle = math.radians(i * 360 / spokes - 90)
        x1 = cx + inner * math.cos(angle)
        y1 = cy + inner * math.sin(angle)
        x2 = cx + outer * math.cos(angle)
        y2 = cy + outer * math.sin(angle)
        draw.line([(x1, y1), (x2, y2)], fill=color, width=3)

def icon_cloud(draw, cx, cy, r, color):
    """Cloud shape."""
    for ox, oy, fr in [(-0.45, 0.15, 0.4), (0, -0.1, 0.55), (0.45, 0.1, 0.42)]:
        rr = r * fr
        draw.ellipse([cx + ox*r - rr, cy + oy*r - rr,
                      cx + ox*r + rr, cy + oy*r + rr], outline=color, width=3)
    # base line
    draw.line([(cx - r*0.8, cy + r*0.45), (cx + r*0.8, cy + r*0.45)], fill=color, width=3)

def icon_terminal(draw, cx, cy, r, color):
    """Terminal window — linux / tmux."""
    bw, bh = r * 1.2, r * 0.9
    draw.rectangle([cx - bw, cy - bh, cx + bw, cy + bh], outline=color, width=3)
    draw.line([(cx - bw, cy - bh + r*0.35), (cx + bw, cy - bh + r*0.35)],
              fill=color, width=2)
    # prompt  >_
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", int(r * 0.55))
    except Exception:
        font = ImageFont.load_default()
    draw.text((cx - bw*0.65, cy - bh*0.25), ">_", fill=color, font=font)

def icon_brain(draw, cx, cy, r, color):
    """Brain — mental health / imposter syndrome / learning."""
    # Two lobes
    draw.arc([cx - r, cy - r*0.8, cx + r*0.05, cy + r*0.6],
             start=200, end=540, fill=color, width=3)
    draw.arc([cx - r*0.05, cy - r*0.8, cx + r, cy + r*0.6],
             start=-20, end=340, fill=color, width=3)
    # central stem
    draw.line([(cx, cy - r*0.8), (cx, cy + r*0.6)], fill=color, width=2)

def icon_rocket(draw, cx, cy, r, color):
    """Rocket — startup / IPO."""
    # body
    draw.polygon([(cx, cy - r),
                  (cx + r*0.4, cy + r*0.4),
                  (cx - r*0.4, cy + r*0.4)], outline=color, width=3)
    # fins
    draw.polygon([(cx - r*0.4, cy + r*0.2), (cx - r*0.7, cy + r*0.8),
                  (cx - r*0.4, cy + r*0.5)], outline=color, width=2)
    draw.polygon([(cx + r*0.4, cy + r*0.2), (cx + r*0.7, cy + r*0.8),
                  (cx + r*0.4, cy + r*0.5)], outline=color, width=2)
    # window
    draw.ellipse([cx - r*0.18, cy - r*0.25, cx + r*0.18, cy + r*0.15],
                 outline=color, width=2)

def icon_server(draw, cx, cy, r, color):
    """Server rack — homelab / NAS."""
    unit_h = r * 0.38
    for i in range(3):
        y = cy - r + i * (unit_h + r*0.1)
        draw.rectangle([cx - r, y, cx + r, y + unit_h], outline=color, width=2)
        draw.ellipse([cx + r*0.65, y + unit_h*0.3,
                      cx + r*0.85, y + unit_h*0.7], outline=color, width=2)
        draw.line([(cx - r*0.8, y + unit_h*0.5), (cx + r*0.45, y + unit_h*0.5)],
                  fill=color, width=2)

def icon_network(draw, cx, cy, r, color):
    """Node mesh — service mesh / devsecops."""
    nodes = [
        (cx,        cy - r),
        (cx + r,    cy - r*0.3),
        (cx + r*0.7, cy + r*0.7),
        (cx - r*0.7, cy + r*0.7),
        (cx - r,    cy - r*0.3),
    ]
    for i, (x1, y1) in enumerate(nodes):
        for j, (x2, y2) in enumerate(nodes):
            if j > i:
                draw.line([(x1, y1), (x2, y2)], fill=color, width=1)
    nr = r * 0.18
    for (nx, ny) in nodes:
        draw.ellipse([nx - nr, ny - nr, nx + nr, ny + nr], fill=color)
    draw.ellipse([cx - nr, cy - nr, cx + nr, cy + nr], fill=color)

def icon_key(draw, cx, cy, r, color):
    """Key — auth / JWT / OAuth."""
    kr = r * 0.42
    draw.ellipse([cx - r - kr, cy - kr, cx - r + kr, cy + kr], outline=color, width=3)
    draw.ellipse([cx - r - kr*0.35, cy - kr*0.35,
                  cx - r + kr*0.35, cy + kr*0.35], fill=color)
    draw.line([(cx - r + kr, cy), (cx + r, cy)], fill=color, width=3)
    for ox in [r*0.2, r*0.55]:
        draw.line([(cx + ox, cy), (cx + ox, cy + r*0.4)], fill=color, width=3)

def icon_infinity(draw, cx, cy, r, color):
    """Infinity loop — DevOps / CI/CD."""
    for sign in [-1, 1]:
        ox = sign * r * 0.5
        draw.arc([cx + ox - r*0.5, cy - r*0.45, cx + ox + r*0.5, cy + r*0.45],
                 start=0 if sign == 1 else 180,
                 end=360 if sign == 1 else 540,
                 fill=color, width=4)
    # arrows on ends
    for angle, ax, ay in [(0, cx + r, cy), (180, cx - r, cy)]:
        a = math.radians(angle)
        for da in [30, -30]:
            da_r = math.radians(angle + da + 180)
            draw.line([(ax, ay),
                       (ax + math.cos(da_r)*r*0.22,
                        ay + math.sin(da_r)*r*0.22)],
                      fill=color, width=3)

def icon_people(draw, cx, cy, r, color):
    """Two figures — people / empathy / culture."""
    for ox in [-r*0.38, r*0.38]:
        hx, hy = cx + ox, cy - r*0.55
        hr = r * 0.22
        draw.ellipse([hx - hr, hy - hr, hx + hr, hy + hr], outline=color, width=2)
        draw.arc([hx - hr*1.6, hy + hr, hx + hr*1.6, hy + r*1.0],
                 start=0, end=180, fill=color, width=2)

def icon_chart(draw, cx, cy, r, color):
    """Bar chart going up — data / monitoring / metrics."""
    bars = [0.4, 0.65, 0.9, 0.55, 0.8]
    bw = r * 0.28
    ox = cx - r
    for i, h in enumerate(bars):
        x = ox + i * (bw + r*0.08)
        top = cy + r - r * 2 * h
        draw.rectangle([x, top, x + bw, cy + r], outline=color, width=2)
    # axes
    draw.line([(cx - r - bw*0.4, cy - r), (cx - r - bw*0.4, cy + r + 5),
               (cx + r + bw*0.4, cy + r + 5)], fill=color, width=2)

def icon_gear(draw, cx, cy, r, color):
    """Cog / gear — tools / ops / automation."""
    teeth = 10
    ir, or_ = r * 0.55, r
    pts = []
    for i in range(teeth * 2):
        angle = math.radians(i * 180 / teeth)
        rad = or_ if i % 2 == 0 else ir
        pts.append((cx + rad * math.cos(angle), cy + rad * math.sin(angle)))
    draw.polygon(pts, outline=color, width=2)
    draw.ellipse([cx - ir*0.55, cy - ir*0.55, cx + ir*0.55, cy + ir*0.55],
                 outline=color, width=3)

def icon_diamond(draw, cx, cy, r, color):
    """Diamond / gem — Obsidian / notes."""
    draw.polygon([(cx, cy - r), (cx + r*0.7, cy - r*0.2),
                  (cx + r*0.7, cy + r*0.2), (cx, cy + r),
                  (cx - r*0.7, cy + r*0.2), (cx - r*0.7, cy - r*0.2)],
                 outline=color, width=3)
    draw.line([(cx - r*0.7, cy - r*0.2), (cx, cy - r), (cx + r*0.7, cy - r*0.2)],
              fill=color, width=2)
    draw.line([(cx - r*0.7, cy - r*0.2), (cx, cy + r), (cx + r*0.7, cy - r*0.2)],
              fill=color, width=1)

def icon_pen(draw, cx, cy, r, color):
    """Pen / quill — blog / writing."""
    draw.polygon([(cx, cy - r), (cx + r*0.25, cy), (cx, cy + r), (cx - r*0.25, cy)],
                 outline=color, width=2)
    draw.line([(cx, cy + r), (cx - r*0.5, cy + r*1.4)], fill=color, width=3)
    draw.line([(cx - r*0.5, cy + r*1.4), (cx - r*0.3, cy + r*0.9)], fill=color, width=2)

def icon_gamepad(draw, cx, cy, r, color):
    """Game controller."""
    # body
    draw.ellipse([cx - r, cy - r*0.55, cx + r, cy + r*0.55], outline=color, width=3)
    # d-pad
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        draw.rectangle([cx - r*0.5 + dx*r*0.22 - r*0.1, cy + dy*r*0.22 - r*0.1,
                         cx - r*0.5 + dx*r*0.22 + r*0.1, cy + dy*r*0.22 + r*0.1],
                       fill=color)
    # buttons
    for bx, by in [(r*0.4, -r*0.15), (r*0.55, r*0.05),
                   (r*0.25, r*0.05), (r*0.4, r*0.25)]:
        draw.ellipse([cx + bx - r*0.09, cy + by - r*0.09,
                      cx + bx + r*0.09, cy + by + r*0.09], fill=color)

def icon_torch(draw, cx, cy, r, color):
    """Torch / light — learning / AI learning."""
    # bulb
    draw.arc([cx - r*0.55, cy - r, cx + r*0.55, cy + r*0.3],
             start=30, end=150, fill=color, width=3)
    draw.line([(cx - r*0.55, cy + r*0.3), (cx - r*0.35, cy + r*0.7)],
              fill=color, width=3)
    draw.line([(cx + r*0.55, cy + r*0.3), (cx + r*0.35, cy + r*0.7)],
              fill=color, width=3)
    draw.line([(cx - r*0.35, cy + r*0.7), (cx + r*0.35, cy + r*0.7)],
              fill=color, width=3)
    # rays
    for angle in [-60, -30, 0, 30, 60]:
        a = math.radians(angle - 90)
        x1 = cx + r * 0.65 * math.cos(a)
        y1 = cy + r * 0.65 * math.sin(a) - r*0.35
        x2 = cx + r * math.cos(a)
        y2 = cy + r * math.sin(a) - r*0.35
        draw.line([(x1, y1), (x2, y2)], fill=color, width=2)

def icon_pi(draw, cx, cy, r, color):
    """Raspberry Pi inspired: Pi symbol."""
    # bar across top
    draw.line([(cx - r, cy - r*0.4), (cx + r, cy - r*0.4)], fill=color, width=3)
    # left leg
    draw.arc([cx - r, cy - r*0.4, cx, cy + r], start=0, end=270, fill=color, width=3)
    # right straight leg
    draw.line([(cx + r*0.5, cy - r*0.4), (cx + r*0.5, cy + r)], fill=color, width=3)

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
}

# ─────────────────────────────────────────────────────────────────────────────
# Icon selection by title keywords
# ─────────────────────────────────────────────────────────────────────────────

ICON_KEYWORDS = [
    (["hacking my way", "hacker", "oscp", "red team", "pentest",
       "pwned", "modern cloud hack"],                                   "skull"),
    (["ctf", "threat model", "target"],                                "target"),
    (["phish", "social engineer", "how hackers think"],                "target"),
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
    (["devops tool", "devsecops tool", "toolbelt", "toolbelt"],        "gear"),
    (["devops", "devsecops", "cicd", "pipeline", "infinity"],         "infinity"),
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
    (["blog", "create your own", "writing"],                           "pen"),
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
    palette = pick_palette(title)
    icon_name = pick_icon(title)
    bg, mid, accent = palette
    h = int(hashlib.md5(title.encode()).hexdigest(), 16)

    # ── gradient background ──────────────────────────────────────────────────
    img = Image.new("RGB", (WIDTH, HEIGHT), bg)
    draw = ImageDraw.Draw(img)
    for y in range(HEIGHT):
        t = y / HEIGHT
        r = int(bg[0] + (mid[0] - bg[0]) * t)
        g = int(bg[1] + (mid[1] - bg[1]) * t)
        b = int(bg[2] + (mid[2] - bg[2]) * t)
        draw.line([(0, y), (WIDTH, y)], fill=(r, g, b))

    # ── diagonal accent lines ────────────────────────────────────────────────
    lc = tuple(min(255, x + 18) for x in mid)
    for i in range(6):
        off = (h >> (i * 5)) % 280
        draw.line([(off, 0), (off + 350, HEIGHT)], fill=lc, width=1)
        draw.line([(WIDTH - off, 0), (WIDTH - off - 350, HEIGHT)], fill=lc, width=1)

    # ── accent shape (subtle, top-right corner) ──────────────────────────────
    sc = tuple(min(255, x + 30) for x in accent)
    shape = h % 3
    sx = (h >> 36) % (WIDTH // 3) + WIDTH // 2
    if shape == 0:
        draw.polygon([(sx, 20), (sx - 60, 130), (sx + 60, 130)], outline=sc, width=1)
    elif shape == 1:
        draw.polygon([(sx, 30), (sx + 55, 95), (sx, 160), (sx - 55, 95)],
                     outline=sc, width=1)
    else:
        draw.ellipse([sx - 65, 20, sx + 65, 150], outline=sc, width=1)

    # ── icon ─────────────────────────────────────────────────────────────────
    icon_cx = WIDTH // 2
    icon_cy = HEIGHT // 2 - 40     # vertically centred in the upper portion
    icon_r  = 72
    icon_color = tuple(min(255, x + 80) for x in accent)
    ICONS[icon_name](draw, icon_cx, icon_cy, icon_r, icon_color)

    # ── bottom banner ─────────────────────────────────────────────────────────
    banner_h = 155
    overlay = Image.new("RGBA", (WIDTH, banner_h), (0, 0, 0, 0))
    ov = ImageDraw.Draw(overlay)
    for y in range(banner_h):
        a = int(215 * (y / banner_h))
        ov.line([(0, y), (WIDTH, y)], fill=(0, 0, 0, a))
    img = img.convert("RGBA")
    img.paste(overlay, (0, HEIGHT - banner_h), overlay)
    img = img.convert("RGB")
    draw = ImageDraw.Draw(img)

    font, font_sm = load_fonts()
    lines = textwrap.fill(title, width=38).split("\n")[:3]
    ty = HEIGHT - 135
    for line in lines:
        draw.text((28, ty), line, fill=(255, 255, 255), font=font)
        ty += 34
    draw.text((28, HEIGHT - 28), BRAND, fill=(170, 170, 195), font=font_sm)

    # ── accent colour bar (left edge) ─────────────────────────────────────────
    draw.rectangle([0, 0, 4, HEIGHT], fill=accent)

    if not DRY:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        ext = os.path.splitext(output_path)[1].lower()
        fmt = "PNG" if ext == ".png" else "JPEG"
        img.save(output_path, fmt, quality=88)

    sz = os.path.getsize(output_path) // 1024 if not DRY else 0
    print(f"  {'[DRY]' if DRY else '[ok]':6s} {os.path.basename(output_path):55s}"
          f"  icon={icon_name:10s}  {sz}KB")

# ─────────────────────────────────────────────────────────────────────────────
# Post scanning & updating
# ─────────────────────────────────────────────────────────────────────────────

def safe_stem(title: str) -> str:
    """title → safe-filename-stem (max 55 chars)."""
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
        meta = read_fm(fpath)
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
