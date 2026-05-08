---
title:  "The DevSecOps Toolbelt for 2026"
subtitle: "A practical stack that secures your pipeline without drowning you in tools"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/the-devsecops-toolbelt-for-2026.jpg"
date: 2027-07-04
tags: devsecops security tools cicd sdlc
---

## You Don’t Need Every Tool – You Need the Right Ones

DevSecOps isn’t “install 20 scanners and call it a day.” It’s about picking a small set of tools that cover the main risks across code, dependencies, infrastructure, and runtime, then wiring them into your SDLC so they run by default. OWASP’s DevSecOps guideline and DSOMM both emphasise automated checks at each stage instead of random point tools.

Here’s a 2026‑ready toolbelt that hits the key categories without turning your pipeline into a museum.

---

## Static Analysis (SAST): Catch Bugs in Code

You want fast feedback to developers and customisability.

**Good choices:**

- **Semgrep**
  - Rule‑based SAST, very fast, great for custom rules and CI integration.
  - Strong support for many languages and frameworks; popular with security‑minded teams.

- **SonarQube**
  - Combines code quality with security hotspots.
  - Easy to drop into CI for many languages; widely adopted.

- **Enterprise SAST (Checkmarx, etc.)**
  - Deeper coverage and governance for large, regulated orgs.

**Where it fits:** pull‑requests and nightly scans; must be tuned to reduce noise and aligned with your secure coding standards.

---

## Dependency & Container Scanning (SCA): Don’t Ship Known Vulns

Most real‑world risk comes from dependencies and base images. You need SCA that devs will actually look at.

**Good choices:**

- **Snyk**
  - SCA + container and IaC scanning, with IDE and SCM integration.
  - Strong ecosystem and dev‑friendly remediation advice.

- **Trivy**
  - Open‑source scanner for container images, file systems, and IaC.
  - Very popular in Kubernetes and GitOps pipelines; simple CLI/CI usage.

- **Grype**
  - Lightweight container + SBOM scanner, good for CI and registries.

**Where it fits:** on PRs for manifest changes and container builds, and on registries as a gate before deploying to higher environments.

---

## IaC & Policy‑as‑Code: Secure the Infrastructure Definition

Terraform/CloudFormation/K8s/Helm need their own security checks. OWASP DevSecOps guidance explicitly calls out IaC scanning.

**Good choices:**

- **Checkov**
  - Static analysis for Terraform, CloudFormation, Kubernetes manifests, Helm, and more.
  - Large rule set plus custom policies.

- **Terrascan / KICS**
  - Similar role; strong support across cloud and IaC formats.
  - Integrate in CI and pre‑commit hooks.

**Where it fits:** on every infra PR, plus periodic scans against main branches. Treat failing policies like failing tests.

---

## DAST & API Testing: Test the Running App

Static tools can’t see everything. You still need to hit the app “from the outside” in a controlled way.

**Good choices:**

- **OWASP ZAP**
  - Free, scriptable DAST for web apps and APIs.
  - Can be run in “baseline” mode in CI to catch obvious issues early.

- **Burp Suite**
  - Industry standard for deeper manual web testing.
  - Less about automation, more about focused assessments.

- Modern CI‑friendly DAST (e.g. Beagle Security and others)
  - Designed for continuous API and app tests with pipeline hooks.

**Where it fits:** scheduled scans against staging/pre‑prod and as a nightly CI job against deployed test environments.

---

## Secrets: Store, Rotate, and Stop Leaks

DevSecOps fails fast if secrets are scattered through repos and YAML.

**Good choices:**

- **HashiCorp Vault**
  - Centralised secrets management and dynamic credentials.
  - Integrates with K8s, CI/CD, and cloud IAM.

- **Secret scanners (Gitleaks, trufflehog, etc.)**
  - Scan repos and pipelines for hard‑coded secrets.
  - Critical for catching accidental leaks early.

**Where it fits:** scanning on every push/PR, and Vault (or equivalent) plugged into your apps and pipelines for runtime access.

---

## Cloud & Runtime: CNAPP / CSPM and K8s Detection

Cloud misconfig and runtime issues are a big chunk of modern risk.

**Good choices:**

- **CNAPP / CSPM (e.g. Wiz, Aqua, etc.)**
  - Cloud posture management, workload scanning, and runtime protection.
  - Unified view of misconfig, vulnerabilities, and exposures.

- **Falco**
  - CNCF project for runtime threat detection at the kernel level, especially in Kubernetes.
  - Rules catch suspicious syscalls and container behaviour.

**Where it fits:** always‑on scanning in your cloud accounts and clusters, sending findings into whatever you use as a central security view.

---

## “Platform” Approaches: Fewer Vendors, More Coverage

To avoid tool sprawl, many teams prefer security platforms that bundle multiple capabilities.

