---
title:  "Tmux: The Tool That Makes Your Terminal Feel Like a Cockpit"
subtitle: "Deep skills, not just a cheat sheet"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/tmux-the-tool-that-makes-your-terminal-feel-like-a-cock.jpg"
date: 2026-12-20
tags: tmux terminal linux productivity devops
---

## Tmux: The Tool That Makes Your Terminal Feel Like a Cockpit

Tmux is one of those tools that quietly separates “someone who can use a shell” from “someone who *lives* in the shell.” It’s perfect for remote work, long‑running jobs, CTFs, and serious DevSecOps work.

Here’s how to go beyond the cheat sheet and actually own it.

---

## Core Concepts: Sessions, Windows, Panes

If you understand these three, you understand tmux:

- **Session** – a whole tmux “workspace”. You can detach and reattach to it later.
- **Window** – like a tab inside a session, each with its own layout.
- **Pane** – splits inside a window (like tiling terminals).

Example homelab / security layout:

- One session per *engagement* (`pentest-clientA`, `lab-thm`, `homelab`).
- Windows per *activity* (`recon`, `web-app`, `notes`, `infra`).
- Panes for *supporting views* (logs, shells, editors).

---

## Getting Started: Install, Detach, Reattach

Install tmux:

```bash
# Debian/Ubuntu
sudo apt install tmux

# RHEL/Fedora
sudo dnf install tmux
```

Basic flow:

tmux new -s ctf – new session called ctf.

Detach: Ctrl-b d.

List: tmux ls.

Reattach: tmux a -t ctf.

Training drill:

SSH into a box, start tmux new -s practice.

Run ping 8.8.8.8.

Detach, close SSH.

Reconnect, reattach, enjoy the still‑running ping.

Windows and Panes: Organising Your Brain
Windows (tabs):

New window: Ctrl-b c.

Next/prev: Ctrl-b n / Ctrl-b p.

Rename: Ctrl-b ,.

List: Ctrl-b w.

Panes (splits):

Vertical split: Ctrl-b %.

Horizontal split: Ctrl-b ".

Move: Ctrl-b + arrows.

Show numbers: Ctrl-b q then number.

Example CTF layout:

Window recon: two panes (nmap + shell).

Window web: two panes (ffuf + curl).

Window notes: one pane (vim/neo‑vim).

Same pattern every time; your brain knows where to look.

Customising Tmux Without Going Mad
Edit ~/.tmux.conf and add:

Mouse support:

```bash
set -g mouse on
```
Vi‑style keys in copy mode:

```bash
setw -g mode-keys vi
```
(Optional) change prefix:

```bash
set -g prefix C-a
unbind C-b
bind C-a send-prefix
```
Restart tmux or tmux source-file ~/.tmux.conf to apply.

Using Tmux as a Training Tool
Make tmux part of your learning:

Rule: any serious task (THM room, homelab change, incident) happens in a named tmux session.

Keep a dedicated ops session for on‑call with:

Window dash: metrics, kubectl get pods, logs.

Window deploy: CI/CD, helm upgrade.

Window notes: incident scratchpad.

For multi‑host work:

One window, one pane per host.

Enable sync: Ctrl-b :setw synchronize-panes on.

Run commands across all at once (carefully!).

A 7‑Day Tmux Challenge
To actually own tmux:

Day 1–2: sessions only; always use tmux new -s.

Day 3–4: add windows; standardise shell + notes.

Day 5: add panes; practise splits and navigation.

Day 6: add small customisations (mouse, vi mode).

Day 7: complete a full THM room using only tmux and your editor.

By the end of that week, tmux stops being “extra keystrokes” and starts being home. And once the shell is home, everything else gets easier.


<img src="img/authors/geeky.jpg" width="40"/>
