---
title:  "Deep Walkthrough: Threat Modelling a Simple Web App"
subtitle: "From blank page to ‘we actually understand how this could be attacked’"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/deep-walkthrough-threat-modelling-a-simple-web-app.jpg"
date: 2026-10-11
tags: threat-modelling web-app security devsecops STRIDE
---

## Deep Walkthrough: Threat Modelling a Simple Web App

Threat modelling often gets treated like some mystical architecture ceremony. In reality, it’s a structured way of asking “how could this thing be broken, and what are we going to do about it?”

Let’s walk through a simple example so you can actually run this with your own team.

---

## The System: A Boring but Realistic Web App

Assume:

- Users log in via email/password.
- They can view and edit their own profile and some “documents”.
- Backend is a REST API talking to a SQL database.
- There’s an admin panel for support staff.

We’ll threat‑model:

- Auth & session.
- Data access.
- Admin functions.

---

## Step 1: Draw a Rough Data Flow Diagram (DFD)

You don’t need Visio. A whiteboard or Obsidian canvas is fine.

Elements:

- External entities:
  - User’s browser.
  - Admin’s browser.
- Entry points:
  - HTTPS load balancer / reverse proxy.
- Components:
  - Web/API servers.
  - Auth service (if separate).
  - Database.
- Data stores:
  - User table.
  - Documents table.
  - Audit logs.

Draw arrows for:

- Login flow.
- Normal CRUD operations.
- Admin actions.

Now you can point at something concrete when you say “what if this goes wrong?”

---

## Step 2: Choose a Lens – STRIDE Works Fine

Use STRIDE:

- Spoofing (who you are).
- Tampering (changing data).
- Repudiation (denying actions).
- Information disclosure.
- Denial of service.
- Elevation of privilege.

Walk each data flow and component, asking:

- What STRIDE categories apply here?
- What could an attacker do?
- What would the impact be?

---

## Step 3: Identify Key Threats

Examples:

**Login endpoint:**

- Spoofing:
  - Credential stuffing with reused passwords.
  - Phished credentials.
- DoS:
  - Brute forcing causing lockouts or load.

Mitigations:

- Rate limiting.
- MFA.
- Password strength and checking against known breach lists.

**User → Docs API → DB:**

- Tampering/Info disclosure:
  - Insecure direct object reference (IDOR): user accessing `doc_id` that isn’t theirs.
- Elevation:
  - Missing checks that let normal users hit admin‑only endpoints.

Mitigations:

- Proper authz:
  - Always check `owner_id` in DB, not just trust client IDs.
- Centralised authorisation logic instead of sprinkling `if isAdmin` everywhere.

**Admin panel:**

- Elevation:
  - Privilege escalation via flaws in role handling.
- Repudiation:
  - No real audit of who did what.

Mitigations:

- Role‑based access control.
- Stronger auth, potentially separate IdP policy for admins.
- Detailed audit logging for admin actions.

---

## Step 4: Prioritise – You Can’t Fix Everything at Once

Score threats roughly on:

- Likelihood (L).
- Impact (I).

Focus on:

- High L / High I first.
- High I / medium L next.

For most web apps, top tier will be:

- Auth & session issues.
- Access control/IDOR.
- Admin misuse/compromise.
- Injection into DB or template engines.

Make a small list of:

- 5–10 priority threats.
- Owner for each.
- Proposed mitigation.

This becomes your short‑term security roadmap.

---

## Step 5: A Sample Threat-Model Document

Stash this in `docs/threat-model.md` in the repo. The shape is the artefact — fill it in for your own app and update each release.

```markdown
# Threat Model: Acme Docs (v1.2 — 2026-10)

## Scope
- In: web frontend, REST API, Postgres, S3 (uploaded files), Auth0 IdP.
- Out: marketing site, billing system (separate threat model).

## Data Flow Diagram
[ user browser ] -> [ ALB ] -> [ API ] -> [ Postgres ]
                              \-> [ S3 (uploads) ]
                              \-> [ Auth0 (OIDC) ]

## Trust Boundaries
- Internet → ALB
- ALB → API (TLS, no further auth on the LB itself)
- API → Postgres (network policy + DB user auth)
- API → S3 (IAM role)

## Top Threats (STRIDE-tagged, scored Likelihood × Impact 1-5)

| # | Threat                                       | STRIDE | L | I | Mitigation                                     | Owner | Status   |
|---|----------------------------------------------|--------|---|---|------------------------------------------------|-------|----------|
| 1 | Credential stuffing on login                 | S      | 5 | 4 | Rate-limit + breach-list check + MFA           | api   | Done     |
| 2 | IDOR on /docs/:id                            | T,I    | 4 | 5 | Server-side ownership check; tests on every PR | api   | Done     |
| 3 | SSRF via document-import URL                 | T,I    | 3 | 4 | Allowlist + IMDSv2 only on hosts               | api   | Planned  |
| 4 | Admin token leak via XSS in shared docs      | E,I    | 3 | 5 | CSP + HttpOnly cookies via BFF                 | web   | In progress |
| 5 | S3 bucket misconfig exposes uploads          | I      | 2 | 5 | Public-access-block + Checkov gate             | infra | Done     |
| 6 | Audit-log tampering by compromised admin     | R      | 2 | 4 | WORM bucket + signed log shipping              | infra | Planned  |
| 7 | DoS via large file uploads                   | D      | 3 | 3 | Max body size + per-user rate limit            | api   | Done     |

## Accepted Risks (with expiry)
- A8 — No anomaly detection on admin actions yet. Owner: security. Reaccept by: 2027-Q1.

## Out-of-Band Notes
- Last reviewed: 2026-10-09 by @stephen, @alice, @bob.
- Next review: 2027-04 (next major release).
```

Two things worth noticing in this template:

- **Scoring is rough on purpose.** L×I on a 1-5 scale forces conversations without pretending the numbers are accurate. The interesting bit is the discussion that produces the numbers, not the numbers themselves.
- **Accepted risks have expiry dates.** "We're not fixing this" is a valid choice; "we're not fixing this and never reviewing it" is technical security debt that compounds.

## Step 6: Feed It Back Into Dev and DevSecOps

Threat model isn’t a static doc:

- Capture it in your repo (`docs/threat-model.md`) so it lives next to the code it describes.
- Link security stories/issues to specific row numbers in the table — when the issue tracker says "fixes T3", you can read what T3 actually was.
- Update when you add new features, change auth flows, migrate infra (e.g. to K8s or to a new IdP).

Add checks to:

- PR templates: "Does this change affect any documented threats?"
- Design reviews: quick threat-modelling pass for new major components.

For the Obsidian-shaped variant of this — managing many threat models with consistent frontmatter and a Dataview dashboard for stale ones — see [Obsidian as a Second Brain for Security and DevOps](https://geekyblinder.co.uk/#/2027/02/28/Obsidian-as-a-Second-Brain-for-Security-and-DevOps).

---

## Final Thought

Threat modelling doesn’t need a special tool or a consultancy. It needs:

- A diagram.
- A structured way to think about bad things.
- A willingness to write down “we chose not to fix this *yet*, and here’s why.”

Run a 60–90 minute session with your team for one app. You’ll be surprised how much risk you surface — and how many low‑effort mitigations you find once everyone’s actually looking.

<img src="img/authors/geeky.jpg" width="40"/>