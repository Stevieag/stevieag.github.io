---
title:  "Minikube Linkerd"
subtitle: "This is a tutorial start"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/minikube.png"
date:   2024-10-11
tags: minikube linkerd micro service
---

Here is a part of a tutorial I wrote for Linkerd use and a [5 Week DevOps training plan](https://geekyblinder.co.uk/#/2024/11/25/Five-Week-DevOps-Training-Plan).

# Content

Minikube  
Install Linkerd  
Linkerd on your Minikube cluster  
Linkerd features  
- Dashboard          – Traffic management  
- Security           – Monitoring  
- Debugging          – Tap  
- Top  

Cleaning up

# Prerequisites

- Minikube: Ensure you have Minikube installed and running. You can install it from the [official Minikube website](https://minikube.sigs.k8s.io/docs/start/).
- kubectl: Make sure you have kubectl installed and configured to work with your Minikube cluster. [Kubernetes tools website](https://kubernetes.io/docs/tasks/tools/)
- Linkerd: Familiarise yourself with the basics of Linkerd, a service mesh. [Linkerd getting started](https://linkerd.io/2.16/getting-started/)

# Set up Minikube

## Start Minikube

```bash
minikube start
