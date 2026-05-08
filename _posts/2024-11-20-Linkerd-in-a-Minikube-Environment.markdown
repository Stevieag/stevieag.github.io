---
title:  "Minikube Linkerd"
subtitle: "A working service-mesh tutorial — install, observe, secure, route"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/minikube-linkerd.jpg"
date: 2024-10-11
tags: minikube linkerd micro service
---

This is the worked tutorial I wish I'd had when I first stood up a service mesh on a laptop — install Linkerd into Minikube, deploy a sample app, see the mesh in action (mTLS, observability, traffic split, authorization), then tear it down. Pairs with my [5-Week DevOps Training Plan](https://geekyblinder.co.uk/#/2024/11/25/Five-Week-DevOps-Training-Plan); also useful prep for [Helm, Docker, and Kubernetes: A Tiny Training App to Break (and Fix)](https://geekyblinder.co.uk/#/2027/08/01/Helm-Docker-K8s).

# Contents

- Prerequisites
- Set up Minikube
- Deploy a sample app
- Install Linkerd
- Inject the proxies
- Explore the mesh
  - Dashboard and observability
  - mTLS verification
  - Traffic management with HTTPRoute
  - Authorization policies (mTLS-enforced access)
  - Tap and Top
- Cleaning up
- Troubleshooting
- Where to go next

# Prerequisites

