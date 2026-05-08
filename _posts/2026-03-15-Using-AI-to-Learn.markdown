---
title:  "Using AI to Learn Without Turning Your Brain to Slop"
subtitle: "How to use AI as a tutor, not a copy‑paste vending machine"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/using-ai-to-learn-without-turning-your-brain-to-slop.jpg"
date: 2026-03-15
tags: AI learning devsecops coding education chatgpt
---

## Using AI to Learn Without Turning Your Brain to Slop

AI can be the best mentor you’ve never had — or the fastest way to become that engineer who pastes things into prod they don’t understand.

Let’s talk about using it to *learn* skills, not outsource thinking.

---

## AI as a Tutor, Not a Typist

Good uses:

- Ask for conceptual explanations in your own words: “Explain Kubernetes Services as if I’m a network engineer.”
- Ask for comparisons: “Helm vs Kustomize vs plain YAML — when is each a good fit?”
- Ask for step‑by‑step plans: “Build me a 4‑week plan to learn web app hacking with real labs.”
- Use it as a rubber duck on steroids. Explaining a problem clearly enough for an AI to help often surfaces the answer before it even replies — the forced articulation is the value. Pay attention when that happens; that’s your brain doing the actual work.

Then:

- Run the commands yourself.
- Break the lab intentionally.
- Ask follow‑up questions until you can explain it without notes.

Bad use:

- “Give me a complete Terraform module/K8s deployment for X” and shipping it straight to prod without review.

---

## Prompts That Actually Make You Smarter

Steal these. Tweak the topic. Notice the shape — every one of them puts the work back on you.

- **The reverse-tutor.** *“Explain X. Then ask me three questions to check I understood. Don’t give the answers until I try.”*
- **The Socratic mentor.** *“I want to learn Kubernetes networking. Ask me questions until you’re confident I understand it. Don’t lecture; just probe.”*
- **The diff reviewer.** *“Review this code. Don’t fix anything yet — tell me what’s wrong and why, and let me try the fix.”*
- **The pair-debugger.** *“I’ll describe a bug. Ask me what I’ve already tried, what I think the cause is, and what I observed — before suggesting causes.”*
- **The mock interviewer.** *“Give me 5 senior-engineer interview questions on JWT security. Mark my answers harshly. Show me what a strong answer looks like only after I’ve answered.”*

You’ll notice none of these are “write me X”. That’s the point.

---

## Trust, but Verify

AI confidently makes things up. Non-existent CLI flags, wrong RFC numbers, deprecated APIs, libraries that have never been published. The output is fluent regardless of whether it’s right, and the fluency is the trap — a wrong answer in a confident voice is worse than no answer at all, because it stops you looking further.

Treat the output like a confident-sounding Wikipedia article: useful starting point, never the source of truth.

- Run the command. If it errors, the man page is closer to the truth than the chat window.
- Check version numbers and release dates against the actual project, not the model’s memory.
- For security-relevant code, read the real library docs before pasting.
- For anything you’re going to say out loud in a meeting, find a primary source.

---

## Code, Licences, and Legal Slop

Many models are trained on public code that is:

- Licensed under GPL, MIT, Apache, proprietary, or unknown.
- Vulnerable, outdated, or outright wrong.

Risks:

- You accidentally pull in code that is effectively a derivative work of a GPL project and then drop it into your closed‑source product.
- You copy code containing someone else’s secrets or identifiers.
- You adopt patterns that conflict with your company’s coding standards or policies.

Safer pattern:

- Use AI to *explain* a pattern, then implement your own version.
- Use it to review your code: “Is there any obvious security issue in this handler?”
- Ask it to translate concepts between languages instead of dumping raw blocks into your repo.

And if your company has legal or OSS counsel: talk to them about policy. Don’t guess.

---

## Security Implications of AI‑Generated Code

Security concerns:

- **Insecure defaults.** Missing auth, weak crypto, sloppy input validation.
- **Hidden assumptions.** Relies on global state, works only in trivial examples.
- **Prompt injection** if you build AI into your product.
- **Code-copilot context exfiltration.** Copilot, Cursor, and the rest send context to a third party. A poisoned README or comment in a dependency can manipulate suggestions to leak secrets sitting in your buffer or insert subtle backdoors. Audit what your editor sends, where, and check your org’s policy on it.
- **Hallucinated package names.** AI happily suggests `import requests-helper` or `npm install fast-yaml-parser` for libraries that don’t exist. Attackers register the typo-squat *after* watching what AI tends to invent (sometimes called “slopsquatting”). Always verify a package exists on the real registry, with real download counts and a real maintainer, before installing.

Defensive moves:

- Treat AI‑generated code like code from an unknown contributor.
- Run SAST, DAST, and dependency scanning as standard.
- Build a code review culture where reviewers feel comfortable saying “I don’t think you really understand this block; let’s rewrite it.”

Remember: attackers are also using AI — to generate payloads, fuzz inputs, and explore weird corners of your stack faster.

---

## Learning With AI vs Learning From AI

If you want to really learn:

- Use AI to test you, not just teach you: “Give me 5 interview‑style questions about JWT security and then mark my answers.”
- Get it to play “Socratic mentor”: “Ask me questions until you’re confident I understand Kubernetes networking.”
- Iterate: each time you solve something in a lab (THM room, CTF challenge), get AI to help you produce a writeup — then refine it yourself.

Using AI as scaffolding for your own thinking makes you dangerous in the good way. Using it as a copy‑paste vending machine makes you a liability.

---

## Symptoms You’ve Stopped Learning

The early-warning signs are subtle. Catch yourself doing any of these and step away from the chat window for an afternoon.

- You can’t debug your own code without pasting the error in.
- You can’t explain why something in your repo is structured the way it is.
- You ask AI before trying anything yourself — even five-second things you used to do reflexively.
- You copy error messages in verbatim before reading them.
- You can’t write a 200-line program from a blank file without help.
- You feel anxious when the AI is slow or unavailable.

If two or more of those land, you’re not using AI to learn; you’re using it as a prosthetic. Take an afternoon off the tools, fix something hard the slow way, and remember why you got into this.

---

## Final Thought

AI should be the slightly annoying teacher that keeps asking “why?”, not the friend who lets you copy their homework.

If you come out of a session with AI understanding the concept well enough to explain it to someone else, you’ve used it right. If you come out with a blob of code you can’t quite explain… you’ve just added a future incident ticket with your name on it.

For the development side of all this — keeping AI useful in your workflow without losing your security or your soul — see [AI-Assisted Development Without Losing Your Soul or Your Security](https://geekyblinder.co.uk/#/2027/05/09/AI-Assisted-Development-Without-Losing-Your-Soul-or-Your-Sec) when it lands. For the offence/defence side, [Blue Team vs AI Red Team](https://geekyblinder.co.uk/#/2027/04/25/Blue-Team-vs-AI-Red-Team-How-to-Build-Defences-That-Learn-Fa).

<img src="img/authors/geeky.jpg" width="40"/>
