---
title:  "Helm, Docker, and Kubernetes: A Tiny Training App to Break (and Fix)"
subtitle: "Learning K8s by actually doing something vaguely fun"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/tri.png"
date: 2026-03-01
tags: kubernetes helm docker devops devsecops training
---

## Helm, Docker, and Kubernetes: A Tiny Training App to Break (and Fix)

Let’s stop learning Kubernetes by reading error messages in tears at 2 a.m. and instead build a small lab app that you *expect* to break. The goal: deploy a tiny web service with Docker, Kubernetes, and Helm, then deliberately cause the classic problems (CrashLoopBackOff, ImagePullBackOff, bad ports, resource issues) and practise fixing them until it feels routine. [web:12][web:24][web:27]

Our project will be a very simple “Hello K8s” HTTP API running in Docker, exposed via a Kubernetes Deployment, Service, and optional Ingress, and managed by a Helm chart. This pattern mirrors most real microservices and follows common Helm and chart‑structure best practices. [web:22][web:28]

---

## Step 1: Choose a Simple but Realistic Project

**Project:** A tiny “Hello K8s” JSON API.

- Implementation options:
  - Node.js + Express: responds to `/` and `/health`.
  - Python + Flask: similar endpoints.
  - Go HTTP server if you like static binaries.

**Why this project is applicable:**

- HTTP + JSON is what most internal services look like.
- Health checks map directly to Kubernetes liveness/readiness probes.
- Stateless by design, so you can focus on Kubernetes behaviour, not databases.

**Training objectives at this stage:**

- Understand how app behaviour (ports, env vars, logging) affects Docker and K8s.
- Make the app easy to observe and easy to misconfigure on purpose.

**What could go wrong at this stage (and how to fix):**

- Hard‑coding the port inside the app and later misaligning it with Kubernetes.
  - Fix: Accept `PORT` from an environment variable, with a sensible default (e.g. 3000).
- No `/health` endpoint, making it hard to differentiate “app is truly down” from “route is wrong”.
  - Fix: Add a simple health endpoint that returns a 200 and a tiny JSON payload.

---

## Step 2: Build a Solid Docker Image

We now containerise the app with a clean, production‑style Dockerfile.

**Key Dockerfile principles:**

- Use a slim base image (e.g. `node:20-alpine`, `python:3.12-alpine`) to keep images small and pulls fast. [web:22][web:26]
- Install dependencies from a lockfile or requirements file before copying the whole app so Docker layer caching works efficiently. [web:26]
- Run the app as a non‑root user inside the container; many clusters enforce non‑root execution for security. [web:22]

**Functional requirements for the container:**

- Listens on the port defined by `PORT` env var (or a default).
- Logs to stdout/stderr (no log files), so Kubernetes and log collectors can capture output. [web:22]
- Exits with a non‑zero code on fatal startup error (bad env etc.), so Kubernetes can detect failure.

**Common mistakes to practise:**

1. **Bloated image**
   - Error pattern: Copying the entire repo, including `.git`, tests, and node_modules, resulting in very large images.
   - Training fix:
     - Use `.dockerignore` to exclude `.git`, local `node_modules`, large assets.
     - Copy only the files needed for building and running the app.
2. **Running as root**
   - Error pattern: Pods get rejected or flagged by Pod security policies because the container runs as root.
   - Training fix:
     - Add a user with `RUN adduser` (or equivalent) and `USER` directive in Dockerfile.
     - Later, align Pod `securityContext` with this non‑root user when needed. [web:22]
3. **Wrong or fixed port**
   - Error pattern: App listens on 3000, but you configure Kubernetes to route to 8080.
   - Training fix:
     - Standardise on a port (e.g. 8080) and wire that via `PORT` env var.

**How to verify correctness:**

- Run `docker build` and `docker run -p 8080:8080` and test:
  - `curl http://localhost:8080/` returns your JSON.
  - `curl http://localhost:8080/health` returns a 200.
- If it fails:
  - Use `docker logs` to inspect startup errors.
  - Use `docker exec` to check user, port, and environment if the container is running but misbehaving.

---

## Step 3: Deploy “Raw” to Kubernetes with Manifests

Before Helm, you should feel how Kubernetes works with plain YAML.

**Create the following manifests:**

- **Deployment**:
  - Uses your image and runs 2–3 replicas.
  - Sets `containerPort` to match your app (e.g. 8080).
  - Includes at least:
    - Liveness probe hitting `/health`.
    - Readiness probe also hitting `/health`. [web:28]
