---
title:  "The AI Gold Rush Is Making the Internet Worse — And Could Get You Hacked"
subtitle: "AI slop, backdoors, and the data leakage nobody wants to talk about"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/the-ai-gold-rush-is-making-the-internet-worse-and-could.jpg"
date: 2026-01-04
tags: AI security devsecops chatgpt coding copilot data-leakage supply-chain
---

## The AI Gold Rush Is Making the Internet Worse — And Could Get You Hacked

AI is everywhere, and a depressing amount of it is mediocre, insecure, or both. The industry is sprinting to bolt “AI-powered” onto everything while quietly ignoring the attack surface it’s creating. The board sees velocity, the engineers see whichever bit of the iceberg is in their lane, and nobody is looking at the *whole* shape of what's coming on board.

Let’s talk about the mess: AI slop, packaged-up vulnerabilities, poisoned models, and the way your own staff are leaking your crown jewels into someone else’s GPU cluster without meaning to. With names of actual tools, actual incidents, and actual things you can do today.

---

## What AI Slop Actually Looks Like in Your Repo

AI slop is all the confident rubbish we’re drowning in: code, blog posts, docs, and "advice" generated and deployed without anyone actually understanding it. The dangerous bit isn’t that AI can be wrong — it’s that it’s wrong in ways that look professional. The patterns I keep seeing in real codebases:

- A junior asks an assistant how to verify JWTs, gets an answer based on some 2021 StackOverflow thread, and copies it in. No `aud` check. No `kid` validation. `verify(token, secret)` with the algorithm pulled from the token header itself — the textbook `alg: none` bypass that has been documented since 2015 and that AI assistants still happily produce.
- A "secure file upload with Node and Express" prompt yields code with no size limit, no content-type validation, files written straight to a web-reachable directory. Looks senior. Slides through review. It’s an arbitrary file upload bug waiting for a `.php` to land.
- Crypto helpers that use `crypto.randomBytes(16)` for a salt but `Math.random()` for the IV. Nobody notices because the function works.
- Tests that mock the very thing the code is supposed to verify (the AI signs the test in a way that always passes).

Confident wrongness at scale is dangerous. When the wrongness is in your auth, crypto, or input handling, it’s not just embarrassing, it’s exploitable. And it’s not theoretical — Stanford CRFM and other groups have repeatedly published studies showing that developers using AI assistants ship code with measurably more security vulnerabilities while feeling more confident about its quality.

What you can actually do, today:

