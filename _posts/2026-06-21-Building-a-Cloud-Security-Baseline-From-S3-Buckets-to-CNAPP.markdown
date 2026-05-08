---
title:  "Building a Cloud Security Baseline: From S3 Buckets to CNAPP"
subtitle: "A deep walkthrough for engineers who want to do this properly"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/building-a-cloud-security-baseline-from-s3-buckets-to-c.jpg"
date: 2026-06-21
tags: cloud security AWS GCP Azure CSPM CNAPP devsecops
---

## Building a Cloud Security Baseline: From S3 Buckets to CNAPP

Cloud security used to mean "don’t leave S3 open to the world". These days you've got multi-cloud, containers, serverless, AI services, and forty different dashboards all trying to warn you at once.

This post is the working baseline — six steps from "we have some stuff in the cloud" to "we have a posture that doesn’t crumble on contact with reality", with real Terraform, real CLI commands, and real detection rules. Examples are AWS-flavoured because that's where most teams start; the patterns translate directly to GCP and Azure. Pairs with [Zero Trust Architecture: A Deep Practical Walkthrough](https://geekyblinder.co.uk/#/2026/05/10/Zero-Trust-Architecture-A-Deep-Practical-Walkthrough) and [The DevSecOps Toolbelt for 2026](https://geekyblinder.co.uk/#/2027/07/04/The-DevSecOps-Toolbelt-for-2026).

---

## Step 1: Know What You Actually Have

You can’t secure what you don’t know exists.

Discover:

- Enumerate accounts/subscriptions/projects across AWS/GCP/Azure. AWS Organizations, Azure Management Groups, GCP folder hierarchy.
- Inventory: storage, compute, databases, IAM principals, network exposure.
- Identify shadow accounts spun up over the years and never claimed.

Tools that pay off:

```bash
# AWS — list every account in your Organization, plus a per-account inventory
aws organizations list-accounts \
  --query 'Accounts[?Status==`ACTIVE`].[Id,Name,Email]' --output table

# Per-account, regional resource enumeration via Resource Explorer (must be enabled)
aws resource-explorer-2 search \
  --query-string "*" --max-results 1000 \
  --view-arn arn:aws:resource-explorer-2:eu-west-2:111111111111:view/all/...

# Or use Steampipe for SQL-like queries across all your AWS accounts
steampipe query "select account_id, name, region from aws_s3_bucket where bucket_policy_is_public"
```

