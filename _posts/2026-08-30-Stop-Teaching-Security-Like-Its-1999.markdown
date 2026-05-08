---
title:  "Stop Teaching Security Like It's 1999"
subtitle: "Turn your homelab, codebase, and AI tools into a brutal (but fun) training ground"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/stop-teaching-security-like-its-1999.jpg"
date: 2026-08-30
tags: education security training devsecops AI hands-on TryHackMe
---

## Security Training Is Boring. Attackers Aren't.

Most "security training" is still slide decks, checkbox quizzes, and the same e-learning videos nobody watches. Meanwhile, attackers are using AI, custom tooling, and your own cloud against you.

If you want to keep up in 2026, stop thinking in terms of "completed an annual module" and start thinking in terms of **reps** — hands-on labs, live drills, and feedback loops that look more like how we train pilots than how we train office workers.

This post is the working playbook: which platforms to use as warm-ups, how to convert your own codebase into custom labs (with a real worked example), how to wire your homelab as a training range, and how to design micro-engagements that feel like actual work. Pairs with [Building a Home Lab to Learn Hacking Without Going to Jail](https://geekyblinder.co.uk/#/2026/07/19/Building-a-Home-Lab-to-Learn-Hacking-Without-Going-to-Jail).

---

## Why Hands-On Beats Slide-Decks

Static training has three big problems:

- **Generic.** Examples rarely match your stack or your risks.
- **Passive.** You watch, click "Next", forget.
- **Unmeasured.** You tick compliance boxes without knowing if anyone can handle a real incident.

Hands-on labs flip every one of those:

- You work with realistic systems — web apps, cloud, K8s, CI/CD.
- You see what insecure code actually does, not what a bullet list says.
- You can track practical skills, not just quiz answers.

[TryHackMe](https://tryhackme.com/), [Hack The Box](https://www.hackthebox.com/), [PortSwigger Web Security Academy](https://portswigger.net/web-security), and [AppSecEngineer](https://www.appsecengineer.com/) prove the model works at scale: safe, guided labs with progressive difficulty and realistic objectives. Take that mindset and apply it to your own systems.

---

## Level 1: Use Existing Platforms as Your "Security Gym"

If you're starting out, don't reinvent the entire training stack.

**Useful starting paths in 2026:**

- **TryHackMe** — SOC Level 1, Jr Penetration Tester, Cyber Defence pathways. Strong for fundamentals.
- **HackTheBox Academy** — covers the same ground with more depth on bug-bounty patterns and active-directory work.
- **PortSwigger Academy** — best free web-security training out there, full stop. Walks you through every common bug class with hands-on labs.
- **AppSecEngineer** — secure coding, cloud, DevSecOps, K8s, threat modelling, AI security. The breadth is the point.
- **CyberDefenders / LetsDefend / SANS Cyber Aces** — blue-team focused alternatives for SOC-shaped roles.

**How to use them properly:**

- Block out regular time. Two hours a week beats sixteen hours once a quarter.
- Treat each room/lab like a mini engagement: recon, exploitation, *and* remediation.
- Keep writeups (see [How To Write a CTF Writeup That's Actually Worth Reading](https://geekyblinder.co.uk/#/2026/02/01/How-To-Write-a-CTF-Writeup)). The writeup is where the learning consolidates.

This becomes your muscle memory and your portfolio.

---

## Level 2: Turn Your Codebase Into Custom Labs

Generic labs are great. Your own code is better — because the attack patterns map directly to systems your team will actually ship.

**The pain points that bite most teams:**

- Bad authentication, weak permissions.
- Insecure direct object references (IDOR).
- Injection via unparameterised queries.
- Secrets in code and configs.
- Ignored dependency vulnerabilities (supply chain).

Instead of just talking about these, deliberately build small vulnerable versions of the patterns you actually use.

### A Worked Example: Forking a Service into a Lab

Take a real-ish service from your stack — a small Go or Node API, ideally one with auth and a database. Fork it into a `<service-name>-lab` repo. Then *deliberately* inject vulnerabilities into the fork.

**Example diff (Node/Express, fictional `orders-service`):**

```diff
// orders.js — the lab fork

 router.get('/orders/:id', requireAuth, async (req, res) => {
-  const order = await db.orders.findOne({
-    where: { id: req.params.id, userId: req.user.id }   // ownership check
-  });
+  const order = await db.orders.findOne({
+    where: { id: req.params.id }                         // ⚠️ IDOR — no ownership
+  });
   if (!order) return res.status(404).send();
   res.json(order);
 });

 router.get('/orders/search', requireAuth, async (req, res) => {
-  const rows = await db.query(
-    'SELECT id, total FROM orders WHERE customer LIKE ?',
-    [`%${req.query.q}%`]
-  );
+  const rows = await db.query(
+    `SELECT id, total FROM orders WHERE customer LIKE '%${req.query.q}%'`   // ⚠️ SQLi
+  );
   res.json(rows);
 });
```

Wrap the fork in a brief students can follow:

```markdown
# Lab: orders-service-lab

## Background
Internal orders service. Authenticated; uses session cookies.
You have a developer test account: alice@example.com / labpass1.

## Objectives
1. Read the orders of another user without their credentials.
2. Extract the schema of the orders database.
3. Identify and fix both bugs in code. Add regression tests.

## Rules
- Document each finding (request used, response, severity, recommended fix).
- For the fix, open a PR against the lab repo with your changes.
- Bonus: add a unit test that fails on the vulnerable version.

## Reference
- Auth, OAuth, and JWTs — [link]
- OWASP API Security Top 10 — [link]
```

Stash the lab brief in a `LAB.md` in the repo. Run sessions monthly with rotating engineers; each session, swap two lab repos so people see different patterns. Capture findings in a `FINDINGS-<date>.md` per session and review next month.

### Automate the Pattern at Scale

If you've got more than one team, [Snyk Learn](https://learn.snyk.io/), [SecureFlag](https://www.secureflag.com/), and [Avatao](https://avatao.com/) let you upload your own code (or representative variants) and turn them into managed labs with grading. Worth the cost if you're trying to do this for an org of 100+ engineers.

For solo / small-team work, the hand-rolled fork pattern above is plenty.

---

## Level 3: Make Your Homelab a Training Range

Your homelab doesn't have to just run Plex and Jellyfin. It can be your personal cyber range. The full setup is in [Building a Home Lab to Learn Hacking Without Going to Jail](https://geekyblinder.co.uk/#/2026/07/19/Building-a-Home-Lab-to-Learn-Hacking-Without-Going-to-Jail). The shape:

- **Offensive layer.** Vulnerable apps (DVWA, Juice Shop, your own lab forks). Misconfigured cloud resources (open buckets, over-broad IAM, unrestricted egress).
- **Defensive layer.** Wazuh or Security Onion. Suricata or Zeek sensors. ELK / OpenSearch / Loki for logs. Falco for K8s runtime.

### A Concrete Drill You Can Run This Weekend

**Saturday morning — attack:**

```
Goal: exploit IDOR in the lab orders-service.
Steps:
  1. Log in as alice. GET /orders/<your-id>. Note response.
  2. GET /orders/<another-id>. Confirm IDOR.
  3. Capture the request/response in Burp.
  4. Repeat with a SQLi payload in /orders/search.

Time-box: 60 min.
```

**Saturday afternoon — defend:**

```
Goal: detect both attacks from logs alone.
Steps:
  1. Open access log. Identify suspicious patterns.
  2. Write a Wazuh rule that fires on IDOR-shaped behaviour
     (same user-agent hitting many distinct order IDs in a window).
  3. Write a Wazuh rule that fires on SQLi-shaped query strings.
  4. Re-run the attacks. Confirm rules fire. Tune for noise.

Time-box: 90 min.
```

A starter Wazuh rule for the SQLi-shape (drop in `/var/ossec/etc/rules/local_rules.xml`):

```xml
<group name="webattacks,">
  <rule id="100501" level="10">
    <if_sid>31104,31108,31151</if_sid>
    <regex type="pcre2">UNION\s+SELECT|sleep\(\d+\)|--\s*$</regex>
    <description>Possible SQL injection attempt</description>
    <mitre><id>T1190</id></mitre>
  </rule>
  <rule id="100502" level="8">
    <if_sid>31104</if_sid>
    <field name="data.url">/orders/\d+</field>
    <same_source_ip />
    <different_url />
    <frequency>15</frequency>
    <timeframe>120</timeframe>
    <description>Possible IDOR scan: many distinct order IDs from one source</description>
  </rule>
</group>
```

You're training your hands *and* your eyes — what attacks look like from the defender's perspective. Most engineers miss the second part entirely.

---

## Level 4: Add AI, But Don't Let It Do the Work For You

AI is now everywhere in cyber: attackers using it for recon, phishing, and evasion; defenders using it for hunting and triage. (See [AI Hacking for Red and Blue Teams](https://geekyblinder.co.uk/#/2027/03/28/AI-Hacking-for-Red-and-Blue-Teams-Friends-Foes-and-Autonomou) for the deeper picture.)

**Good educational uses in your lab:**

- Ask AI to explain a vulnerability you encountered in your own words. Then check the explanation against the OWASP/CWE entry.
- Generate variants of payloads you then test, debug, and explain.
- Quiz yourself: *"Ask me 5 questions about IDOR and API authz, mark me harshly, show strong answers only after I try."*
- Translate detection requirements into draft Sigma/KQL/SPL rules.

**Bad uses:**

- Paste entire lab solutions or exploit scripts and never understand them.
- Let AI generate code or K8s manifests you ship without reading.
- Ship AI-suggested package names without checking they exist on the real registry.

In training, AI should be your coach, not your autopilot. The full thinking lives in [Using AI to Learn Without Turning Your Brain to Slop](https://geekyblinder.co.uk/#/2026/03/15/Using-AI-to-Learn).

---

## Level 5: Design "Micro-Engagements" That Feel Real

The most useful training is when it feels like the actual job.

**Micro-bounty in your own cloud.** Spin up a tiny SaaS in a lab cloud account: login, profile, document upload. Plant one obvious vuln, one subtle authz bug, one cloud misconfig. Write a "program brief" with scope, rules, and rewards. Attack it as a researcher; fix it as the internal security engineer. Document both passes. The pattern is detailed in [Building a Home Lab](https://geekyblinder.co.uk/#/2026/07/19/Building-a-Home-Lab-to-Learn-Hacking-Without-Going-to-Jail) (Bonus Scenario 3).

**Internal red/blue drill template** — fits on one page:

```
Drill: <name>     Date: ____      Duration: 90 min

Scenario brief (read aloud at start):
  <one paragraph: what happened, who is involved, what they need to do>

Roles:
  Red team:   <names>      Goal: <objective>
  Blue team:  <names>      Goal: detect, contain, recover
  Observer:   <name>       Captures the timeline, calls time

Environment:
  <list of in-scope systems / labs>

Rules of engagement:
  - No production systems
  - No real customer data
  - Time-box: <X> minutes
  - Stop on any genuine outage of unrelated systems

Success criteria:
  Red:    achieved <objective>?  yes / no
  Blue:   detected within <X> min?  contained within <Y> min?

Debrief (15 min after time):
  - What worked?
  - What was missed?
  - Top 3 changes to take back to production.
```

Run one a quarter to start. Run one a month if your team is bought in. The retro is where the value is — the drill itself is the excuse to have the retro.

**Developer-focused labs.** Show a simple insecure pattern from your codebase. Let devs exploit it. Then guide them to implement the fix and add tests. The diff above is the shape — adapt it to your stack.

---

## Level 6: Rep the Top Five Developer Security Traps

If you're a dev or DevOps, your training should hammer the patterns that bite most teams. Five to always cover:

1. **Injection.** SQL, NoSQL, command, LDAP. Lab: insecure query → exploit → parameterise → add a regression test.
2. **Broken auth and weak permissions.** Authenticated ≠ authorised. Lab: the IDOR diff above. (See [Auth, OAuth, and JWTs](https://geekyblinder.co.uk/#/2026/06/07/Auth-OAuth-and-JWTs-How-They-Work-and-How-Attackers-Break-Th) for the broader picture.)
3. **Secrets in code and configs.** API keys, DB creds, tokens. Lab: leak a fake key, find it with [`gitleaks`](https://github.com/gitleaks/gitleaks) or [`trufflehog`](https://github.com/trufflesecurity/trufflehog) → move to a vault, rotate, add pre-commit/pre-push hooks.
4. **Dependency hell (supply chain).** Outdated/vulnerable packages, malicious deps, slopsquatting. Lab: pin a known-vulnerable version, observe SCA tools (Snyk, Trivy, Dependabot) flag it, patch and re-test. (Slopsquatting depth in [The AI Gold Rush Is Making the Internet Worse](https://geekyblinder.co.uk/#/2026/01/04/The-AI-Gold-Rush-Is-Making).)
5. **Missing logging and monitoring.** The vuln matters; so does seeing it. Lab: trigger attacks, then add structured logging, dashboards, alerts. Wire to the Wazuh rules above.

Once you've broken each in a safe lab and fixed it properly, you've got a deep understanding no multiple-choice test will ever give you.

---

## Turning Reps Into Career Firepower

Don't just do labs and walk away. Capture the work.

- Keep a learning log — date, lab, techniques, "aha" moments. (Templates in [Obsidian as a Second Brain for Security and DevOps](https://geekyblinder.co.uk/#/2027/02/28/Obsidian-as-a-Second-Brain-for-Security-and-DevOps).)
- Turn the best scenarios into blog posts (sanitised, educational), internal brown-bag sessions, or live-stream walkthroughs.
- Tie your reps to current trends — AI-assisted attacks and defence, cloud-native threats, the supply-chain story, developer mistakes you now know how to spot at code-review time.

When you can tell a story like:

> "I built a mini-SaaS in my lab, found my own auth bugs, exploited them, instrumented logging, and then used the same pattern to harden our real services"

…you're no longer "someone who did some CTFs". You're someone who can design, attack, and defend modern systems — and bring the rest of the team along.

That's not just exciting. It's rare. And it's the difference between security engineers who keep their job through the next AI-shaped hiring shake-up and those who don't.

<img src="img/authors/geeky.jpg" width="40"/>
