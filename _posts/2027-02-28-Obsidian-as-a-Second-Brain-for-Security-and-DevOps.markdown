---
title:  "Obsidian as a Second Brain for Security and DevOps"
subtitle: "Turning scattered notes into an actual knowledge system"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/obsidian-as-a-second-brain-for-security-and-devops.jpg"
date: 2027-02-28
tags: Obsidian note-taking PKM security devops learning
---

## Obsidian as a Second Brain for Security and DevOps

Obsidian is one of the few tools that actually makes you think better instead of giving you another place to park half‑finished notes. It's perfect if you're juggling CTFs, on‑call incidents, K8s weirdness, threat models you keep meaning to formalise, and "I should turn this into a talk later" moments.

This is the working setup I use after years of trying every productivity tool that wasn't bolted to the floor. Concrete templates, real Dataview queries that pay off in security and DevOps work, a vault structure that doesn't fight you, and the things you should *not* put in a vault even when it's local-first.

---

## Why Obsidian Works for Technical People

At its core, Obsidian is "just" a local Markdown editor with superpowers: links between notes, a graph view, and a healthy ecosystem of plugins (Dataview, Templater, Tasks, Git).

For security, DevOps, and learning specifically:

- **Local-first by default.** Sensitive thinking stays on your disk, not in someone else’s cloud. Obsidian Sync is end-to-end encrypted; the alternative is rolling your own with Git or iCloud Drive (more on that below).
- **Plain Markdown.** Plays nicely with `git diff`, `grep`, scripts, and any future tool. You're not locked into a database format that needs the vendor's editor.
- **Dataview turns notes into a queryable database.** This is the killer feature for security/DevOps work. Tag every incident or CTF the same way and you get a live dashboard for free.
- **The graph isn't gimmick.** When you can see that "JWT" connects to four incidents, six CTFs, two talks, and a runbook, you stop forgetting what you've already learned.

---

## Step 1: A Vault Structure That Doesn’t Fight You

Don't spend three hours designing the perfect taxonomy. The real magic is links and Dataview, not folders. A working structure that I've used for years:

```
GeekyBlinder-Knowledge/
├── 00-Inbox/                  # capture-everything dump; weekly triage
├── 01-Maps/                   # high-level index notes (manuals from future-you)
│   ├── Security Fundamentals.md
│   ├── Kubernetes.md
│   ├── Cloud Security.md
│   └── On-Call Runbook Index.md
├── 02-Projects/               # things with an end-state
│   ├── Build Startup Security Baseline/
│   ├── K8s Cluster Hardening 2027/
│   └── Talk - DevSecOps for Startups/
├── 03-Areas/                  # ongoing responsibility, no end-state
│   ├── Security/
│   │   ├── Concepts/          # JWT, OAuth, mTLS, etc.
│   │   ├── Threat Models/     # one per system
│   │   ├── Incidents/         # post-mortems
│   │   └── CTF/               # writeups
│   ├── DevOps/
│   ├── Cloud/
│   └── Learning/
├── 04-Reference/              # vendor docs, papers, snippets you actually use
├── 99-Archive/                # done projects, retired material
├── _templates/                # Templater templates (see below)
└── _meta/                     # vault config, plugin notes
```

