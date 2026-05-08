---
title:  "Helm, Docker, and Kubernetes: A Tiny Training App to Break (and Fix)"
subtitle: "Learning K8s by actually doing something vaguely fun"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/helm-docker-and-kubernetes-a-tiny-training-app-to-break.jpg"
date: 2027-08-01
tags: kubernetes helm docker devops devsecops training
---
{% raw %}

## Helm, Docker, and Kubernetes: A Tiny Training App to Break (and Fix)

Let's stop learning Kubernetes by reading error messages in tears at 2 a.m. and instead build a small lab app that you *expect* to break. The goal: deploy a tiny web service with Docker, Kubernetes, and Helm, then deliberately cause the classic problems — `CrashLoopBackOff`, `ImagePullBackOff`, port mismatches, OOMKilled — and practise fixing them until it feels routine. We'll also bake in the security defaults you should be using on day one rather than retrofitting in a panic at audit time.

The project: a tiny "Hello K8s" JSON API. Node.js + Express because it's the simplest thing that still feels like a real microservice. The same shape works for Python/Flask or Go if you'd rather.

You'll need: Docker Desktop or [colima](https://github.com/abiosoft/colima), [`kind`](https://kind.sigs.k8s.io/) or `minikube` for a local cluster, `kubectl`, and `helm` v3.14+.

---

## Step 1: The App

```bash
mkdir hello-k8s-training && cd hello-k8s-training
npm init -y
npm install express
```

`index.js`:

```js
const express = require("express");
const app = express();
const PORT = process.env.PORT || 8080;

app.get("/", (req, res) => {
  res.json({
    message: "Hello, K8s!",
    time: new Date().toISOString(),
    hostname: process.env.HOSTNAME || "unknown"
  });
});

app.get("/health", (req, res) => {
  res.status(200).json({ status: "ok", uptime: process.uptime() });
});

if (!process.env.APP_NAME) {
  console.error("APP_NAME environment variable is required");
  process.exit(1);
}

app.listen(PORT, "0.0.0.0", () => {
  console.log(`Server listening on port ${PORT}`);
});
```

Test locally:

```bash
APP_NAME=local npm start
curl http://localhost:8080/
curl http://localhost:8080/health

PORT=9090 APP_NAME=local npm start
curl http://localhost:9090/health
```

The deliberately strict `APP_NAME` check is there so we have a guaranteed `CrashLoopBackOff` scenario to practise on later.

---

## Step 2: The Container

`.dockerignore` first — without it, your image ships your `node_modules`, your git history, and any `.env` you forgot about:

```text
.git
node_modules
npm-debug.log
.gitignore
README.md
.env
tests/
```

`Dockerfile` — multi-stage, non-root, minimal:

```dockerfile
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev

FROM node:20-alpine AS production
RUN addgroup --gid 1001 appgroup && \
    adduser --uid 1001 --system --ingroup appgroup appuser
WORKDIR /app
COPY --from=builder --chown=appuser:appgroup /app/node_modules ./node_modules
COPY --chown=appuser:appgroup . .
USER appuser
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=3s \
  CMD wget --no-verbose --tries=1 --spider http://localhost:8080/health || exit 1
CMD ["npm", "start"]
```

Build, smoke-test, push:

```bash
docker build -t hello-k8s:v1.0.0 .
docker run --rm -e APP_NAME=docker -p 8080:8080 hello-k8s:v1.0.0 &
curl http://localhost:8080/health
docker ps --format '{{.ID}}' | head -1 | xargs docker stop

docker run --rm hello-k8s:v1.0.0 whoami     # appuser  ✓
docker images | grep hello-k8s              # < 200 MB ✓

# Push to your registry (replace yourusername)
docker tag hello-k8s:v1.0.0 yourusername/hello-k8s:v1.0.0
docker push yourusername/hello-k8s:v1.0.0
```

Common breaks worth practising:

