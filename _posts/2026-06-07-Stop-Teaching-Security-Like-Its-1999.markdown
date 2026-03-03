---
title:  "Stop Teaching Security Like It’s 1999"
subtitle: "Turn your homelab, codebase, and AI tools into a brutal (but fun) training ground"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/stop-teaching-security-like-its-1999.jpg"
date: 2026-06-07
tags: education security training devsecops AI hands-on TryHackMe
---

## Security Training Is Boring. Attackers Aren’t.

Most “security training” is still slide decks, checkbox quizzes, and videos nobody actually watches. Meanwhile, attackers are using AI, custom tooling, and your own cloud against you.

If you want to keep up in 2026, you need to stop thinking in terms of “completed an annual module” and start thinking in terms of **reps**: hands‑on labs, live fire drills, and feedback loops that look a lot more like how we train pilots than how we train office workers.

---

## Why Hands‑On Beats Slide‑Decks

Static training has three big problems:

- It’s generic — examples rarely match your stack or risks.
- It’s passive — you watch, click “Next”, forget.
- It’s unmeasured — you tick compliance boxes without knowing if anyone can actually handle a real incident.

Hands‑on labs flip that:

- You work with **realistic systems** (web apps, cloud, K8s, CI/CD).
- You see what insecure code actually does, not just what a bullet list says.
- You can track **practical skills**, not just quiz answers.

Platforms like TryHackMe, Hack The Box, AppSecEngineer and others have proved this model works at scale: safe, guided labs with progressive difficulty and realistic objectives.

Now take that mindset and apply it to your own world.

---

## Level 1: Use Existing Platforms as Your “Security Gym”

If you’re starting out, don’t reinvent the entire training stack.

Good starting points:

- TryHackMe:
  - SOC Level 1, Jr Penetration Tester pathways.
  - Great for network, web, and blue‑team basics.
- Other hands‑on platforms:
  - Cover secure coding, cloud, DevSecOps, K8s, threat modelling.

How to use them *properly*:

- Block out regular time (e.g. 2–4 hours a week).
- Treat each room/lab like a mini engagement:
  - Recon, exploitation, *and* remediation.
- Keep writeups:
  - What the bug was.
  - How you found it.
  - How you’d fix it for real.

This becomes your **muscle memory** and your portfolio.

---

## Level 2: Turn Your Codebase into Custom Labs

Generic labs are great; **your own code** is better.

Pain points we see again and again:

- Bad authentication and weak roles.
- Insecure direct object references (IDOR).
- Injection via unparameterised queries.
- Secrets in code and configs.
- Ignored dependency vulnerabilities (supply chain issues).

Instead of just talking about these, deliberately **build small, vulnerable versions** of the patterns you actually use:

- Take a slice of your stack (e.g. a feature service).
- Clone it to a lab version.
- Inject controlled flaws:
  - Hardcoded API key.
  - Missing authz checks.
  - Raw string concatenation in DB queries.
- Wrap it as a self‑contained lab with:
  - “User story” style background.
  - Clear objectives (“steal user B’s data”, “pop RCE from this endpoint”).
  - Bonus: “fix this and write a test so it doesn’t come back.”

You can do this manually or with tools that help turn your own code into labs.

---

## Level 3: Make Your Homelab a Training Range

Your homelab doesn’t have to just run Plex and Jellyfin. It can be your personal cyber range.

Combine ideas:

- **Offensive**:
  - Vulnerable apps (DVWA, Juice Shop, etc.).
  - Misconfigured cloud resources (open buckets, over‑broad IAM).
- **Defensive**:
  - Wazuh or Security Onion.
  - Suricata or Zeek sensors.
  - ELK/OpenSearch for logs.

Then run drills:

- “This weekend I’m going to:
  - Exploit an IDOR in my lab web app.
  - Watch the HTTP/access logs.
  - Write a basic detection rule in Wazuh/Suricata.”
