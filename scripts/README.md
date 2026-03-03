# Scripts

## Requirements

Python 3.10+ with Pillow. Use a virtual environment to avoid system Python conflicts on macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install Pillow reportlab python-docx
```

---

## process_images.py — regenerate all card images

Scans every post in `_posts/`, generates a 728×469 card image in `img/cards/`, and updates the `image:` field in each post's front matter to match.

```bash
python3 scripts/process_images.py          # generate all
python3 scripts/process_images.py --dry    # preview (no files written)
```

Each post gets a themed image based on keywords in the title:

| Category | Background | Icon |
|---|---|---|
| Security / zero trust | Hex grid | Shield |
| Red team / hacking | Code rain | Skull |
| CTF / threat model | Code rain | Flag / Target |
| Kubernetes / containers | Hex grid | K8s wheel |
| Cloud / AWS | Hex grid | Cloud |
| AI / LLM | Neural network | Brain |
| DevOps / CI/CD | Dot matrix | Infinity loop |
| Linux / tmux | Scanlines + hex chars | Terminal |
| Data / monitoring | Dot matrix | Bar chart |
| Raspberry Pi / homelab | Circuit board | Pi / Server |
| Startup / IPO | Starburst | Rocket |
| People / culture | Wavy lines | People |
| Mental health / burnout | Wavy lines | Brain |
| Writing / blog | Diagonal grid | Pen |
| Tools | Dot matrix | Gear |

---

## make_card.py — generate a single card image

Generate one image from a title, with optional overrides for icon and colour palette.

```bash
# Auto-detect theme from title
python3 scripts/make_card.py "Zero Trust Architecture"

# Custom output path
python3 scripts/make_card.py "Zero Trust Architecture" --out img/cards/zero-trust.jpg

# Override the icon
python3 scripts/make_card.py "My Post" --icon skull

# Override the colour palette
python3 scripts/make_card.py "My Post" --palette redteam

# Preview without writing
python3 scripts/make_card.py "My Post" --dry

# List all available icons
python3 scripts/make_card.py --list-icons

# List all available palettes
python3 scripts/make_card.py --list-palettes
```

### Available icons

`brain` `chart` `cloud` `diamond` `flag` `gamepad` `gear` `infinity` `k8s` `key` `network` `padlock` `pen` `people` `pi` `rocket` `server` `shield` `skull` `target` `terminal` `torch`

### Available palettes

`ai` `blueteam` `cloud` `data` `devops` `game` `hack` `home` `k8s` `linux` `mental` `people` `pi` `redteam` `security` `startup` `tool` `writing`

---

## add_banner.py — add a banner to an existing image

```bash
python3 scripts/add_banner.py <image> "Banner text"
```

---

## Workflow for a new post

1. Write the post in `_posts/`
2. Run `python3 scripts/make_card.py "Your Post Title"` to preview the image
3. Tweak with `--icon` or `--palette` if the auto-selection isn't right
4. The script saves to `img/cards/` and prints the path — add it to front matter:
   ```yaml
   image: "img/cards/your-post-title.jpg"
   ```
5. Or just run `python3 scripts/process_images.py` to regenerate everything at once
