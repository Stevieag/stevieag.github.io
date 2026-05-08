---
title:  "Deep Walkthrough: Hardening a Kubernetes Namespace for a Real Team"
subtitle: "RBAC, Pod Security, and network policies without losing everyone’s will to live"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/deep-walkthrough-hardening-a-kubernetes-namespace-for-a.jpg"
date: 2026-09-27
tags: kubernetes security RBAC network-policy devsecops
---

## Deep Walkthrough: Hardening a Kubernetes Namespace for a Real Team

“Kubernetes hardening” often turns into either a 200‑page CIS benchmark or vibes‑based YAML. Let’s do something more useful: take one namespace and walk it from “wild west” to “this wouldn’t embarrass us in an audit.”

Assume: one product team, one namespace, shared cluster.

---

## Step 1: Namespace and Basic Separation

Give the team:

- Their own namespace, e.g. `team-a-prod` and `team-a-staging`.
- A convention:
  - `*-prod` = stricter, fewer humans.
  - `*-staging` = more freedom, but still not chaos.

Lock down:

- Don’t let people deploy straight into `default` or `kube-system`.
- Network policies will assume namespace separation, so get this right early.

---

## Step 2: RBAC – Who Can Do What?

Create:

- A `developer` role:
  - Can CRUD most resources in `team-a-staging`.
  - Read‑only in `team-a-prod` (logs, events, pod specs).
- A `release-engineer` or `system` role:
  - Can deploy/update in `team-a-prod`.
  - Maybe held by CI/CD service accounts, not humans.

Use:

- RoleBindings to tie roles to groups/service accounts.
- Group claims from your IdP (e.g. “k8s-team-a-devs”) instead of per‑user RBAC.

Goal: people can do their job without needing `cluster-admin` “just in case.”

---

## Step 3: Pod Security (PodSecurityStandards / Admission)

If your cluster supports the new Pod Security Admission:

- Start with `baseline` for staging.
- `restricted` for prod namespace.

Enforce:

- No privileged containers.
- No hostPath mounts unless explicitly allowed.
- Non‑root users where possible.

Keep a small documented escape hatch for weird cases, but require justification and periodic review.

---

## Step 4: Network Policies – Stop Everything Talking to Everything

By default, K8s is “allow all” inside the cluster. Fix that.

In `team-a-prod`:

- Default‑deny ingress:
  - Only allow:
    - Ingress controller to hit app pods.
    - App pods to talk to DB/cache/whatever is needed.
- Default‑deny egress (if you’re brave):
  - Allow:
    - DNS.
    - Necessary external APIs.
    - Internal services.

This can be iterative:

- Start by restricting between namespaces.
- Then tighten inside the namespace around particularly sensitive services.

Use labels wisely (`app`, `role`, `tier`) to make policies readable.

---

## Step 5: Secrets and Config

Baseline:

- Use Kubernetes Secrets or external secret stores (Vault, AWS/GCP/etc. Secrets Manager).
- No secrets in ConfigMaps, no hardcoded values in manifests.

Better:

- External secrets operator pulling from your cloud vault.
- RBAC limiting who/what can read those secret objects.

Add:

- Periodic secret rotation where possible.
- Policies (Kyverno/OPA) to reject manifests that try to sneak env vars with obviously secret‑looking keys into plain ConfigMaps.

---

## Step 6: Admission Control and Policy as Code