- Remove `.dockerignore` → bloated 1 GB+ image. Fix: put it back.
- Comment out `USER appuser` → container runs as root. Fix: uncomment, rebuild, verify with `docker run --rm <image> whoami`.

---

## Step 3: Raw Kubernetes (No Helm Yet)

A namespace with [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) enforcement enabled — the `restricted` baseline catches the majority of weak-pod-spec mistakes for you:

`k8s/namespace.yaml`:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: playground
  labels:
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/enforce-version: latest
    pod-security.kubernetes.io/warn: restricted
```

`k8s/deployment.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-k8s
  namespace: playground
  labels:
    app: hello-k8s
spec:
  replicas: 3
  selector:
    matchLabels:
      app: hello-k8s
  template:
    metadata:
      labels:
        app: hello-k8s
    spec:
      automountServiceAccountToken: false
      securityContext:
        runAsNonRoot: true
        runAsUser: 1001
        runAsGroup: 1001
        fsGroup: 1001
        seccompProfile:
          type: RuntimeDefault
      containers:
        - name: hello-k8s
          image: yourusername/hello-k8s:v1.0.0
          imagePullPolicy: IfNotPresent
          ports:
            - containerPort: 8080
              name: http
          env:
            - name: APP_NAME
              value: "training"
          resources:
            requests:
              cpu: "50m"
              memory: "64Mi"
            limits:
              cpu: "100m"
              memory: "128Mi"
          securityContext:
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
            capabilities:
              drop: ["ALL"]
          livenessProbe:
            httpGet:
              path: /health
              port: http
            initialDelaySeconds: 10
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /health
              port: http
            initialDelaySeconds: 5
            periodSeconds: 5
```

`k8s/service.yaml`:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: hello-k8s
  namespace: playground
spec:
  selector:
    app: hello-k8s
  ports:
    - port: 80
      targetPort: http
  type: ClusterIP
```

A default-deny `NetworkPolicy` so the pod can only do what we allow it to (you do have a CNI that supports policies — Calico, Cilium, AWS VPC CNI with policy mode, etc.):

`k8s/networkpolicy.yaml`:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: hello-k8s-default-deny
  namespace: playground
spec:
  podSelector:
    matchLabels:
      app: hello-k8s
  policyTypes: [Ingress, Egress]
  ingress:
    - from:
        - namespaceSelector:
            matchLabels:
              kubernetes.io/metadata.name: playground
      ports:
        - port: 8080
          protocol: TCP
  egress:
    - to:
        - namespaceSelector:
            matchLabels:
              kubernetes.io/metadata.name: kube-system
      ports:
        - port: 53
          protocol: UDP
```

Deploy and verify:

```bash
kubectl apply -f k8s/
kubectl get pods -n playground -w     # 3 Running ✓

kubectl run debug --rm -it --restart=Never \
  --image=curlimages/curl -n playground -- \
  curl http://hello-k8s:80/health     # 200 ✓
```

Breaks worth practising at this stage:

- `image: yourusername/hello-k8s:latest` → you'll never know which version is actually running. Fix: pin tags.
- Drop `runAsNonRoot: true` → with the namespace's `pod-security` label set to `restricted`, the pod is rejected. Fix: put it back. (This is the *point* — Pod Security Standards catch this for you.)
- `targetPort: 3000` in the Service → Service has no endpoints, `curl` returns connection refused. Fix: match the container's `containerPort: 8080`.
- Remove `env: APP_NAME` → `CrashLoopBackOff`, app refuses to start. Fix: add it back.

---

## Step 4: Convert to a Helm Chart

```bash
helm create hello-k8s
cd hello-k8s
rm -rf charts/ templates/tests/
```

Replace the generated files with leaner versions.

`Chart.yaml`:

```yaml
apiVersion: v2
name: hello-k8s
description: Training chart
type: application
version: 0.1.0
appVersion: "1.0.0"
```

`values.yaml`:

```yaml
replicaCount: 3

