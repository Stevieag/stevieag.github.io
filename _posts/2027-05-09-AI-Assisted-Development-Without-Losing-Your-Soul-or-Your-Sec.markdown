---
title:  "AI-Assisted Development Without Losing Your Soul (or Your Security)"
subtitle: "Using AI tools in 2026 as a professional engineer, not a code-copying robot"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/ai-assisted-development-without-losing-your-soul-or-you.jpg"
date: 2027-05-09
tags: AI devsecops security devops burnout craftsmanship
---

## AI Coding Tools Work — That's the Problem

By 2026, most teams use AI coding tools in some form: code completion, chat-based helpers, test generation, infra templates. They genuinely speed up routine work and help teams ship faster. The same data also shows real concerns about long-term code quality, security vulnerabilities, IP risk, and skill erosion when teams adopt AI without guardrails.

This isn't "AI bad". It's about using AI the way a good senior uses a junior — helpful, fast, and supervised. Concrete artefacts (PR templates, review checklists, CI gates, repo-level config) below. Pairs with [Using AI to Learn Without Turning Your Brain to Slop](https://geekyblinder.co.uk/#/2026/03/15/Using-AI-to-Learn) for the foundations and [The AI Gold Rush Is Making the Internet Worse](https://geekyblinder.co.uk/#/2026/01/04/The-AI-Gold-Rush-Is-Making) for the broader risk picture.

---

## Where AI Helps Most (If You Let It)

Teams report the biggest productivity wins in:

- **Boilerplate and glue** — wiring handlers, basic CRUD, serializers, DTOs.
- **Legacy spelunking** — explaining unfamiliar code, generating quick summaries.
- **Test scaffolding** — basic unit tests, fuzzing ideas, fixtures.
- **Infra and YAML** — drafting K8s manifests, CI pipelines, Terraform skeletons.

Used here, AI offloads drudge work and frees humans for design, architecture, and risk decisions. The trap is letting it creep into areas you don't understand, then shipping unread code.

---

## The Real Risks: Security, IP, and Skill Rot

Three big categories keep coming up in 2026 data.

### 1. Security Holes in AI-Generated Code

AI-generated code is often correct on the happy path, weak on edge cases, and prone to:

- Insecure defaults (permissive CORS, weak crypto, `alg:none` JWT verification — see [Auth, OAuth, and JWTs: How They Work and How Attackers Break Them](https://geekyblinder.co.uk/#/2026/06/07/Auth-OAuth-and-JWTs-How-They-Work-and-How-Attackers-Break-Th)).
- Missing input validation.
- Bad authz patterns (no ownership checks, IDOR-shaped APIs).
- Hallucinated package names — slopsquatting bait.

If nobody actually reviews it, you quietly ship new attack surface into prod.

### 2. IP and Licensing Landmines

- Code that closely resembles licensed/open-source snippets.
- Unclear training data provenance.
- Mixed licences sneaking into proprietary codebases.
- Compatibility issues (GPL-derived code in a proprietary product is a different problem to having it in an open-source library).

Legal and OSS counsel are increasingly writing policy around how AI can be used in code generation. Talk to yours; don't guess.

### 3. Over-Reliance and Skill Erosion

If AI always thinks for you:

- Troubleshooting and debugging muscles atrophy.
- Engineers stop deeply understanding their own systems.
- Onboarding gets harder because the architecture is inconsistent — over-engineered by suggestion in some places, fragile in others.

Bad for individuals; catastrophic for teams over a few years. The "Symptoms You've Stopped Learning" section of [Using AI to Learn](https://geekyblinder.co.uk/#/2026/03/15/Using-AI-to-Learn) is the canary.

---

## A DevSecOps Playbook for AI-Assisted Development

Treat AI as a first-class part of your DevSecOps model, with process and controls.

### 1. Set Team-Level Usage Rules

Document where AI is allowed (boilerplate, docs, tests, PoCs), restricted (core crypto, auth, payment logic, safety-critical paths), and banned (copy-pasting large blobs straight into production code; pasting customer data into prompts).

For the org-wide governance shape, see [AI Governance for Engineers: Guardrails That Aren't Just Slideware](https://geekyblinder.co.uk/#/2026/08/16/AI-Governance-for-Engineers-Guardrails-That-Arent-Just-Slide). For team-level practice, the rest of this section.

### 2. PR Template and Review Checklist

The simplest control that actually changes behaviour. Add an AI-disclosure section to your `.github/PULL_REQUEST_TEMPLATE.md` (or GitLab equivalent):

```markdown
## What changed
<!-- one or two sentences -->

## AI assistance disclosure
- [ ] No AI assistance
- [ ] AI-assisted (specify tool: Copilot / Cursor / Claude / ChatGPT / other: ___)
- [ ] AI-generated (>50% of new code)

If AI-assisted or AI-generated, I confirm:
- [ ] I have read every line and can explain why it works
- [ ] I have checked dependencies are real packages with known maintainers
- [ ] I have tested edge cases the AI did not suggest
- [ ] No secrets, customer data, or proprietary code were sent to a public AI tool

## Security review
- [ ] Input validation on every external boundary
- [ ] Authorization checks on every protected endpoint
- [ ] No new secrets in code or config
- [ ] Error handling doesn't leak sensitive data
- [ ] New dependencies have been reviewed
```

A reviewer-side checklist worth pinning in the team handbook:

```markdown
## Reviewing an AI-assisted PR

Before approving, check:
- [ ] Author has confirmed they understand every line (ask if unsure)
- [ ] No hallucinated package names — every new import exists with a credible
      maintainer and download history
- [ ] No drift from project conventions (style, error handling, logging,
      naming) — AI suggestions tend to be generic; flag inconsistency
- [ ] Tests cover not just the happy path but at least one abuse case
- [ ] No "kitchen-sink" defensive code (try/catch around every line, every
      possible config option exposed) — over-engineering is an AI tell
- [ ] Auth/authz logic, crypto, parsing, and deserialisation got an explicit
      second pair of eyes before approval
```

### 3. Bake Security Checks into the Pipeline

If AI can generate insecure patterns, automate catching them. A working GitHub Actions snippet that wires the standard gates for an AI-assisted-friendly project:

```yaml
# .github/workflows/security.yml
name: security-gates
on: [pull_request, push]

jobs:
  sast:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Semgrep
        uses: returntocorp/semgrep-action@v1
        with:
          config: |
            p/r2c-ci
            p/security-audit
            p/owasp-top-ten
            p/javascript            # or your stack
            p/jwt                   # catches alg:none and friends
            p/secrets

  sca:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Trivy filesystem scan
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: fs
          severity: HIGH,CRITICAL
          exit-code: 1
          ignore-unfixed: true

  secrets:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: { fetch-depth: 0 }
      - name: gitleaks
        uses: gitleaks/gitleaks-action@v2
        env:
          GITLEAKS_LICENSE: ${{ secrets.GITLEAKS_LICENSE }}

  iac:
    runs-on: ubuntu-latest
    if: hashFiles('**/*.tf', '**/*.yaml') != ''
    steps:
      - uses: actions/checkout@v4
      - name: Checkov
        uses: bridgecrewio/checkov-action@master
        with:
          quiet: true
          framework: terraform,kubernetes,dockerfile
```

Pair with branch-protection rules requiring all four jobs to pass before merge. AI becomes "just another contributor" feeding into the same secure pipeline.

For the deeper toolbox, see [The DevSecOps Toolbelt for 2026](https://geekyblinder.co.uk/#/2027/07/04/The-DevSecOps-Toolbelt-for-2026).

### 4. Adversarial Evals on AI-Integrated Features

If your *product* uses an LLM (chatbot, summariser, code-completion of customer code), add `garak` and `promptfoo` evals to CI for the prompts and pipelines. Catch jailbreaks and prompt injection before users do. The depth on this is in [Blue Team vs AI Red Team](https://geekyblinder.co.uk/#/2027/04/25/Blue-Team-vs-AI-Red-Team-How-to-Build-Defences-That-Learn-Fa).

---

## Repo-Level AI Configuration

Most assistants honour repo-local config files that tell them your standards. Use them. A working `copilot-instructions.md` (Copilot) / `.cursorrules` (Cursor) / `CLAUDE.md` (Claude) for a typical Node service:

```markdown
# AI Assistant Instructions for orders-service

## Stack and conventions
- Node.js 20 LTS, TypeScript strict mode
- Express 4.x with Zod for input validation
- Postgres via parameterised pg-promise — never string-interpolate SQL
- Auth: JWT verification with @simplewebauthn/server; allowlisted algorithms
- Logging: pino structured JSON; never log full bodies

## Security defaults
- Every route handler must validate input with a Zod schema
- Every route that returns user data must check ownership server-side
- Never store secrets in code; use process.env, with envalid validation
- All async DB calls inside try/catch with structured error logging

## What to avoid
- localStorage for tokens (use HttpOnly cookies via the BFF pattern)
- alg:none or unconstrained JWT verification
- String concatenation in SQL
- node-fetch (use the standard fetch); axios is approved for legacy code

## Test conventions
- Vitest, not Jest
- Each handler needs at least: happy-path, missing-input, unauthorised, IDOR
- Integration tests run against a real postgres in docker-compose, not mocks

## Style
- 2-space indent, single quotes, trailing commas
- Prefer named exports
- No comments unless explaining non-obvious WHY
```

The assistant pulls this in as context on every suggestion. Suggestions that would violate your conventions become rare.

---

## Best Practices for Individual Engineers

If you’re using AI day-to-day, treat it like a sharp tool.

### 1. Use AI to Improve Understanding, Not Replace It

Good prompts:

- *"Explain what this code does, line by line."*
- *"What are potential edge cases or security issues in this function?"*
- *"Give me three simpler implementations of this algorithm."*

Bad prompts:

- *"Write the full payment service with PCI-compliant security."*
- *"Generate a complete K8s stack for production."*

Use AI to learn and explore alternatives, then make the final call yourself. The full prompt catalogue is in [Using AI to Learn](https://geekyblinder.co.uk/#/2026/03/15/Using-AI-to-Learn).

### 2. Trust but Verify

For any non-trivial suggestion:

- Run tests; add new tests for edge cases AI didn’t consider.
- Check against known best practices: [OWASP](https://owasp.org/), language-specific secure coding guides, relevant RFCs.
- Validate performance and complexity. AI is prone to over-engineering — extra middleware, extra config knobs, extra interfaces nobody asked for.

If you can’t explain why it works and why it’s safe, you don’t own it.

### 3. Protect Your Inputs

Your prompts may be logged or used to retrain models, depending on the tool. Don’t paste:

- Full proprietary codebases.
- Secrets, keys, tokens.
- Sensitive customer data.
- Internal architecture diagrams the rest of the world doesn't get to see.

Use sanitised snippets, or self-hosted / on-prem models when dealing with sensitive contexts. Route everything through a sanctioned [AI gateway](https://geekyblinder.co.uk/#/2026/08/16/AI-Governance-for-Engineers-Guardrails-That-Arent-Just-Slide) where possible.

---

## Leadership: Preventing AI-Assisted Burnout and Chaos

Leaders sometimes assume "AI will fix burnout". Surveys show burnout stays high when AI is added without rethinking workload, expectations, and culture.

To use AI without frying your team:

- **Don't treat AI as free headcount.** If throughput increases by 30%, don't silently expand scope by 30%. The human review and judgement bottleneck doesn't speed up just because suggestions appear faster.
- **Invest in platform and DevSecOps.** Golden paths, internal platforms, CI/CD plus security automation give AI-assisted devs a safe runway. AI on top of a chaotic platform amplifies chaos.
- **Reward depth, not lines.** Encourage engineers to understand AI suggestions and architectural trade-offs. Reward deep debugging and design, not lines of code shipped.
- **Make space for the AI-free reps.** Once a quarter, ask the team to fix something hard the slow way. The skill of "knowing when the AI is wrong" is built by having the underlying skill in the first place.

AI plus good leadership and culture reduces toil. AI plus pressure and chaos accelerates burnout.

---

## The New Bar for Engineers

In 2026, the bar isn't "can you write everything by hand?". It’s:

- Can you **direct** AI tools effectively?
- Can you **spot** when they're wrong, insecure, or over-complicated?
- Can you keep your **craftsmanship and threat-modelling** skills sharp while using AI as an accelerator?

If you treat AI as a fast, fallible assistant — not an autopilot — you’ll ship more, ship safer, and still be proud of the systems you’re building ten years from now.

For the broader picture: [AI-shaped offence and defence in security teams](https://geekyblinder.co.uk/#/2027/03/28/AI-Hacking-for-Red-and-Blue-Teams-Friends-Foes-and-Autonomou). For the foundation: [Using AI to Learn](https://geekyblinder.co.uk/#/2026/03/15/Using-AI-to-Learn).

<img src="img/authors/geeky.jpg" width="40"/>
