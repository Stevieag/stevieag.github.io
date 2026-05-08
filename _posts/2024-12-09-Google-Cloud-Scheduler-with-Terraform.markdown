---
title: "Google Cloud Scheduler in Terraform"
subtitle: "Cron jobs as code, with a service account that can't do too much"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/google-cloud-scheduler-in-terraform.jpg"
date: 2024-12-09
tags: gcp scheduler terraform
---

Cloud Scheduler is GCP’s managed cron. It’s genuinely good — pay nothing, fire HTTPS or Pub/Sub on a schedule, get retries and a viewable history without standing up a VM or a Cloud Run service for the privilege. It also pairs nicely with Terraform: cron schedules belong in version control alongside the things they trigger.

This post is the working example I keep reaching for: two scheduler jobs (Pub/Sub and HTTPS-with-OIDC), a least-privilege service account that can only do one thing, retry config that won't melt your downstream, and a monitoring alert that pages you when a job fails three times in a row.

---

## What You'll Need

- A GCP project with billing enabled.
- `gcloud` and `terraform` installed locally.
- An identity with `roles/owner` or equivalent for the bootstrap (you'll narrow this down for the *running* automation in a moment).

Enable the APIs:

```bash
gcloud services enable \
  cloudscheduler.googleapis.com \
  pubsub.googleapis.com \
  run.googleapis.com \
  monitoring.googleapis.com \
  iam.googleapis.com
```

---

## A Minimal Working Module

This is the whole thing. Save as `main.tf` and `terraform apply` from a fresh directory.

```hcl
terraform {
  required_version = ">= 1.5"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

variable "project_id" {
  type = string
}

variable "region" {
  type    = string
  default = "europe-west2"
}
```

A single Terraform file that does the thing — Pub/Sub example first, then HTTPS, then SA + alert.

---

## Example 1: Pub/Sub Target

The simplest case. Scheduler publishes a message; whatever's subscribed picks it up.

```hcl
resource "google_pubsub_topic" "weekly_rollup" {
  name = "weekly-rollup"
}

resource "google_cloud_scheduler_job" "weekly_rollup" {
  name        = "weekly-rollup"
  description = "Kicks off the Friday rollup at 16:30"
  schedule    = "30 16 * * 5"  # Fri 16:30 — using cron, not the goofy 0=Sunday variant
  time_zone   = "Europe/London"
  region      = var.region

  pubsub_target {
    topic_name = google_pubsub_topic.weekly_rollup.id
    data       = base64encode(jsonencode({ trigger = "weekly", source = "scheduler" }))
  }

  retry_config {
    retry_count          = 3
    min_backoff_duration = "10s"
    max_backoff_duration = "300s"
    max_doublings        = 3
  }
}
```

Two things worth noticing:

- **`time_zone` is mandatory if you care when it actually fires.** Without it, the job runs in UTC and you'll be paged at 17:30 BST by mistake. Ask me how I know.
- **The `data` field must be base64.** The `jsonencode` keeps the payload as a real JSON object on the wire so subscribers can parse it cleanly.

---

## Example 2: HTTPS Target with OIDC Auth

When the target is a Cloud Run service or any HTTPS endpoint that authenticates Google identities, you want OIDC — not "URL with a secret in the query string". This is the bit most blog posts skip.

```hcl
resource "google_service_account" "scheduler_invoker" {
  account_id   = "scheduler-invoker"
  display_name = "Cloud Scheduler invoker SA"
}

resource "google_cloud_scheduler_job" "nightly_report" {
  name        = "nightly-report"
  description = "Hits the report-generator Cloud Run service nightly"
  schedule    = "0 2 * * *"
  time_zone   = "Europe/London"
  region      = var.region

  http_target {
    http_method = "POST"
    uri         = "https://report-generator-xyz-nw.a.run.app/generate"

    headers = {
      "Content-Type" = "application/json"
    }

    body = base64encode(jsonencode({ report = "nightly" }))

    oidc_token {
      service_account_email = google_service_account.scheduler_invoker.email
      audience              = "https://report-generator-xyz-nw.a.run.app"
    }
  }

  retry_config {
    retry_count          = 5
    min_backoff_duration = "30s"
    max_backoff_duration = "600s"
    max_doublings        = 4
  }
}
```

Then grant the SA permission to invoke that one service:

```hcl
resource "google_cloud_run_service_iam_member" "scheduler_invokes_report" {
  location = var.region
  service  = "report-generator"
  role     = "roles/run.invoker"
  member   = "google_service_account.scheduler_invoker.member"
}
```

This is least-privilege done properly: the SA can invoke *exactly one* Cloud Run service, nothing else. Don't grant `roles/run.invoker` at the project level "to keep it simple" — that lets the same SA call any Cloud Run service in the project, including ones you haven't built yet.

For Pub/Sub-targeted jobs the equivalent role is `roles/pubsub.publisher`, scoped to the topic.

---

## Retry Config: The One Block Everyone Skips

Defaults aren't sane for most workloads. Cloud Scheduler will retry on any non-2xx response, including transient 5xx and timeouts, with exponential backoff:

| Field | What it does | Sensible default |
|-------|--------------|------------------|
| `retry_count` | Max attempts per fire | 3–5 |
| `min_backoff_duration` | First-retry delay | 10s for fast tasks, 30s+ for heavy |
| `max_backoff_duration` | Cap on delay between retries | 300s–600s |
| `max_doublings` | How many times the backoff doubles before flat-lining | 3–4 |
| `max_retry_duration` | Total time across all retries | leave empty unless you need it |

Set `retry_count = 0` if your job is non-idempotent and you'd rather have one failure than two half-successes.

---

## A Monitoring Alert That's Actually Useful

Cloud Scheduler emits a `logging.googleapis.com/log_entry_count` metric you can alert on. The trick is to filter to *failed* runs only — otherwise you'll page yourself for every successful job at 02:00.

```hcl
resource "google_monitoring_notification_channel" "email_oncall" {
  display_name = "On-call email"
  type         = "email"
  labels = {
    email_address = "oncall@example.com"
  }
}

resource "google_monitoring_alert_policy" "scheduler_failures" {
  display_name = "Cloud Scheduler job failed 3+ times in 30 min"
  combiner     = "OR"

  conditions {
    display_name = "Failure rate"
    condition_threshold {
      filter = <<-EOT
        metric.type = "logging.googleapis.com/log_entry_count"
        AND resource.type = "cloud_scheduler_job"
        AND metric.labels.severity = "ERROR"
      EOT

      duration        = "1800s"
      comparison      = "COMPARISON_GT"
      threshold_value = 3

      aggregations {
        alignment_period   = "300s"
        per_series_aligner = "ALIGN_SUM"
      }
    }
  }

  notification_channels = [google_monitoring_notification_channel.email_oncall.id]

  documentation {
    content = "Three or more Scheduler error log entries in the last 30 minutes. Check `gcloud scheduler jobs describe <name>` and look at recent runs."
  }
}
```

Tune `threshold_value` and `duration` to taste. The point is to alert on *patterns* of failure, not single transient blips that the retry config already handles.

---

## Bootstrap Workflow

```bash
terraform init
terraform plan -out=tfplan
terraform apply tfplan
```

To trigger a job manually for testing without waiting for the cron to fire:

```bash
gcloud scheduler jobs run weekly-rollup \
  --location=europe-west2

gcloud scheduler jobs describe weekly-rollup \
  --location=europe-west2 \
  --format="value(state, lastAttemptTime, status)"
```

To pull the most recent Pub/Sub messages off a subscription (for debugging):

```bash
gcloud pubsub subscriptions pull weekly-rollup-sub \
  --limit=5 --auto-ack
```

---

## Console Equivalent (When You Just Want to Eyeball It)

If you're checking what Terraform built, the console view at *Cloud Scheduler → Jobs* shows:

- Last run state and time.
- Next scheduled run.
- A "Force run" button (handy for manual smoke-tests).
- Per-job logs link (taking you to Cloud Logging filtered to that job).

Don't create jobs in the console for production — they drift, and you'll waste an afternoon trying to work out why two environments behave differently. Console is read-only in your head; Terraform owns the state.

---

## Final Thought

Cloud Scheduler is one of the cheapest, dullest, most reliable services GCP offers. Wire it up properly once — least-privilege SA, OIDC auth, retry config, a monitoring alert that fires on patterns rather than every blip — and you can forget it exists. That's the goal of every piece of infrastructure: useful enough to depend on, boring enough to ignore.

<img src="img/authors/geeky.jpg" width="40"/>
