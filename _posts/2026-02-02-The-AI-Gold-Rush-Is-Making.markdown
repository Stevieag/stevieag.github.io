---
title:  "The AI Gold Rush Is Making the Internet Worse — And Could Get You Hacked"
subtitle: "AI slop, backdoors, and the data leakage nobody wants to talk about"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "https://escp.eu/thechoice/tomorrow-choices/how-to-prevent-ai-slop-from-taking-over-your-workplace/"
date: 2026-02-02
tags: AI security devsecops chatgpt coding copilot data-leakage supply-chain
---

## The AI Gold Rush Is Making the Internet Worse — And Could Get You Hacked

AI is everywhere, and a depressing amount of it is mediocre, insecure, or both. The industry is sprinting to bolt “AI-powered” onto everything while quietly ignoring the attack surface it’s creating.

Let’s talk about the mess: AI slop, built‑in vulns, poisoned models, and the way your own staff can leak your crown jewels into someone else’s GPU cluster without meaning to.

---

## What Is AI Slop, Really?

AI slop is all the confident rubbish we’re now drowning in: code, blog posts, docs, and “advice” generated and deployed without anyone actually understanding it.

You’ve seen it:

- Code that compiles, passes a basic test, and quietly hardcodes secrets or skips input validation.
- “Security best practice” blog posts that read fine but are technically wrong in three subtle ways.
- Docs written by someone who clearly asked an LLM “explain X” and hit publish.

This isn’t about AI being imperfect. It’s about people shipping AI output straight to production and treating it like gospel. A junior asks an assistant how to secure JWTs, gets an answer based on some 2021 StackOverflow thread, and copies it into the auth service. No key rotation, no audience checks, no proper expiry handling. It *works* until it very much doesn’t.

Confident wrongness at scale is dangerous. When the wrongness is in your auth, crypto, or input handling, it’s not just embarrassing — it’s exploitable.

---

## When Your Coding Assistant Is a Vulnerability Factory

A lot of code‑assist tools are trained on public repos. That means:

- Old insecure patterns.
- Deprecated crypto (hello, SHA‑1 and home‑rolled “encryption”).
- Terrible error handling and logging that leak secrets.
- “Example” code that was never meant for production.

You ask for “secure file upload with Node and Express,” and it suggests:

- No size limits.
- No content‑type validation.
- Files written straight to disk in a web‑reachable directory.

Looks neat in the IDE. Looks “senior”. Slides through code review because it fits everyone’s mental pattern of “proper code structure.” But under the surface it’s an arbitrary file upload bug waiting for a `.php` or `.jsp` to land.

The dangerous bit isn’t that AI can be wrong. It’s that it’s wrong in ways that look professional.

---

## Backdoors, Poisoned Models, and the Supply Chain Nightmare

We already had the XZ backdoor incident showing what happens when one malicious actor quietly poisons a critical dependency over time. Now add AI into that equation.

Attackers can:

- Generate thousands of package variants with subtle bugs that only trigger in edge cases.
- Use AI to write plausible READMEs, tests, and commit history.
- Seed ecosystems like npm, PyPI, crates.io with “handy utilities” that contain backdoors.

On the model side:

- You download a “fine‑tuned security helper model” from some random repo because it promises great exploit detection.
- It’s been fine‑tuned to inject a specific header into generated code, or to “forget” certain checks, or to respond to magic prompts in ways that leak information or sabotage output.

If you wouldn’t `curl | bash` a script from a stranger, why are you pulling models and containers without verifying signatures, provenance, and checksums?

Treat models like dependencies:

- Pin versions.
- Verify signatures where available.
- Mirror internally and restrict outbound model pulls.
- Audit outputs the same way you audit library updates.

---

## Data Leakage: Pasting Your Crown Jewels into a Prompt Box

Employees are absolutely pasting sensitive information into AI tools:

- Source code.
- Database errors with real customer data.
- Architecture diagrams described in prose.
- Internal strategy docs and HR notes.

The risks:

- Regulatory: shoving personal data into a third‑party model with no DPA/BAA is a GDPR/UK GDPR time‑bomb.
- Competitive: proprietary algorithms, pricing logic, client lists, future roadmap.
- Operational: internal hostnames, IP ranges, IAM role names, internal S3 bucket naming patterns — everything you’d normally hide from OSINT.

You can’t “undo” this. Once the data’s been handed over, you’re relying on the vendor’s retention, jurisdiction, and deletion promises. You don’t get to re‑train the model to forget your secrets.

Minimum bar for any halfway serious org:

- Clear AI usage policy with examples of what is and *isn’t* allowed.
- Technical controls: outbound URL/DNS monitoring, DLP, or at least some guardrails on where prompts can be sent.
- Private AI where practical: run sensitive workloads on models you host, on infra you control.

---

## The Model Might Not Be What You Think It Is

Open models and community checkpoints are brilliant, but also a fresh attack surface.

Risks include:

- Datasets poisoned so the model underperforms on specific topics (e.g. security checks) but behaves fine otherwise.
- Trigger phrases that cause the model to output unsafe recommendations or hidden content.
- Fine‑tunes that subtly bias outputs toward particular libraries, vendors, or “shortcuts” that just happen to be insecure.

Again: treat models like part of your software supply chain. If you wouldn’t accept unsigned binary blobs into prod, don’t blindly accept opaque model files.

---

## What Sensible AI Use Looks Like

For developers:

- Use AI to draft, not to decide; treat it like a keen junior who’s great at boilerplate but terrible at security.
- Run SAST and dependency scans as a non‑negotiable part of CI.
- Never paste secrets, customer data, or proprietary code into public tools.
- Keep architectural decisions in human hands and use AI for scaffolding, tests, and refactors — then review them like any other PR.

For organisations:

- Have an AI policy that’s actually enforced, not a Confluence page nobody reads.
- Choose vendors that support data‑processing agreements, regional data residency, and training‑opt‑out.
- Include AI in vendor risk assessments and threat modelling.

For security teams:

- Add AI‑generated code as an explicit threat vector in your models.
- Train developers on “AI slop” patterns: insecure defaults, missing checks, reliance on outdated advice.
- Run secure code reviews that call out “looks right, but is it necessary?”

---

## Final Thought

AI isn’t evil and it’s not going away. The real risk isn’t “the robots take our jobs”; it’s “we let statistically‑plausible text engines quietly re‑write our critical systems while we’re too busy chasing feature roadmaps.”

Use the tools. But keep your threat model up to date, your reviewers awake, and your hand firmly on the wheel.