- **Service (ClusterIP)**:
  - Exposes port 80 externally (inside the cluster) and forwards to `targetPort` 8080 on Pods.
- **Optional Ingress**:
  - Routes `http://hello.local/` → your Service (depends on ingress controller).

**Core Kubernetes concepts to train:**

- Pods are ephemeral; the Deployment ensures the desired number of replicas is maintained.
- Service provides a stable virtual IP and DNS name over changing Pod IPs.
- Ingress is the HTTP entrypoint from outside the cluster into Services.

**Intentional mistakes and fixes:**

1. **Using `:latest` tags everywhere**
   - Problem: You push new images with the same tag, and Kubernetes may not pull the new image; rollbacks become guesswork. [web:20]
   - Training fix:
     - Tag images with a version or git SHA.
     - Update the Deployment’s `image` to that specific tag.
2. **Missing resource requests/limits**
   - Problem: No CPU/memory requests/limits → one noisy app can starve others and cause instability. [web:18]
   - Training fix:
     - Add conservative requests and reasonable limits in the Deployment.
     - Observe scheduling behaviour when resources are constrained.
3. **Wrong ports in Service**
   - Problem: Service `targetPort` doesn’t match `containerPort`, so traffic fails silently.
   - Training fix:
     - Check `kubectl describe svc` and `kubectl get endpoints` to ensure the Service has correct endpoints.
     - Align ports and redeploy.

**How to verify correctness:**

- `kubectl get pods` ⇒ Pods should be `Running`, not `Pending` or `CrashLoopBackOff`. [web:24]
- `kubectl get svc` ⇒ Service exists with an internal IP.
- If using Ingress, `kubectl get ingress` shows correct host and paths.
- From a debug Pod in the cluster, `curl http://<service-name>/health` should return 200.

---

## Step 4: Turn Those Manifests into a Helm Chart

Now we convert our working manifests into a Helm chart.

**Standard chart layout (Helm‑recommended):**

- `Chart.yaml`: Metadata (name, version, appVersion). [web:22][web:28]
- `values.yaml`: Default values for image, replicas, resources, env vars, Ingress host, etc. [web:22]
- `templates/`:
  - `deployment.yaml`, `service.yaml`, `ingress.yaml` using Go templates and `.Values`. [web:28]
- Optional:
  - `_helpers.tpl` for reusable snippets (labels, names).
  - `charts/` for dependencies, `tests/` for chart tests. [web:22]

**Why this is correct and scalable:**

- Helm’s template language renders YAML manifests using values, then sends them to Kubernetes; this is the official, supported model. [web:28]
- Keeping configuration in `values.yaml` and structure in `templates/` matches Helm best practices and simplifies reuse across environments. [web:22][web:25]

**Common Helm mistakes and training fixes:**

1. **Mis‑indentation in templates**
   - Problem: Mixing Go templates and YAML can produce invalid YAML or subtle bugs. [web:13][web:28]
   - Training fix:
     - Run `helm lint` to catch basic issues. [web:22]
     - Run `helm template` to inspect the fully rendered YAML before deploying. [web:28]
2. **Not quoting values**
   - Problem: YAML treats unquoted `true`, `false`, `01`, etc. as booleans/numbers when you wanted strings. [web:22]
   - Training fix:
     - Quote values that might be misinterpreted.
     - Prefer explicit types in `values.yaml` for things like feature flags.
3. **Hard‑coding environment‑specific data**
   - Problem: Hostnames, image tags, or resource limits baked into templates, making the chart hard to reuse. [web:22][web:25]
   - Training fix:
     - Move those fields into `values.yaml`.
     - Use separate `values.dev.yaml`, `values.prod.yaml` with overrides. [web:25]

**Check your Helm chart:**

- `helm lint ./hello-k8s` ⇒ Should pass with no errors. [web:22]
- `helm template hello ./hello-k8s` ⇒ Render manifests and visually confirm:
  - Correct image, ports, probes, labels.
- `helm install hello ./hello-k8s -n playground` ⇒ Install into a dedicated namespace. [web:23]

---

## Step 5: Break It On Purpose – Classic K8s Failure Modes

Now we use the chart as a playground for the most common Kubernetes errors.

### Scenario A: CrashLoopBackOff (App Keeps Crashing)

**Break it:**

- Set an invalid env var in `values.yaml` (e.g. bad database URL or missing secret).
- Or deliberately introduce a bug that causes the app to exit at startup.

**What you’ll see:**

- `kubectl get pods` shows status `CrashLoopBackOff`. [web:12][web:24][web:27]

**How to analyse correctly:**

