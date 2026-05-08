---
title:  "AIOps in Real Life: A Practical Guide to Cutting DevOps Toil (Not Just Adding More Dashboards)"
subtitle: "How to go from alert spam and 3am pages to sane, AI‑assisted operations in 6 steps"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/aiops-in-real-life-a-practical-guide-to-cutting-devops.jpg"
date: 2027-05-23
tags: AIOps devops sre toil automation reliability
---

## Why AIOps (Really) Exists: Kill Toil, Not Jobs

AIOps is "AI for IT operations": ML and automation applied to logs, metrics, events, and traces to make sense of the storm and act on it. Done right, it cuts noise, speeds up detection and diagnosis, and automates the repetitive bits of incident work.

Done badly — which is most of the time — it adds another dashboard, generates a slightly different kind of alert spam, and gives the platform team something else to maintain. This post is the working playbook for getting it right: real correlation rules, real automation snippets, and honest numbers about what to expect rather than vendor-deck claims. For vendor picks, see [Top AIOps Platforms for DevOps Teams in 2026](https://geekyblinder.co.uk/#/2027/06/06/Top-AIOps-Platforms-for-DevOps-Teams-in-2026).

---

## Step 1: Define Toil and Baseline It

Before you buy or build anything, get a clear picture of the current pain. Otherwise you’ll have nothing to measure success against and the AIOps vendor will pick the metrics for you.

Measure for 4–8 weeks. The numbers worth tracking:

- **Alert volume per shift.** Total raw alerts hitting on-call.
- **Actionability rate.** Of those alerts, what percentage led to a real action (config change, restart, escalation, post-mortem)? Anything below 30% is alert spam.
- **MTTD and MTTR.** Per-class median, not mean — outliers skew this badly. Median time from first symptom to first alert; median from alert to resolution.
- **Toil markers.** How many times in a week the team did the same fix (kafka consumer restart, cache flush, RDS scale-up, killing a stuck deployment). Track the top three.
- **Self-reported burnout.** Anonymous one-question survey: "How sustainable does on-call feel right now?" 1–5. Run it weekly. The platform won't tell you this; the people will.

Stick the baseline in a wiki page with a date. AIOps success is measured against this, not against the demo.

---

## Step 2: Get Observability in Order (AIOps Needs Decent Data)

Every serious AIOps post says the same thing because it’s the same truth: if your telemetry is poor, fix that first. AIOps doesn’t magic signal out of bad data — it just makes confusing dashboards faster.

Minimum viable telemetry:

- **Metrics.** RED method (Rate, Errors, Duration) per service. USE method (Utilisation, Saturation, Errors) per resource. SLO burn-rate alerts in addition to threshold alerts.
- **Logs.** Structured JSON or logfmt, not free-form. Correlation IDs that survive across services (W3C `traceparent` is the modern standard).
- **Traces.** OpenTelemetry SDKs, `traceparent` headers propagated end-to-end. Sample at 100% in dev/staging, 1–10% in prod with tail-based sampling.
- **Events.** Deploys, config changes, feature flag toggles, scaling events, feature-flag flips — all going into the same event stream as alerts so they can correlate.

Two underrated patterns that pay off later:

- **One service-name field, used everywhere.** If your traces call it `service`, your logs call it `app`, and your metrics call it `application`, no AIOps tool will correlate them properly. Standardise on `service.name` (the OpenTelemetry convention) and tag absolutely everything with it.
- **Send deploys to your monitoring system.** Datadog, Dynatrace, Grafana, and most others have a deploy-marker API. A two-line CI hook gets you "service X deployed at 14:23" overlaid on every chart. Eighty percent of incidents correlate with a recent deploy; surfacing this for free saves hours.

If you don’t have those, "AI magic" is priority *one*, not zero.

---

## Step 3: Pick Three High‑Value Use Cases (Not Twenty)

The rollouts that fail try to turn on every feature simultaneously. The ones that succeed pick three things that hit current pain hardest, prove value on those, then extend.

### Use Case 1: Alert Noise Reduction and Correlation

Goal: fewer, better alerts.

The two cheap wins, doable in any reasonable monitoring stack:

**Prometheus / Alertmanager grouping.** Group related alerts so on-call gets one notification per incident, not fifty:

```yaml
# alertmanager.yml
route:
  group_by: ['service', 'cluster', 'severity']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 4h
  receiver: oncall

inhibit_rules:
  # If a host is down, suppress per-process alerts on the same host
  - source_matchers:
      - alertname = "HostDown"
    target_matchers:
      - alertname =~ "ProcessDown|HighMemory|DiskFull"
    equal: ['instance']
```

**Dynamic thresholds where static ones fail.** Static "CPU > 80%" alerts at 3am during the batch run wake you up forever. Use baseline-aware alerts where supported (Datadog anomaly monitors, Dynatrace Davis baselines, Prometheus + `predict_linear` or holt-winters via `holt_winters`):

```promql
# Alert when error rate is 3+ standard deviations above the trailing 7-day baseline
(
  rate(http_requests_total{status=~"5.."}[5m])
  /
  rate(http_requests_total[5m])
) > on(service) (
  avg_over_time(error_rate_baseline[7d])
  +
  3 * stddev_over_time(error_rate_baseline[7d])
)
```

What good looks like: alerts per shift drops 40–60% in the first month. Actionability rate climbs above 50%. If you’re seeing the marketing 90% noise reduction figure, your inputs were probably broken to begin with — useful, but not what to expect on a healthy estate.

### Use Case 2: Faster Root Cause Analysis

Goal: get to "what's actually broken" quicker.

Three things that compound:

- **Anomaly detection on golden signals.** RED metrics per service, USE per resource. Catches degradations before threshold alarms fire.
- **Correlated symptom rendering.** When an alert fires, show on the same screen: linked logs from that service in the last 15 minutes, recent deploys to that service or its upstreams, recent infra events (node restarts, scaling). Datadog calls this "Watchdog Insights"; Dynatrace does it with Davis problem cards; in Grafana you wire it via Loki + the deploy-marker API.
- **Similar-incident search.** "This looks like the outage from last March." Stash post-mortems in a structured format (one YAML/MD file per incident with `symptoms`, `root_cause`, `runbook_link`) and let any LLM-augmented search hit them.

### Use Case 3: Auto‑Resolution of Repetitive Fixes

Goal: stop being woken up for the same thing.

Pick one specific class of issue your on-call has fixed at least 5 times in the last quarter the same way. Automate that one. Worked example — stuck Kafka consumer:

```yaml
# Sketch of an auto-remediation runbook (PagerDuty/Rundeck/Argo Workflows shape)
trigger:
  alert: KafkaConsumerLagHigh
  service: order-processor
  condition:
    - lag_messages > 10000
    - duration > 10m

preconditions:
  - last_restart_within_24h: false   # don't loop-restart
  - business_hours_or_low_severity: true

steps:
  - name: snapshot_lag
    run: kubectl exec -n prod order-processor -- /usr/bin/kafka-lag-dump.sh
  - name: rolling_restart
    run: kubectl rollout restart deployment/order-processor -n prod
  - name: verify
    wait: 5m
    check: lag_messages < 1000
  - name: notify
    on_failure: page_oncall
    on_success: post_to_slack_channel
```

Track every auto-action. If it fires more than 3 times in 24 hours, page a human and make someone fix the root cause — the automation is a band-aid, and the bandage shouldn’t become permanent.

---

## Step 4: Buy or Build the Capabilities

You can buy a platform (Dynatrace, Datadog AIOps, BigPanda, PagerDuty AIOps) or stitch capabilities from your existing observability stack (Prometheus + Alertmanager + Grafana OnCall + custom correlation). The decision is mostly about size and where your engineers’ time is best spent.

The capabilities you’re actually shopping for:

- Data ingestion that matches *your* tools (logs, metrics, traces, events, alerts from existing systems).
- Alert correlation and dedup, ideally based on topology and time.
- Anomaly detection on timeseries that respects seasonality (your traffic on Sunday is not your traffic on Tuesday).
- Incident enrichment — linking metrics, logs, deploys, and runbooks to alerts automatically.
- Integration with your incident tools (PagerDuty, Opsgenie, Squadcast), chat (Slack, Teams), and automation (SOAR, custom runbooks).

Whatever you choose, integrate with existing workflows. Adding another silo undoes most of the value before you start. For a vendor-by-vendor breakdown, see [Top AIOps Platforms for DevOps Teams in 2026](https://geekyblinder.co.uk/#/2027/06/06/Top-AIOps-Platforms-for-DevOps-Teams-in-2026).

---

## Step 5: Roll Out in Phases (Pilot, Then Scale)

The pattern that fails is "turn it on for everyone, everywhere, on Tuesday". The pattern that works is phased.

**Phase 0 — Pick your target.** One critical-but-well-understood service. One on-call team that volunteers. Baseline their alerts/MTTR/toil for the four weeks before you change anything.

**Phase 1 — Switch on the low-risk capabilities.** Alert correlation, deduplication, anomaly detection on golden signals, context enrichment on alerts. Keep all responses manual. Let the team see what the platform suggests and judge it.

**Phase 2 — Introduce safe auto-actions.** For the well-understood, low-blast-radius patterns from Use Case 3. Guardrails that should be non-negotiable:

- **Preconditions** — only act if specific metrics and states are met.
- **Rate limits** — at most N actions per hour per type per service.
- **Time-of-day gating** — auto-restarts in business hours; page-only at 3am for the first month.
- **Escalation** — if automation fails or fires N times, hand to a human.
- **Audit trail** — every auto-action logged with the alert that triggered it, the preconditions checked, the action taken, the outcome.

Start with "suggest in chat", graduate to "auto-run with notify", graduate to "auto-run silently" only after months of clean data.

**Phase 3 — Measure and decide.** After 1–3 months, compare to baseline. Better numbers and better morale → expand. No improvement → debug, adjust, or roll back without shame.

---

## Step 6: Anti-Patterns to Avoid

The traps I’ve watched real teams fall into:

- **AIOps as a band-aid for bad SLOs.** No amount of alert correlation fixes the fact that you’re alerting on the wrong things. Get your SLOs right first.
- **Vanity noise reduction.** "Alerts dropped 60%!" because you turned off three noisy ones manually. Track *actionable* signal, not just volume.
- **Auto-remediation without root-cause work.** The kafka consumer that gets restarted twice a week for a year is not a success story; it’s a deferred outage. Track repeat incidents and treat them as regressions.
- **Black-box alerts.** "AIOps says there's a problem with `payment-service`" with no chain back to the symptoms. On-call won't trust it; they shouldn't.
- **Replacing on-call humans with the platform.** Adoption fails completely if engineers feel it’s being done *to* them rather than *with* them. Involve them in choosing use cases, tuning rules, and deciding what auto-remediates.

---

## What "Good" Looks Like After 6–12 Months

Healthy implementations show, roughly, against your own baseline:

- **30–50% reduction in raw alert volume**, with actionability climbing toward 60–70%. (Reduction percentages above 70% are usually achievable only on estates that started in alert hell — they’re cleaning up the mess as much as adding intelligence.)
- **MTTD reductions of 20–40%** on the classes of incident you instrumented for.
- **MTTR reductions of 15–30%** — context enrichment and similar-incident search account for most of this; auto-remediation contributes a smaller fraction unless your toil is concentrated.
- **Auto-remediation handling 10–25% of incidents on covered services** — within tight scope, with audit trails, with humans getting paged the moment it stops working.
- **On-call engineers reporting less burnout, fewer pointless wake-ups, and a sense that AI is taking the drudge work, not the interesting work.**

That last one is the only metric that matters in the end. If it isn’t true, the rest of the numbers are decoration.

When AIOps stops being a buzzword in the platform team’s OKRs and starts being "how we run prod now", you’ve done it right.

<img src="img/authors/geeky.jpg" width="40"/>
