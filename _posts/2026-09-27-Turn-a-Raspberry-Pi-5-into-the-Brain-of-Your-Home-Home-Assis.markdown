---
title:  "Turn a Raspberry Pi 5 into the Brain of Your Home (Home Assistant Deep Dive)"
subtitle: "Full start‑to‑finish build: SSD, OS, Home Assistant, backups, and automations"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/turn-a-raspberry-pi-5-into-the-brain-of-your-home-home.jpg"
date: 2026-09-27
tags: raspberrypi5 home-assistant homelab automation MQTT
---

## What You’re Building

We’re going to turn a Raspberry Pi 5 into a full‑fat Home Assistant hub running from SSD, with proper backups, remote access, and a couple of practical automations (lights and presence). The goal is a setup you’d actually rely on day‑to‑day, not just a weekend toy.

You’ll need:

- Raspberry Pi 5 (ideally 8GB)
- 32GB+ microSD (for flashing only) or direct USB boot
- NVMe SSD + Pi 5 NVMe HAT *or* good USB 3 SSD
- Wired network connection (recommended)
- Optional: Zigbee/Z‑Wave USB stick if you use those

---

## Step 1: Plan Your Topology

Decide:

- Where the Pi will live (stable power, network, decent airflow).
- How it will connect:
  - Wired Ethernet is best for reliability.
- What you’ll integrate:
  - Smart bulbs/switches (Hue, Shelly, Tasmota).
  - Media (TV, speakers).
  - Presence (phones, router, Bluetooth).

Sketch a simple diagram: Pi 5 in the middle, with arrows to router, sensors, and key services. It’ll help later when you add more.

---

## Step 2: Prepare Storage and Boot

### 2.1 Update Pi 5 Bootloader (if needed)

If you’ve used the Pi before, update firmware once via Raspberry Pi Imager:

- On a laptop:
  - Install Raspberry Pi Imager.
  - Choose “Misc utility images → Bootloader”.
  - Flash to microSD, boot Pi once to update.

Newer Pi 5s often ship up‑to‑date, but this ensures good SSD/USB boot support.

### 2.2 Decide: Home Assistant OS vs Supervised vs Container

For a dedicated hub, use **Home Assistant OS**:

- Managed appliance feel.
- Built‑in supervisor, add‑ons, backups.
- Less faff than rolling Docker yourself.

We’ll use Home Assistant OS booting from SSD.

---

## Step 3: Install Home Assistant OS on SSD

### 3.1 Flash the Image

On your laptop:

1. Download Home Assistant OS for Raspberry Pi 5 from the official site.
2. Use Raspberry Pi Imager or Balena Etcher:
   - Select the HA OS image.
   - Target the SSD (via USB dock or NVMe enclosure).
   - Flash and verify.

### 3.2 First Boot

- Connect SSD to Pi 5 (NVMe HAT or USB 3).
- Plug Pi into Ethernet.
- Power on.
- Wait 10–20 minutes for first boot and setup.

Visit:

- `http://homeassistant.local:8123`
- Or: `http://<Pi_IP>:8123`

You should see the onboarding wizard.

---

## Step 4: Initial Home Assistant Setup

### 4.1 Onboarding

- Create an admin user (strong, unique password).
- Set your location, timezone, units.
- Home Assistant will auto‑discover some devices (router, smart TVs, etc.).

### 4.2 Set a Static IP

You want the hub on a fixed address:

- Either reserve DHCP in your router for the Pi’s MAC, or
- Use Home Assistant → Supervisor → Network to set static IP details.

Note the IP; you’ll use it constantly.

---

## Step 5: Basic Hardening and Backups

### 5.1 Enable Multi‑Factor Auth

- Profile → Security.
- Add an authenticator app (TOTP).
- Store recovery codes securely.

This stops “password only” being your single line of defence.

### 5.2 Set Up Backups (Snapshots)

- Go to Settings → System → Backups.
- Create a full backup now.
- Enable automatic backups (e.g. weekly).
- Integrate off‑Pi storage:
  - Add‑on: Google Drive Backup, S3 backup, or NFS mount.