- **Minikube.** [Install](https://minikube.sigs.k8s.io/docs/start/). 4 GB RAM allocated to the VM is comfortable; 2 GB will work but be sluggish.
- **kubectl.** Configured to talk to your Minikube cluster.
- **Linkerd CLI.** We'll install this in a moment.
- **A few minutes of patience.** Container pulls take longer than the docs imply.

You don't need to know Linkerd's internals to follow this — the proxy is a sidecar that intercepts traffic for each pod, and the control plane manages identity, configuration, and metrics. That's the mental model.

# Set up Minikube

Start the cluster with enough resources to be useful:

```bash
minikube start --cpus=4 --memory=4096 --kubernetes-version=v1.30.0
minikube status
kubectl get nodes
```

Confirm `kubectl get nodes` shows a Ready node before moving on.

# Deploy a Sample Application: emojivoto

Linkerd ships a small demo app called *emojivoto* — a couple of Go services with a Vue frontend, deliberately a bit broken (the doughnut vote always fails, on purpose, so you can see the mesh catch errors).

```bash
curl --proto '=https' --tlsv1.2 -sSfL https://run.linkerd.io/emojivoto.yml | \
  kubectl apply -f -

kubectl get pods -n emojivoto
```

Wait until all pods are `Running`. Then port-forward the web service so you can hit it from a browser:

```bash
kubectl -n emojivoto port-forward svc/web-svc 8080:80
```

Open `http://localhost:8080`. You should see the emoji voting page. Click an emoji or two — you're now generating traffic that the mesh will see once we install it.

Leave the port-forward running in another terminal.

# Install Linkerd

## Install the CLI

Pin a version. Linkerd's stable channel as of writing is 2.16+; check [linkerd.io/2/install](https://linkerd.io/2/getting-started/) for current.

```bash
curl --proto '=https' --tlsv1.2 -sSfL https://run.linkerd.io/install | sh
export PATH=$PATH:$HOME/.linkerd2/bin

# stash this in your shell rc so it survives a new shell
echo 'export PATH=$PATH:$HOME/.linkerd2/bin' >> ~/.zshrc

linkerd version
```

## Pre-flight Check

Linkerd is paranoid about installing into a cluster it doesn't trust. Run the pre-flight before you commit:

```bash
linkerd check --pre
```

Every check should be green. If anything's red, fix it before continuing — installing on top of a half-working cluster is a recipe for confusing failures later.

## Install the Control Plane

Two-step install — CRDs first, then the control plane:

```bash
linkerd install --crds | kubectl apply -f -
linkerd install | kubectl apply -f -

# verify
linkerd check
```

The full check is the moment of truth — every section green means the mesh is ready.

# Inject the Proxies

Linkerd doesn't apply itself automatically; you tell it which workloads should be meshed. The simplest way is to grab the existing deployments, pipe them through `linkerd inject`, and re-apply:

```bash
kubectl get -n emojivoto deploy -o yaml | \
  linkerd inject - | \
  kubectl apply -f -

# pods will roll over with sidecars attached
kubectl get pods -n emojivoto
```

Each pod should now show `2/2` containers running (your app + the `linkerd-proxy` sidecar). That `2/2` is the visual confirmation the mesh is on.

For production, you'd typically annotate the namespace so any deployment in it gets injected automatically:

```bash
kubectl annotate namespace emojivoto linkerd.io/inject=enabled
```

# Explore the Mesh

## Dashboard and Observability

Linkerd Viz is a separate extension for the dashboard, Prometheus, Grafana, and Jaeger.

```bash
linkerd viz install | kubectl apply -f -
linkerd viz check
linkerd viz dashboard &
```

The dashboard opens in your browser. Click into the `emojivoto` namespace and you'll see live metrics — request rate, success rate, p50/p95/p99 latency, retries, and TCP-level stats — for every service. The vote-doughnut endpoint is going to look red because that's the deliberately-broken bit.

Linkerd's metrics live in Prometheus and are available via `linkerd viz`:

```bash
# RPS by service
linkerd viz stat deploy -n emojivoto

# detailed view of one service
linkerd viz stat deploy/web -n emojivoto --window 1m
```

A useful pattern: get raw Prometheus metrics out of the viz extension and write your own queries / dashboards in your own Grafana:

```bash
kubectl port-forward -n linkerd-viz svc/prometheus 9090:9090

# Then in your browser at http://localhost:9090:
# rate(request_total{namespace="emojivoto"}[1m])
# histogram_quantile(0.99, rate(response_latency_ms_bucket{namespace="emojivoto"}[1m]))
```

## mTLS Verification

The killer feature: every meshed pod gets a workload identity, certificates issued and rotated automatically, and traffic between meshed pods is mTLS-encrypted with no app changes. Verify it:

```bash
linkerd viz tap deploy/web -n emojivoto
```

Hit the website, vote a few emojis. The tap output will scroll past, with lines like:

```
req id=12:0 proxy=in src=10.244.0.60:59620 dst=10.244.0.58:8080 tls=true
rsp id=12:0 proxy=in src=10.244.0.60:59620 dst=10.244.0.58:8080 tls=true :status=200 latency=959µs
```

`tls=true` is what you're looking for. That's mutual TLS between the source and destination pods — no per-app TLS engineering, no certificate juggling, no surprises.

## Traffic Management with HTTPRoute

Linkerd 2.14+ uses the [Gateway API](https://gateway-api.sigs.k8s.io/) (`HTTPRoute`) for traffic splitting; the older `TrafficSplit` resource is deprecated.

Imagine you've built `web-v2` with new colours and want 50% of traffic to hit it. (We won't actually deploy a v2 here — assume it exists for the demo.)

```bash
kubectl apply -f - <<'EOF'
apiVersion: gateway.networking.k8s.io/v1beta1
kind: HTTPRoute
metadata:
  name: web-split
  namespace: emojivoto
spec:
  parentRefs:
    - name: web-svc
      kind: Service
      group: ""
      port: 80
  rules:
    - backendRefs:
        - name: web-svc
          port: 80
          weight: 50
        - name: web-v2-svc
          port: 80
          weight: 50
EOF
```

You can change the weights any time and the mesh will rebalance traffic without restarting anything. Canaries, blue/green, and progressive delivery patterns build on top of this primitive.

## Authorization Policies (mTLS-Enforced Access)

Past 2.12, Linkerd has first-class authorization policies. Combine `Server` (which port on which workload accepts traffic) with `AuthorizationPolicy` (who can reach it) to enforce identity-based access between meshed workloads.

Lock down the `voting-svc` so only the `web` service can call it:

```bash
kubectl apply -f - <<'EOF'
apiVersion: policy.linkerd.io/v1beta1
kind: Server
metadata:
  name: voting-grpc
  namespace: emojivoto
spec:
  podSelector:
    matchLabels: { app: voting-svc }
  port: 8080
  proxyProtocol: gRPC
---
apiVersion: policy.linkerd.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: voting-allow-web
  namespace: emojivoto
spec:
  targetRef:
    group: policy.linkerd.io
    kind: Server
    name: voting-grpc
  requiredAuthenticationRefs:
    - kind: ServiceAccount
      name: web
      namespace: emojivoto
EOF
```

Any other meshed pod trying to call `voting-svc:8080` now gets denied at the proxy. This is real, identity-based service-to-service authorisation — no IP allowlists, no shared secrets. For the broader picture this fits into, see [Zero Trust Architecture: A Deep Practical Walkthrough](https://geekyblinder.co.uk/#/2026/05/10/Zero-Trust-Architecture-A-Deep-Practical-Walkthrough).

## Tap and Top

Two CLI tools that pay off when something's broken at 11pm:

```bash
# live request stream — tcpdump for HTTP
linkerd viz tap deploy/web -n emojivoto

# top-N requests by route, like top(1) but for service traffic
linkerd viz top deploy/web -n emojivoto
```

`top` is the one I reach for first when something's slow — it shows the path that's hot and lets you drill in. Pair with the dashboard for the visual view.

# Cleaning Up

Tear it all down in reverse order:

```bash
# remove the demo app
curl --proto '=https' --tlsv1.2 -sSfL https://run.linkerd.io/emojivoto.yml | \
  kubectl delete -f -

# remove Linkerd Viz
linkerd viz uninstall | kubectl delete -f -

# remove the Linkerd control plane
linkerd uninstall | kubectl delete -f -

# stop Minikube if you're done
minikube stop

# nuke it entirely if you want a clean slate
minikube delete
```

# Troubleshooting

The errors I've actually hit during fresh installs:

**"No objects passed to apply"** during `linkerd install` — you forgot the CRDs step. Run:

```bash
linkerd install --crds | kubectl apply -f -
```

then re-run the control-plane install.

**Pods stuck `Init:Error` after injection** — usually `proxyInit` running into kernel-permission issues on local clusters. The default is fine on most Minikube setups; if it isn't, you'll want to investigate the init container logs:

```bash
kubectl logs -n emojivoto <pod> -c linkerd-init
```

If you see iptables errors, the older workaround was `--set proxyInit.runAsRoot=true` on install. Modern Linkerd handles this without the flag on most setups.

**`linkerd check` red on identity** — usually clock skew between Minikube and your host. Restart Minikube and the host time-sync, run `linkerd check` again.

**`tls=false` in `linkerd viz tap`** — the source pod isn't meshed, or the destination isn't. Check both have `2/2` containers running.

# Where to Go Next

Real things to try once you're comfortable:

- **Multicluster.** [Linkerd's multicluster extension](https://linkerd.io/2/features/multicluster/) lets meshes span clusters with mTLS-everywhere over the public internet — useful for HA across regions, gradual cluster migration, or tying staging to a separate cluster.
- **Service Profiles and retry budgets.** Define per-route retry policies and timeouts in YAML; let the mesh handle transient failures without app code knowing.
- **Replace Viz Prometheus with your own.** The bundled Prometheus is fine for play; in prod, point Linkerd's metrics at your existing Prometheus or Mimir.
- **Argo Rollouts + Linkerd.** Progressive delivery using `HTTPRoute` weights, automated based on success-rate metrics from the mesh.
- **Run [Buoyant Cloud](https://buoyant.io/cloud) or self-hosted Buoyant Enterprise for Linkerd** if you want a managed control plane — same OSS Linkerd underneath, with extras for compliance and FIPS.

# Additional Resources

- [Linkerd Documentation](https://linkerd.io/2/getting-started/) — official, current, comprehensive.
- [Linkerd Slack](https://linkerd.io/community/) — surprisingly responsive for an OSS project.
- [Minikube Documentation](https://minikube.sigs.k8s.io/docs/) — for managing your local cluster.
- [5-Week DevOps Training Plan](https://geekyblinder.co.uk/#/2024/11/25/Five-Week-DevOps-Training-Plan) — service mesh, K8s, and the rest of the curriculum this fits into.

<img src="img/authors/geeky.jpg" width="40"/>
