---
title:  "Helm, Docker, and Kubernetes: A Tiny Training App to Break (and Fix)"
subtitle: "Learning K8s by actually doing something vaguely fun"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/helm-docker-and-kubernetes-a-tiny-training-app-to-break.jpg"
date: 2026-03-01
tags: kubernetes helm docker devops devsecops training
---

## Helm, Docker, and Kubernetes: A Tiny Training App to Break (and Fix)

Let's stop learning Kubernetes by reading error messages in tears at 2 a.m. and instead build a small lab app that you *expect* to break. The goal: deploy a tiny web service with Docker, Kubernetes, and Helm, then deliberately cause the classic problems (CrashLoopBackOff, ImagePullBackOff, bad ports, resource issues) and practise fixing them until it feels routine.

Our project will be a very simple "Hello K8s" HTTP API running in Docker, exposed via a Kubernetes Deployment, Service, and optional Ingress, and managed by a Helm chart. This pattern mirrors most real microservices.

---

## Step 1: Choose a Simple but Realistic Project + How to Build It

**Project:** A tiny "Hello K8s" JSON API.

We'll use **Node.js + Express** (simplest). 

```bash
mkdir hello-k8s-training && cd hello-k8s-training
npm init -y
npm install express
index.js:

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
Test it:

npm start
curl http://localhost:8080/
curl http://localhost:8080/health

PORT=9090 npm start
curl http://localhost:9090/health
Verification: App works, respects PORT, fails cleanly without APP_NAME.

Step 2: Build Docker Image + How to Do It
Create .dockerignore:

.git
node_modules
npm-debug.log
.gitignore
README.md
.env
tests/
Production Dockerfile:

FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM node:20-alpine AS production
RUN addgroup --gid 1001 appgroup && \
    adduser --uid 1001 --system --ingroup appgroup appuser
WORKDIR /app
COPY --from=builder --chown=appuser:appgroup /app/node_modules ./node_modules
COPY --chown=appuser:appgroup . .
USER appuser
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=3s CMD wget --no-verbose --tries=1 --spider http://localhost:8080/health || exit 1
CMD ["npm", "start"]
Build and test:

docker build -t hello-k8s:v1.0.0 .
docker run -p 8080:8080 --rm hello-k8s:v1.0.0
curl http://localhost:8080/health

docker run --rm hello-k8s:v1.0.0 whoami  # appuser ✓
docker images | grep hello-k8s          # <200MB ✓

# Push to your registry
docker tag hello-k8s:v1.0.0 yourusername/hello-k8s:v1.0.0
docker push yourusername/hello-k8s:v1.0.0
Common breaks to practise:

Remove .dockerignore → bloated image (1GB+)

Comment USER appuser → runs as root

Fix each and re‑verify.

Step 3: Deploy Raw Kubernetes + How to Do It
Create k8s/ folder with these files.

k8s/deployment.yaml:

apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-k8s
  namespace: playground
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
      containers:
      - name: hello-k8s
        image: yourusername/hello-k8s:v1.0.0  # ← YOUR IMAGE
        ports:
        - containerPort: 8080
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
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 10
        readinessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 5
k8s/service.yaml:

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
    targetPort: 8080
  type: ClusterIP
Deploy:

kubectl create ns playground
kubectl apply -f k8s/ -n playground
kubectl get pods -n playground  # 3 Running ✓

kubectl run debug --rm -i --tty --image=curlimages/curl -n playground -- \
  curl http://hello-k8s:80/health  # 200 ✓
Breaks to practise:

image: yourusername/hello-k8s:latest → no auto‑update
Fix: use specific tags.

targetPort: 3000 → connection refused
Fix: match containerPort.

Remove env: APP_NAME → CrashLoopBackOff
Fix: add back.

Remove resources → potential scheduling issues in busy clusters
Fix: add requests/limits.

Step 4: Convert to Helm Chart + How to Do It
Create chart structure:

helm create hello-k8s
cd hello-k8s
rm -rf charts/ templates/tests/  # Clean slate
Chart.yaml:

apiVersion: v2
name: hello-k8s
description: Training chart
version: 0.1.0
appVersion: "1.0.0"
values.yaml:

replicaCount: 3

image:
  repository: yourusername/hello-k8s
  tag: "v1.0.0"
  pullPolicy: IfNotPresent

service:
  type: ClusterIP
  port: 80

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
templates/_helpers.tpl:

{{/*
Common labels
*/}}
{{- define "hello-k8s.labels" -}}
helm.sh/chart: {{ .Chart.Name }}-{{ .Chart.Version | replace "+" "_" }}
app.kubernetes.io/name: {{ .Chart.Name }}
{{- end }}
templates/deployment.yaml:

apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Release.Name }}
  namespace: {{ .Release.Namespace }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      {{- include "hello-k8s.labels" . | nindent 6 }}
  template:
    metadata:
      labels:
        {{- include "hello-k8s.labels" . | nindent 8 }}
    spec:
      containers:
      - name: {{ .Chart.Name }}
        image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
        ports:
        - containerPort: 8080
        env:
        {{- range $key, $value := .Values.env }}
        - name: {{ $key }}
          value: {{ $value | quote }}
        {{- end }}
        resources:
{{ toYaml .Values.resources | nindent 10 }}
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: {{ .Values.probes.initialDelaySeconds }}
        readinessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: {{ sub .Values.probes.initialDelaySeconds 5 }}
templates/service.yaml:

apiVersion: v1
kind: Service
metadata:
  name: {{ .Release.Name }}
  namespace: {{ .Release.Namespace }}
spec:
  selector:
    {{- include "hello-k8s.labels" . | nindent 6 }}
  ports:
  - port: {{ .Values.service.port }}
    targetPort: 8080
Test & deploy:

helm lint .
helm template hello-k8s .
helm install hello-k8s . -n playground --create-namespace
kubectl get pods -n playground  # 3 Running ✓
Step 5: Break Everything + Exact Fix Sequences

A. CrashLoopBackOff
Break:

# values.yaml
env:
  APP_NAME: ""
Apply:

helm upgrade hello-k8s . -n playground
kubectl get pods -n playground  # CrashLoopBackOff
Fix exactly:

kubectl logs deployment/hello-k8s -n playground  # "APP_NAME environment variable is required"

# Edit values.yaml:
# env:
#   APP_NAME: "fixed"

helm upgrade hello-k8s . -n playground
kubectl rollout status deploy/hello-k8s -n playground  # Complete ✓

B. ImagePullBackOff
Break:

# values.yaml
image:
  tag: "v9999"
Apply:

helm upgrade hello-k8s . -n playground
kubectl get pods -n playground          # ImagePullBackOff
kubectl describe pod <pod> -n playground  # "manifest unknown"
Fix exactly:

# Edit values.yaml:
# image:
#   tag: "v1.0.0"

helm upgrade hello-k8s . -n playground
kubectl rollout status deploy/hello-k8s -n playground  # Complete ✓

C. Service Port Wrong
Break (if you parameterise targetPort in values later):

# values.yaml
service:
  port: 80
  targetPort: 3000
Assuming templates/service.yaml used it:

ports:
  - port: {{ .Values.service.port }}
    targetPort: {{ .Values.service.targetPort }}
Apply:

helm upgrade hello-k8s . -n playground
kubectl run debug --rm -i --tty --image=curlimages/curl -n playground -- \
  curl http://hello-k8s:80/  # Connection refused

kubectl get endpoints hello-k8s -n playground  # No endpoints or wrong ports
Fix exactly (simplest: hard‑code back to 8080 in template):

ports:
  - port: {{ .Values.service.port }}
    targetPort: 8080
Then:

helm upgrade hello-k8s . -n playground
kubectl get endpoints hello-k8s -n playground  # Endpoints appear ✓

D. Resource Limits Too Low
Break:

# values.yaml
resources:
  limits:
    memory: "32Mi"

Apply:
helm upgrade hello-k8s . -n playground
kubectl get pods -n playground               # OOMKilled or Pending
kubectl describe pod <pod> -n playground     # "Insufficient memory" / OOMKilled
Fix exactly:

# values.yaml
resources:
  limits:
    memory: "128Mi"
Then:
helm upgrade hello-k8s . -n playground
kubectl get pods -n playground  # Running ✓
Step 6: Helm Workflows + Rollback Practice
Safe upgrade pattern:

helm upgrade hello-k8s . -n playground --wait
helm get values hello-k8s -n playground
helm get manifest hello-k8s -n playground
Rollback drill:

# Break something (e.g. bad image tag in values.yaml)
helm upgrade hello-k8s . -n playground

helm history hello-k8s -n playground  # Note REVISION 2
helm rollback hello-k8s 1 -n playground

kubectl get pods -n playground        # Healthy again ✓
Step 7: Clean Up & Next Steps

helm uninstall hello-k8s -n playground
kubectl delete ns playground
You’ve now mastered:

✅ Build production Docker images
✅ Deploy raw Kubernetes manifests
✅ Create working Helm charts
✅ Fix CrashLoopBackOff, ImagePullBackOff, port issues
✅ Safe Helm upgrade/rollback

<img src="img/authors/geeky.jpg" width="40"/>