image:
  repository: yourusername/hello-k8s
  tag: "v1.0.0"
  pullPolicy: IfNotPresent

service:
  type: ClusterIP
  port: 80
  targetPort: 8080

resources:
  requests:
    cpu: "50m"
    memory: "64Mi"
  limits:
    cpu: "100m"
    memory: "128Mi"

env:
  APP_NAME: "helm-training"

probes:
  initialDelaySeconds: 10
  periodSeconds: 10
```

`templates/_helpers.tpl`:

```yaml
{{/* Common labels */}}
{{- define "hello-k8s.labels" -}}
helm.sh/chart: {{ .Chart.Name }}-{{ .Chart.Version | replace "+" "_" }}
app.kubernetes.io/name: {{ .Chart.Name }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
app: {{ .Chart.Name }}
{{- end }}
```

`templates/deployment.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Release.Name }}
  namespace: {{ .Release.Namespace }}
  labels:
    {{- include "hello-k8s.labels" . | nindent 4 }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app: {{ .Chart.Name }}
  template:
    metadata:
      labels:
        {{- include "hello-k8s.labels" . | nindent 8 }}
    spec:
      automountServiceAccountToken: false
      securityContext:
        runAsNonRoot: true
        runAsUser: 1001
        runAsGroup: 1001
        fsGroup: 1001
        seccompProfile:
          type: RuntimeDefault
      containers:
      - name: {{ .Chart.Name }}
        image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
        imagePullPolicy: {{ .Values.image.pullPolicy }}
        ports:
        - name: http
          containerPort: 8080
        env:
        {{- range $key, $value := .Values.env }}
        - name: {{ $key }}
          value: {{ $value | quote }}
        {{- end }}
        resources:
{{ toYaml .Values.resources | indent 10 }}
        securityContext:
          allowPrivilegeEscalation: false
          readOnlyRootFilesystem: true
          capabilities:
            drop: ["ALL"]
        livenessProbe:
          httpGet:
            path: /health
            port: http
          initialDelaySeconds: {{ .Values.probes.initialDelaySeconds }}
          periodSeconds: {{ .Values.probes.periodSeconds }}
        readinessProbe:
          httpGet:
            path: /health
            port: http
          initialDelaySeconds: {{ sub .Values.probes.initialDelaySeconds 5 }}
          periodSeconds: {{ .Values.probes.periodSeconds }}
```

`templates/service.yaml`:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: {{ .Release.Name }}
  namespace: {{ .Release.Namespace }}
  labels:
    {{- include "hello-k8s.labels" . | nindent 4 }}
spec:
  type: {{ .Values.service.type }}
  selector:
    app: {{ .Chart.Name }}
  ports:
  - name: http
    port: {{ .Values.service.port }}
    targetPort: {{ .Values.service.targetPort }}
```

Lint, render, deploy:

```bash
helm lint .
helm template demo . | less          # eyeball the rendered manifests
helm install demo . -n playground --create-namespace

kubectl get pods -n playground       # 3 Running ✓
helm list -n playground              # demo  deployed  rev 1
```

---

## Step 5: Break Everything (Methodically)

The point of this lab is repeated, deliberate breakage. Each scenario has the same shape: tweak `values.yaml`, `helm upgrade`, observe the failure, fix.

### A. CrashLoopBackOff

Break:

```yaml
# values.yaml
env:
  APP_NAME: ""
```

```bash
helm upgrade demo . -n playground
kubectl get pods -n playground       # CrashLoopBackOff
kubectl logs deploy/demo -n playground --tail=20
# "APP_NAME environment variable is required"
```

Fix: restore a non-empty `APP_NAME`, `helm upgrade`, watch `kubectl rollout status deploy/demo -n playground` go green.

### B. ImagePullBackOff

Break:

```yaml
image:
  tag: "v9999"
```

```bash
helm upgrade demo . -n playground
kubectl get pods -n playground             # ImagePullBackOff
kubectl describe pod -l app=hello-k8s -n playground | grep -A2 Events
# "Failed to pull image ... manifest unknown"
```

Fix: revert to a tag that exists.

### C. Service targetPort Mismatch

Break:

```yaml
service:
  port: 80
  targetPort: 3000      # wrong on purpose — app listens on 8080
```

```bash
helm upgrade demo . -n playground
kubectl get endpoints demo -n playground   # endpoints empty or wrong port

kubectl run debug --rm -it --restart=Never \
  --image=curlimages/curl -n playground -- \
  curl --max-time 3 http://demo:80/        # connection refused / timeout
```

Fix: `targetPort: 8080` (or use the named port `http` — even better, harder to get wrong).

### D. Memory Limit Too Low

Break:

```yaml
resources:
  limits:
    memory: "16Mi"      # below Node's startup heap
```

```bash
helm upgrade demo . -n playground
kubectl get pods -n playground             # OOMKilled, then CrashLoopBackOff
kubectl describe pod -l app=hello-k8s -n playground | grep -E 'Reason|Last State'
# Reason: OOMKilled
```

Fix: bump limits back to `128Mi` (or higher if you've added libraries).

### E. NetworkPolicy Lockout

Add a `templates/networkpolicy.yaml` that mistakenly denies DNS, then watch the app fail to start because Node can't resolve anything. The fix — allow egress to `kube-system` on UDP/53 — is in the raw-K8s example above. Worth doing once; it teaches you to read `kubectl describe` carefully.

---

## Step 6: Helm Upgrade and Rollback Drill

```bash
# A safe upgrade waits for the rollout
helm upgrade demo . -n playground --wait --timeout 2m

# Inspect what's deployed
helm list -n playground
helm get values demo -n playground
helm get manifest demo -n playground | head -40

# Now break it on purpose
sed -i.bak 's/v1\.0\.0/v9999/' values.yaml
helm upgrade demo . -n playground         # ImagePullBackOff incoming

# Roll back
helm history demo -n playground           # note REVISION 2 = the bad one
helm rollback demo 1 -n playground
kubectl get pods -n playground            # back to 3 Running ✓
mv values.yaml.bak values.yaml
```

Always practise the rollback. The first time you do it should not be in production at 11pm.

---

## Step 7: Cleanup and What to Build Next

```bash
helm uninstall demo -n playground
kubectl delete ns playground
```

Where to take this lab next, in increasing order of effort:

- **Ingress.** Add an `ingress-nginx` (or Traefik) controller, expose `demo.local` via your `/etc/hosts` and an Ingress resource, hit it with `curl`.
- **TLS.** [`cert-manager`](https://cert-manager.io/) with a self-signed `ClusterIssuer` is enough to learn the workflow without burning a real certificate.
- **Secrets.** Move `APP_NAME` into a `Secret` rendered from `values.yaml`, then graduate to External Secrets Operator pointing at Vault or your cloud secret manager.
- **HPA.** A `HorizontalPodAutoscaler` keyed off CPU; load-test with `hey` or `vegeta` and watch it scale.
- **Argo CD.** Point it at the chart in a git repo and stop running `helm upgrade` by hand.
- **Policy.** Drop in [Kyverno](https://kyverno.io/) or [OPA Gatekeeper](https://open-policy-agent.github.io/gatekeeper/) and write a rule that rejects deployments without resource limits. Then break it intentionally and admire the rejection.

You've now done the boring, fundamental loop most production K8s work boils down to: build → deploy → break → fix → upgrade → rollback. Everything else — service mesh, GitOps, autoscaling, multi-cluster — sits on top of that loop. Get this comfortable first and the rest stops being scary.

<img src="img/authors/geeky.jpg" width="40"/>

{% endraw %}
