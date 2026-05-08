---
title:  "Zero Trust Architecture: A Deep, Practical Walkthrough"
subtitle: "From buzzword to concrete design and rollout"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/zero-trust-architecture-a-deep-practical-walkthrough.jpg"
date: 2026-05-10
tags: zero-trust ZTNA NIST identity network security architecture
---

## So What Is Zero Trust, Really?

Zero Trust is not "install vendor X and call it a day". It's a security architecture built on one uncomfortable assumption: **nothing is implicitly trusted** — not your office network, not your VPN, not that laptop you've "always" used.

In NIST SP 800-207's framing, Zero Trust Architecture (ZTA) assumes breach as a starting point and continuously verifies every user, device, and request before granting tightly-scoped, per-session access. The principle is simple; the implementation is a multi-year programme. This post is the working walkthrough — the policies you can copy, the tooling that's actually any good, and the order to do it in so the business doesn't break.

For the auth pillar in particular, see [Auth, OAuth, and JWTs: How They Work and How Attackers Break Them](https://geekyblinder.co.uk/#/2026/06/07/Auth-OAuth-and-JWTs-How-They-Work-and-How-Attackers-Break-Th).

The three things to remember if you forget everything else:

- Never trust, always verify.
- Least privilege, everywhere.
- Continuous evaluation, not one-and-done checks.

---

## Core Pillars (Without the Vendor Bingo)

Different frameworks slice it slightly differently — NIST 800-207, CISA Zero Trust Maturity Model, the various 7-pillar models — but they converge on the same areas.

- **Identity** — strong, centralised auth, MFA, policy-driven access for users *and* workloads.
- **Device** — only healthy, compliant devices touch sensitive resources.
- **Network** — micro-segmentation, identity-aware proxies, encrypted everywhere.
- **Application & Workload** — apps authenticate and authorise properly; never trust the network.
- **Data** — classified, encrypted, monitored for abuse and exfiltration.
- **Automation & Analytics** — telemetry feeds policy decisions in real time.

If you remember nothing else: **identity + device health + least privilege + continuous monitoring**. The rest is implementation detail.

---

## Step 1: Define Your Protect Surface (Not "Secure Everything")

Zero Trust starts with **protect surfaces** — the specific data, apps, assets, and services that really matter. Pick three at most for the first phase. Common picks for most orgs:

- The IdP itself (Entra ID / Okta / Google Workspace tenant).
- Production cloud admin consoles + key-management services.
- The customer-data plane (the database holding PII / payment / health records).

For each protect surface, document:

```yaml
# protect-surface.yaml — keep one per system in git
name: production-postgres-cluster
classification: red
owner: data-platform-team
data_sensitivity: customer-pii, payment-card
who_needs_access:
  human:
    - role: dba-oncall
      method: jit-via-pam
    - role: data-engineer
      method: read-only-via-bastion
  workload:
    - service: payments-api
      method: workload-identity + iam-binding
allowed_paths:
  - source: pam-bastion
    proto: tcp/5432
    cipher: tls1.3
disallowed_paths:
  - source: developer-laptop
    note: never standing access; jit only
breakglass:
  - account: emergency-dba
    audit: pagerduty + slack #security-breakglass
    review: weekly
```

You'll quickly realise you don't need ZT perfection everywhere on day one. You need strong ZT controls **around the protect surfaces first**, then expand.

---

## Step 2: Identity as the Control Plane

Identity is the first and most important pillar. Get this wrong and nothing else matters.

### Conditional Access Policies That Actually Bite

Pick whichever IdP you have and start with three policies that catch the largest blast-radius cases. Examples in Entra/Okta-shape:

**Policy 1: MFA + compliant device for all admin roles**

```json
{
  "displayName": "ZT-01 Admin: MFA + compliant device required",
  "state": "enabled",
  "conditions": {
    "users": {
      "includeRoles": [
        "Global Administrator",
        "Privileged Role Administrator",
        "Security Administrator",
        "Cloud Application Administrator"
      ]
    },
    "applications": { "includeApplications": ["All"] }
  },
  "grantControls": {
    "operator": "AND",
    "builtInControls": [
      "mfa",
      "compliantDevice",
      "passwordChange"
    ]
  },
  "sessionControls": {
    "signInFrequency": { "value": 4, "type": "hours" },
    "persistentBrowser": { "mode": "never" }
  }
}
```

**Policy 2: Block legacy auth (basic auth, IMAP, SMTP, POP)** — these protocols predate MFA and are the single biggest credential-stuffing vector.

```json
{
  "displayName": "ZT-02 Block legacy authentication everywhere",
  "state": "enabled",
  "conditions": {
    "users": { "includeUsers": ["All"] },
    "clientAppTypes": ["exchangeActiveSync", "other"]
  },
  "grantControls": { "operator": "OR", "builtInControls": ["block"] }
}
```

**Policy 3: Risk-based MFA for normal users** — Microsoft Entra ID Protection (or Okta Behaviour Detection / equivalent) flags impossible travel, new countries, leaked credentials, anomalous IPs. Tie those signals to step-up MFA.

```json
{
  "displayName": "ZT-03 Risk-based step-up MFA",
  "state": "enabled",
  "conditions": {
    "users": { "includeUsers": ["All"] },
    "signInRiskLevels": ["high", "medium"]
  },
  "grantControls": {
    "operator": "AND",
    "builtInControls": ["mfa"]
  }
}
```

### JIT Access via PAM (No Standing Admin Rights)

Privileged accounts are where attackers go after they're inside. Standing access is the attack surface; just-in-time access is the fix. Real options as of 2026:

- **Teleport** — open-source-core, modern, certificate-based. Strong fit for K8s/SSH/database access.
- **HashiCorp Boundary** — open-source-core, integrates well with Vault for credential brokering.
- **CyberArk PAM** — enterprise-heavy, broad coverage, expensive.
- **BeyondTrust PRA** — similar enterprise tier, good for legacy estates.
- **Cloud-native** — AWS IAM Identity Center temporary access, GCP service-account impersonation, Entra PIM for Azure roles. Free-ish if you're already on the platform.

The common shape: a request via Slack/portal → approval (auto for trusted patterns, human for sensitive) → time-bound credential issued → audited session → credential expires automatically. Standing god-accounts go away.

Treat your IdP as the **brain** of Zero Trust. It decides "who is this really, and under what conditions should they get *any* access?"

---

## Step 3: Device Trust — Healthy Endpoints or No Entry

Zero Trust doesn't just care who you are; it cares what you're holding. A compromised laptop is a compromised "identity with extra steps".

### What "Healthy" Means in Practice

A workable compliance baseline for a managed laptop:

- OS within N versions of current. Auto-updates enforced.
- Disk encryption (FileVault on macOS, BitLocker on Windows) with key escrow.
- EDR running, signatures fresh (CrowdStrike, SentinelOne, Defender for Endpoint, etc.).
- Firewall on, screen-lock under 5 min, password complexity meets policy.
- No jailbreak / no rooted state.
- MDM / device certificate present.

### Tooling That Enforces It

- **Microsoft Intune** — natural fit if you're on Entra; deep integration with Conditional Access.
- **Jamf** — macOS-first, the standard for Apple-heavy orgs.
- **Kandji** — modern macOS MDM; cleaner UX than Jamf for smaller teams.
- **Workspace ONE / Ivanti** — multi-platform enterprise.
- **Google Workspace Endpoint Management** — basic, free with Workspace.

The compliance check feeds back into Conditional Access — Tier-0 apps (IdP, admin portals, production consoles) only allow connections from compliant devices, regardless of who the user is.

This is where Zero Trust starts to feel real: a password alone is no longer a skeleton key.

---

## Step 4: Network — Micro-Segmentation and ZTNA

ZTA doesn't kill firewalls; it makes them smarter and closer to what matters.

### ZTNA Tools (Replace the Flat VPN)

The flat-VPN model — "if you're authenticated to the VPN, you can reach anything internal" — is the single biggest legacy ZT problem. ZTNA tools replace it with identity-aware, application-level access.

- **Cloudflare Access / Cloudflare Tunnel** — strong default for cloud-first orgs; free tier covers small teams.
- **Tailscale** — WireGuard-based mesh VPN with identity-aware ACLs. Loved by smaller teams; getting more enterprise-capable.
- **Twingate** — purpose-built ZTNA, identity-integrated, decent SSH/HTTP support.
- **Zscaler Private Access** — enterprise-tier, strong for large global estates.
- **Palo Alto Prisma Access** — large-enterprise ZTNA + SASE bundle.

A working Tailscale ACL, identity-aware, that gives developers SSH to dev hosts but not prod:

```hcl
{
  "groups": {
    "group:developers": ["alice@example.com", "bob@example.com"],
    "group:sre":        ["carol@example.com"],
  },
  "tagOwners": {
    "tag:dev-host":  ["group:sre"],
    "tag:prod-host": ["group:sre"],
  },
  "acls": [
    { "action": "accept",
      "src":    ["group:developers"],
      "dst":    ["tag:dev-host:22"] },
    { "action": "accept",
      "src":    ["group:sre"],
      "dst":    ["tag:dev-host:22", "tag:prod-host:22"] },
  ],
  "ssh": [
    { "action": "check",
      "src":    ["group:developers"],
      "dst":    ["tag:dev-host"],
      "users":  ["root", "ubuntu"] },
  ],
}
```

`"action": "check"` here forces a re-authentication before SSH — even on a connected tailnet, prod-shaped destinations require fresh confirmation.

### Kubernetes NetworkPolicy: Micro-Segmentation Inside the Cluster

Default-deny per namespace, then allow only what each service actually needs:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: payments-default-deny
  namespace: payments
spec:
  podSelector: {}
  policyTypes: [Ingress, Egress]
  ingress: []
  egress:
    # allow DNS only
    - to:
        - namespaceSelector:
            matchLabels: { kubernetes.io/metadata.name: kube-system }
      ports:
        - { port: 53, protocol: UDP }
---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: payments-api-egress
  namespace: payments
spec:
  podSelector: { matchLabels: { app: payments-api } }
  policyTypes: [Egress]
  egress:
    # allow only to the postgres service in the data namespace
    - to:
        - namespaceSelector:
            matchLabels: { kubernetes.io/metadata.name: data }
          podSelector:
            matchLabels: { app: postgres }
      ports:
        - { port: 5432, protocol: TCP }
```

Pair with [Cilium](https://cilium.io/) or [Calico](https://www.tigera.io/project-calico/) for L7-aware policies (HTTP method, path, header) when L4 isn't enough.

### Service-to-Service mTLS

For internal service auth, mTLS via a service mesh ([Linkerd](https://linkerd.io/), [Istio](https://istio.io/), [Cilium Service Mesh](https://cilium.io/use-cases/service-mesh/), [Consul](https://www.consul.io/)) gives you mutual identity verification without per-app TLS engineering. Authorization policies on top:

```yaml
apiVersion: security.istio.io/v1
kind: AuthorizationPolicy
metadata:
  name: payments-db-only-payments-api
  namespace: data
spec:
  selector:
    matchLabels: { app: postgres }
  action: ALLOW
  rules:
    - from:
        - source:
            principals:
              - "cluster.local/ns/payments/sa/payments-api"
      to:
        - operation:
            ports: ["5432"]
```

Now the database accepts connections only from the `payments-api` service-account-identity, not from any pod that happens to land in the right namespace.

For the broader networking-without-the-VPN-myth take, see [Zero Trust VPNs and the Myth of the Safe Internal Network](https://geekyblinder.co.uk/#/2026/05/24/Zero-Trust-VPNs-and-the-Myth-of-the-Safe-Internal-Network).

---

## Step 5: Application and Data Controls

Apps and data can no longer assume the network is the bouncer.

### Authorization with a Policy Engine

Centralise authorization decisions in [OPA](https://www.openpolicyagent.org/) or [AWS Cedar](https://www.cedarpolicy.com/) so they're auditable and consistent across services.

A Cedar policy that enforces "users can read their own profile; admins can read anyone's; nobody else":

```cedar
permit (
  principal,
  action == Action::"ReadProfile",
  resource
)
when {
  principal == resource.owner ||
  principal in Group::"admins"
};

forbid (
  principal,
  action == Action::"ReadProfile",
  resource
)
unless {
  principal == resource.owner ||
  principal in Group::"admins"
};
```

Enforcement happens in the app — the policy engine evaluates the decision and returns allow/deny. The app trusts the engine, not its own logic.

### Data Classification and Encryption

- Classify by sensitivity (public, internal, confidential, restricted/regulated).
- Encrypt at rest (volume + DB-level + envelope encryption with cloud KMS).
- Encrypt in transit (TLS 1.2+, ideally 1.3).
- Customer-managed keys (CMK) for the highest sensitivity tiers — gives you the kill-switch and the audit trail.
- Database activity monitoring on critical stores; alert on anomalous access patterns and bulk reads.

DLP at the egress points (web proxy, email, SaaS) catches the "user pastes customer data into a chatbot" pattern. See [AI Governance for Engineers](https://geekyblinder.co.uk/#/2026/08/16/AI-Governance-for-Engineers-Guardrails-That-Arent-Just-Slide) for the AI-specific shape.

---

## Step 6: Policy Engine and Telemetry — The ZT "Brain and Nerves"

Zero Trust decisions should be made by policy engines that see identity, device, network, and app context — not scattered if-statements across thirty services.

The architecture, in NIST language:

```
[ User / Workload / Device ]
        │
        ▼
[ Policy Enforcement Point (PEP) ]      ← proxy, gateway, sidecar, agent
        │   "can this happen?"
        ▼
[ Policy Decision Point (PDP) ]         ← OPA, Cedar, IdP CA, ZTNA controller
        │   reads context from:
        ▼
[ Identity, Device, Threat-intel, Risk signals, Audit history ]
```

### What to Log

The telemetry Zero Trust depends on:

- **IdP** — every sign-in (success/failure), MFA challenge result, Conditional Access decision, role activation, consent grant.
- **Device** — compliance state changes, EDR detections, OS-level audit (sudoers, new processes), patch level.
- **Network** — VPC flow logs, ZTNA access decisions, DNS queries (especially to known-bad domains), TLS metadata.
- **Application** — authn/authz decisions, sensitive-action audit events (admin role created, API key generated, data exported).
- **Data** — DB activity logs, S3 access logs (or equivalent), DLP events.

### Detections That Earn Their Keep

Feed all of the above into a SIEM/XDR ([Microsoft Sentinel](https://azure.microsoft.com/en-us/products/microsoft-sentinel), [Splunk](https://www.splunk.com/), [Elastic SIEM](https://www.elastic.co/security/siem), [Sumo Logic](https://www.sumologic.com/), [Panther](https://panther.com/)). The Zero-Trust-specific detections worth building:

- **Impossible travel** — sign-ins from geographically incompatible locations within a short window.
- **New device + privileged action** — first time a device is seen, and immediately a sensitive operation is performed.
- **Standing-admin escalation paths** — any user gaining standing admin rights without going through PAM.
- **Out-of-hours access to crown-jewel apps** — with allowlist for on-call rotations.
- **Token or credential reuse from a different IP/user-agent** — refresh-token anomalies are particularly noisy without this rule.
- **JIT request denials** — repeated denials from the same user often signal an attacker probing.
- **Conditional Access policy bypass attempts** — sign-ins blocked by policy, especially clustered from the same source.

Zero Trust without telemetry is just a slogan. Continuous verification dies on bad logging.

---

## Step 7: A Phased Implementation Plan (Realistic, Not Fantasy)

You can't big-bang ZTA. You *can* roll it out in phases over 18–36 months.

**Phase 1 — Prepare and Map (Months 1–3).** Asset and identity inventory. Define top three protect surfaces. Gap analysis vs NIST SP 800-207 / CISA ZT Maturity Model. Pick the SIEM/policy engine vendor.

**Phase 2 — Identity and Device Foundation (Months 3–9).** Unify IdPs, full SSO + MFA rollout. Conditional Access baseline (the three policies above). Block legacy auth. Enforce baseline device compliance for privileged access. Kill flat VPN for new app rollouts.

**Phase 3 — Network and Access Modernisation (Months 6–15, parallel).** Pilot ZTNA for one critical internal app. Micro-segment around the highest-value system. Enforce TLS / mTLS everywhere for those flows. Roll out PAM for privileged access; turn off standing-admin where safe.

**Phase 4 — Application and Data Hardening (Months 9–24).** Refactor key apps to token-based authn/authz with a policy engine. Turn on DLP and DB activity monitoring on the riskiest data stores. Introduce policy engines for infrastructure (OPA/Kyverno in K8s).

**Phase 5 — Telemetry and Continuous Improvement (Ongoing from month 12).** Centralise logs. Build the ZT-specific detections. Iterate on policy based on real behaviour. Expand ZTNA and micro-segmentation to more systems each quarter.

Pace it so the business doesn't hate you. Audit modes before enforce modes. Pilot teams that opt in, then wider rollouts.

---

## Worked Example: Zero Trust for a Remote-First SaaS Startup

50 staff, all remote, AWS + Entra ID + GitHub + Slack + Snowflake. Realistic 12-month target:

- **Identity** — Entra ID with Conditional Access (the three policies above), MFA mandatory, passkeys for all admins, no legacy auth.
- **Device** — Intune for Windows, Kandji for Mac. Compliance baseline enforced for prod access.
- **Network/Access** — Cloudflare Access for internal tools (Jenkins, Jira, Argo). Tailscale for SSH to staging hosts. AWS SSO with permission sets for cloud console access; no IAM users with long-lived keys. Production DB access via Teleport with JIT approvals.
- **Apps** — All services validate JWTs against Entra (see [Auth, OAuth, and JWTs](https://geekyblinder.co.uk/#/2026/06/07/Auth-OAuth-and-JWTs-How-They-Work-and-How-Attackers-Break-Th)). OPA policies for the customer-data API. Every admin action audited.
- **Data** — Customer PII encrypted with CMK. S3 buckets default-block-public + bucket policies. Snowflake row-level security. Quarterly access review for restricted datasets.
- **Telemetry** — Sentinel ingesting Entra, Intune, Cloudflare, AWS CloudTrail, GitHub audit, Snowflake. Detections for the patterns above. Weekly review of denied-access patterns.

That's not "Zero Trust complete". It *is* Zero Trust **in motion** — and that's what matters in year one.

---

## Common Pitfalls

- **Thinking Zero Trust is a product.** Vendors are building blocks. The architecture and policies are yours.
- **Trying everything at once.** Start with three protect surfaces and high-impact flows.
- **Locking everything down and breaking the business.** Pilot, monitor, then enforce. Audit-mode policies first.
- **Ignoring people and process.** Train teams on *why* it's changing. Integrate into normal engineering workflow.
- **Forgetting break-glass.** The day every IdP is down, you'll need offline access to critical systems. Plan that, document it, test it quarterly.

---

## Final Thought

Zero Trust done properly isn't a shiny dashboard. It's a multi-year shift in how your org thinks about access, identity, devices, and apps. The good news is the building blocks exist: IdP Conditional Access, MDM, ZTNA, PAM, policy engines, mesh mTLS, SIEM. The hard work is the order, the policies, and the patience to roll it out without breaking the business.

Start small. Be honest about your current state. Push toward identity- and device-centric decisions, tight auditable access to what matters, continuous verification instead of blind trust.

If "on the VPN" still means "basically god mode", you've already picked your first Zero Trust project.

<img src="img/authors/geeky.jpg" width="40"/>
