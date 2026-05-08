---
title:  "AI Hacking for Red and Blue Teams: Friends, Foes, and Autonomous Chaos"
subtitle: "How AI is changing offensive and defensive security – and how to use it without losing control"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/ai-hacking-for-red-and-blue-teams-friends-foes-and-auto.jpg"
date: 2027-03-28
tags: AI red-team blue-team security automation
---

## AI Has Joined the Red and Blue Teams (Whether You Planned For It or Not)

By 2027 nearly every security team has AI in its stack — sometimes deliberately, often because a vendor renamed an existing feature. Red teams use it to scale recon and adversary emulation, blue teams use it for triage, detection engineering, and runbook generation. The autonomous variants — call them ARTs and ABTs if you want, "agents that occasionally do useful work and sometimes do alarming work" if you're being honest — are showing up in the same toolchains.

Used well, this is continuous purple teaming with a productivity multiplier. Used badly, it’s a new way to ship incidents and blind spots. This post is about how human red and blue teams *use* AI as a tool. For how to *defend* your own AI systems against red-team probing, see [Blue Team vs AI Red Team](https://geekyblinder.co.uk/#/2027/04/25/Blue-Team-vs-AI-Red-Team-How-to-Build-Defences-That-Learn-Fa).

---

## Red Team: What AI Augments and What It Doesn’t

Where AI genuinely makes red-team work faster:

- **Recon summarisation.** Feed `nmap`/`gobuster`/`amass`/`shodan` output into an LLM and ask for prioritised targets — what’s exposed, what’s likely vulnerable, what’s worth manual time. [PentestGPT](https://github.com/GreyDGL/PentestGPT) and [HackingBuddyGPT](https://github.com/ipa-lab/hackingBuddyGPT) wrap this loop. They’re not magic; they cut the boring synthesis time roughly in half on typical engagements.
- **Phishing and pretext content.** Tailored phishing copy at one-per-target speed. Industry-specific lures, accurate company-tone matching, and context from public profiles. The defenders' problem is now "every phish reads well" rather than "spot the typo".
- **Payload obfuscation and variants.** Generate a hundred variants of a known payload that survive signature-based detection. Use [`garak`](https://github.com/NVIDIA/garak) and similar to test prompt-injection variants against AI-integrated targets.
- **Adversary emulation at scale.** [MITRE Caldera](https://caldera.mitre.org/) plugins now expose LLM-driven decision-making for plan execution; [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) tests can be selected and chained by AI based on the discovered environment.
- **Agentic red-team frameworks** — [AutoGen](https://github.com/microsoft/autogen), [LangGraph](https://www.langchain.com/langgraph), and bespoke ReAct loops let you build agents that plan, execute, and adapt across multi-step engagements. [Cybersecurity AI](https://github.com/aliasrobotics/cai) is one of the more mature open frameworks.

Where AI genuinely doesn’t help, despite the marketing:

- **Novel exploit development.** LLMs hallucinate CVEs, invent flag combinations, and confuse vulnerability classes. Use one to draft a PoC and you’ll spend more time fixing its mistakes than writing it from scratch.
- **Lateral movement decisions.** Path-planning across a real environment requires reading state from twelve places at once and weighing it against mission goals. Agents can do parts of this; they consistently miss the bits that matter.
- **Operational security.** AI agents leak. They log to vendor backends, they emit telemetry, and they include identifying patterns in their outputs that are already being detection-engineered against. If your engagement requires stealth, the AI tool is part of your attack surface.

The pattern that works in 2027 red-team engagements: **AI for breadth, humans for depth.** The agent maps and triages; the operator decides what to chase.

---

## Blue Team: What AI Augments and What It Doesn’t

Where AI genuinely makes blue-team work faster:

- **Alert triage and clustering.** [Microsoft Security Copilot](https://www.microsoft.com/en-us/security/business/ai-machine-learning/microsoft-security-copilot), [CrowdStrike Charlotte AI](https://www.crowdstrike.com/platform/charlotte-ai/), [Anthropic Claude in Splunk](https://www.splunk.com/en_us/blog/), and the various open equivalents collapse hundreds of related alerts into one incident summary with linked artefacts. The job goes from "read a hundred lines" to "agree or disagree with the synthesis".
- **Detection engineering.** "Catch repeated attempts to override the system prompt with leetspeak" → draft Sigma rule. "Find sessions where the agent issued a refund within 60 seconds of being told the customer was angry" → draft KQL/SPL. Blank-page time drops to almost nothing; you still review and tune.
- **Runbook drafting.** First-draft incident runbooks for AI-shaped attacks, ransomware variants, novel CVE response. Useful starting points; not source-of-truth.
- **Log search assistance.** Natural-language to KQL/SPL. Splunk's `AI Assistant`, Sentinel Copilot, and Elastic's AI features all offer this. Good for curious investigators, less reliable for repeatable evidence.
- **Threat intel synthesis.** Pulling together vendor reports, blog posts, and CVE feeds into a single brief with cross-references. Speeds up morning triage; needs human verification before any of it lands in customer comms.

Where AI genuinely doesn’t help, again, despite the marketing:

- **Fully autonomous incident response.** "Suggest a containment action": fine. "Execute it without a human": fine in narrowly-scoped, idempotent runbooks (revoke a leaked token, isolate a known-compromised laptop). Anywhere broader, the failure mode is taking your business down to defend it.
- **Threat hunting from cold.** Hunting needs hypothesis formation and tacit knowledge of *your* environment. AI helps with hypothesis enumeration and data pulling; the actual hunt is still humans.
- **First-line analyst replacement.** Augments well, replaces badly. The skill that goes is "know when the AI is wrong" — and that skill is built by *being* tier-1 first. Replace tier-1 with AI and your tier-2 supply dries up in three years.

The pattern that works in 2027 SOCs: **AI as the analyst's prep partner, not the analyst.** It clusters, drafts, and explains. Humans decide.

---

## The Purple Team Sweet Spot: Continuous AI-Augmented Testing

The most interesting use of AI in security operations isn’t red-side or blue-side — it’s the loop between them.

A working continuous purple-team pattern:

- **Monday morning automated run.** ART executes a curated playbook (a slice of MITRE ATT&CK relevant to your environment) against staging. ABT watches via the SIEM. Detections that should fire are checked off; ones that didn’t become tickets.
- **Findings become detections.** Every novel attack pattern → Sigma rule → CI-tested SIEM content → deployed. Nothing should "work twice".
- **Findings become tests.** Every successful red prompt or path is added to a regression suite (`promptfoo` for AI surfaces, BAS tools like [SafeBreach](https://www.safebreach.com/) or [AttackIQ](https://www.attackiq.com/) for the broader environment).
- **Monthly tabletop.** Pick one finding. Walk it through end-to-end with red, blue, AI/ML, and product. What stopped it? What detected it? What's the rollback? What's the org-shaped fix?
- **Detection-as-code in a git repo.** Sigma rules, KQL queries, SPL searches, runbooks. Reviewed in PRs. Tested in CI against historical telemetry. Deployed via your normal pipeline.

This stops being "we did a pen test in February" and becomes "we tested again on Tuesday at 14:00 and the results are in this Slack channel". The cadence is the win.

---

## Risks and Limits You Can’t Ignore

AI in red/blue operations has serious caveats. The ones that bite teams:

- **Hallucinated CVEs and IOCs.** AI confidently invents CVE numbers, attributes attacks to the wrong group, and produces plausible-but-fictional indicators. Verify before any of it lands in a report or runbook.
- **Over-automation.** Autonomous systems making changes (revoking access, blocking IPs, isolating hosts) without adequate scope. Your emergency-brake list should be specific and your scope should be tight.
- **Data exposure.** Feeding sensitive logs, customer data, or proprietary configs into external AI systems leaks what you're protecting. Use private/hosted models or vendors with proper DPAs and data-residency guarantees. See [AI Governance for Engineers](https://geekyblinder.co.uk/#/2026/08/16/AI-Governance-for-Engineers-Guardrails-That-Arent-Just-Slide).
- **Detectability of AI tooling.** Defenders are already building rules for "Caldera + AI plugin", "LangGraph user-agent strings", and the telemetry signatures of common agent frameworks. If you're red-teaming with AI, assume the tool itself is on someone's signature list.
- **Regulatory and ethical limits.** Offensive AI used outside scope is a CFAA / Computer Misuse Act problem in a smart suit. The fact that it's automated doesn't change who gets prosecuted. Authorization documents matter; agent guardrails matter.
- **Skills atrophy.** Over-reliance creates analysts who can prompt but can't pcap. Mix AI use with deliberate AI-free practice. (See [Using AI to Learn Without Turning Your Brain to Slop](https://geekyblinder.co.uk/#/2026/03/15/Using-AI-to-Learn) for the deeper version.)

Mitigations are mostly the obvious ones done properly: humans in the loop on impactful actions, audit trails on AI decisions, scope documents that match what the agent can actually do, and a tested kill-switch that disables the autonomy fast.

---

## Practical On-Ramp for Solo / Small Teams

You don't need a SOC budget to use this stuff usefully. The minimum-viable purple loop with off-the-shelf tools:

For red-shaped work in a lab:

- Run [`PentestGPT`](https://github.com/GreyDGL/PentestGPT) or [HackingBuddyGPT](https://github.com/ipa-lab/hackingBuddyGPT) against [DVWA](https://github.com/digininja/DVWA), [HackTheBox retired boxes](https://www.hackthebox.com/), or your own deliberately-vulnerable lab. Treat the AI like a study partner — explain what it suggests before you run it.
- Use [`garak`](https://github.com/NVIDIA/garak) against any LLM you’ve deployed yourself. See what jailbreaks land.
- Try [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) tests with an LLM picking which to run based on a description of your "victim" environment.

For blue-shaped work:

- Build a free Sentinel or Splunk Cloud Free instance. Forward the laptop's auth logs, browser history (carefully), and home-router NetFlow.
- Practice "natural-language to KQL" by asking an LLM to draft queries against the schema; check them with `kql-magic` or directly in the workspace.
- Translate one ATT&CK technique into a Sigma rule manually, then ask an LLM to do the same and compare.

For purple:

- Run a lab attack (Caldera against a vulnerable VM), capture logs, ask AI to help you draft a detection, implement it, then re-run the attack and check the rule fires.
- Do this once a week for two months and you'll have a genuine working knowledge of the loop most enterprise teams are still trying to build.

You're using AI as a force-multiplier for your own thinking, not a replacement for it.

---

## Final Thought

AI isn't going to replace red or blue teams any time soon — but the people and organisations who learn to integrate it thoughtfully will outpace those who don't. The principle is simple even when the implementation isn't:

- AI is a fast but fallible junior. Useful, supervised, accountable to a human review.
- AI is a way to connect red findings and blue defences into continuous purple teaming.
- AI is itself a new attack surface that must be governed, gateway-fronted, and tested. The system you depend on is also the system the next attacker will probe.

If you treat AI in security as another power tool — sharp, useful, and capable of removing fingers if you point it at yourself — you'll be on the right side of this shift, using AI to probe and harden your systems faster than the attackers can.

For deeper reading: [Blue Team vs AI Red Team](https://geekyblinder.co.uk/#/2027/04/25/Blue-Team-vs-AI-Red-Team-How-to-Build-Defences-That-Learn-Fa) covers defending your own AI systems against red-team probing. [AI Governance for Engineers](https://geekyblinder.co.uk/#/2026/08/16/AI-Governance-for-Engineers-Guardrails-That-Arent-Just-Slide) covers the org-level controls. [AI-Assisted Development Without Losing Your Soul or Your Security](https://geekyblinder.co.uk/#/2027/05/09/AI-Assisted-Development-Without-Losing-Your-Soul-or-Your-Sec) covers the dev-time side.

<img src="img/authors/geeky.jpg" width="40"/>
