---
title:  "Running a Game Server on a Raspberry Pi 5"
subtitle: "Tiny board, shared worlds, big grin"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/running-a-game-server-on-a-raspberry-pi-5.jpg"
date: 2026-03-29
tags: raspberry-pi gaming minecraft server homelab
---

## Running a Game Server on a Raspberry Pi 5

Running a game server on a Raspberry Pi 5 is the sweet spot between “I own a data centre” and “I’ve wedged a laptop under the TV.” The Pi 5 has finally got enough grunt to host real games for friends without catching fire.

We’ll focus on a Minecraft Java server, because that’s the classic use case — but the pattern works for other games too.

---

## What the Pi 5 Brings to the Party

Pi 5 in human terms:

- Quad‑core Cortex‑A76 at 2.4 GHz.
- Up to 16 GB RAM.
- Faster I/O and overall throughput than older Pis.

Practically:

- A Pi 5 can happily host a small Minecraft server for a handful of players if you keep settings sensible.
- It’s quiet and low‑power, so you can run it 24/7.

---

## Base Setup: OS, Storage, Network

- Use Raspberry Pi OS Lite (64‑bit) for a headless server.
- Flash it to a decent SD card, or better, an external SSD.
- Enable SSH for remote management.
- Prefer wired Ethernet over Wi‑Fi for stability.

Give the Pi a static IP (via your router’s DHCP reservation) so players have a stable address.

---

## Installing Minecraft Java Server

1. Update:

```bash
sudo apt update && sudo apt upgrade -y
```

2. Install Java:

```bash
sudo apt install -y openjdk-17-jre-headless
```
Create a dedicated user:

```bash
sudo adduser --system --home /opt/minecraft --group minecraft
sudo su - minecraft
```
Download server JAR into /opt/minecraft/server, run it once, accept eula.txt, then run again.

Use:

```bash
java -Xms512M -Xmx2048M -jar server.jar nogui
```
Adjust memory based on Pi RAM and how many players you want.

## Optimising for the Pi
Edit server.properties:

Lower view distance:

```text
view-distance=4
```
Limit players, e.g.:

```text
max-players=5
```
Consider using Paper/Purpur for better performance.

---

## Run It as a Service
Create a systemd unit:

```text
[Unit]
Description=Minecraft Server
After=network.target

[Service]
WorkingDirectory=/opt/minecraft/server
User=minecraft
Group=minecraft
Restart=always
ExecStart=/usr/bin/java -Xms512M -Xmx2048M -jar server.jar nogui

[Install]
WantedBy=multi-user.target
```
Enable it:

```bash
sudo systemctl daemon-reload
sudo systemctl enable minecraft
sudo systemctl start minecraft
```
Now it survives reboots and auto‑restarts.

---

## Letting People Join (Safely)
On the LAN: join using the Pi’s IP address.

Over the internet:

Forward port 25565/TCP from your router to the Pi.

Keep online-mode=true for proper authentication.

Consider whitelisting players.

Never expose SSH or admin panels to the internet. Keep the Pi updated and don’t overload it with other sensitive services.

---

## Backups and Maintenance
Regularly back up the world folder to another disk or NAS.

Take a backup before major changes.

Monitor CPU/RAM and adjust view distance, mob settings, or player count as needed.

---

## Final Thought
A Pi 5 game server is peak geek: cheap, quiet, and more than capable of hosting a little shared world for you and your mates.

Do it right — separate user, sensible limits, backups, and careful port forwarding — and you get a training lab for Linux and networking and somewhere to blow up blocky mountains after work.

<img src="img/authors/geeky.jpg" width="40"/>