- “Next weekend:
  - Abuse an over‑permissive EC2 role.
  - Watch CloudTrail/logs.
  - Model how I’d stop this in production.”

You’re training your hands and your **eyes** — how attacks look from the defender’s perspective.

---

## Level 4: Add AI, But Don’t Let It Do the Work For You

AI is now everywhere in cyber: attackers using it for recon, phishing, and evasion; defenders using it for hunting and triage.

Good, educational uses in your lab:

- Ask AI to:
  - Explain vulnerabilities you encounter in your own words.
  - Generate variants of payloads you then test and debug.
  - Quiz you on topics you’ve just covered (“ask me 5 questions about IDOR and API authz”).

Bad uses:

- Paste entire lab solutions or exploit scripts and never understand them.
- Let AI generate code or K8s manifests you ship without really reading.

In training, AI should be your **coach**, not your autopilot.

---

## Level 5: Design “Micro‑Engagements” That Feel Real

The most exciting (and useful) training is when it feels like real work.

Examples you can build:

- **Micro‑bounty** in your own cloud:
  - Tiny SaaS: login, profile, document upload.
  - Plant:
    - One obvious vuln (e.g. missing authz).
    - One subtle misconfig (e.g. over‑permissive storage bucket).
  - Write a “program brief”:
    - Scope, rules, rewards (even if it’s just kudos).
  - Attack it like a researcher, then fix it like the internal security engineer.

- **Internal red/blue drills**:
  - Red:
    - Use your lab to practise an attack chain end‑to‑end.
  - Blue:
    - Use your logging stack to detect it.
  - Retrospective:
    - What worked?
    - What would you change in a real environment?

- **Developer‑focused labs**:
  - Show a simple insecure pattern from your codebase.
  - Let devs exploit it.
  - Then guide them to implement the fix and add tests.

This is where training starts to feel like a game — but a game that actually makes you better at your job.

---

## Level 6: Avoid the Top 5 Developer Security Traps (By Practising Them)

If you’re a dev or DevOps, your “exciting” training should be targeted at the stuff that bites most teams.

Five to always cover:

1. **Injection**
   - SQL, NoSQL, command, LDAP.
   - Lab: insecure query; goal is to exploit, then parameterise and test.

2. **Broken auth & weak permissions**
   - Logged‑in vs allowed is not the same.
   - Lab: change an ID in a URL to read someone else’s data (IDOR); then fix.

3. **Secrets in code and configs**
   - API keys, DB creds, tokens in repos.
   - Lab: leak a fake key, find it with grep/trufflehog; then move to a vault.

4. **Dependency hell (supply chain)**
   - Outdated/vulnerable packages, malicious deps.
   - Lab: add a known vulnerable version, observe SCA tools flag it, patch and re‑test.

5. **Missing logging and monitoring**
   - The vuln matters, but so does seeing it.
   - Lab: trigger attacks, then add structured logging, dashboards, and alerts.

Once you’ve broken each one in a safe lab and fixed it properly, you’ve got a deep understanding that no multiple‑choice test will ever give you.

---

## How to Turn All This into Career Firepower

Don’t just do labs and walk away. Capture it.

- Keep a **learning log**:
  - Date, lab, techniques, “aha” moments.
- Turn the best scenarios into:
  - Blog posts (sanitised, educational).
  - Internal brown‑bag sessions.
  - THM‑style live streams.
- Tie it to the trends:
  - AI‑assisted attacks and defence.
  - Cloud‑native threats and continuous monitoring.
  - Developer security mistakes you now know how to spot.

When you can tell a story like:

> “I built a mini‑SaaS in my lab, found my own auth bugs, exploited them, instrumented logging, and then used that pattern to harden our real services.”

…you’re no longer just “someone who did some CTFs.” You’re someone who can design, attack, and defend modern systems — and bring everyone else along for the ride.

That’s not just exciting. That’s rare.

<img src="img/authors/geeky.jpg" width="40"/>