[Steampipe](https://steampipe.io/) and [Cartography](https://github.com/cartography-cncf/cartography) are the OSS tools worth knowing — both turn cloud APIs into queryable graphs. Save the inventory output as a starting point, even if it's a CSV and a wiki page.

---

## Step 2: Identity First — IAM and Access

Identity is the new perimeter.

### Baseline

- No long-lived access keys for humans. SSO + short-lived role assumption.
- Per-app roles/service accounts, not shared "god roles".
- Least privilege — start with managed policies, chip away based on access logs.
- MFA mandatory for humans; phishing-resistant where possible.
- Break-glass admin accounts with strong controls and out-of-band recovery.

### Concrete: Least-Privilege Service Account in Terraform

```hcl
# instead of giving the app role AmazonS3FullAccess, scope to one bucket
resource "aws_iam_role" "orders_app" {
  name = "orders-app"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = { Service = "ec2.amazonaws.com" }
      Action = "sts:AssumeRole"
      Condition = {
        StringEquals = {
          "aws:SourceAccount" = data.aws_caller_identity.current.account_id
        }
      }
    }]
  })
}

resource "aws_iam_policy" "orders_s3_scoped" {
  name = "orders-s3-scoped"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"]
        Resource = ["${aws_s3_bucket.orders.arn}/uploads/*"]
        Condition = {
          StringEquals = { "s3:RequestObjectTagKeys" = ["env"] }
        }
      },
      {
        Effect = "Allow"
        Action = ["s3:ListBucket"]
        Resource = aws_s3_bucket.orders.arn
        Condition = {
          StringLike = { "s3:prefix" = ["uploads/*"] }
        }
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "orders_s3" {
  role       = aws_iam_role.orders_app.name
  policy_arn = aws_iam_policy.orders_s3_scoped.arn
}
```

The Condition blocks are the difference between "least-privilege written on a slide" and "least-privilege the role actually has".

For human access, AWS IAM Identity Center (formerly SSO) with permission sets and PermissionBoundaries is the modern path; AWS IAM users for humans are deprecated in spirit if not in policy.

### Find Unused Privilege

```bash
# IAM Access Analyzer's unused-access feature surfaces unused permissions
aws accessanalyzer list-findings-v2 \
  --analyzer-arn arn:aws:access-analyzer:eu-west-2:111111111111:analyzer/unused-access \
  --filter '{"findingType":{"eq":["UnusedPermission","UnusedIAMRole"]}}' \
  --max-results 100
```

Run quarterly; the findings are direct candidates for the chipping-away pass.

---

## Step 3: Configuration and Posture Management

Something needs to watch your cloud configs for footguns.

### Cheap Start: Native Tools

Switch them on, even if you don't have a CSPM yet:

```bash
# AWS — enable Security Hub and the foundational standards
aws securityhub enable-security-hub --enable-default-standards

# Enable GuardDuty in every region
for region in $(aws ec2 describe-regions --query 'Regions[].RegionName' --output text); do
  aws guardduty create-detector --enable --region $region
done

# Enable Config recorder in every region (deliver to a central log account)
aws configservice put-configuration-recorder \
  --configuration-recorder name=default,roleARN=arn:aws:iam::111111111111:role/AWSConfigRole

# Enable Access Analyzer at organization level
aws accessanalyzer create-analyzer --analyzer-name org --type ORGANIZATION
```

GCP equivalents: Security Command Center (Premium for the good detectors), GCP CSPM. Azure: Defender for Cloud, Microsoft Sentinel for SIEM-side.

### S3 Bucket Done Properly (Terraform)

```hcl
resource "aws_s3_bucket" "orders" {
  bucket = "orders-${var.env}-${random_id.suffix.hex}"
}

resource "aws_s3_bucket_public_access_block" "orders" {
  bucket = aws_s3_bucket.orders.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_server_side_encryption_configuration" "orders" {
  bucket = aws_s3_bucket.orders.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm     = "aws:kms"
      kms_master_key_id = aws_kms_key.orders.arn
    }
    bucket_key_enabled = true
  }
}

resource "aws_s3_bucket_versioning" "orders" {
  bucket = aws_s3_bucket.orders.id
  versioning_configuration { status = "Enabled" }
}

resource "aws_s3_bucket_logging" "orders" {
  bucket        = aws_s3_bucket.orders.id
  target_bucket = aws_s3_bucket.audit_logs.id
  target_prefix = "s3/orders/"
}

resource "aws_s3_bucket_lifecycle_configuration" "orders" {
  bucket = aws_s3_bucket.orders.id
  rule {
    id     = "expire-noncurrent"
    status = "Enabled"
    noncurrent_version_expiration { noncurrent_days = 90 }
  }
}
```

Five resources, every protection on. Run [Checkov](https://www.checkov.io/) against this in CI to catch any future regressions:

```bash
checkov -d ./terraform --framework terraform --quiet
```

### Scaling Up: CSPM/CNAPP

When you outgrow the native tools (usually around the 5–10 cloud account mark):

- [Wiz](https://www.wiz.io/) — graph-based, strong attack-path visualisation.
- [Aqua](https://www.aquasec.com/) / [Prisma Cloud](https://www.paloaltonetworks.com/prisma/cloud) — broader CNAPP, covers runtime + cloud + supply chain.
- [Orca Security](https://orca.security/) — agentless scanning, fast deploy.
- [Datadog Cloud Security Management](https://www.datadoghq.com/product/cloud-security-management/) — natural fit if you already run Datadog.

The choice is mostly about how the findings show up in your existing workflow. Triage rate matters more than feature count — a CSPM nobody opens is just an expensive log.

---

## Step 4: Workloads — Containers, Serverless, and Friends

Once infra posture is semi-sane, harden the workloads.

### Containers

- Minimal base images (`distroless`, `alpine`, `chainguard`).
- Image scanning in CI ([Trivy](https://github.com/aquasecurity/trivy), [Snyk](https://snyk.io/), [Grype](https://github.com/anchore/grype)).
- Sign images with [Cosign](https://github.com/sigstore/cosign); verify on deploy.
- Runtime: no privilege escalation, read-only root filesystem, drop all caps, non-root user. (See [Helm, Docker, and Kubernetes: A Tiny Training App](https://geekyblinder.co.uk/#/2027/08/01/Helm-Docker-K8s) for the worked example.)

### Serverless

- Tight IAM roles per function, never `*:*`.
- Timeouts, retries, dead-letter queues to avoid runaway invocations and cost surprises.
- Function URL / API Gateway with WAF in front, rate-limited.
- Secrets via Secrets Manager / Parameter Store, fetched at cold start, never in env.

### Traditional VMs

- Patching, hardening (CIS benchmark), endpoint protection.
- Same as on-prem, just with cloud-native tooling (SSM Patch Manager, Azure Update Manager, OS Config in GCP).

### CI/CD Tie-In

```yaml
# .github/workflows/cloud-security.yml — just the cloud bits
- uses: bridgecrewio/checkov-action@master
  with:
    framework: terraform
    soft_fail: false           # block PR on failures

- uses: aquasecurity/trivy-action@master
  with:
    scan-type: fs
    scanners: vuln,misconfig,secret
    severity: CRITICAL,HIGH
    exit-code: 1

- name: Generate SBOM
  uses: anchore/sbom-action@v0
  with:
    image: app:${{ github.sha }}
    format: cyclonedx-json
```

Keep SBOMs alongside artefacts. When the next big CVE drops you'll be able to answer "are we affected?" in minutes.

---

## Step 5: Logging, Monitoring, and Detection

Security without visibility is just vibes.

### What to Log

- **AWS** — CloudTrail (org trail to a central log archive account), VPC flow logs, ALB/NLB logs, S3 access logs, GuardDuty findings, Config history.
- **GCP** — Cloud Audit Logs (Admin Activity, Data Access, Policy), VPC Flow Logs, Security Command Center findings.
- **Azure** — Activity Logs, NSG flow logs, Microsoft Defender for Cloud alerts.

Centralise. A dedicated log-archive account/project with immutable retention (S3 Object Lock or equivalent) is non-negotiable for incident response.

### High-Value Detections to Build First

These earn their keep on day one:

- New IAM user, new long-lived access key, new admin role binding.
- S3 bucket policy or public access block changed.
- Security group exposing 22/3389 to 0.0.0.0/0.
- Root account login.
- Disabling of CloudTrail, GuardDuty, Config, or KMS key deletion.

A working EventBridge → SNS pattern for the "S3 went public" detection:

```hcl
resource "aws_cloudwatch_event_rule" "s3_public" {
  name        = "detect-s3-public-bucket"
  description = "Catch S3 bucket policies opening up to public"
  event_pattern = jsonencode({
    source      = ["aws.s3"]
    detail-type = ["AWS API Call via CloudTrail"]
    detail = {
      eventSource = ["s3.amazonaws.com"]
      eventName   = ["PutBucketPolicy", "PutBucketAcl", "DeletePublicAccessBlock"]
    }
  })
}

resource "aws_cloudwatch_event_target" "s3_public_sns" {
  rule      = aws_cloudwatch_event_rule.s3_public.name
  target_id = "sns-security"
  arn       = aws_sns_topic.security_alerts.arn
}
```

Pair every detection with a runbook: "When alert X fires, we do Y, and the on-call has Z minutes to acknowledge."

---

## Step 6: Governance Without Process Hell

You don’t need a 400-page policy PDF. You do need:

- **Clear rules** on how new cloud accounts/projects are created. New accounts come from an account vending pipeline (AWS Control Tower, Azure landing zones, GCP folder structure with Terraform), pre-baked with the baseline above.
- **IaC-only changes** to anything that matters. Click-ops in production cloud is the #1 source of drift and audit findings.
- **Lightweight review** for high-risk changes (internet-facing, sensitive data, new regions). A required reviewer label on Terraform PRs touching `production/*` is enough.
- **Annual security review** per protect-surface, plus event-triggered (M&A, big architectural shifts, post-incident).

If governance makes it impossible to ship, people tunnel under it. Aim for "just enough friction to make people think".

---

## Final Thought

Cloud security isn't a one-off hardening sprint. It's a continuous feedback loop between what you have, how it's configured, how it's being used, and how people are trying to break it.

The shape that works in 2026: identity-first, IaC for everything that matters, posture management running constantly, detections wired to runbooks, and an SBOM trail for when the inevitable CVE drops. Start small, automate what hurts, and keep security as close to the engineers and pipelines as possible.

For the rest of the picture, see [Zero Trust Architecture](https://geekyblinder.co.uk/#/2026/05/10/Zero-Trust-Architecture-A-Deep-Practical-Walkthrough), [The DevSecOps Toolbelt for 2026](https://geekyblinder.co.uk/#/2027/07/04/The-DevSecOps-Toolbelt-for-2026), and [Modern Cloud Hacking: Misconfigurations That Really Get You Popped](https://geekyblinder.co.uk/#/2027/08/15/Modern-Cloud-Hacking-Misconfigurations-That-Really-Get-You-P).

<img src="img/authors/geeky.jpg" width="40"/>