**Examples:**

- **GitLab Ultimate**
  - SAST, SCA, dependency scanning, container/IaC scanning, DAST built into the pipeline.
- **GitHub Advanced Security**
  - CodeQL SAST, Dependabot, secret scanning, and some IaC rules.
- **App‑sec platforms (Aikido, Cycode, etc.)**
  - Aggregate SAST, SCA, IaC, secrets, and supply‑chain security into a single UI.

These line up well with OWASP’s DevSecOps guideline, which focuses on coverage and automation rather than specific brands.

---

## A Minimal but Serious DevSecOps Stack

If you want a concrete starting point:

- **Code & PRs** — Semgrep (SAST), Snyk or Trivy/Grype (SCA), Checkov (IaC), gitleaks (secret scanner).
- **Build & deploy** — Container scanning (Trivy/Snyk), SBOM generation (Syft → CycloneDX), image signing (Cosign).
- **Runtime & cloud** — Falco for K8s runtime, CNAPP/CSPM for cloud posture.
- **Periodic** — ZAP / DAST against staging nightly; manual Burp / pen-test where warranted.

---

## Wiring the Toolbelt: A Working CI Pipeline

The point of "minimal" is to actually run on every change. Here's a GitHub Actions workflow that runs the PR-time gates in parallel and the nightly DAST on a schedule.

```yaml
# .github/workflows/devsecops.yml
name: devsecops
on:
  pull_request:
  push: { branches: [main] }
  schedule: [{ cron: "0 2 * * *" }]   # nightly 02:00 UTC

permissions:
  contents: read
  security-events: write

jobs:
  sast:
    runs-on: ubuntu-latest
    if: github.event_name != 'schedule'
    steps:
      - uses: actions/checkout@v4
      - name: Semgrep
        uses: returntocorp/semgrep-action@v1
        with:
          config: |
            p/r2c-ci
            p/security-audit
            p/owasp-top-ten
            p/secrets

  sca:
    runs-on: ubuntu-latest
    if: github.event_name != 'schedule'
    steps:
      - uses: actions/checkout@v4
      - name: Trivy filesystem
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: fs
          severity: HIGH,CRITICAL
          exit-code: 1
          ignore-unfixed: true

  iac:
    runs-on: ubuntu-latest
    if: github.event_name != 'schedule' && hashFiles('**/*.tf', '**/*.yaml') != ''
    steps:
      - uses: actions/checkout@v4
      - name: Checkov
        uses: bridgecrewio/checkov-action@master
        with:
          framework: terraform,kubernetes,dockerfile,helm
          quiet: true

  secrets:
    runs-on: ubuntu-latest
    if: github.event_name != 'schedule'
    steps:
      - uses: actions/checkout@v4
        with: { fetch-depth: 0 }
      - name: gitleaks
        uses: gitleaks/gitleaks-action@v2

  container:
    runs-on: ubuntu-latest
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4
      - name: Build image
        run: docker build -t app:${{ github.sha }} .
      - name: Trivy image scan
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: app:${{ github.sha }}
          severity: HIGH,CRITICAL
          exit-code: 1
      - name: Generate SBOM
        uses: anchore/sbom-action@v0
        with:
          image: app:${{ github.sha }}
          format: cyclonedx-json
      - name: Sign image
        run: cosign sign --yes app:${{ github.sha }}
        env:
          COSIGN_EXPERIMENTAL: "1"

  dast:
    runs-on: ubuntu-latest
    if: github.event_name == 'schedule'
    steps:
      - name: ZAP baseline scan
        uses: zaproxy/action-baseline@v0.10.0
        with:
          target: https://staging.example.com
          fail_action: true
```

The shape that matters:

- **PR gates run in parallel** — fail-fast feedback to the developer.
- **Container scan + SBOM + signing on `main` push** — supply-chain provenance for production images.
- **DAST on a schedule** — too slow for PRs, just right for nightly.
- **`exit-code: 1`** on the high-severity gates — CI red, merge blocked. Anything below `HIGH` is a soft signal you triage offline.

For the GitLab Ultimate equivalent, the same gates exist as built-in templates (`SAST.gitlab-ci.yml`, `Container-Scanning.gitlab-ci.yml`, `DAST.gitlab-ci.yml`) — include them and tune.

The "best tools" are the ones your team can actually run on every change and respond to. Start small, wire them properly into CI/CD, then iterate based on signal-to-noise, not feature lists. For the AI-shaped variation of this pipeline, see [AI-Assisted Development Without Losing Your Soul or Your Security](https://geekyblinder.co.uk/#/2027/05/09/AI-Assisted-Development-Without-Losing-Your-Soul-or-Your-Sec).

<img src="img/authors/geeky.jpg" width="40"/>