Goal: if the SSD dies, you reinstall HA OS and restore backup. No tears.

---

## Step 6: Add Integrations and Devices

### 6.1 Core Integrations

Common starting points:

- Router presence (UniFi, Fritz!Box, etc.).
- Smart lights (Philips Hue, Shelly, Tasmota).
- Media (Chromecast, Sonos, LG/Samsung TVs).
- Weather (Met Office, OpenWeatherMap).

Go to Settings → Devices & Services → “Add Integration”, search and configure.

### 6.2 Zigbee/Z‑Wave (Optional)

For Zigbee:

- Plug in Zigbee coordinator (e.g. Sonoff/Zigbee USB).
- Install ZHA or Zigbee2MQTT:
  - Add Zigbee2MQTT add‑on.
  - Configure serial port.
- Pair sensors/switches via the integration UI.

For Z‑Wave:

- Similar: plug stick, install Z‑Wave JS add‑on, start including nodes.

---

## Step 7: Build Useful Automations (Not Just Party Tricks)

We’ll create two practical automations: **arrival lights** and **night mode**.

### 7.1 Arrival Lights

Goal: when any family member arrives home after dark, turn on hallway light.

Prereqs:

- Presence:
  - Router‑based device tracking, or
  - Home Assistant Companion app on phones.
- Light entity (hallway).  

Automation:

- Settings → Automations & Scenes → Create Automation.
- Trigger:
  - State change: `person.<name>` from `not_home` to `home`.
- Condition:
  - Sun: after sunset.
- Action:
  - Turn on `light.hallway` with desired brightness and colour.

Test by toggling person state manually or actually going for a walk.

### 7.2 Night Mode and Notifications

Goal: at 23:00, dim certain lights, lower thermostat, silence non‑critical notifications.

Automation:

- Trigger:
  - Time: 23:00.
- Actions:
  - Set scene “Night” (pre‑configured lights).
  - Adjust climate entities.
  - Enable a “quiet” notification mode (e.g. set an `input_boolean.night_mode`).

Then, in other automations, add a condition “only if night_mode is off” for noisy alerts.

---

## Step 8: Remote Access (Safely)

You have two main options:

### 8.1 Home Assistant Cloud (Nabu Casa)

- Paid, but:
  - Encrypted remote access without port forwarding.
  - Easy voice assistant integration.
- Enable via Settings → Home Assistant Cloud.

### 8.2 VPN (WireGuard/OpenVPN)

- Run WireGuard on router or separate Pi.
- Connect from phone/laptop, then access HA via its LAN IP.
- This avoids exposing HA directly to the internet.

For most people, VPN or Nabu Casa is safer than DIY reverse proxies with port forwards.

---

## Step 9: Monitor and Maintain

Healthy hub behaviour:

- CPU/RAM under ~50–60% most of the time.
- SSD S.M.A.R.T. OK.
- Regular backups succeeding.

Use:

- Settings → System → Logs.
- Add System Monitor integration for CPU, memory, disk, temperature.

Plan:

- Monthly:
  - Update Home Assistant + add‑ons.
  - Check backup restore test occasionally.
- When adding devices:
  - Keep notes on what’s paired, where, and how.

---

## Optional: Integrate with Your Wider Homelab

On a Pi 5 you can also:

- Expose metrics to Prometheus + Grafana.
- Feed logs into Wazuh/Elastic for unified monitoring.
- Use MQTT as a central bus for other DIY projects.

Home Assistant then becomes the human‑friendly layer on top of your increasingly nerdy network.

---

## Final Notes

You now have:

- Pi 5 booting from SSD with Home Assistant OS.
- Static IP, backups, and MFA.
- Integrations for your common devices.
- A couple of useful automations you’ll feel daily.

From here, the fun is incremental:

- Add more sensors.
- Refine automations.
- Integrate with your security and homelab stack.

This is the kind of project that makes your life easier *and* teaches you skills you’ll reuse constantly as a DevOps/security/homelab engineer.

---

<img src="img/authors/geeky.jpg" width="40"/>