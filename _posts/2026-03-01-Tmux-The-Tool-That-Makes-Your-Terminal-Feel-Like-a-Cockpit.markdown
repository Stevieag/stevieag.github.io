---
title:  "Tmux: The Tool That Makes Your Terminal Feel Like a Cockpit"
subtitle: "Deep skills, not just a cheat sheet"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/tmux-the-tool-that-makes-your-terminal-feel-like-a-cock.jpg"
date: 2026-03-01
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

bash
set -g mouse on
Vi‑style keys in copy mode:

bash
setw -g mode-keys vi
(Optional) change prefix:

bash
set -g prefix C-a
unbind C-b
bind C-a send-prefix
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

text

***

```markdown
---
title:  "Work–Life Balance in Tech Isn’t a Wellness Poster"
subtitle: "How to stay sane in startups and still ship"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/work-life-balance-in-tech-isnt-a-wellness-poster.jpg"
date: 2026-03-01
tags: burnout startups mental-health worklife leadership
---

## Work–Life Balance in Tech Isn’t a Wellness Poster

Work–life balance in tech isn’t about scented candles and a mindfulness app you never open. It’s about not burning your life down for someone else’s backlog — especially in startups, where the line gets blurred on purpose.

Let’s talk about what balance actually looks like when you’re shipping hard, how to protect yourself, and what a halfway decent leadership team should be doing.

---

## Hustle Culture vs Actually Getting Things Done

Tech and startups love the myth of the heroic 80‑hour week. “We’re a family.” “We’re all in this together.” Translation: we didn’t plan properly and you’re going to pay for it with your evenings.

A few awkward truths:

- Burnout is ridiculously common among software engineers and worse in fast‑moving environments.
- Long hours past a certain point don’t increase output; they just increase mistakes and attrition.
- Startups with “permanent crunch” often lose their best people just as things get interesting.

Balance is not “never work late.” Balance is “if we push hard for a week, it’s unusual, deliberate, and followed by recovery — not the default.”

---

## Why Startups Are Uniquely Bad at Balance

Startups are ambiguity machines. Common patterns:

- You wear five hats: infra, security, release engineer, part‑time therapist.
- Everything is “critical” because priorities are fuzzy.
- Slack and PagerDuty bleed into evenings, weekends, and holidays because nobody drew a line.

Passion hides overwork. If you care about the mission, it’s easy to normalise 12‑hour days. Remote/hybrid blurs home and work until your laptop might as well be grafted onto your hands.

None of this is inevitable. It’s a choice — by founders, managers, and sometimes by us when we don’t set boundaries.

---

## What Work–Life Balance Actually Looks Like

Real balance looks like:

- Defined work hours that mean something.
- Protected off‑time: no expectation of responding to non‑urgent messages at night or on holidays.
- Deep work without constant pings: meeting‑free or Slack‑light blocks so you can actually think.
- Pacing, not sprinting forever: intense pushes followed by deliberate slowdowns.

Personally, it also means:

- Having non‑negotiables outside tech (family, hobbies, sport, whatever).
- Being able to stop thinking about that broken microservice long enough to sleep properly.

---

## How to Protect Yourself Without Torching Your Career

Practical moves:

- Set explicit boundaries *and* communicate them.
- Guardrails around tools: mute non‑critical channels outside work, separate work and personal profiles.
- Say “yes, but”: “Yes, I can jump on this incident, but that means feature X slips — which do you prefer?”
- Use data: track hours and error rates; bring that to your manager if things creep into 60–70 hour territory.
- Know your line: decide what “too far” looks like (permanent weekends, missing important life stuff, health impacts).

If the company normalises that for months, that’s data about the culture, not a reflection on you.

---

## What Good Leaders and Startups Should Be Doing

Healthy leadership:

- Plans realistically and cuts scope instead of casually demanding heroics.
- Models boundaries — not sending non‑urgent messages at 11 pm.
- Has clear on‑call structure with compensation and recovery time.
- Talks about burnout like it’s real, because it is.

If you’re leading a team: this is part of your job. If you’re not yet, this is what you should expect from the people who are.

---

## Final Thought

The industry loves to talk about “sustainable scaling” for systems. It talks a lot less about sustainable scaling for humans.

Work–life balance isn’t about doing less. It’s about choosing where your energy goes so you can still show up sharp — for your team, your users, and your life outside the keyboard. If your current setup makes that impossible, the problem isn’t your resilience. It’s the system you’re in — and systems can be changed, or left.

<img src="img/authors/geeky.jpg" width="40"/>