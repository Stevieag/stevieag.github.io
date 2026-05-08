---
title:  "Dynatrace vs Splunk ITSI for Large DevOps Teams"
subtitle: "Which AIOps platform actually makes on‑call life easier?"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/dynatrace-vs-splunk-itsi-for-large-devops-teams.jpg"
date: 2027-06-20
tags: AIOps devops sre dynatrace splunk ITSI observability
---

## Short Answer

For most large DevOps/SRE organisations, **Dynatrace** is the better default if your main pain is end-to-end visibility and fast root-cause analysis on a cloud-native stack. **Splunk ITSI** wins when Splunk is already the logging backbone and you want service-health analytics layered on top of an existing data lake.

That short answer hides a real architectural difference, a real query-language difference, a real pricing model difference, and a real philosophical difference about whether you want AI to do RCA for you (Dynatrace) or you want to model your services explicitly and have AI work on top of that (Splunk ITSI). If you’re writing a procurement decision into a spreadsheet, this post is the long answer.

For the wider field, see [Top AIOps Platforms for DevOps Teams in 2026](https://geekyblinder.co.uk/#/2027/06/06/Top-AIOps-Platforms-for-DevOps-Teams-in-2026).

---

## How They Think About the World

### Dynatrace: Push-Based, Auto-Discovered, Opinionated

Dynatrace's whole model is: install OneAgent on every host (or sidecar in K8s), and it auto-instruments infra, runtimes, services, traces, and dependencies without you telling it what to look for. Smartscape builds the topology automatically. Davis AI sits on top, continuously evaluating that topology against telemetry to identify a single root cause when something breaks.

```
[ host / pod ]
   └─ OneAgent  ─── auto-instrumentation, traces, metrics
                    push ────────► Dynatrace SaaS / Managed
                                   ├── Smartscape (topology)
                                   ├── Davis AI (RCA)
                                   └── DQL (query)
```

Strengths: minimal config, fast time-to-value, dynamic discovery, automated RCA across the full stack. The "answers, not data" pitch is real — Davis usually gives you "this deploy broke this service" rather than "here are 47 correlated alerts".

Weaknesses: opinionated. You buy into the worldview, the agent, the data model, and the AI’s judgements. Custom analytics that fall outside the schema get harder.

### Splunk ITSI: Pull-Based Logs, Explicit Service Models, Power Tools

Splunk's whole model is: pull logs (and metrics, traces, events) into Splunk via Universal Forwarders, HEC, or whatever ingestion path. ITSI is an add-on that lets you define **services** (a hierarchy that maps to your business), define **KPIs** for each service (calculated by SPL queries against the data), define **glass tables** (custom dashboards), and run ML on top.

```
[ host / app ]
   └─ Universal Forwarder ─► Splunk indexers ─► Splunk Cloud / Enterprise
       (logs, metrics, events)                  ├── ITSI services + KPIs
                                                ├── Glass tables
                                                ├── ML toolkit
                                                └── SPL (query)
```

Strengths: explicit modelling means the service map is *your* business reality, not the vendor’s inference. SPL is enormously powerful for ad-hoc analytics. Pricing scales with what you ingest, which gives you real choice over what you collect.

Weaknesses: service modelling is real, sustained engineering work — KPIs, thresholds, entity definitions, glass tables. ITSI rewards investment; punishes neglect. Steep learning curve combining SPL, ITSI concepts (services, episodes, neighbours), and the GUI.

Worth knowing: Cisco completed its acquisition of Splunk in March 2024. Expect deeper integration with Cisco's networking and security portfolio over the medium term — Cisco Observability Platform, ThousandEyes, and security tooling are converging into the Splunk story.

---

## Query Languages, Side by Side

The day-to-day reality of either platform is "which query do I write to find what’s broken at 2am?". The two languages target similar problems differently.

**The task:** find services with elevated 5xx rate over the last 15 minutes.

**Dynatrace DQL:**

```sql
fetch logs
| filter dt.entity.service != ""
  and matchesValue(loglevel, "ERROR")
  and toLong(timestamp) > now() - 15m
| summarize errors = count(), by: { dt.entity.service }
| join [
    fetch logs
    | filter dt.entity.service != ""
      and toLong(timestamp) > now() - 15m
    | summarize total = count(), by: { dt.entity.service }
  ], on: { dt.entity.service }
| fieldsAdd error_rate = errors / total
| filter error_rate > 0.05
| sort error_rate desc
```

DQL is functional/pipeline-style, similar in shape to KQL or Splunk's pipe-based SPL. The data model is dimensional and entity-aware (`dt.entity.service` is the service identifier across the platform).

**Splunk ITSI SPL:**

```spl
index=app sourcetype=access_log earliest=-15m
| stats count(eval(status>=500)) as errors, count as total by service
| eval error_rate = errors/total
| where error_rate > 0.05
| sort - error_rate
```

SPL is also pipe-based but more sed/awk-flavoured — closer to text-processing than to a structured query language. Easier to start writing if you've come from log search; can become harder at scale than DQL when you're working across multiple data types.

For service-health monitoring specifically, ITSI gives you a higher-level abstraction: define an `error_rate` KPI on a service once, threshold it once, and the service health rolls up automatically. With Dynatrace, the equivalent capability is built into Smartscape and you don't define it explicitly — Davis surfaces it when relevant.

---

## Pricing — Worked, Roughly

Both vendors hate publishing fixed prices and the real number is whatever your procurement team negotiates. Public list-price ballparks (verify before committing):

**Dynatrace** (per-host, "Davis Units" billing):

- Full-stack monitoring: ~$0.08/host/hour ≈ ~$58/host/month list.
- For 500 hosts × 12 months: roughly $350K/year list.
- Logs/RUM/synthetic add separately.

**Splunk ITSI**:

- Splunk Cloud licensing is per-GB ingested or per-vCPU (workload pricing) depending on tier. Public list ≈ $1,500–$2,500 per ingested GB/year for Cloud.
- ITSI Premium SKU on top — typically a ~30–40% uplift over the underlying Splunk spend.
- For 1 TB/day ingest: roughly $1.5–2M/year list before discount.

The shape of the cost is genuinely different:

- **Dynatrace cost scales with the size of your fleet**, regardless of how chatty the apps are.
- **Splunk cost scales with how much data you ingest**, regardless of how many machines produce it.

Implication: if you have a small, chatty estate (financial trading, IoT), Dynatrace is often cheaper. If you have a large, quiet estate (corporate IT, regulated batch workloads), Splunk's volume model can come out lower if you’re selective about ingest. Real procurement deals usually involve volume discounts of 30–60%; treat the figures above as a relative-cost compass, not a quote.

---

## RCA Philosophy: Automated vs Explicit

This is the difference that splits opinion most consistently among teams who've used both.

**Dynatrace Davis AI does RCA for you.** When a problem is detected, Davis evaluates topology, recent changes, dependencies, and related telemetry to point to a single root cause. You get a "problem card" that says "this deploy of service X is the root cause; here are the affected dependents". Engineers who like it call it the killer feature; engineers who don't trust black-box AI call it "Davis says so, fine". Davis usually gets it right; when it doesn't, debugging the AI is harder than debugging your own correlation rules.

**Splunk ITSI gives you the building blocks for explicit RCA.** You model the services. You define the KPIs. You set the thresholds. You build the glass tables. Episodes (correlated incidents) surface based on rules and ML you can inspect and tune. When it gets RCA wrong, you know exactly which knob to turn. When it's right, you have a clear chain of reasoning you can audit.

The tradeoff:

- Davis is faster to value and lower maintenance. ITSI is more transparent and tunable.
- Davis works best when your environment matches the patterns it was trained on. ITSI works best when your team has the SRE/SPL skills to build the model.
- Davis abstracts away the work of correlation. ITSI rewards teams who do that work explicitly.

In regulated industries (finance, healthcare, defence) where auditors ask "why did the system flag this incident?", explicit ITSI models are easier to defend. In high-velocity startups and cloud-native shops where the topology changes weekly, automated Davis usually wins.

---

## Operational Reality: A Day in the Life of On-Call

What does "the platform makes my life easier" actually look like? The shape of a typical 2am alert in each:

**On Dynatrace:**

1. PagerDuty or Slack notification: "Davis problem: payment-service latency degraded".
2. Click the problem card. See: timeline of when it started, the deploy 15 minutes earlier, the affected services downstream, the metric/log/trace evidence.
3. Look at the suggested root cause: "Deploy `payment-service:v2.3.7` 16 minutes ago". Davis is nearly certain.
4. Roll back. Confirm via the same card that the problem ends.

Time-to-action is usually under 5 minutes if Davis has it right. If Davis has it wrong, you're back to manual investigation but with worse tools than you'd have natively.

**On Splunk ITSI:**

1. PagerDuty or Slack notification: "ITSI episode: payment-service health KPI breach".
2. Open the service's glass table. See: SLO trend, the KPIs in red, recent change events.
3. Drill into SPL: `index=payment-prod earliest=-30m` then iterate. Or click through to the linked saved searches you set up for this service.
4. Identify the cause via SPL searches across logs, metrics, and trace data.
5. Roll back, fix, or escalate.

Time-to-action varies more — usually 5–20 minutes — because you're driving the investigation. The flip side: when you nail the root cause, the search is reusable. When you've done it three times, the saved search becomes a runbook step. ITSI rewards the kind of team that builds up that institutional knowledge over years.

---

## Decision Tree

Run through these in order. The first "yes" is likely your answer.

1. **Is Splunk already your logging backbone, with significant data and team skill invested?** → Splunk ITSI. The cost of moving off Splunk usually exceeds the value of switching to Dynatrace unless something else is broken.
2. **Are you regulated/compliance-heavy with strict log retention requirements?** → Splunk (with or without ITSI) for the data lake; pair with Dynatrace if you also want a separate APM layer.
3. **Is your environment cloud-native, Kubernetes-heavy, microservices-heavy, with rapid topology change?** → Dynatrace. Auto-discovery and Davis RCA are most valuable in exactly this shape.
4. **Greenfield with a strong DevOps/SRE team and no Splunk legacy?** → Dynatrace as the default; consider [Datadog or Grafana Cloud](https://geekyblinder.co.uk/#/2027/06/06/Top-AIOps-Platforms-for-DevOps-Teams-in-2026) before committing.
5. **Heavy ML/data-science team that wants to build custom analytics on top?** → Splunk ITSI gives you SPL and ML toolkit hooks Dynatrace doesn't expose as openly.
6. **Cost is *the* decision factor and you're medium-sized?** → Run both POCs. The cost shape difference (per-host vs per-GB) means one is often dramatically cheaper for your specific data profile.

---

## A Practical Way to Decide

For a large DevOps team, run a time-boxed evaluation against real services and real incidents. Don’t trust demos.

- **Pick 2 critical services** with different shapes — one cloud-native (K8s, microservices), one traditional (VM, monolith). Different platforms favour different shapes.
- **Run for 6–12 weeks each** — the same shape pilot on each platform if you can stomach the parallel cost; sequentially if not.
- **Measure against your baseline:**
  - Time to deploy and get full telemetry. (Days, not weeks.)
  - Reduction in alert noise vs your before-picture.
  - Speed and quality of root-cause suggestions during real incidents — track each one and rate "did the platform get there before I did?".
  - Cost projected at full estate scale, including the add-ons you actually used.
  - On-call sentiment via anonymous survey.
- **Decide on the data, not the demo.**

If you’re starting relatively greenfield, Dynatrace is usually the safer, quicker win. If Splunk is already the beating heart of your monitoring and your team can write SPL in their sleep, ITSI is the more economical and integrated route.

The "best" platform is the one your DevOps/SRE engineers actually trust at 3am — and that comes down to how quickly it gives them a believable root cause and a clear next step. Davis does it for you; ITSI gives you the materials to do it yourself. Pick the one that matches the team you have.

<img src="img/authors/geeky.jpg" width="40"/>
