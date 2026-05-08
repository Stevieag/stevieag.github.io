---
title:  "Running a Game Server on a Raspberry Pi 5"
subtitle: "Tiny board, shared worlds, big grin"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/running-a-game-server-on-a-raspberry-pi-5.jpg"
date: 2026-04-12
tags: raspberry-pi gaming minecraft server homelab
---

## Running a Game Server on a Raspberry Pi 5

A Pi 5 is the sweet spot between “I own a data centre” and “I’ve wedged a laptop under the telly.” It’s the first Pi with enough grunt that you can host a real Minecraft server for your mates without it bursting into flames or chunking its way through every player movement.

This post is the working tutorial: hardware that actually matters, a Paper server installed properly, JVM flags that don’t embarrass you, a systemd unit that survives reboots and crashes, RCON-driven backups, and three increasingly sensible ways to let friends connect. I’ve run this exact build on an 8 GB Pi 5 with NVMe and an active cooler since the start of 2026 — six players, four chunks of view distance, idles at 25–35% CPU, peaks around 80% during big builds.

We’ll focus on Minecraft Java because it’s the classic case. Three other Pi-friendly games go at the bottom.

---

## What You Actually Need (Beyond a Pi 5)

The Pi 5 itself is fine. The problem is that out of the box, two things will bite you. Plan for both.

