---
title:  "Building a DevSecOps Homelab That Actually Teaches You Something"
subtitle: "From empty Proxmox box to a mini pipeline with real security checks"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/building-a-devsecops-homelab-that-actually-teaches-you.jpg"
date: 2026-07-05
tags: homelab devsecops CI/CD docker kubernetes security
---

## Building a DevSecOps Homelab That Actually Teaches You Something

A lot of "homelabs" are just increasingly expensive ways to host Plex. Nothing wrong with that, but if you want to get good at DevSecOps, you need something closer to reality: code, pipelines, images, scanners, and breakable apps.

Let’s build a small but serious lab you can iterate on, demo, and talk about in interviews. Pairs with [Building a Home Lab to Learn Hacking Without Going to Jail](https://geekyblinder.co.uk/#/2026/07/19/Building-a-Home-Lab-to-Learn-Hacking-Without-Going-to-Jail) (the offensive sibling) and [The DevSecOps Toolbelt for 2026](https://geekyblinder.co.uk/#/2027/07/04/The-DevSecOps-Toolbelt-for-2026) (the toolchain reference).

---

## Step 1: Core Platform – Proxmox or Plain Linux

You want:

- One box (or a couple) running:
  - Proxmox VE, or
  - A solid Linux host with Docker/Podman and maybe K3s.

Proxmox route:

- Proxmox host on bare metal.
- VMs or LXCs for:
  - `gitlab` or `gitea + runner`.
  - `registry` (private container registry).
  - `k3s` or K8s cluster for deployments.

Plain Linux route:

- One host running:
  - GitLab/Gitea.
  - Docker.
  - K3s cluster (even single‑node).

Think of this as your tiny “company infra.”

---

## Step 2: The App – Something Real Enough to Break

You don’t need microservices chaos. One modest web app is enough.

Pick:

- A simple API + frontend:
  - E.g. Node/Express + Vue/React.
- Or a known vulnerable app (DVWA/OWASP Juice Shop) if you want red‑team focus.

Put it in Git:

- `main` branch → production.
- `develop` branch → staging.

Add a Dockerfile and Kubernetes or Docker Compose manifests.

---

## Step 3: CI/CD With Security in the Loop

Set up a pipeline that runs the standard gates on every change. The shape:

1. Unit tests.
2. SAST (Semgrep, with `p/r2c-ci` and language-specific rule packs).
3. Container build.
4. Container vulnerability scan (Trivy or Grype).
5. SBOM generation (Syft → CycloneDX format).
6. Push image to your private registry.
7. Deploy to staging (K8s manifest or Helm, ArgoCD if you want to learn GitOps).
8. Nightly DAST against staging (OWASP ZAP baseline).

A working `.gitlab-ci.yml` skeleton:

```yaml
stages: [test, build, scan, deploy, dast]

unit:
  stage: test
  image: node:20-alpine
  script: ["npm ci", "npm test"]

sast:
  stage: test
  image: returntocorp/semgrep
  script:
    - semgrep --config p/r2c-ci --config p/security-audit --error

build:
  stage: build
  image: docker:24
  services: [docker:24-dind]
  script:
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA

container-scan:
  stage: scan
  image: aquasec/trivy:latest
  script:
    - trivy image --exit-code 1 --severity HIGH,CRITICAL --ignore-unfixed \
        $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA

sbom:
  stage: scan
  image: anchore/syft:latest
  script:
    - syft $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA -o cyclonedx-json > sbom.json
  artifacts: { paths: [sbom.json], expire_in: 30 days }

deploy-staging:
  stage: deploy
  image: bitnami/kubectl:latest
  script:
    - kubectl set image -n staging deploy/app app=$CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
  only: [develop]

dast:
  stage: dast
  image: ghcr.io/zaproxy/zaproxy:stable
  script:
    - zap-baseline.py -t http://staging.lab.local -r zap.html
  only: { variables: [$CI_PIPELINE_SOURCE == "schedule"] }
```

The goal isn't perfection, it's *flow*: a commit goes in, security tests run automatically, you get feedback in minutes. For the deeper toolbox and the GitHub Actions equivalent, see [The DevSecOps Toolbelt for 2026](https://geekyblinder.co.uk/#/2027/07/04/The-DevSecOps-Toolbelt-for-2026).

Now you've got something you can walk through end-to-end with a hiring manager.

---

## Step 4: Observability and Security Monitoring

Add:

- Prometheus + Grafana or Netdata for metrics.
- Logs aggregated into something like Loki or at least a central syslog.
- A basic SIEM‑ish view (even if it’s a couple of tuned dashboards).

Security‑wise:

- Wazuh/Security Onion if you’re keen.
- At minimum, alert on:
  - Unusual auth.
  - New containers.
  - Pod restarts and crash loops.

You’re essentially recreating a trimmed‑down SOC view over your own infra.

---

## Step 5: Break It On Purpose

Once it all works, your job is to dismantle it:

- Introduce a vulnerable dependency and see if your scanners catch it.
- Push a bad K8s manifest (no resource limits, or running as root) and add a policy tool (OPA/Gatekeeper or Kyverno) to block it.
- Simulate an incident:
  - Add a cryptominer container or unexpected outbound calls.
  - Detect it via metrics/logs.
  - Practise response (containment, eradication, recovery).

Document these drills as mini runbooks. That’s prime “tell me about a time you handled an incident” material.

---

## Step 6: Tell the Story

Treat the lab as:

- A case study on your CV.
- Demo material for interviews.
- Content for blogs, talks, or streams.

Cover:

- Architecture diagram.
- Tooling choices and why you made them.
- Trade‑offs and things you’d do differently at scale.

The tech is good; the narrative is what gets you hired.

---

## Final Thought

A DevSecOps homelab doesn’t need 40 nodes and RGB lighting. It needs just enough moving parts to mimic reality: code, pipeline, registry, runtime, monitoring, and some attacks.

Build something small but real, then keep iterating. You’ll learn more from that than from another 10 YouTube videos about “the DevSecOps lifecycle.”

<img src="img/authors/geeky.jpg" width="40"/>