This is the [PARA-style](https://fortelabs.com/blog/para/) layout (Projects, Areas, Resources, Archive) with security-relevant areas pre-cut. Maps are the bit most people skip — high-level index pages with handpicked links into your areas. They’re what makes a 5,000-note vault still feel small.

---

## Step 2: Daily Notes and Templates That Pay Off

Turn on the **Daily notes**, **Templates**, and **Templater** plugins. Templater is the upgrade over the core Templates plugin — supports JS, dynamic dates, and prompts.

A daily-notes template that costs you 30 seconds and saves you hours over a year:

```markdown
---
date: <% tp.date.now("YYYY-MM-DD") %>
day: <% tp.date.now("dddd") %>
tags: [daily]
---

# <% tp.date.now("YYYY-MM-DD - dddd") %>

## Today
- [ ] Main focus:
- [ ] On-call status: green / amber / red

## Learning
- [[Concept] -

## Incidents / Findings
-

## Ideas
-

## Tomorrow
- [ ]
```

A threat-model template — drop into `_templates/threat-model.md`, then "New from template" anywhere:

```markdown
---
type: threat-model
system:
status: draft
last_review:
owner:
classification: internal
tags: [threat-model]
---

# Threat Model: {{system}}

## Scope
- What's in scope:
- What's out of scope:

## Assets
- Crown jewels:
- Supporting:

## Trust Boundaries
- (what crosses each boundary, who controls each side)

## Data Flows
- (mermaid diagram or ascii)

## STRIDE
- **Spoofing:**
- **Tampering:**
- **Repudiation:**
- **Information Disclosure:**
- **Denial of Service:**
- **Elevation of Privilege:**

## Top Risks (Likelihood × Impact)
| # | Risk | L | I | Mitigation | Owner | Due |
|---|------|---|---|------------|-------|-----|

## Open Questions
-

## Related
- [[Concept]]
- [[On-Call Runbook]]
```

An incident post-mortem template — same shape, different topic:

```markdown
---
type: incident
incident_id: INC-2027-NN
date:
severity: SEV1 | SEV2 | SEV3
duration_min:
service:
detection: alert | customer | manual
status: open | resolved | post-mortem-written
tags: [incident]
---

# {{title}}

## TL;DR
- What broke:
- Customer impact:
- Resolution:

## Timeline (UTC)
- HH:MM —

## Symptoms
-

## Root Cause
-

## What Went Well
-

## What Didn't
-

## Action Items
- [ ] (assigned to / due)

## Related
- [[Service]]
- [[Similar Incident]]
```

A CTF/THM writeup template that ties to your training tracker:

```markdown
---
type: ctf
platform: TryHackMe | HackTheBox | PortSwigger | other
difficulty: easy | medium | hard | insane
status: in-progress | completed
date_started:
date_completed:
category: [web, network, crypto, forensics, pwn]
tags: [ctf]
---

# {{title}}

## Overview
- Platform / Box:
- Difficulty:
- Tags:

## Recon
- Tools:
- Findings:

## Exploitation
- Entry point:
- Payload:
- Reference: [[Concept]]

## Privilege Escalation
- Technique:
- Misconfig / vuln type:

## Flags
- User:
- Root:

## Lessons Learned
-

## Related
- [[Concept]]
```

The discipline is consistency. Five different threat models in five different shapes is useless; five identical-shaped ones become a queryable library overnight.

---

## Step 3: Dataview Queries That Earn Their Keep

The point of consistent frontmatter is what comes next. A few queries that pay off in real security/DevOps work:

**Open threat models with stale review dates:**

````
```dataview
table without id
  file.link as "System",
  classification as "Class",
  owner as "Owner",
  last_review as "Last Reviewed"
from "03-Areas/Security/Threat Models"
where status != "archived"
  and (last_review = null or last_review < date(today) - dur(180 days))
sort last_review asc
```
````

**Incidents grouped by service for the last quarter** — patterns jump out fast:

````
```dataview
table without id
  service as "Service",
  length(rows) as "Incidents",
  rows.file.link as "Postmortems"
from "03-Areas/Security/Incidents"
where date >= date(today) - dur(90 days)
group by service
sort length(rows) desc
```
````

**CTF tracker with completion stats** — your own training LMS:

````
```dataview
table without id
  file.link as "Box",
  platform as "Platform",
  difficulty as "Difficulty",
  status as "Status",
  date_completed as "Completed"
from "03-Areas/Security/CTF"
where type = "ctf"
sort date_completed desc
limit 30
```
````

**Concept hubs that need attention** — notes that are linked from many places but are themselves thin:

````
```dataview
table without id
  file.link as "Concept",
  length(file.inlinks) as "Linked from",
  length(file.tasks) as "Open TODOs",
  file.size as "Size (bytes)"
from "03-Areas/Security/Concepts"
where length(file.inlinks) >= 3 and file.size < 1500
sort length(file.inlinks) desc
```
````

That last query is genuinely useful — it surfaces the concepts your future self keeps wanting to reference and that you keep forgetting to flesh out.

---

## Step 4: Use Obsidian *While* You Work

The big unlock is keeping Obsidian open *during* the work, not after. Quick capture during:

- A THM room → CTF template gets filled live, not from memory.
- A production incident → incident template at the start, timeline grows in real-time, post-mortem half-written by the time the incident closes.
- Architecture review → threat-model template captures STRIDE rows as they come up.
- Learning a concept → concept note in `03-Areas/[domain]/Concepts/` gets a stub the first time, gets fleshed out the second, becomes a reference the third.

After a few months of this you have a personal threat library tuned to your stack, ready-made material for blog posts and talks, and patterns that jump out — "these four incidents all involved missing timeouts" or "every K8s exploit I've solved involved a misconfigured ServiceAccount".

For the writeup pattern specifically, see [How To Write a CTF Writeup That's Actually Worth Reading](https://geekyblinder.co.uk/#/2026/02/01/How-To-Write-a-CTF-Writeup).

---

## Step 5: Sync and Backup (Without Leaking Your Vault)

Two patterns that work, depending on threat model:

**Obsidian Sync** — official, end-to-end encrypted, ~£8/month. Easiest if you've got more than one device and don't want to think about it. Encryption keys never leave your device; vendor can't read your notes.

**Git** — flexible, free, Git-native diff and history. Pair with `obsidian-git` plugin for auto-commit. Works well if your vault is one-person and you keep it on a private repo.

If you go the Git route, the gotcha is **don't ever commit secrets**. Add a pre-commit hook with [`gitleaks`](https://github.com/gitleaks/gitleaks) to refuse to commit anything that looks like a secret:

```bash
# .git/hooks/pre-commit (or use pre-commit framework)
gitleaks protect --staged --redact --verbose
```

A `.gitignore` for the obvious sensitive paths doesn't hurt either:

```gitignore
.obsidian/workspace.json
.obsidian/workspace-mobile.json
00-Inbox/scratch/
*.pcap
*.har
*.kdbx
.env*
**/secrets/
```

---

## Step 6: What *Not* to Put in Your Vault

Local-first doesn't mean attack-resistant. Things to never put in plain text in your vault, however convenient:

- **Real production secrets.** API keys, passwords, TLS keys, customer PII. Use a password manager (1Password, Bitwarden) — see [Password Managers](https://geekyblinder.co.uk/#/2026/02/15/Password-Managers).
- **Customer data.** Even debugging output — redact before pasting. Especially if your sync is anything other than Obsidian Sync's E2E.
- **Active engagement findings.** If you're doing pen-testing work, exploitation details for live targets stay in the engagement vault with proper retention controls, not in your personal second brain.
- **Things you're under NDA on.** "I'll just paste the architecture here for context" is how NDAs become incident reports.

The lazy rule: if a screenshot of the note would be embarrassing in The Register, it doesn't go in the vault.

---

## Step 7: Plugins Worth the Friction

Default install comes with the basics. Add these and stop there:

- **Templater** — every template you'll write benefits from this over the core Templates plugin.
- **Dataview** — non-negotiable for the queries above.
- **Tasks** — for `- [ ]` TODOs across the whole vault, with due dates and recurring tasks.
- **Obsidian Git** — auto-commit, useful even if you don't push to a remote.
- **Excalidraw** — quick architecture diagrams and threat-model data flows. Better than mermaid for anything visual.
- **Advanced Tables** — turns markdown table editing from awful to bearable.

Resist the urge to add 30 plugins. Each is a maintenance cost when Obsidian updates break them.

---

## Final Thought

Used well, Obsidian becomes a security engineer's private, evolving runbook plus lab notebook plus content engine plus training tracker, all in one folder you control. Used badly, it’s another place to forget things — slightly prettier than the last one.

The pattern that matters: capture during the work, structure with consistent frontmatter, query with Dataview when you want to spot patterns, and link aggressively. Give it a week where every fix, break, and learning passes through Obsidian. If you don’t feel sharper at the end, I’ll eat my YAML.

<img src="img/authors/geeky.jpg" width="40"/>