Use a policy engine — [Kyverno](https://kyverno.io/) (YAML-native, easier to read) or [OPA Gatekeeper](https://open-policy-agent.github.io/gatekeeper/) (Rego, more powerful) — to enforce things at admission rather than discovering them in production.

A working Kyverno policy that disallows `latest` image tags, requires resource limits, and enforces mandatory ownership labels:

```yaml
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: ns-baseline
  annotations:
    policies.kyverno.io/category: Best Practices
spec:
  validationFailureAction: Audit   # flip to Enforce once clean
  background: true
  rules:
    - name: disallow-latest-tag
      match:
        any:
          - resources:
              kinds: [Pod]
              namespaces: ["team-a-prod", "team-a-staging"]
      validate:
        message: "Image tag ':latest' or empty tag is not allowed."
        pattern:
          spec:
            containers:
              - image: "!*:latest & *:*"

    - name: require-resources
      match:
        any:
          - resources:
              kinds: [Pod]
              namespaces: ["team-a-prod"]
      validate:
        message: "CPU and memory requests/limits are required."
        pattern:
          spec:
            containers:
              - resources:
                  requests: { cpu: "?*", memory: "?*" }
                  limits:   { cpu: "?*", memory: "?*" }

    - name: require-ownership-labels
      match:
        any:
          - resources:
              kinds: [Deployment, StatefulSet, DaemonSet, Job, CronJob]
              namespaces: ["team-a-prod", "team-a-staging"]
      validate:
        message: "Workloads must carry team and owner labels."
        pattern:
          metadata:
            labels:
              team: "?*"
              owner: "?*"
              env: "?*"

    - name: disallow-host-namespaces
      match:
        any:
          - resources:
              kinds: [Pod]
              namespaces: ["team-a-prod", "team-a-staging"]
      validate:
        message: "Host networking, PID, and IPC are not allowed."
        pattern:
          spec:
            =(hostNetwork): false
            =(hostPID): false
            =(hostIPC): false
```

Start with `validationFailureAction: Audit` and let it run for a week. Read the [PolicyReports](https://kyverno.io/docs/policy-reports/) to see what would have been blocked. Fix the patterns. Once the report is clean for a couple of days, flip to `Enforce`.

### Exemption Workflow (Because Real Life Has Edge Cases)

Some workloads legitimately need things the policy blocks (a debug sidecar that must run as root, a one-off batch job that needs `hostPath` access). Make exemptions auditable, not unwritten:

```yaml
apiVersion: kyverno.io/v2
kind: PolicyException
metadata:
  name: debug-sidecar-host-network
  namespace: team-a-staging
  annotations:
    requested-by: alice@example.com
    approved-by: security-on-call
    reason: "Quarterly perf debug; tracked in JIRA SEC-1284"
    expires: "2026-11-30"           # human-readable; pair with a CronJob to delete after
spec:
  exceptions:
    - policyName: ns-baseline
      ruleNames: [disallow-host-namespaces]
  match:
    any:
      - resources:
          kinds: [Pod]
          names: ["debug-net-*"]
          namespaces: ["team-a-staging"]
```

Treat each exemption like a short-lived security debt: name the requester, approver, reason, and expiry. A CronJob that scans for expired exemptions and pings the security channel keeps the list honest.

Document each policy in language the team understands: "This stops one broken pod killing the node" or "This stops accidental exposure of host filesystem". Policy without explanation just feels like the platform team being mean.

---

## Step 7: Observability and Alerts for Security‑Relevant Events

Hook into:

- Audit logs:
  - Watch for `RoleBinding`, `ClusterRoleBinding`, and `ServiceAccount` changes.
- Pod and deployment events:
  - Unexpected restarts.
  - ImagePullBackOff for prod services.

Surface:

- Dashboards showing:
  - Which policies are failing (pre‑merge in CI and at admission).
  - Which namespaces are “clean” vs constantly violating guardrails.

Tie alerts to:

- Slack/Teams channels the team actually reads.
- Runbooks that say “if you see this, do that.”

---

## Final Thought

Hardening a namespace isn’t about throwing every control at it. It’s about:

- Giving teams freedom where it’s safe.
- Putting walls where one bad manifest turns into an outage or incident.
- Making security visible and fixable *before* merge and deploy.

Do it once, properly, for one namespace. Then treat that as your gold standard and copy the pattern across the cluster.

<img src="img/authors/geeky.jpg" width="40"/>