- Run **Semgrep** with the `r2c-ci` and `gitleaks` rule packs in CI on every PR. Cheap, fast, catches a chunk of slop including hardcoded secrets and the JWT-style anti-patterns.
- Add a **`r2c.dev/ai-generated`** signal — most editors can be configured to mark AI-suggested blocks; flag them for stricter review.
- Use **Snyk Code** or **GitHub Advanced Security** for SAST that understands AI-style insecure patterns specifically; their rule sets get updated faster than hand-rolled regexes.
- Re-read the [OWASP LLM Top 10](https://genai.owasp.org/llm-top-10/) once a quarter. It updates and the quiet additions are the ones worth knowing.

---

## When Your Coding Assistant Hallucinates Whole Packages

Slopsquatting is the 2025-onwards evolution of typosquatting. Researchers at Lasso Security, Vulcan, and others showed that the major code assistants invent package names with surprising regularity — `huggingface-cli` instead of `huggingface_hub`, `node-cache-fast` instead of `node-cache`, plausible-but-fictional names that look right and even compile in trivial test scripts. Attackers register the invented names *after* observing what the AI tends to make up, push a malicious package, and wait.

The proof points are out there: research published through 2024–2025 documented thousands of hallucinated package names across npm, PyPI, and crates.io, with reproducibility rates high enough that adversaries treat it as a discovery channel. The first wave of malicious slopsquatted packages started appearing in late 2024.

What you can do:

- Pre-install allowlists in CI — packages must exist in your internal mirror (Artifactory, Nexus, GitHub Packages, Verdaccio) before they can be installed. Outbound to public registries is blocked from build runners.
- Lockfile-only installs (`npm ci`, `pip install -r requirements.txt --require-hashes`, `cargo build --frozen`) — if it's not in the lockfile, the build fails.
- Tools like **Socket** or **Phylum** that flag packages with low download counts, no maintainer history, or dependency signals that don't match a legitimate library.
- Manual verification: before adding *any* AI-suggested package, check the registry for download count, maintainer, age, and source repo. Most invented names have <1k weekly downloads and a `description` field that reads like an LLM wrote it.

---

## Backdoors, Poisoned Models, and the Supply Chain Nightmare

The XZ backdoor (CVE-2024-3094) showed what one patient malicious maintainer can do to a critical dependency over years. Now add AI to that equation: an attacker can generate thousands of plausible-looking package variants, write convincing READMEs and commit histories, and seed them across npm/PyPI/crates.io faster than any review queue can keep up.

On the model side, the same supply-chain logic applies, with extra teeth:

- A "fine-tuned security helper model" pulled from Hugging Face because it promises great exploit detection. It’s been fine-tuned to inject specific backdoor patterns into generated code, "forget" certain checks, or respond to magic prompts in ways that leak training data.
- The infamous PyTorch nightly compromise of December 2022 (a malicious dependency in the nightly build pipeline) showed the ML toolchain isn't immune.
- "Pickle" model formats can execute arbitrary code on load — `.pkl` and `.pth` files are not just data, they're scripts. Anyone deserialising untrusted pickles is one bad file away from RCE.

Treat models like the production-grade dependencies they are:

- **Pin versions and hashes.** Hugging Face supports revision-pinning by commit SHA: `from_pretrained(name, revision="<sha>")`. Use it.
- **Prefer `safetensors` over pickle.** It’s the format Hugging Face has been pushing since 2023 specifically because it can’t execute code on load. If you must load `.pkl` from anyone outside your org, do it in a sandbox.
- **Sigstore-sign your models.** Hugging Face supports [model signing via Sigstore](https://huggingface.co/docs/hub/security-sigstore); you can verify on download. Your internal model registry should require it.
- **Mirror internally.** Don’t pull foundation models or fine-tunes directly from public hubs into prod. Mirror to an internal registry, hash, scan, sign, and pin. The same hygiene you (hopefully) apply to container images.
- **Scan inputs.** Use [`ProtectAI/modelscan`](https://github.com/protectai/modelscan) or similar to flag models containing pickled payloads or suspicious operators before you load them.

If you wouldn’t `curl | bash` a script from a stranger, why are you pulling models without verifying signatures, provenance, or checksums?

---

## Data Leakage: Pasting Your Crown Jewels into a Prompt Box

Samsung famously banned ChatGPT internally in 2023 after engineers pasted proprietary source code and a chip-level bug fix into the public version. Apple, Amazon, JPMorgan, Verizon, and Citigroup all implemented bans or strict controls within months. The pattern repeats: every quarter, another corporate name surfaces in a "AI data leakage incident" news cycle. The behaviour is universal — engineers under pressure paste sensitive data into prompt boxes because it’s faster than redacting it.

The categories of risk that arrive at your incident channel:

- **Regulatory.** Personal data into a third-party model with no DPA/BAA is a UK GDPR / EU GDPR / CCPA timebomb. The EU AI Act (in force from August 2024, with phased obligations through 2026 and 2027) adds a fresh compliance layer on top.
- **Competitive.** Proprietary algorithms, pricing logic, client lists, future roadmap, internal architecture. Once it’s in someone else’s training set, it’s gone.
- **Operational.** Internal hostnames, IP ranges, IAM role names, S3 bucket naming conventions — exactly the OSINT you’d normally hide. Pasted into a prompt for "help me debug this connection error".

You can’t "undo" any of it. Once data is handed over, you’re relying on the vendor’s retention policy, jurisdiction, and deletion promises. Most public AI tools’ default policies do not include "we’ll forget your data".

Minimum bar for any halfway serious org:

- **An AI-acceptable-use policy** with concrete examples of allowed and forbidden prompts, written in plain language and cross-referenced from onboarding docs.
- **A vendor pick that actually offers data controls.** Of the big three: OpenAI Enterprise, Azure OpenAI, Anthropic Claude (via direct API or AWS Bedrock), and Google Vertex AI all support data-processing agreements, no-training-on-inputs, regional residency, and zero-retention modes. *None* of them offer this on the consumer free tiers. The tier matters.
- **A gateway in front of public models.** Cloudflare AI Gateway, [Lakera Guard](https://www.lakera.ai/), [Portkey](https://portkey.ai/), or a thin in-house proxy. Gives you logging, rate-limiting, output filtering, and a single chokepoint to enforce policy.
- **DLP that catches the obvious paste-events.** Microsoft Purview, Nightfall, Forcepoint, and Symantec all have DLP rules for "blocks of source code being uploaded to chat.openai.com / claude.ai / gemini.google.com". Browser-extension DLP (Push, Island, Citrix Secure Browser) catches this at the form-submit layer.
- **Private AI where sensitivity warrants it.** Self-host with Ollama, vLLM, or LM Studio for local models. Use Bedrock / Vertex / Azure AI with private endpoints in your own VPC for hosted ones. The same model can be private-by-default if you wire it up correctly.

The single biggest lever is making the right path the default — give engineers a sanctioned, fast, decent AI tool inside the gateway, and the temptation to paste into the public version drops to almost nothing.

---

## When the Model Itself Isn’t What You Think

Open models and community checkpoints are brilliant, and a fresh attack surface. Risks include:

- **Datasets poisoned** so the model underperforms on specific topics (e.g. it produces subtly weaker security checks) but behaves fine elsewhere. Hard to spot on a benchmark suite that doesn’t test for it.
- **Trigger phrases** that cause the model to output unsafe recommendations or hidden content. Researchers have demonstrated this on multiple commercial and open models — backdoor "magic words" that flip behaviour.
- **Fine-tunes that bias** outputs toward particular libraries, vendors, or "shortcuts" that happen to be insecure. Easy to do, hard to detect once the model is integrated.

Defences are roughly the same as supply chain: pin, verify, mirror, scan. Plus eval suites — you should be running [`Garak`](https://github.com/NVIDIA/garak) and similar against any model you’re putting in production, not just trusting the vendor’s safety card.

For more on testing models adversarially, see [Blue Team vs AI Red Team](https://geekyblinder.co.uk/#/2027/04/25/Blue-Team-vs-AI-Red-Team-How-to-Build-Defences-That-Learn-Fa).

---

## What Sensible AI Use Actually Looks Like

For developers:

- Use AI to draft, not to decide. Treat it like a keen junior who's great at boilerplate and terrible at security.
- SAST and dependency scanning are non-negotiable in CI. Same goes for [secret scanning](https://github.com/gitleaks/gitleaks) on pre-commit *and* on push.
- Never paste secrets, customer data, or proprietary code into public tools. Use sanctioned ones with DPAs.
- For learning, see [Using AI to Learn Without Turning Your Brain to Slop](https://geekyblinder.co.uk/#/2026/03/15/Using-AI-to-Learn).

For organisations:

- An AI policy that's actually enforced — not a Confluence page nobody reads. The deeper version: [AI Governance for Engineers](https://geekyblinder.co.uk/#/2026/08/16/AI-Governance-for-Engineers-Guardrails-That-Arent-Just-Slide).
- Vendor evaluation that asks the right questions: data residency, training opt-out, retention, audit logs, compliance certifications (SOC 2, ISO 27001, ISO 42001, EU AI Act readiness).
- AI in your vendor risk assessments and threat modelling. Not a special case — just another supplier with another risk profile.

For security teams:

- Add AI-generated code as an explicit threat vector in your models.
- Train developers on AI-slop patterns: insecure defaults, missing checks, reliance on outdated advice.
- Run secure code reviews that ask "looks right, but is it necessary, and has anyone read it line by line?"
- Bake adversarial AI testing into your purple-team rotation. The tools exist; use them.

---

## Final Thought

AI isn’t evil and it’s not going away. The real risk isn’t "the robots take our jobs", it’s "we let statistically-plausible text engines quietly re-write our critical systems while we’re too busy chasing feature roadmaps."

Use the tools. But pin your models, mirror your dependencies, sign what matters, log what crosses your boundary, give engineers a sanctioned fast path so they don't take the unsanctioned one, and keep your reviewers awake. The orgs that win the next few years are the ones who treat AI as boring infrastructure: useful, signed, monitored, and replaceable. Not magic. Not gospel. Just another tool in a stack you keep an eye on.

<img src="img/authors/geeky.jpg" width="40"/>
