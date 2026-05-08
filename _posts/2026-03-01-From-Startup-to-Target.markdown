---
title:  "From ‘We’re Just a Startup’ to ‘We’re a Target’"
subtitle: "Building a security baseline before the big clients arrive"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/from-were-just-a-startup-to-were-a-target.jpg"
date: 2026-03-01
tags: startups security baseline SOC2 ISO27001 devsecops
---

## From “We’re Just a Startup” to “We’re a Target”

Every founder tells themselves the same story: “We’ll sort security later, once we’ve proved the product.” Then “later” arrives in the form of big‑name clients, vendor questionnaires, and — if you’re unlucky — attackers.

You don’t need a Fortune 500 security budget. You do need a baseline.

---

## The Things You Should Never Have Skipped

Some controls should exist from day zero:

- Identity and access management basics: unique accounts, MFA everywhere, no shared “admin” logins.
- Secrets management: no API keys in `.env` files committed to Git; use a proper secrets store.
- Environment separation: clear dev/test/prod boundaries, with restricted access to prod.
- Logging: centralised logs for infra and apps, retained long enough to investigate incidents.

If you’re moving from scrappy startup to “we have serious clients now,” you need to check:

- Are backups tested and restorable?
- Do you have at least a basic incident response plan (who does what, when)?
- Do you know your data flows and where customer data actually lives?

---

## What Becomes Non‑Negotiable as You Grow

Once you’re holding sensitive data for large clients, the must‑haves look like:

- Formal access control (RBAC) across cloud, K8s, CI/CD, and SaaS; no “everyone is Owner on the project” nonsense.
- Strong endpoint security for staff laptops (disk encryption, EDR, patching).
- Vendor risk management: don’t shove your data into random SaaS without understanding how they secure it.
- Vulnerability management: regular scanning plus a way to triage and remediate, not just create tickets that rot.

For many B2B contracts you’ll be asked about:

- SOC 2 / ISO 27001 alignment, or at least controls inspired by them.
- Data residency and retention policies.
- How you handle security incidents and notify customers.

You don’t need a certificate on day one, but you do need credible answers.

---

## Security by Phase, Not by Panic

Think in phases:

**Seed / Early:**

- Harden IAM, MFA, secrets, backups.
- Get basic logging and alerting in place.
- Document minimal policies (acceptable use, access control).

**Series A:**

- Formalise RBAC, separate duties in prod vs dev.
- Introduce security reviews for major features.
- Start threat modelling your core architecture.

**Post‑Enterprise Logo:**

- Dedicated security owner (if not a team).
- Regular third‑party tests (pentests, cloud config reviews).
- Clear change management around risky systems.

Security that grows with you beats security you panic‑buy after the first breach.

---

## A One-Page Baseline Checklist (Stick This in a Doc)

Steal this. Adjust the owners. Tick or red-flag every line. If a row stays red for more than a quarter, it's a backlog item that's earned the right to a real conversation about scope vs scale.

```markdown
# Startup Security Baseline — last reviewed: ____

## Identity & access
- [ ] SSO (Google / Okta / Entra) for every SaaS that supports it
- [ ] MFA mandatory on email, Git, cloud console, and IdP
- [ ] No shared "admin" logins; per-human accounts only
- [ ] Joiner/leaver checklist with same-day SaaS deprovisioning
- [ ] Break-glass admin account documented + tested quarterly

## Code & secrets
- [ ] No secrets in repos (gitleaks pre-commit + CI scan)
- [ ] Secrets stored in Vault / cloud secret manager (not .env)
- [ ] Per-env secrets separation (no prod creds in dev)
- [ ] Dependency scanning on every PR (Snyk / Trivy / Dependabot)
- [ ] SAST on every PR (Semgrep / GitHub Advanced Security)

## Cloud & infra
- [ ] IaC for everything that matters (Terraform / Pulumi)
- [ ] Cloud config monitoring (Security Hub / Defender for Cloud / SCC)
- [ ] No public S3/Blob/GCS unless explicit, reviewed, and tagged
- [ ] Production access via SSO + JIT (no standing admin)
- [ ] CloudTrail / Audit Logs / Activity Logs centralised + retained

## Endpoints
- [ ] Disk encryption (FileVault / BitLocker) on every laptop
- [ ] EDR / antivirus running, signatures fresh
- [ ] OS patch SLA (e.g. 14 days for high CVEs)
- [ ] MDM enrolled (Intune / Jamf / Kandji)
- [ ] Lock screen, password manager use, screen-share hygiene baked in

## Data
- [ ] Customer data classified (where it lives, who can see it)
- [ ] Encryption at rest + in transit, no exceptions
- [ ] Backups exist, are tested, and stored off the production account
- [ ] Data retention + deletion policy written and enforced
- [ ] DSAR / right-to-be-forgotten process documented

## Process
- [ ] Documented IR plan with on-call rotation
- [ ] Vendor risk: every third-party tool reviewed before onboarding
- [ ] Acceptable Use Policy + AI usage policy signed at hire
- [ ] Annual security awareness training (real, not slideware)
- [ ] At least one pentest in the last 12 months
```

This is roughly the SOC 2 / ISO 27001 starter scope mapped to engineering reality. Most B2B questionnaires from sensible buyers boil down to "show me you can answer most of these confidently". You don't need certificates on day one; you need to be able to walk a serious customer through this list without inventing things.

For the cloud-side deepening, see [Building a Cloud Security Baseline: From S3 Buckets to CNAPP](https://geekyblinder.co.uk/#/2026/06/21/Building-a-Cloud-Security-Baseline-From-S3-Buckets-to-CNAPP). For the architecture this lives inside, [Zero Trust Architecture: A Deep Practical Walkthrough](https://geekyblinder.co.uk/#/2026/05/10/Zero-Trust-Architecture-A-Deep-Practical-Walkthrough).

---

## Final Thought

If you’re already signing big clients, congratulations: you’re now interesting to people you’d rather weren’t interested in you.

You can’t retroactively secure year one, but you can stop pretending that "we’re just a startup" is still a valid excuse. Draw a line, build a baseline, and make "we take security seriously" something you can demonstrate — not just say.

<img src="img/authors/geeky.jpg" width="40"/>