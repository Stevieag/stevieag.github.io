---
title:  "AI Governance for Engineers: Guardrails That Aren’t Just Slideware"
subtitle: "What you should actually put in place before AI eats your company"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/ai-governance-for-engineers-guardrails-that-arent-just.jpg"
date: 2026-08-16
tags: AI governance risk compliance security data
---

## AI Governance for Engineers: Guardrails That Aren’t Just Slideware

Everyone from the board to your mate in support is suddenly talking about AI. The hype is loud, the risk is real, and somewhere in the middle you, the engineer, are wondering how to let people use the tools without setting yourself on fire. Most "AI governance" advice you'll read is a 60-page Confluence page, three sub-pages of risk taxonomy, and a slide showing "responsible AI" in seventeen-point font.

This is the engineer’s version: real classifications, real tools, real policy text, real CI hooks, and real numbers. By the time you finish reading you should know exactly what to ship next week to make AI use safer in your org without slowing it down.

---

## Why AI Needs Guardrails (Beyond the Buzzwords)

The risks you actually need to plan for in 2026:

- **Data leakage.** Engineers paste source code and customer data into public tools. Samsung, JPMorgan, Apple, and a dozen others banned consumer ChatGPT internally over this.
- **Insecure outputs.** Code with vulnerabilities baked in (see [The AI Gold Rush Is Making the Internet Worse](https://geekyblinder.co.uk/#/2026/01/04/The-AI-Gold-Rush-Is-Making)). Wrong advice presented confidently.
- **Compliance and legal.** EU AI Act phased obligations are landing through 2026 and 2027. UK GDPR / EU GDPR / CCPA all care about what data goes where. ISO/IEC 42001 is the new AI management-system standard your auditor will eventually ask about.
- **Model behaviour.** Prompt injection, jailbreaks, biased outputs, hallucinated facts in customer-facing surfaces.
- **Copilot context exfiltration.** Modern code copilots send local context to a third party. A poisoned README in a dependency can manipulate suggestions to leak secrets sitting in the buffer.

Ignoring this because "we’re iterating fast" is the 2026 version of leaving an S3 bucket open to the world. The clean-up costs are the same shape; the embarrassment is different.

---

## Step 1: Classify Data, Not Tools

The mistake most policies make is starting with "is ChatGPT allowed?" — the answer always becomes "it depends" and nobody can remember when. Classify the *data* first; the tool restrictions fall out of that.

A working three-tier classification:

| Class | Examples | Public AI (free tier) | Public AI (Enterprise / paid with DPA) | Internal/private AI |
|-------|----------|-----------------------|----------------------------------------|---------------------|
| **Red** — regulated or unique to your business | customer PII, payment data, source code of core differentiators, unreleased product, board materials, security findings, signed contracts | ❌ Never | ❌ Never | ✅ With logging |
| **Amber** — sensitive but recoverable | non-core source code, internal architecture diagrams, debugging logs, anonymised test data, draft external content | ❌ Never | ✅ With approval | ✅ Default |
| **Green** — public or trivially leaked | published docs, marketing copy, public APIs, snippets from open-source you maintain | ✅ OK | ✅ OK | ✅ OK |

Concrete is the point. "Sensitive data" written in a policy means whatever the engineer wants it to mean at 4pm on a Friday.

---

## Step 2: An Acceptable-Use Policy You Can Actually Read

Bin the 60-page Confluence drama. Use this skeleton — it fits on one page, covers the actual decisions, and ends with examples:

```
AI Acceptable Use Policy — v1.0 (last reviewed: 2026-08)

What you can use AI tools for:
- Drafting code, prose, and documentation that you will review.
- Summarising public information and your own non-Red content.
- Explaining concepts, reviewing your own code, generating tests.
- Translating between languages or formats.

What you must NOT do:
- Paste Red-tier data into any public AI tool, ever — this includes the
  free tier of any of the big providers.
- Paste Amber-tier data into a tool that is not on the approved list.
- Ship AI-generated code without security review and SAST passing.
- Use AI output as the sole source of truth for security-relevant
  decisions (auth, crypto, input validation).

The approved tools list:
- For internal/Red use:           <gateway URL>  (Azure OpenAI / Bedrock)
- For Amber use with approval:    <Enterprise tier of your chosen vendor>
- For Green use:                  any reputable public tool

Examples of OK:
- "Help me name this Go function": Green ✓
- "Write a Postgres migration to add a soft-delete column": Amber, OK
  via the internal gateway ✓

Examples of not OK:
- Pasting a customer support email to ask AI to draft a reply: Red ✗
- Pasting your auth service to ask "is this secure?": Red ✗
- "Write a phishing email I can send to a real client": always ✗

Reporting: if you think you've leaked data into an AI tool,
report it to security@<your org> within 24 hours. We will not
punish honest reports; the data still needs to be tracked.
```

Make it short, make it concrete, and put it where humans actually live (Slack onboarding bot, IDE pre-commit message, the printout next to the coffee machine if you're old-fashioned).

---

## Step 3: An AI Gateway, Not a Free-For-All

Don't try to control AI use by policy alone. Put a gateway in front of any AI traffic that matters and you get logging, rate-limiting, content filtering, and a single chokepoint for policy. Multiple decent options:

- **Self-hosted thin proxy** — most teams' best bet. A small FastAPI/Express service that authenticates the user (your SSO), forwards to the chosen model API, logs the prompt + response + classification, and applies output filters. Less than a week to a useful v1.
- **[Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/)** — drop-in proxy in front of OpenAI/Anthropic/etc with caching, logging, and rate limits. Fast to deploy if your traffic isn't huge.
- **[Portkey](https://portkey.ai/)** — vendor neutral, supports caching, fallbacks, prompt versioning, RBAC.
- **[Lakera Guard](https://www.lakera.ai/guard)** — adds prompt-injection and PII detection to whatever proxy you put it behind.
- **Cloud-native gateways** — Azure API Management with the AI policies, AWS Bedrock with VPC endpoints, Google Vertex AI with VPC-SC. If you're already on one of those clouds and you want their data-residency story, this is the path.

What the gateway must enforce:

- **AuthN/AuthZ via your SSO.** No anonymous usage. Group membership controls which classifications you can submit.
- **Per-request classification tag.** Engineer asserts the tier (Red/Amber/Green) on the request; the gateway logs it and gates accordingly.
- **PII detection on the way in.** Use [`microsoft/presidio`](https://github.com/microsoft/presidio) or Lakera Guard to flag prompts containing what looks like PII.
- **Output filtering on the way out.** Strip credentials, internal hostnames, and token-shaped strings from responses before they go back to the user.
- **Logging.** Prompt, response, classification, user, timestamp, model, gateway decision (allowed/blocked/rewritten). 90-day retention is reasonable.
- **Cost controls.** Per-user and per-team budgets. AI bills surprise nobody who's looked at them, and they're frequently the first signal that an automation has gone rogue.

---

## Step 4: AI in the SDLC — Treat Output as Untrusted Input

AI-generated code is a third-party submission into your codebase. Your existing third-party-review machinery should handle it:

- **PR template.** Add a checkbox: *"Portions of this PR were AI-assisted: yes / partial / no"*. Yes/partial triggers extra reviewer attention and blocks self-merge.
- **Required CI gates.** SAST (Semgrep, Snyk Code, GitHub Advanced Security), secret scanning (gitleaks pre-commit + push), dependency scanning (Trivy/Snyk/OSV-Scanner). None of these are AI-specific, but they *catch* a chunk of AI-shaped errors.
- **A `.cursorrules` / `copilot-instructions.md` / equivalent in the repo.** Tell the assistant your standards: language version, lint config, security-relevant constraints. Most AI-shaped vulnerabilities come from generic defaults; nudging the assistant to read your conventions helps.
- **Verify package names.** Use a Renovate/Dependabot config that pins to known-good registries; block direct installs from npm/PyPI in CI. See the slopsquatting note in [The AI Gold Rush Is Making the Internet Worse](https://geekyblinder.co.uk/#/2026/01/04/The-AI-Gold-Rush-Is-Making).
- **Adversarial evals on AI-integrated features.** If your product *uses* an LLM, add `garak` and `promptfoo` runs to CI for the prompts and pipelines. Catch jailbreaks before users do. (See [Blue Team vs AI Red Team](https://geekyblinder.co.uk/#/2027/04/25/Blue-Team-vs-AI-Red-Team-How-to-Build-Defences-That-Learn-Fa) for the deeper version.)

---

## Step 5: Logging and Audit (For Real, Not for Show)

If something does go wrong — accidental Red-tier paste, a prompt-injection through your customer-facing chatbot, a model swap that introduces a regression — you want to be able to answer:

- *Who* asked *what*, *when*?
- What classification was asserted? Did the gateway flag it?
- What did the model return?
- Did the response leave your network, and where to?

A useful log schema:

```json
{
  "timestamp": "2026-08-16T14:23:01Z",
  "request_id": "req_8d7f...",
  "user_id": "stephen.agius@example.com",
  "user_groups": ["engineering", "security"],
  "tool": "internal-gateway",
  "model": "gpt-4.1-mini",
  "model_version": "2026-07-18",
  "classification_asserted": "amber",
  "classification_inferred": "amber",
  "input_tokens": 412,
  "output_tokens": 187,
  "guardrail_decisions": {
    "presidio_pii": "none",
    "lakera_injection": "low",
    "policy_engine": "allow"
  },
  "prompt_hash": "sha256:9c3f...",
  "response_hash": "sha256:d2e1..."
}
```

Hash the prompt and response by default; store the full text only with explicit policy and short retention. Don't accidentally build the privacy disaster you were trying to prevent.

---

## Step 6: Train Humans (The Hard Part)

Tech is easy compared to people. Make the training:

- **Short.** 25–30 minutes max. Quarterly refresh.
- **Concrete.** Walk through real incidents (Samsung, the various data-leak news cycles). People remember stories, not policy clauses.
- **Role-shaped.** Engineers see the slop-pattern reel. Sales sees the "do not paste contract terms into ChatGPT" reel. Support sees the "here is the customer-data redaction macro" reel.
- **Practised.** A tabletop exercise per team per year, walking through a hypothetical Red-tier paste and the response.

The goal isn't to memorise the policy — it's to install the reflex of "wait, what tier is this?" before paste.

---

## Step 7: Don’t Forget Compliance Has Its Own Asks

Two specific frameworks worth knowing as of 2026:

- **EU AI Act.** Phased enforcement, with the prohibited-practices ban from Feb 2025 and high-risk-system obligations rolling in across 2026 and 2027. If you serve EU users or process EU data, you need a clear inventory of any AI you're using in classified high-risk roles (recruitment, credit decisions, biometric ID, etc.) and the risk-management documentation behind it.
- **ISO/IEC 42001.** AI management-system standard published 2023. Increasingly being asked for in B2B procurement. If you have ISO 27001 already, the structure is familiar — it's an MSSP-style standard for AI specifically.

US regulation is more fragmented. NIST AI Risk Management Framework (AI RMF 1.0, with 1.1+ updates) is the closest thing to an industry baseline.

For internal sign-off, an "AI system register" mirroring your data-protection-impact-assessment register is probably what you'll end up needing. Same shape, AI-specific fields (model, vendor, data classifications, evals run, last review date).

---

## Final Thought

AI governance doesn’t need to be a 60-page document nobody reads. It needs to be:

- **Clear** on what's allowed by data class and tool tier — one page.
- **Backed by a gateway** so the easy path is the safe path.
- **Wired into CI** so AI-shaped mistakes get caught the same way other mistakes do.
- **Logged** so you can answer the question "what did we send and where did it go?".
- **Trained** because policy is what you do, not what you wrote.
- **Evolving** as fast as the tools — if your last review was over six months ago, it's stale.

If your AI "strategy" is just a slide saying "we’re exploring AI", you don’t have a strategy. You have a risk with marketing attached.

<img src="img/authors/geeky.jpg" width="40"/>