1. Run `kubectl logs <pod>`:
   - Look for stack traces or config errors (missing env, invalid argument). [web:12]
2. Run `kubectl describe pod <pod>`:
   - Check `Last State` for exit code and reason.
3. Distinguish CrashLoopBackOff from other states:
   - CrashLoopBackOff: container *starts, crashes, restarts repeatedly*. [web:24][web:27]
   - ImagePullBackOff: image never pulled; container never starts. [web:12][web:24][web:27]
   - Pending: Pod scheduled but no container created yet (often resource/scheduling issues). [web:24]

**Fix it:**

- Correct the env var in `values.yaml` or fix the application bug.
- `helm upgrade hello ./hello-k8s -n playground`.
- Watch with `kubectl get pods` until status is `Running`.

### Scenario B: ImagePullBackOff (Image Cannot Be Pulled)

**Break it:**

- Change the image tag in `values.yaml` to a non‑existent one.
- Or point to a private registry without proper credentials.

**What you’ll see:**

- `kubectl get pods` shows `ImagePullBackOff` or `ErrImagePull`. [web:12][web:24][web:27]

**Correct analysis steps:**

1. `kubectl describe pod <pod>`:
   - In the `Events` section, read the detailed error message (e.g. “manifest unknown”, “authentication required”). [web:12][web:27]
2. Try `docker pull` the same image from your machine:
   - If it fails, the image name/tag or registry is wrong.
   - If it succeeds, check network access and Kubernetes imagePullSecrets. [web:12]

**Fix it:**

- Correct image name/tag and ensure the image is pushed to the registry.
- For private registries, create an imagePullSecret and reference it in the Pod spec.
- `helm upgrade` and confirm Pods move to `Running`.

### Scenario C: Pending Pods (Scheduling Issues)

**Break it:**

- Set resource requests (CPU/memory) in `values.yaml` higher than any node can offer.

**What you’ll see:**

- `kubectl get pods` shows `Pending` for a long time. [web:24]

**Analysis:**

- `kubectl describe pod <pod>`:
  - Look for messages like “0/3 nodes are available: X Insufficient memory, Y Insufficient cpu”. [web:18][web:24]

**Fix it:**

- Reduce resource requests in `values.yaml` to realistic values.
- Optionally scale your cluster or node resources if this were production.
- Re‑deploy and confirm pods become `Running`.

---

## Step 6: Use Helm Properly to Iterate and Recover

We now use Helm workflows to upgrade, debug and roll back safely.

**Key Helm commands and why they matter:**

- `helm upgrade --install hello ./hello-k8s -n playground`:
  - Ensures the release exists and updates it in one command; this is a common recommended pattern. [web:23]
- `helm get values hello -n playground`:
  - Shows the effective config used for the release; crucial for debugging misconfigurations. [web:22]
- `helm get manifest hello -n playground`:
  - Lets you inspect the exact manifests Kubernetes sees.
- `helm rollback hello <revision> -n playground`:
  - Revert to a previous working version when a change breaks things.

**Training exercise: upgrade–break–rollback:**

1. Start from a healthy deployment.
2. Introduce a bug (bad env, wrong port, non‑existent image tag) in `values.yaml`.
3. `helm upgrade` and watch pods fail.
4. `helm rollback` to the previous revision, confirm it recovers.
5. Repeat with a different failure mode.

This builds muscle memory for safe iteration in real environments.

---

## Step 7: Reflect and Extend – Training Opportunities

You now have a repeatable mini‑lab that hits real skills:

- Writing a sensible Dockerfile and understanding layering and security. [web:22][web:26]
- Deploying basic Kubernetes resources: Deployment, Service, Ingress.
- Converting static manifests into a reusable Helm chart with proper structure. [web:22][web:28]
- Recognising and fixing the most common Kubernetes error states:
  - CrashLoopBackOff, ImagePullBackOff, Pending. [web:12][web:24][web:27]
- Using Helm to manage configuration, upgrades, and rollbacks cleanly. [web:22][web:23]

To keep it fun and evolving:

- Turn each scenario into “tickets”:
  - “Service returns 502”, “Pods in CrashLoopBackOff”, “ImagePullBackOff for new release”.
- Time yourself diagnosing and fixing each one.
- Write short internal “incident reports” for each failure, describing:
  - Symptom, root cause, commands you ran, and the fix.

The more you run these drills, the more Kubernetes stops feeling like an unpredictable monster and starts feeling like a system with well‑understood failure modes that you know how to drive and repair.

<img src="img/authors/geeky.jpg" width="40"/>