- **An active cooler.** Without it, the Pi 5 throttles down to ~1.5 GHz under sustained load. The official Raspberry Pi Active Cooler is £5 and clips on; a case with a built-in fan (Argon NEO 5, Flirc) is fine too. Passive heatsinks are not enough for a 24/7 server.
- **An NVMe SSD, not an SD card.** Minecraft’s chunk I/O murders SD cards within months and is the single biggest source of lag spikes on a Pi server. The official [Raspberry Pi M.2 HAT+](https://www.raspberrypi.com/products/m2-hat-plus/) takes a 2230/2242 NVMe drive over the Pi 5’s PCIe lane. Pimoroni’s NVMe Base and the 52Pi P02 are the same idea. A 256 GB NVMe is plenty.
- **8 GB RAM minimum.** 4 GB works for two players; 16 GB is overkill for a Java server but lets you run a Velocity proxy or other services alongside.
- **Wired Ethernet.** Wi-Fi works but adds 2–10 ms of jitter that players feel.
- **A real PSU.** The official 27 W USB-C PSU. The Pi 5 will silently underclock with anything weaker.

Total kit cost as of writing: around £130–£160 with NVMe.

---

## Boot the Pi from NVMe (Once, Properly)

You want NVMe-only boot, not “SD card with the rootfs on the NVMe” fragility.

Flash Raspberry Pi OS Lite (64-bit, Bookworm) onto the NVMe with `rpi-imager`. In the imager’s settings cog: enable SSH (key auth), set hostname (`mcpi`), set username, set Wi-Fi only as a fallback.

First boot the Pi from an SD card to update the bootloader and switch boot order:

```bash
sudo apt update && sudo apt full-upgrade -y
sudo rpi-eeprom-update -a
sudo raspi-config
# Advanced Options → Bootloader Version → Latest
# Advanced Options → Boot Order → NVMe/USB Boot

sudo reboot
```

Power off, remove the SD card, boot from NVMe. From here on everything is on the SSD.

Then, on the Pi, lock down the basics:

```bash
sudo apt update && sudo apt full-upgrade -y
sudo apt install -y ufw fail2ban htop tmux unattended-upgrades
sudo dpkg-reconfigure --priority=low unattended-upgrades

sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow from 192.168.0.0/16 to any port 22 proto tcp
sudo ufw enable
```

Give the Pi a static IP via your router’s DHCP reservation — players need a stable address, and a moving target breaks every backup script.

---

## Pick a Server Flavour

You have three sensible choices.

- **Vanilla** (Mojang official) — slowest, no plugins, fine for two friends and a quiet world.
- **[Paper](https://papermc.io/)** — Spigot fork with serious performance work and a healthy plugin ecosystem. **Default pick** for a Pi.
- **[Purpur](https://purpurmc.org/)** — Paper fork with extra config knobs and gameplay tweaks. Same performance, more rope to hang yourself with. Pick once you know you want a specific Purpur feature.

We’ll use Paper. Same systemd unit, RCON, and backup story applies to Purpur if you swap it later.

---

## Install Paper Properly

Paper 1.21+ requires Java 21. JDK 17 is the wrong answer in 2026 — `openjdk-17` will start the server and then quietly refuse to load 1.21 worlds.

```bash
sudo apt install -y openjdk-21-jre-headless curl jq
java -version   # expect 21.x
```

Create a dedicated, login-disabled user:

```bash
sudo adduser --system --home /opt/minecraft --group --disabled-login minecraft
sudo install -d -o minecraft -g minecraft /opt/minecraft/server
```

Fetch the latest Paper build via their API. This script grabs the newest stable build for whatever Minecraft version you set — no scraping, no broken links.

```bash
sudo -u minecraft bash <<'EOF'
set -euo pipefail
cd /opt/minecraft/server

MC_VERSION="1.21.4"   # bump when you want to update; check papermc.io for current
BUILD=$(curl -s "https://api.papermc.io/v2/projects/paper/versions/${MC_VERSION}/builds" \
  | jq -r '[.builds[] | select(.channel=="default")][-1].build')
JAR="paper-${MC_VERSION}-${BUILD}.jar"

curl -sLo "${JAR}" \
  "https://api.papermc.io/v2/projects/paper/versions/${MC_VERSION}/builds/${BUILD}/downloads/${JAR}"

ln -sf "${JAR}" paper.jar
echo "Installed ${JAR}"
EOF
```

Accept the EULA (read it once, then this is fine):

```bash
sudo -u minecraft tee /opt/minecraft/server/eula.txt > /dev/null <<'EOF'
eula=true
EOF
```

First run — generates `server.properties` and the world. Stop it as soon as it says “Done”:

```bash
sudo -u minecraft bash -c 'cd /opt/minecraft/server && \
  java -Xms2G -Xmx4G -jar paper.jar nogui'
# wait for "Done", then type: stop
```

---

## Tune `server.properties` for a Pi

Edit `/opt/minecraft/server/server.properties`. The lines that matter for a Pi:

```properties
view-distance=6
simulation-distance=4
max-players=8
network-compression-threshold=256
sync-chunk-writes=false
entity-broadcast-range-percentage=80
spawn-protection=0

enable-rcon=true
rcon.port=25575
rcon.password=CHANGE_ME_TO_A_LONG_RANDOM_STRING
broadcast-rcon-to-ops=false

online-mode=true
white-list=true
enforce-whitelist=true
```

Why each one:

- `view-distance=6` is the visual radius. Each step up is roughly quadratic CPU. 6 looks good and stays cheap.
- `simulation-distance=4` is what the server actually ticks. Keeping it lower than view distance is the single biggest performance win.
- `network-compression-threshold=256` saves CPU on a LAN. Lower (default 256, raise to 512) if you’re running over the internet.
- `sync-chunk-writes=false` is safe on NVMe and removes a stutter source. Don’t disable it on an SD card.
- `enforce-whitelist=true` is the difference between “my mates and I” and “anyone who finds my IP”.

Generate a strong RCON password:

```bash
openssl rand -hex 24
```

Paste it in, also stash it somewhere safe — you’ll use it from the systemd shutdown hook and the backup script.

Add yourself and your mates to the whitelist. With the server stopped:

```bash
sudo -u minecraft tee /opt/minecraft/server/whitelist.json > /dev/null <<'EOF'
[
  { "uuid": "00000000-0000-0000-0000-000000000000", "name": "geekyblinder" }
]
EOF
```

(Look up real UUIDs at [mcuuid.net](https://mcuuid.net/) or just let the server populate `whitelist.json` after you `whitelist add <name>` from the console.)

---

## A systemd Unit That Doesn’t Embarrass You

Aikar’s flags are the well-tested JVM tuning for Paper-family servers. Use them. Match `-Xms` and `-Xmx` to give the JVM a fixed heap — variable heap on a Pi causes long GC pauses.

For an 8 GB Pi with nothing else running, allocate 6 GB to the heap (leave 2 GB for the kernel and disk cache). For a 4 GB Pi, allocate 2.5 GB.

Create `/etc/systemd/system/minecraft.service`:

```ini
[Unit]
Description=Minecraft Paper Server
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=minecraft
Group=minecraft
WorkingDirectory=/opt/minecraft/server

ExecStart=/usr/bin/java \
  -Xms6G -Xmx6G \
  -XX:+UseG1GC \
  -XX:+ParallelRefProcEnabled \
  -XX:MaxGCPauseMillis=200 \
  -XX:+UnlockExperimentalVMOptions \
  -XX:+DisableExplicitGC \
  -XX:+AlwaysPreTouch \
  -XX:G1HeapWastePercent=5 \
  -XX:G1MixedGCCountTarget=4 \
  -XX:G1NewSizePercent=30 \
  -XX:G1MaxNewSizePercent=40 \
  -XX:G1HeapRegionSize=8M \
  -XX:G1ReservePercent=20 \
  -XX:G1MixedGCLiveThresholdPercent=90 \
  -XX:G1RSetUpdatingPauseTimePercent=5 \
  -XX:SurvivorRatio=32 \
  -XX:+PerfDisableSharedMem \
  -XX:MaxTenuringThreshold=1 \
  -Dusing.aikars.flags=https://mcflags.emc.gs \
  -Daikars.new.flags=true \
  -jar paper.jar nogui

ExecStop=/usr/local/bin/mcrcon-stop

Restart=on-failure
RestartSec=10s
TimeoutStopSec=60s

# hardening
NoNewPrivileges=true
ProtectSystem=strict
ProtectHome=true
PrivateTmp=true
PrivateDevices=true
ProtectKernelTunables=true
ProtectKernelModules=true
ProtectControlGroups=true
RestrictSUIDSGID=true
LockPersonality=true
ReadWritePaths=/opt/minecraft

[Install]
WantedBy=multi-user.target
```

The `ExecStop` script does a clean RCON shutdown — `save-all flush` then `stop` — so the world is consistent on disk. We’ll write that next.

---

## RCON: Live Admin and Clean Shutdowns

Install `mcrcon`:

```bash
sudo apt install -y build-essential
git clone https://github.com/Tiiffi/mcrcon.git /tmp/mcrcon
cd /tmp/mcrcon && make && sudo install -m 0755 mcrcon /usr/local/bin/
```

Stash the password in a root-readable file:

```bash
sudo install -d -m 0700 /etc/minecraft
echo 'CHANGE_ME_TO_A_LONG_RANDOM_STRING' | \
  sudo tee /etc/minecraft/rcon.pass > /dev/null
sudo chmod 0600 /etc/minecraft/rcon.pass
```

The clean-shutdown helper, `/usr/local/bin/mcrcon-stop`:

```bash
#!/bin/bash
set -e
PASS=$(cat /etc/minecraft/rcon.pass)
mcrcon -H 127.0.0.1 -P 25575 -p "$PASS" \
  "say Server stopping in 10 seconds..." \
  "save-all flush" \
  "save-off"
sleep 10
mcrcon -H 127.0.0.1 -P 25575 -p "$PASS" "stop"
```

```bash
sudo chmod 0755 /usr/local/bin/mcrcon-stop
```

Now bring it up:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now minecraft
sudo systemctl status minecraft
sudo journalctl -u minecraft -f
```

Live admin from the Pi (no need to attach to the console):

```bash
mcrcon -H 127.0.0.1 -P 25575 -p "$(sudo cat /etc/minecraft/rcon.pass)" \
  "list"
```

---

## Backups That Actually Restore

The world on disk is *not* consistent if you `cp` it while the server is running. The fix is to flush state via RCON, copy the world, then turn writes back on. Here’s `/usr/local/bin/mc-backup`:

```bash
#!/bin/bash
set -euo pipefail

WORLD_DIR=/opt/minecraft/server
BACKUP_DIR=/mnt/backups/minecraft
RCON_PASS=$(cat /etc/minecraft/rcon.pass)
STAMP=$(date +%Y%m%d-%H%M%S)
ARCHIVE="${BACKUP_DIR}/world-${STAMP}.tar.zst"

mkdir -p "$BACKUP_DIR"

# flush, then freeze writes
mcrcon -H 127.0.0.1 -P 25575 -p "$RCON_PASS" \
  "say Backup starting" "save-off" "save-all flush"

trap 'mcrcon -H 127.0.0.1 -P 25575 -p "$RCON_PASS" "save-on" "say Backup finished" || true' EXIT

tar --use-compress-program=zstd -cf "$ARCHIVE" \
  -C "$WORLD_DIR" world world_nether world_the_end \
  server.properties whitelist.json ops.json banned-players.json banned-ips.json

# keep last 14 daily snapshots
find "$BACKUP_DIR" -name 'world-*.tar.zst' -mtime +14 -delete
```

```bash
sudo chmod 0755 /usr/local/bin/mc-backup
```

Schedule it via cron — not on the minecraft user, on root, since we want predictable PATH and exit codes:

```bash
sudo crontab -e
# every day at 04:30
30 4 * * * /usr/local/bin/mc-backup >> /var/log/mc-backup.log 2>&1
```

Mount `/mnt/backups` from somewhere off the Pi — a NAS via NFS, an external SSD, or push the archives off-site with `restic` or `rclone`. A backup that lives on the same disk as the world isn’t a backup; it’s a slightly delayed loss.

---

## Letting Friends Join, Ranked by Sensibleness

### Best: Tailscale

Spin up Tailscale on the Pi and on your friends’ machines. Everyone gets a stable 100.x.x.x address; friends connect to `mcpi` (or the tailnet IP) on port 25565. No port forwarding, no exposing your home IP, end-to-end encrypted, free for personal use up to ~100 nodes.

```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up --ssh
```

Share the tailnet with your mates from the [Tailscale admin console](https://login.tailscale.com/admin/users). They install Tailscale, accept the share, and join your server with the tailnet hostname.

### Middle: a tunneling service (`playit.gg`, `ngrok`)

[playit.gg](https://playit.gg/) is purpose-built for game servers; it gives you a public address that proxies into your Pi without you opening a port. Free tier works fine for small groups. Performance hit is minimal; latency adds 5–20 ms depending on the chosen exit node.

### Last resort: open 25565 to the internet

Forward TCP/25565 from your router to the Pi. Add a UFW allow rule and lock down the rate at the router if you can:

```bash
sudo ufw allow 25565/tcp comment 'minecraft'
```

Then a Dynamic DNS record (DuckDNS, no-ip, or your registrar’s) so friends have a stable hostname. The risks are real — bots will find you within hours and try Bedrock/Java exploits, dictionary-attack any open ports they can see, and hammer the Pi. If you do this, **keep `enforce-whitelist=true`, `online-mode=true`, fail2ban running, and never expose 22 to the internet** — keep SSH on the LAN/Tailscale only.

---

## Monitoring: Catch Problems Before Players Do

In-game performance: install the [Spark plugin](https://spark.lucko.me/). Drop the jar in `/opt/minecraft/server/plugins/` and restart. Then in-game or via RCON:

```
/spark tps
/spark profiler --timeout 30
```

Pi-level: `htop` for the eyeball view, `vcgencmd measure_temp` for thermals, `vcgencmd get_throttled` to confirm you’re not throttling. If `get_throttled` returns anything other than `0x0`, your cooler or PSU isn’t up to the job.

For a longer-term picture, drop a Prometheus node-exporter on the Pi and scrape it from a Grafana box on your network. For Minecraft itself, [`minecraft-exporter`](https://github.com/dirien/minecraft-prometheus-exporter) hooks into Spark and gives you TPS, MSPT, player count, and chunk counts as Prom metrics.

---

## Other Pi 5–Friendly Servers, in Brief

The same shape (dedicated user, systemd unit, NVMe storage, backup script, Tailscale) applies to all of these.

- **Terraria via [TShock](https://tshock.co/)** — runs on Mono. 6–10 player worlds are comfortable on a Pi 5.
- **PocketMine-MP** — Bedrock-edition Minecraft for phones/console players. Lighter than Java; happy on a 4 GB Pi.
- **Factorio headless** — one of the best-optimised servers around. Works fine on Pi 5 for small (~4-player) games. The official binary is x86_64; you’ll want the ARM64 community build or a `box64` wrapper.
- **Vintage Story** — survival sandbox, Mono-based. Light enough for a small group, heavier than Terraria.

Heavy hitters that **won’t** run usefully on a Pi 5: ARK, 7 Days to Die, Valheim with mods, Project Zomboid with a dozen players. The Pi is a small server, not a magic one.

---

## Final Thought

A Pi 5 game server is peak geek: cheap, quiet, and good enough to run the shared world your group actually plays in. Done right, it doubles as a Linux training lab — you’ll learn systemd, JVM tuning, RCON scripting, backups, networking, and zero-trust ingress, all in one box that costs less than a single AAA game.

Get the cooler. Get the NVMe. Use Tailscale. Whitelist your mates. Back up the world. The rest is just blowing up blocky mountains after work.

<img src="img/authors/geeky.jpg" width="40"/>
