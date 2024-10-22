---
title:  "Service Mesh DevOps Training!"
subtitle: "Heres one I prepared earlier"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/SerMesh.jpg"
date:   2029-10-22
tags: training mesh service devops istio minikube kind linkerd
---

Here is a training plan I wrote to learn service mesh - I hope its useful

5-Week Training Plan: Service Mesh, Kubernetes, and Related Technologies

> ![](converted/media/image1.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Week 1: Fundamentals and Kubernetes
>
> ![](converted/media/image2.png){width="5.555555555555555e-2in"
> height="4.1666666666666664e-2in"}Day 1-2: Kubernetes Basics and Local
> Development Environments
>
> Kubernetes Architecture and Core Concepts
>
> ![](converted/media/image3.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"} Control Plane Components
>
> ![](converted/media/image4.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"} Node Components
>
> ![](converted/media/image5.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Core Concepts
>
> ![](converted/media/image6.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Additional Components
>
> Local Kubernetes Development Options
>
> ![](converted/media/image7.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"} kind (Kubernetes in Docker)
>
> ![](converted/media/image8.png){width="5.555555555555555e-2in"
> height="5.555555555555555e-2in"}Installation
>
> ![](converted/media/image9.png){width="5.555555555555555e-2in"
> height="5.555555555555555e-2in"}Creating a cluster
>
> ![](converted/media/image10.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"} Minikube
>
> ![](converted/media/image11.png){width="5.555555555555555e-2in"
> height="5.555555555555555e-2in"}Installation
>
> ![](converted/media/image12.png){width="5.555555555555555e-2in"
> height="5.555555555555555e-2in"}Starting a cluster
>
> Practice with Basic Kubernetes Resources
>
> ![](converted/media/image13.png){width="5.555555555555555e-2in"
> height="5.555555555555555e-2in"}Day 3-4: Advanced Kubernetes
>
> ConfigMaps, Secrets, and Volumes
>
> ![](converted/media/image14.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} ConfigMaps
>
> ![](converted/media/image15.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Secrets
>
> ![](converted/media/image16.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"} Volumes
>
> Kubernetes Networking and Ingress
>
> ![](converted/media/image17.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Networking Model
>
> ![](converted/media/image18.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Services
>
> ![](converted/media/image19.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"} Ingress
>
> Kubernetes RBAC and Security Concepts
>
> ![](converted/media/image20.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Role-Based Access Control (RBAC)
>
> ![](converted/media/image21.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Security Contexts
>
> ![](converted/media/image22.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Network Policies
>
> ![](converted/media/image23.png){width="5.555555555555555e-2in"
> height="5.555555555555555e-2in"}Day 5: Working with local K8s options
>
> Docker Images in kind
>
> ![](converted/media/image24.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Building a custom Docker image
>
> ![](converted/media/image25.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Loading the image into kind cluster
>
> ![](converted/media/image26.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"} Limitations and workarounds for
> Docker-in-Docker scenarios
>
> ![](converted/media/image27.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Creating deployments with custom
> images
>
> Working with Images in Minikube
>
> ![](converted/media/image28.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Using the Host Docker Daemon
>
> ![](converted/media/image29.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"} Loading Images into Minikube
>
> ![](converted/media/image30.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"} Creating Deployments with Custom
> Images
>
> ![](converted/media/image31.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Minikube-Specific Features
>
> ![](converted/media/image32.png){width="5.555555555555555e-2in"
> height="5.555555555555555e-2in"}Built-in Docker Registry
>
> ![](converted/media/image33.png){width="5.555555555555555e-2in"
> height="5.555555555555555e-2in"}Direct Image Building
>
> ![](converted/media/image34.png){width="5.555555555555555e-2in"
> height="5.555555555555555e-2in"}Monitoring and Troubleshooting
>
> ![](converted/media/image35.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Cleaning Up
>
> Best Practices
>
> ![](converted/media/image36.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}Week 2: Service Mesh Concepts and
> Python
>
> ![](converted/media/image37.png){width="5.555555555555555e-2in"
> height="5.555555555555555e-2in"}Day 1-2: Service Mesh
>
> Fundamentals
>
> ![](converted/media/image38.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Core concepts of service mesh
>
> ![](converted/media/image39.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Problems service meshes solve
>
> ![](converted/media/image40.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"} Evolution of ingress\
> Service Mesh Architecture
>
> ![](converted/media/image41.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Data Plane
>
> ![](converted/media/image42.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Control Plane\
> Key Features and Use Cases
>
> ![](converted/media/image43.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"} Service Discovery and Load Balancing
>
> ![](converted/media/image44.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Traffic Management
>
> ![](converted/media/image45.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Observability
>
> ![](converted/media/image46.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"} Security
>
> ![](converted/media/image47.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"} Challenges and Best Practices
>
> ![](converted/media/image48.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Performance Considerations
>
> ![](converted/media/image49.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Complexity Management
>
> ![](converted/media/image50.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"} Monitoring and Troubleshooting
>
> ![](converted/media/image51.png){width="5.555555555555555e-2in"
> height="5.555555555555555e-2in"}Day 3-4: Python for Kubernetes\
> Python basics review (if needed)\
> Data Types\
> Python Package Management
>
> ![](converted/media/image52.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"} Installing a package:
>
> ![](converted/media/image53.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Upgrading a package:\
> Python Virtual Environments
>
> ![](converted/media/image54.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Creating a virtual environment:
>
> ![](converted/media/image55.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"} Activating a virtual environment:On
> Unix or MacOS:
>
> ![](converted/media/image56.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Installing packages in a virtual
> environment:
>
> ![](converted/media/image57.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Deactivating a virtual environment:
>
> ![](converted/media/image58.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Creating a requirements file:
>
> ![](converted/media/image59.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"} Installing from a requirements file:\
> Kubernetes Python client library\
> Simple Python scripts for Kubernetes interaction
>
> ![](converted/media/image60.png){width="5.555555555555555e-2in"
> height="5.555555555555555e-2in"}Day 5: Helm Basics\
> Helm\'s Purpose and Architecture\
> Creating and Structure of a Helm Chart\
> Deploying Applications with Helm\
> Advanced Helm Concepts
>
> ![](converted/media/image61.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"} Hooks\
> Dependencies\
> Templating\
> Creating Helm Charts with Python Templates
>
> ![](converted/media/image62.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"} Using Jinja2 for Templating
>
> ![](converted/media/image63.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"} Generating Kubernetes Manifests
> Dynamically
>
> ![](converted/media/image64.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Integrating with CI/CD Pipelines

![](converted/media/image65.png){width="4.1666666666666664e-2in"
height="4.1666666666666664e-2in"}Week 3: Istio Deep Dive

> ![](converted/media/image66.png){width="5.555555555555555e-2in"
> height="5.555555555555555e-2in"}Day 1: Istio Basics\
> Installing Istio on your Kubernetes cluster
>
> ![](converted/media/image67.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Download Istio
>
> ![](converted/media/image68.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Install Istio
>
> ![](converted/media/image69.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"} Enable automatic sidecar injection\
> Istio\'s architecture and core components
>
> ![](converted/media/image70.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Control Plane
>
> ![](converted/media/image71.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Data Plane
>
> ![](converted/media/image72.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"} Addons
>
> Deploying applications with Istio sidecar injection
>
> ![](converted/media/image73.png){width="5.555555555555555e-2in"
> height="5.555555555555555e-2in"}Day 2: Istio Traffic Management\
> Exploring Istio\'s traffic management features\
> Implementing canary deployments and A/B testing\
> Istio\'s load balancing and circuit breaking capabilities
>
> ![](converted/media/image74.png){width="5.555555555555555e-2in"
> height="5.555555555555555e-2in"}Day 3: Istio Security and
> Observability\
> Istio\'s security features
>
> ![](converted/media/image75.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"} mTLS (Mutual TLS)
>
> ![](converted/media/image76.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Authorization Policies\
> Exploring Istio\'s observability stack

+-----------------------+-----------------------+-----------------------+
| ![](vertopa           | ![](vertopal          | > Prometheus          |
| l_c4f4baa402e647588ec | _c4f4baa402e647588ecb |                       |
| b2a507c21de28/media/i | 2a507c21de28/media/im |                       |
| mage77.png){width="5. | age78.png){width="4.1 |                       |
| 555555555555555e-2in" | 666666666666664e-2in" |                       |
| height="5.5           | height="4.16          |                       |
| 55555555555555e-2in"} | 66666666666664e-2in"} |                       |
+=======================+=======================+=======================+
|                       | ![](vertopal          | > Grafana             |
|                       | _c4f4baa402e647588ecb |                       |
|                       | 2a507c21de28/media/im |                       |
|                       | age55.png){width="4.1 |                       |
|                       | 666666666666664e-2in" |                       |
|                       | height="5.5           |                       |
|                       | 55555555555555e-2in"} |                       |
+-----------------------+-----------------------+-----------------------+
|                       | ![](vertopal          | > Kiali               |
|                       | _c4f4baa402e647588ecb |                       |
|                       | 2a507c21de28/media/im |                       |
|                       | age79.png){width="4.1 |                       |
|                       | 666666666666664e-2in" |                       |
|                       | height="4.16          |                       |
|                       | 66666666666664e-2in"} |                       |
+-----------------------+-----------------------+-----------------------+
|                       | ![](vertopal          | > Jaeger/Zipkin       |
|                       | _c4f4baa402e647588ecb |                       |
|                       | 2a507c21de28/media/im |                       |
|                       | age80.png){width="4.1 |                       |
|                       | 666666666666664e-2in" |                       |
|                       | height="4.16          |                       |
|                       | 66666666666664e-2in"} |                       |
+-----------------------+-----------------------+-----------------------+
|                       | > Day 4-5: Deploying  |                       |
|                       | > a Sample            |                       |
|                       | > Application with    |                       |
|                       | > Istio               |                       |
+-----------------------+-----------------------+-----------------------+

> Objective\
> Prerequisites\
> Enable Istio Sidecar Injection\
> Deploy a Sample Application\
> Create a Virtual Service\
> Create a Destination Rule\
> Test the Routing\
> Implement Canary Deployment
>
> ![](converted/media/image81.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}Week 4: Linkerd and Practical
> Applications
>
> ![](converted/media/image82.png){width="5.555555555555555e-2in"
> height="5.555555555555555e-2in"}Day 1: Linkerd Basics\
> Installing Linkerd on your Kubernetes cluster
>
> ![](converted/media/image83.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Install CLI
>
> ![](converted/media/image84.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"} Validate cluster
>
> ![](converted/media/image85.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"} Install Linkerd\
> Linkerd\'s architecture and core components
>
> ![](converted/media/image86.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Control Plane
>
> ![](converted/media/image87.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"} Data Plane
>
> ![](converted/media/image88.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"} Add-ons\
> Linkerd Features\
> Traffic management capabilities\
> Linkerd\'s observability and security features
>
> ![](converted/media/image89.png){width="5.555555555555555e-2in"
> height="5.555555555555555e-2in"}Day 2-4: Hands-on Exercise\
> Deploying and Managing emojivoto with Linkerd

+-----------------------+-----------------------+-----------------------+
| ![](vertopa           | ![](vertopal          | > Deploy the          |
| l_c4f4baa402e647588ec | _c4f4baa402e647588ecb | > emojivoto sample    |
| b2a507c21de28/media/i | 2a507c21de28/media/im | > application         |
| mage90.png){width="5. | age91.png){width="4.1 |                       |
| 555555555555555e-2in" | 666666666666664e-2in" |                       |
| height="5.5           | height="4.16          |                       |
| 55555555555555e-2in"} | 66666666666664e-2in"} |                       |
+=======================+=======================+=======================+
|                       | ![](vertopal          | > Inject Linkerd into |
|                       | _c4f4baa402e647588ecb | > the application     |
|                       | 2a507c21de28/media/im |                       |
|                       | age92.png){width="4.1 |                       |
|                       | 666666666666664e-2in" |                       |
|                       | height="5.5           |                       |
|                       | 55555555555555e-2in"} |                       |
+-----------------------+-----------------------+-----------------------+
|                       | ![](vertopal          | > Observe traffic     |
|                       | _c4f4baa402e647588ecb |                       |
|                       | 2a507c21de28/media/im |                       |
|                       | age93.png){width="4.1 |                       |
|                       | 666666666666664e-2in" |                       |
|                       | height="5.5           |                       |
|                       | 55555555555555e-2in"} |                       |
+-----------------------+-----------------------+-----------------------+
|                       | ![](vertopal          | > Visualize the       |
|                       | _c4f4baa402e647588ecb | > service mesh        |
|                       | 2a507c21de28/media/im |                       |
|                       | age94.png){width="4.1 |                       |
|                       | 666666666666664e-2in" |                       |
|                       | height="4.16          |                       |
|                       | 66666666666664e-2in"} |                       |
+-----------------------+-----------------------+-----------------------+
|                       | ![](vertopal          | > Implement a traffic |
|                       | _c4f4baa402e647588ecb | > split for canary    |
|                       | 2a507c21de28/media/im | > deployment          |
|                       | age95.png){width="4.1 |                       |
|                       | 666666666666664e-2in" |                       |
|                       | height="4.16          |                       |
|                       | 66666666666664e-2in"} |                       |
+-----------------------+-----------------------+-----------------------+
|                       | ![](vertopal          | > Observe the traffic |
|                       | _c4f4baa402e647588ecb | > split               |
|                       | 2a507c21de28/media/im |                       |
|                       | age96.png){width="4.1 |                       |
|                       | 666666666666664e-2in" |                       |
|                       | height="5.5           |                       |
|                       | 55555555555555e-2in"} |                       |
+-----------------------+-----------------------+-----------------------+
|                       | ![](vertopal          | > Gradually increase  |
|                       | _c4f4baa402e647588ecb | > traffic to the new  |
|                       | 2a507c21de28/media/im | > version             |
|                       | age97.png){width="4.1 |                       |
|                       | 666666666666664e-2in" |                       |
|                       | height="5.5           |                       |
|                       | 55555555555555e-2in"} |                       |
+-----------------------+-----------------------+-----------------------+
|                       | ![](vertopal          | > Monitor the canary  |
|                       | _c4f4baa402e647588ecb | > deployment          |
|                       | 2a507c21de28/media/im |                       |
|                       | age67.png){width="4.1 |                       |
|                       | 666666666666664e-2in" |                       |
|                       | height="4.16          |                       |
|                       | 66666666666664e-2in"} |                       |
+-----------------------+-----------------------+-----------------------+
|                       | > Day 5: Service Mesh |                       |
|                       | > Comparison          |                       |
+-----------------------+-----------------------+-----------------------+

> Comparing Istio, Linkerd, and other service mesh solutions
>
> ![](converted/media/image98.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"} Istio
>
> ![](converted/media/image99.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Linkerd
>
> ![](converted/media/image100.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"} Consul Connect
>
> ![](converted/media/image101.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"} NGINX Service Mesh
>
> When to choose one service mesh over another
>
> ![](converted/media/image102.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Week 5: Practical Project\
> Designing and implementing a microservices application\
> Deploying the application using Helm\
> Implementing service mesh features\
> Creating Python scripts for automation
>
> ![](converted/media/image103.png){width="5.555555555555555e-2in"
> height="5.555555555555555e-2in"}Additional Resources and Best
> Practices
>
> ![](converted/media/image104.png){width="5.555555555555555e-2in"
> height="5.555555555555555e-2in"}Tips for Successful Service Mesh
> Adoption
>
> ![](converted/media/image105.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Tools
>
> This document is meant to be a central spring point to allow you to
> understand points to cover yet expects the user to use external
> resources to dig deeper in the points and subjests
>
> Week 1: Fundamentals and Kubernetes
>
> **Day 1-2: Kubernetes Basics and Local Development Environments**
>
> **Kubernetes Architecture and Core Concepts**\
> Kubernetes is a powerful container orchestration platform that manages
> containerized applications across multiple hosts. Its architecture
> consists of two main components: the control plane and worker nodes\
> .

+-----------------------------------+-----------------------------------+
| 1\                                | +------------------------------+  |
| 2\                                | | > +\-\-\-\-\-\-\-            |  |
| 3\                                | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
| 4\                                | | > +\-\-\-\-\-\-\-            |  |
| 5\                                | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
| 6\                                | +==============================+  |
| 7\                                | +------------------------------+  |
| 8\                                |                                   |
| 9\                                | > \| Control Plane \| \| Worker   |
| 10 11 12 13 14                    | > Nodes \|\                       |
|                                   | > \| \| \| \|\                    |
|                                   | > \|                              |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \|                           |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > \| \| kube-apiserver\| \| \| \| |
|                                   | > kubelet \| \|\                  |
|                                   | > \|                              |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \|                           |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > \| \| etcd \| \| \| \|          |
|                                   | > kube-proxy \| \|\               |
|                                   | > \|                              |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \|                           |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > \| \| scheduler \| \| \| \|     |
|                                   | > Container \| \|\                |
|                                   | > \|                              |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \| \| Runtime \| \|\         |
|                                   | > \| \| controller \| \| \|       |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > \| \| manager \| \| \| \|\      |
|                                   | > \|                              |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \| (Multiple nodes) \|       |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > +\-\-\-\-\-\-\-            |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
|                                   | | > +\-\-\-\-\-\-\-            |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **Control Plane Components**
>
> 1\. kube-apiserver: The API server is the front-end for the Kubernetes
> control plane. It exposes the Kubernetes API and handles all
> administrative operations.
>
> 2\. etcd: A consistent and highly-available key-value store used as
> Kubernetes\' backing store for all cluster data.
>
> 3\. kube-scheduler: Responsible for assigning newly created pods to
> nodes based on resource requirements, hardware/software/policy
> constraints, affinity and anti-affinity specifications, and more.
>
> 4\. kube-controller-manager: Runs controller processes that regulate
> the state of the system. These controllers include the node
> controller, replication controller, endpoints controller, and service
> account & token controllers.
>
> 5\. cloud-controller-manager: (Optional) Integrates with underlying
> cloud providers.

+-----------------------------------+-----------------------------------+
| > 1\                              | +------------------------------+  |
| > 2\                              | | > +\-\-\-\-\-\-\-\-\-        |  |
| > 3\                              | | \-\-\-\-\-\-\-\-\-\-\-\-\-\- |  |
| > 4\                              | | \-\-\-\-\-\-\-\-\-\-\-\-\-\- |  |
| > 5                               | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| Control Plane \|        |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \|                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \|                         |  |
|                                   | | > +\-\-                      |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
|                                   | | >                            |  |
|                                   | |  +\-\-\-\-\-\-\-\-\-\-\-\-\- |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
|                                   | | > \|                         |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \| kube-apiserver \| \| |  |
|                                   | | > scheduler \| \|            |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| 6\                                | +------------------------------+  |
| 7\                                | | > \| \| (API Gateway) \| \|  |  |
| 8\                                | | > (Assigns Pods to Nodes) \| |  |
| 9\                                | | > \|                         |  |
| 10 11 12 13 14                    | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \|                         |  |
|                                   | | > +\-\-                      |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
|                                   | | >                            |  |
|                                   | |  +\-\-\-\-\-\-\-\-\-\-\-\-\- |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
|                                   | | > \|                         |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \|                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \|                         |  |
|                                   | | > +\-\-                      |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
|                                   | | >                            |  |
|                                   | |  +\-\-\-\-\-\-\-\-\-\-\-\-\- |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
|                                   | | > \|                         |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \| etcd \| \|           |  |
|                                   | | > controller manager \| \|   |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \| (Cluster State \| \| |  |
|                                   | | > (Maintains Desired State)  |  |
|                                   | | > \| \|                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \| Database) \| \| \|   |  |
|                                   | | > \|                         |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \|                         |  |
|                                   | | > +\-\-                      |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
|                                   | | >                            |  |
|                                   | |  +\-\-\-\-\-\-\-\-\-\-\-\-\- |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
|                                   | | > \|                         |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > +\-\-\-\-\-\-\-\-\-        |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\-\- |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\-\- |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **Node Components**
>
> 1\. kubelet: An agent that runs on each node, ensuring containers are
> running in a Pod.
>
> 2\. kube-proxy: Maintains network rules on nodes, implementing part of
> the Kubernetes Service concept.
>
> 3\. Container runtime: Software responsible for running containers
> (e.g., Docker, containerd, CRI-O).
>
> 4\. Pods: The smallest deployable units in Kubernetes, consisting of
> one or more containers

+-----------------------------------+-----------------------------------+
| 1\                                | > +\-                             |
| 2\                                | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
| 3\                                | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- |
| 4\                                | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+\ |
| 5\                                | > \| Worker Node \|\              |
| 6\                                | > \|                              |
| 7\                                | > +\-\-\-\-\                      |
| 8\                                | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
| 9\                                | > +\-\-\-\-\                      |
| 10 11 12 13 14 15 16 17 18 19     | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > \| \| kubelet \| \| kube-proxy  |
|                                   | > \| \|\                          |
|                                   | > \| \| (Node Agent) \| \|        |
|                                   | > (Network Proxy) \| \|\          |
|                                   | > \|                              |
|                                   | > +\-\-\-\-\                      |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > +\-\-\-\-\                      |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > \| \|\                          |
|                                   | > \|                              |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\-     |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > \| \| Container Runtime \| \|\  |
|                                   | > \| \| (e.g., Docker,            |
|                                   | > containerd) \| \|\              |
|                                   | > \|                              |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\-     |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > \| \|\                          |
|                                   | > \|                              |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\-     |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > \| \| Pods \| \|\               |
|                                   | > \| \| +\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\--+       |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\--+ \|    |
|                                   | > \|\                             |
|                                   | > \| \| \| Container \| \|        |
|                                   | > Container \| \| Container \| \| |
|                                   | > \|\                             |
|                                   | > \| \| +\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\--+       |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\--+ \|    |
|                                   | > \|\                             |
|                                   | > \|                              |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\-     |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > +\                              |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **Core Concepts**
>
> 1\. Pods: The smallest deployable units in Kubernetes, consisting of
> one or more containers.
>
> 2\. Services: An abstraction that defines a logical set of Pods and a
> policy by which to access them.
>
> 3\. Deployments: Provide declarative updates for Pods and ReplicaSets.
>
> 4\. Namespaces: Virtual clusters backed by the same physical cluster,
> providing a way to divide cluster resources between multiple users.
>
> **Additional Components**
>
> These components include the Dashboard (a web-based UI), cluster-level
> logging, container resource monitoring, and network plugins.

+-----------------------------------+-----------------------------------+
| > 1\                              | +------------------------------+  |
| > 2\                              | | > +\-\-\-\-\-\-\-\-\-\-\-\-  |  |
| > 3\                              | | \-\-\-\-\-\-\-\-\-\-\-\-\-\- |  |
| > 4\                              | | \-\-\-\-\-\-\-\-\-\-\-\-\-\- |  |
| > 5\                              | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
| > 6\                              | +==============================+  |
| > 7\                              | +------------------------------+  |
| > 8\                              |                                   |
| > 9                               | +------------------------------+  |
|                                   | | > \| Additional Components   |  |
|                                   | | > \|                         |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \|                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \|                         |  |
|                                   | | > +\-\-\-\-\-\-\-            |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
|                                   | | > +\-\-\-\-\-\-\-\-\-\-\-    |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
|                                   | | > \|                         |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \| Dashboard \| \|      |  |
|                                   | | > Cluster-level Logging \|   |  |
|                                   | | > \|                         |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \| (Web UI) \|          |  |
|                                   | | > \|(Centralized Log         |  |
|                                   | | > Storage)\| \|              |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \|                         |  |
|                                   | | > +\-\-\-\-\-\-\-            |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
|                                   | | > +\-\-\-\-\-\-\-\-\-\-\-    |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
|                                   | | > \|                         |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \|                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \|                         |  |
|                                   | | > +\-\-\-\-\-\-\-            |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
|                                   | | > +\-\-\-\-\-\-\-\-\-\-\-    |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
|                                   | | > \|                         |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 10 11 12 13                     | > \| \| Monitoring \| \| Network  |
|                                   | > Plugins \| \|\                  |
|                                   | > \| \|(Resource Monitoring)\| \| |
|                                   | > (Implement CNI) \| \|\          |
|                                   | > \|                              |
|                                   | > +\-\-\-\-\                      |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > +\-\-\-\-\-\-\-\-\              |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > +\-\-\-\-\                      |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **Local Kubernetes Development Options**
>
> **kind (Kubernetes in Docker)**\
> kind is a tool for running local Kubernetes clusters using Docker
> container \"nodes\". It\'s designed for testing Kubernetes itself, but
> can be used for local development or CI.
>
> **Installation**

  -----------------------------------------------------------------------
  go install sigs.k8s.io/kind@v0.24.0
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

> \# Or for macOS users

  -----------------------------------------------------------------------
  brew install kind
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

> **Creating a cluster**

  -----------------------------------------------------------------------
  kind create cluster
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

> Advantages of kind:
>
> 1\. Lightweight and fast to start up, making it ideal for rapid
> development cycles.
>
> 2\. Supports multi-node clusters, allowing you to simulate more
> complex environments.
>
> 3\. Runs Kubernetes inside Docker containers, which is efficient and
> consistent across different host systems.
>
> 4\. Ideal for testing and CI/CD pipelines due to its speed and
> reproducibility
>
> **Minikube**\
> Minikube is a tool that makes it easy to run Kubernetes locally. It
> runs a single-node Kubernetes cluster inside a VM on your laptop.
>
> **Installation**\
> \# For macOS

  -----------------------------------------------------------------------
  brew install minikube
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

> \# For other systems, refer to the official documentation\
> **Starting a cluster**

  -----------------------------------------------------------------------
  minikube start
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

> Advantages of Minikube:
>
> 1\. More established and feature-rich, with a large community and
> extensive documentation. 2. Supports multiple hypervisors (VirtualBox,
> HyperKit, etc.), allowing flexibility in your local setup. 3. Provides
> built-in addons for common services, making it easy to enable
> additional functionality. 4. Offers a dashboard for visual management
> of your cluster.
>
> **Practice with Basic Kubernetes Resources**\
> To solidify your understanding, practice creating and managing these
> basic Kubernetes resources in both kind and Minikube environments:
>
> 1\. Pods: The smallest deployable units in Kubernetes.
>
> 2\. Deployments: Manage the deployment and scaling of a set of Pods.\
> 3. Services: Expose your application to network traffic.
>
> Example commands:
>
> \# Create a deployment

  -----------------------------------------------------------------------
  kubectl create deployment nginx \--image=nginx
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

> \# Expose the deployment as a service

  -----------------------------------------------------------------------
  kubectl expose deployment nginx \--port=80 \--type=LoadBalancer
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

![](converted/media/image109.png){width="3.640277777777778in"
height="1.4011898512685914in"}![](converted/media/image110.png){width="4.1666666666666664e-2in"
height="4.1666666666666664e-2in"}

> \# List pods

  -----------------------------------------------------------------------
  kubectl get pods
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

> \# List services

  -----------------------------------------------------------------------
  kubectl get services
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

> By thoroughly understanding these concepts and practicing with both
> kind and Minikube, you\'ll build a solid foundation for working with
> Kubernetes in various environments.
>
> You will need to search so that you can view the nginx on your
> localhost\
> eg: minikube external ip expose command
>
> You will ultimately see the nginx default banner
>
> **Day 3-4: Advanced Kubernetes**
>
> **ConfigMaps, Secrets, and Volumes**

+-----------------------------------+-----------------------------------+
| 1\                                | > +\-\-                           |
| 2\                                | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
| 3\                                | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- |
| 4\                                | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+\ |
| 5\                                | > \| Pod \|\                      |
| 6\                                | > \| \|\                          |
| 7\                                | > \|                              |
| 8\                                | >                                 |
| 9\                                | +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
| 10 11 12 13 14 15 16 17 18 19 20  | > +\-\-\-\-\-\-\-\-\-\-\          |
| 21 22                             | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > \| \| Container \| \| Volume    |
|                                   | > Mounts \| \|\                   |
|                                   | > \| \| (Application) \| \|       |
|                                   | > /etc/config -\> ConfigMap \|    |
|                                   | > \|\                             |
|                                   | > \| \| \| \| /etc/secrets -\>    |
|                                   | > Secret \| \|\                   |
|                                   | > \|                              |
|                                   | >                                 |
|                                   | +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\          |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > \| \|\                          |
|                                   | > \|                              |
|                                   | >                                 |
|                                   | +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\          |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > \| \| Environment \| \|         |
|                                   | > ConfigMap \| \|\                |
|                                   | > \| \| Variables \| \| \| \|\    |
|                                   | > \| \| (from ConfigMap\| \|      |
|                                   | > key1: value1 \| \|\             |
|                                   | > \| \| and Secret) \| \| key2:   |
|                                   | > value2 \| \|\                   |
|                                   | > \|                              |
|                                   | >                                 |
|                                   | +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\          |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > \| \|\                          |
|                                   | > \|                              |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\          |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > \| \| Secret \| \|\             |
|                                   | > \| \| username: base64(user) \| |
|                                   | > \|\                             |
|                                   | > \| \| password: base64(pass) \| |
|                                   | > \|\                             |
|                                   | > \|                              |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\          |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > +\-\                            |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **ConfigMaps**

+-----------------------------------+-----------------------------------+
| ![](vertopal_c4f4baa402e64758     | > **ConfigMaps**                  |
| 8ecb2a507c21de28/media/image106.p |                                   |
| ng){width="0.11388779527559055in" |                                   |
| height="0.11388888888888889in"}   |                                   |
+===================================+===================================+
| ![](vertopal_c4f4baa402e647588e   | > Used to store non-confidential  |
| cb2a507c21de28/media/image107.png | > data in key-value pairs.        |
| ){width="4.1666666666666664e-2in" | >                                 |
| height="4.1666666666666664e-2in"} | > Can be consumed as environment  |
|                                   | > variables, command-line         |
| ![](vertopal_c4f4baa402e647588e   | > arguments, or configuration     |
| cb2a507c21de28/media/image108.png | > files in a volume.              |
| ){width="4.1666666666666664e-2in" |                                   |
| height="5.555555555555555e-2in"}  |                                   |
+-----------------------------------+-----------------------------------+

> ![](converted/media/image111.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Example creation:

  ----------------------------------------------------------------------------------------------------------------------------------------
                                                                                                      kubectl create configmap name
                                                                                                      \--from-literal=name=\'{\"first\":
                                                                                                      \"John\", \"second\": \"Doe\"}\'
  --------------------------------------------------------------------------------------------------- ------------------------------------
  ![](converted/media/image112.png){width="4.1666666666666664e-2in"   Example extract
  height="4.1666666666666664e-2in"}                                                                   

  ----------------------------------------------------------------------------------------------------------------------------------------

> kubectl get configmap name -o jsonpath=\'{.dataname}\' or kubectl get
> configmap name3 -o json \| jq -r \'.data.name\'\|

  -----------------------------------------------------------------------
  jq -r .first
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

> **Secrets**

+-----------------------------------+-----------------------------------+
| ![](vertopal_c4f4baa402e64758     | > **Managing Secrets using        |
| 8ecb2a507c21de28/media/image106.p | > kubectl**                       |
| ng){width="0.11388779527559055in" |                                   |
| height="0.11388888888888889in"}   |                                   |
+===================================+===================================+
| ![](vertopal_c4f4baa402e647588e   | > Similar to ConfigMaps but       |
| cb2a507c21de28/media/image113.png | > intended for confidential data. |
| ){width="4.1666666666666664e-2in" | >                                 |
| height="4.1666666666666664e-2in"} | > Base64 encoded by default (not  |
|                                   | > encrypted).                     |
| ![](vertopal_c4f4baa402e647588e   | >                                 |
| cb2a507c21de28/media/image114.png | > Can be mounted as files or      |
| ){width="4.1666666666666664e-2in" | > exposed as environment          |
| height="5.555555555555555e-2in"}  | > variables.                      |
|                                   | >                                 |
| ![](vertopal_c4f4baa402e647588e   | > Example creation:               |
| cb2a507c21de28/media/image115.png |                                   |
| ){width="4.1666666666666664e-2in" |                                   |
| height="5.555555555555555e-2in"}  |                                   |
|                                   |                                   |
| ![](vertopal_c4f4baa402e647588e   |                                   |
| cb2a507c21de28/media/image116.png |                                   |
| ){width="4.1666666666666664e-2in" |                                   |
| height="4.1666666666666664e-2in"} |                                   |
+-----------------------------------+-----------------------------------+

  ---------------------------------------------------------------------------------------------------------------------------------------
                                                                                                      kubectl create secret generic
                                                                                                      user-pass
                                                                                                      \--from-literal=username=john
                                                                                                      \--from-literal=password=s3cr3t
  --------------------------------------------------------------------------------------------------- -----------------------------------
  ![](converted/media/image117.png){width="4.1666666666666664e-2in"   Example extract:
  height="4.1666666666666664e-2in"}                                                                   

  ---------------------------------------------------------------------------------------------------------------------------------------

  -----------------------------------------------------------------------
  kubectl get secrets user-pass -o json \| jq -r .data.password \| base64
  -D
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

> **Volumes**

+-----------------------------------+-----------------------------------+
| ![](vertopal_c4f4baa402e64758     | > **Volumes**                     |
| 8ecb2a507c21de28/media/image106.p |                                   |
| ng){width="0.11388779527559055in" |                                   |
| height="0.11388779527559055in"}   |                                   |
+===================================+===================================+
| ![](vertopal_c4f4baa402e647588e   | > Provide persistent storage for  |
| cb2a507c21de28/media/image118.png | > pods.                           |
| ){width="4.1666666666666664e-2in" | >                                 |
| height="5.555555555555555e-2in"}  | > Types include emptyDir,         |
|                                   | > hostPath, nfs, and cloud        |
| ![](vertopal_c4f4baa402e647588e   | > provider-specific options.      |
| cb2a507c21de28/media/image119.png | >                                 |
| ){width="4.1666666666666664e-2in" | > PersistentVolumes (PV) and      |
| height="4.1666666666666664e-2in"} | > PersistentVolumeClaims (PVC)    |
|                                   | > provide a way to use storage    |
| ![](vertopal_c4f4baa402e647588e   | > resources in a pod-independent  |
| cb2a507c21de28/media/image120.png | > manner.                         |
| ){width="4.1666666666666664e-2in" | >                                 |
| height="4.1666666666666664e-2in"} | > Example                         |
|                                   |                                   |
| ![](vertopal_c4f4baa402e647588e   |                                   |
| cb2a507c21de28/media/image121.png |                                   |
| ){width="4.1666666666666664e-2in" |                                   |
| height="5.555555555555555e-2in"}  |                                   |
+-----------------------------------+-----------------------------------+

> Create a configmap to hold your var

  -----------------------------------------------------------------------
  kubectl create configmap config-vol \--from-literal=log_level=debug
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

> Now create a pod with a running container that mounts the configmap as
> a var

+-----------------------------------+-----------------------------------+
| 1\                                | > cat \<\<EOF \| k apply -f -\    |
| 2\                                | > apiVersion: v1\                 |
| 3\                                | > kind: Pod\                      |
| 4\                                | > metadata:\                      |
| 5\                                | > name: configmap-pod\            |
| 6\                                | > spec:\                          |
| 7\                                | > containers:\                    |
| 8\                                | > - name: test\                   |
| 9\                                | > image: busybox:1.28\            |
| 10 11 12 13 14 15 16 17 18 19 20  | > command: \[\'sh\', \'-c\',      |
| 21                                | > \'echo \"The app is running!\"  |
|                                   | > && tail -f /dev/null\'\]        |
|                                   | > volumeMounts:\                  |
|                                   | > - name: config-vol\             |
|                                   | > mountPath: /etc/config\         |
|                                   | > volumes:\                       |
|                                   | > - name: config-vol\             |
|                                   | > configMap:\                     |
|                                   | > name: config-vol \# Corrected   |
|                                   | > to match the ConfigMap name\    |
|                                   | > items:\                         |
|                                   | > - key: log_level\               |
|                                   | > path: log_level\                |
|                                   | > EOF                             |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> Run a command to extract the var held at this point

  -----------------------------------------------------------------------
  kubectl exec -it configmap-pod \-- cat /etc/config/log_level
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

> OR\
> Exec into the container

  -----------------------------------------------------------------------
  kubectl exec -it configmap-pod \-- sh
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

> Here you can navigate to the location

  -----------------------------------------------------------------------
  cd etc/config
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

> ls \< here you should see log_level

  -----------------------------------------------------------------------
  cat log_level
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

  -----------------------------------------------------------------------
  debug/etc/config
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

> To give a cleave output

  -----------------------------------------------------------------------
  cat log_level ; echo
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

> This could easily be a static volume location as opposed to a
> configmap

+-----------------------------------+-----------------------------------+
| 1\                                | > +\-                             |
| 2\                                | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
| 3\                                | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- |
| 4\                                | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+\ |
| 5\                                | > \| Node \|\                     |
| 6\                                | > \|                              |
| 7\                                | > +\-\-\-\                        |
| 8\                                | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
| 9\                                | > +\-\-\-\-\-\                    |
| 10 11 12 13 14 15 16              | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > \| \| Pod \| \| Persistent      |
|                                   | > Volume \| \|\                   |
|                                   | > \| \|                           |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\--+   |
|                                   | > \| \| \| \|\                    |
|                                   | > \| \| \| Container \| \| \|     |
|                                   | > (Network File Ststem,\| \|\     |
|                                   | > \| \| \| /Volume Mount\| \| \|  |
|                                   | > Cloud Storage, etc. \| \|\      |
|                                   | > \| \|                           |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\--+   |
|                                   | > \| \| \| \|\                    |
|                                   | > \|                              |
|                                   | > +\-\-\-\                        |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > +\-\-\-\-\-\                    |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > \| \|\                          |
|                                   | > \|                              |
|                                   | > +\-\-\-\                        |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > +\-\-\-\-\-\                    |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > \| \| Empty Dir Volume \| \|    |
|                                   | > Host Path Volume \| \|\         |
|                                   | > \| \|(Temporary Storage) \| \|  |
|                                   | > (Node\'s file system) \| \|\    |
|                                   | > \|                              |
|                                   | > +\-\-\-\                        |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > +\-\-\-\-\-\                    |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > \| \|\                          |
|                                   | > +\                              |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **Kubernetes Networking and Ingress**
>
> Networking is a large area of K8s and is the largest challenge or
> concept to learn.

+-----------------------------------+-----------------------------------+
| 1\                                | > External Traffic\               |
| 2\                                | > \|\                             |
| 3\                                | > v\                              |
| 4\                                | > +\-\-\-\-\-\-\-                 |
| 5\                                | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+\ |
| 6\                                | > \| Load Balancer \|\            |
| 7\                                | > +\-\-\-\-\-\-\-                 |
| 8\                                | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+\ |
| 9\                                | > \|\                             |
| 10\                               | > v\                              |
| 11\                               | > +\-\-\-\-\-\-\-\-\-             |
| 12\                               | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+\ |
| 13\                               | > \| Ingress Controller \|\       |
| 14\                               | > \| (e.g., NGINX, Traefik) \|\   |
| 15\                               | > +\-\-\-\-\-\-\-\-\-             |
| 16\                               | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+\ |
| 17\                               | > \| \|\                          |
| 18\                               | > v v\                            |
| 19\                               | >                                 |
| 20\                               | +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
| 21\                               | > +                               |
| 22\                               | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+\ |
| 23\                               | > \| Ingress Rule 1 \| \| Ingress |
| 24\                               | > Rule 2 \|\                      |
| 25\                               | > \| host: foo.com \| \| host:    |
| 26                                | > bar.com \|\                     |
|                                   | > \| path: /app1 \| \| path:      |
|                                   | > /app2 \|\                       |
|                                   | >                                 |
|                                   | +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > +                               |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+\ |
|                                   | > \| \|\                          |
|                                   | > v v\                            |
|                                   | > +\-\-\-\-\-\                    |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > +\-\-\-\-\-\-                   |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+\ |
|                                   | > \| Service 1 \| \| Service 2    |
|                                   | > \|\                             |
|                                   | > \| (ClusterIP/NodePort) \| \|   |
|                                   | > (ClusterIP/NodePort) \|\        |
|                                   | > +\-\-\-\-\-\                    |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > +\-\-\-\-\-\-                   |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+\ |
|                                   | > \| \| \| \|                     |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 27\                             | > v v v v\                        |
| > 28\                             | > +\-\-\-\-\-\-\--+               |
| > 29\                             | > +\-\-\-\-\-\-\--+               |
| > 30\                             | > +\-\-\-\-\-\-\--+               |
| > 31\                             | > +\-\-\-\-\-\-\--+\              |
| > 32\                             | > \| Pod 1A \| \| Pod 1B \| \|    |
| > 33\                             | > Pod 2A \| \| Pod 2B \|\         |
| > 34\                             | > +\-\-\-\-\-\-\--+               |
| > 35\                             | > +\-\-\-\-\-\-\--+               |
| > 36\                             | > +\-\-\-\-\-\-\--+               |
| > 37\                             | > +\-\-\-\-\-\-\--+\              |
| > 38\                             | > \| \| \| \|\                    |
| > 39\                             | > v v v v\                        |
| > 40\                             | > +\-\-\-\-\-\-\-\-\-\-\-\        |
| > 41                              | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+\ |
|                                   | > \| Container Network \|\        |
|                                   | > \| (e.g., Flannel, Calico,      |
|                                   | > Weave, Cilium) \|\              |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\        |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+\ |
|                                   | > \|\                             |
|                                   | > v\                              |
|                                   | > +                               |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+\ |
|                                   | > \| Node Network \|\             |
|                                   | >                                 |
|                                   | +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> This diagram illustrates:
>
> 1\. External traffic enters through a Load Balancer.
>
> 2\. The Ingress Controller (e.g., NGINX or Traefik) receives the
> traffic and processes it based on Ingress Rules.
>
> 3\. Ingress Rules define how traffic should be routed based on
> hostnames and paths.
>
> 4\. Services (ClusterIP or NodePort) receive traffic from the Ingress
> Controller and distribute it to Pods.
>
> 5\. Pods contain the application containers and are distributed across
> nodes.
>
> 6\. The Container Network (implemented by CNI plugins like Flannel,
> Calico, Weave, or Cilium) enables communication between Pods across
> nodes.
>
> 7\. The Node Network connects all nodes in the cluster.
>
> **Networking Model**

+-----------------------------------+-----------------------------------+
| 1\                                | > +\-\-\-\-                       |
| 2\                                | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
| 3\                                | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
| 4\                                | > +\-\-\-\-                       |
| 5\                                | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
| 6\                                | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
| 7\                                | > \| Node 1 \| \| Node 2 \| \|    |
| 8\                                | > +\-\-\-\-\-\-\-\-\-\-\-\-\--+   |
| 9\                                | > +\-\-\-\-\-\-\-\-\-\-\-\-\--+   |
| 10 11 12 13                       | > \| \|                           |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\--+   |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\--+   |
|                                   | > \| \| \| Pod1 \| \| Pod2 \| \|  |
|                                   | > \| \| Pod3 \| \| Pod4 \| \| \|  |
|                                   | > \| IP: 10.1.1 \| \| IP: 10.1.2  |
|                                   | > \| \| \| \| IP: 10.2.1 \| \|    |
|                                   | > IP: 10.2.2 \| \| \|             |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\--+   |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\--+   |
|                                   | > \| \|                           |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\--+   |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\--+   |
|                                   | > \| \| \| \| \| \| \| \| Virtual |
|                                   | > Ethernet Bridge \| \| Virtual   |
|                                   | > Ethernet Bridge \| \| \| \| \|  |
|                                   | > \| \|                           |
|                                   | > +\-\-\-\                        |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\--\|\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > +\-\-\-\                        |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\--\|\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \|\                          |
|                                   | > \| Cluster Network Fabric \|\   |
|                                   | > +\-\-\-\-\-\-\-\-\-             |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 14                              |                                   |
+===================================+===================================+
| ![](vertopal_c4f4baa402e647588e   | > Pod IP Addressing: Each pod is  |
| cb2a507c21de28/media/image122.png | > assigned a unique IP address    |
| ){width="4.1666666666666664e-2in" | > from the cluster-wide CIDR      |
| height="5.555555555555555e-2in"}  | > range. This ensures that every  |
|                                   | > pod has a                       |
+-----------------------------------+-----------------------------------+

> distinct identity within the cluster.
>
> ![](converted/media/image123.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Direct Communication: Pods can
> communicate directly with each other using their assigned IP
> addresses, without the need for Network Address Translation (NAT) or
> port mapping.
>
> ![](converted/media/image124.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Intra-Node Communication: For pods on
> the same node, communication occurs through a virtual ethernet bridge.
> This allows for efficient local traffic routing.
>
> ![](converted/media/image125.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Inter-Node Communication: When pods
> on different nodes need to communicate, the cluster-level network
> layer handles routing based on the pod IP ranges assigned to each
> node.
>
> ![](converted/media/image126.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}CNI Plugins: Container Network
> Interface (CNI) plugins implement the actual networking, ensuring
> proper routing and connectivity across the cluster. Popular CNI
> plugins include Calico, Flannel, and Weave.
>
> This architecture simplifies application design and deployment, as
> pods can be treated similarly to VMs or physical hosts from a
> networking perspective.
>
> **Services**

+-----------------------------------+-----------------------------------+
| 1\                                | > +\-\-\-\-\-\-\-\-\-             |
| 2\                                | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+\ |
| 3\                                | > \| Service \|\                  |
| 4\                                | > \| (ClusterIP/NodePort) \|\     |
| 5\                                | > \| IP: 10.0.0.1 \|\             |
| 6\                                | > +\-\-\-\-\-\-\-\-\-             |
| 7\                                | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+\ |
| 8\                                | > \|\                             |
| 9\                                | > Load Balancing\                 |
| 10 11 12 13 14 15 16 17 18 19     | > \|\                             |
|                                   | > +\-\-\-                         |
|                                   | \-\-\-\-\--+\-\-\-\-\-\-\-\-\--+\ |
|                                   | > \| \| \|\                       |
|                                   | > +\-\-\-\-\-\-\-\-\-\--+ \|      |
|                                   | > +\-\-\-\-\-\-\-\-\-\--+\        |
|                                   | > \| Pod 1 \| \| \| Pod 2 \|\     |
|                                   | > \| IP:10.1 \| \| \| IP:10.2 \|\ |
|                                   | > +\-\-\-\-\-\-\-\-\-\--+ \|      |
|                                   | > +\-\-\-\-\-\-\-\-\-\--+\        |
|                                   | > \|\                             |
|                                   | > +\-\-\-\-\-\-\-\-\-\--+\        |
|                                   | > \| Pod 3 \|\                    |
|                                   | > \| IP:10.3 \|\                  |
|                                   | > +\-\-\-\-\-\-\-\-\-\--+         |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> 20
>
> Kubernetes Services provide a stable network endpoint for a set of
> Pods, enabling reliable communication within the cluster. Services
> abstract the underlying Pod network, offering a consistent way to
> access applications regardless of Pod lifecycle changes. Key aspects
> of Kubernetes Services include:

+-----------------------+-----------------------+-----------------------+
| ![](vertopal_         | > Service Types:      |                       |
| c4f4baa402e647588ecb2 |                       |                       |
| a507c21de28/media/ima |                       |                       |
| ge127.png){width="4.1 |                       |                       |
| 666666666666664e-2in" |                       |                       |
| height="5.5           |                       |                       |
| 55555555555555e-2in"} |                       |                       |
|                       |                       |                       |
| ![](vertopal_         |                       |                       |
| c4f4baa402e647588ecb2 |                       |                       |
| a507c21de28/media/ima |                       |                       |
| ge128.png){width="4.1 |                       |                       |
| 666666666666664e-2in" |                       |                       |
| height="4.16          |                       |                       |
| 66666666666664e-2in"} |                       |                       |
+=======================+=======================+=======================+
|                       | ![](vertopal          | > ClusterIP           |
|                       | _c4f4baa402e647588ecb | > (default): Exposes  |
|                       | 2a507c21de28/media/im | > the service on an   |
|                       | age129.png){width="5. | > internal IP in the  |
|                       | 555555555555555e-2in" | > cluster             |
|                       | height="5.5           |                       |
|                       | 55555555555555e-2in"} |                       |
+-----------------------+-----------------------+-----------------------+
|                       | ![](vertopal          | > NodePort: Exposes   |
|                       | _c4f4baa402e647588ecb | > the service on each |
|                       | 2a507c21de28/media/im | > node\'s IP at a     |
|                       | age130.png){width="5. | > static port         |
|                       | 555555555555555e-2in" |                       |
|                       | height="5.5           |                       |
|                       | 55555555555555e-2in"} |                       |
+-----------------------+-----------------------+-----------------------+
|                       | ![](vertopal          | > LoadBalancer:       |
|                       | _c4f4baa402e647588ecb | > Exposes the service |
|                       | 2a507c21de28/media/im | > externally using a  |
|                       | age131.png){width="5. | > cloud provider\'s   |
|                       | 555555555555555e-2in" | > load balancer       |
|                       | height="5.5           |                       |
|                       | 55555555555555e-2in"} |                       |
+-----------------------+-----------------------+-----------------------+
|                       | ![](vertopal          | > ExternalName: Maps  |
|                       | _c4f4baa402e647588ecb | > the service to the  |
|                       | 2a507c21de28/media/im | > contents of the     |
|                       | age132.png){width="5. | > externalName field  |
|                       | 555555555555555e-2in" |                       |
|                       | height="5.5           |                       |
|                       | 55555555555555e-2in"} |                       |
+-----------------------+-----------------------+-----------------------+
|                       | ![](vertopal          | > Headless: Allows    |
|                       | _c4f4baa402e647588ecb | > direct access to    |
|                       | 2a507c21de28/media/im | > individual pod IPs  |
|                       | age133.png){width="5. |                       |
|                       | 555555555555555e-2in" |                       |
|                       | height="5.5           |                       |
|                       | 55555555555555e-2in"} |                       |
+-----------------------+-----------------------+-----------------------+
|                       | > Service Discovery:  |                       |
|                       | > Services can be     |                       |
|                       | > discovered through  |                       |
|                       | > DNS or environment  |                       |
|                       | > variables, making   |                       |
|                       | > it easy for         |                       |
|                       | > applications to     |                       |
|                       | > find and            |                       |
+-----------------------+-----------------------+-----------------------+

> communicate with each other.
>
> ![](converted/media/image134.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Load Balancing: Services
> automatically distribute incoming traffic across all backend pods,
> ensuring even load distribution.
>
> ![](converted/media/image135.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}Stable Endpoints: Services provide
> stable IP addresses and DNS names for groups of pods, abstracting away
> the dynamic nature of pod lifecycles.
>
> ![](converted/media/image136.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}Cloud Integration: Services can
> integrate with cloud provider load balancers for external access,
> simplifying the process of exposing applications to the internet.
>
> Services play a crucial role in microservices architectures,
> facilitating seamless communication between application components and
> enabling scalability and resilience in Kubernetes environments
>
> **Ingress**

+-----------------------------------+-----------------------------------+
| > 1\                              | +------------------------------+  |
| > 2\                              | | > External Traffic           |  |
| > 3\                              | +==============================+  |
| > 4\                              | +------------------------------+  |
| > 5\                              |                                   |
| > 6                               | +------------------------------+  |
|                                   | | > \|                         |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > +\-\-\-\-\--v\-\-\-\-\--+  |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| Ingress \|              |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| Controller \|           |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > +\-\-\-\-\--+\-\-\-\-\--+  |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| 7\                                | > \|\                             |
| 8\                                | > +\-\-\-\-\--v\-\-\-\-\--+\      |
| 9\                                | > \| Ingress \|\                  |
| 10\                               | > \| Rules \|\                    |
| 11\                               | > +\-\-\-\-\--+\-\-\-\-\--+\      |
| 12\                               | > \|\                             |
| 13\                               | > +\-\-\-\-\--v\-\-\-\-\--+\      |
| 14\                               | > \| Services \|\                 |
| 15\                               | > +\-\-\-\-\--+\-\-\-\-\--+\      |
| 16\                               | > \|\                             |
| 17\                               | > +\-\-\--v\-\-\--+\              |
| 18\                               | > \| Pods \|\                     |
| 19                                | > +\-\-\-\-\-\-\-\--+             |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------------------------------------------+
| > 20                                                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

> Kubernetes Ingress is an API object that manages external access to
> services within a cluster, providing HTTP and HTTPS routing rules. It
> acts as a single entry point for incoming traffic, simplifying the
> exposure of multiple services through a unified interface. Key
> features of Ingress include:

+-----------------------------------+-----------------------------------+
| ![](vertopal_c4f4baa402e647588e   | > Traffic Routing: Ingress can    |
| cb2a507c21de28/media/image137.png | > route traffic based on URL      |
| ){width="4.1666666666666664e-2in" | > paths, hostnames, or other      |
| height="4.1666666666666664e-2in"} | > criteria, allowing for complex  |
|                                   | > routing scenarios. SSL/TLS      |
| ![](vertopal_c4f4baa402e647588e   | > Termination: Ingress can handle |
| cb2a507c21de28/media/image138.png | > SSL/TLS termination, offloading |
| ){width="4.1666666666666664e-2in" | > this responsibility from        |
| height="4.1666666666666664e-2in"} | > individual services.            |
|                                   | >                                 |
| ![](vertopal_c4f4baa402e647588e   | > Load Balancing: Ingress can     |
| cb2a507c21de28/media/image139.png | > distribute traffic across       |
| ){width="4.1666666666666664e-2in" | > multiple backend services,      |
| height="4.1666666666666664e-2in"} | > acting as a load balancer.      |
|                                   | >                                 |
| ![](vertopal_c4f4baa402e647588e   | > Name-based Virtual Hosting:     |
| cb2a507c21de28/media/image140.png | > Ingress supports routing to     |
| ){width="4.1666666666666664e-2in" | > different services based on the |
| height="4.1666666666666664e-2in"} | > hostname, enabling multiple     |
|                                   | > applications to                 |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> share a single IP address.
>
> ![](converted/media/image141.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Ingress Controller: Ingress requires
> an Ingress Controller to function, which implements the actual routing
> and load balancing logic. Popular Ingress Controllers include NGINX,
> Traefik, and Istio.
>
> By consolidating routing rules into a single resource, Ingress
> simplifies network management and reduces the need for multiple load
> balancers, making it an essential component for production-ready
> Kubernetes deployments.
>
> Examples:\
> Create a simple web application

+-----------------------------------+-----------------------------------+
| 1\                                | > cat \<\<EOF \| k apply -f -\    |
| 2\                                | > apiVersion: apps/v1\            |
| 3\                                | > kind: Deployment\               |
| 4\                                | > metadata:\                      |
| 5\                                | > name: web-app\                  |
| 6\                                | > spec:\                          |
| 7\                                | > replicas: 2\                    |
| 8\                                | > selector:\                      |
| 9\                                | > matchLabels:\                   |
| 10 11 12 13 14 15 16 17 18 19 20  | > app: web-app\                   |
| 21 22 23 24 25                    | > template:\                      |
|                                   | > metadata:\                      |
|                                   | > labels:\                        |
|                                   | > app: web-app\                   |
|                                   | > spec:\                          |
|                                   | > containers:\                    |
|                                   | > - name: web-app\                |
|                                   | > image: nginx:latest\            |
|                                   | > ports:\                         |
|                                   | > - containerPort: 80\            |
|                                   | > \-\--\                          |
|                                   | > apiVersion: v1\                 |
|                                   | > kind: Service\                  |
|                                   | > metadata:\                      |
|                                   | > name: web-app-service           |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 26 27 28 29 30 31 32            | > spec:\                          |
|                                   | > selector:\                      |
|                                   | > app: web-app\                   |
|                                   | > ports:\                         |
|                                   | > - protocol: TCP\                |
|                                   | > port: 80\                       |
|                                   | > targetPort: 80                  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| 33 34                             | > EOF                             |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> This will create an app named web-app with a port 80 exposure to the
> pod.
>
> It will also create a service directing calls to the deployment named
> web-app on port 80 to port 80 of one of the containers.

  -----------------------------------------------------------------------
  kubectl get deployments
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

  -----------------------------------------------------------------------
  kubectl get pods
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

  -----------------------------------------------------------------------
  kubectl get services
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

> giving something like

+-----------------------------------+-----------------------------------+
| > 1\                              | > NAME READY UP-TO-DATE AVAILABLE |
| > 2                               | > AGE\                            |
|                                   | > web-app 2/2 2 2 46s             |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 3\                              | > NAME READY STATUS RESTARTS AGE  |
| > 4\                              | > web-app-6fdf6bcdd6-cfkjk 1/1    |
| > 5\                              | > Running 0 42s                   |
| > 6                               | > web-app-6fdf6bcdd6-nxv7f 1/1    |
|                                   | > Running 0 42s                   |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 7\                              | > NAME TYPE CLUSTER-IP            |
| > 8\                              | > EXTERNAL-IP PORT(S) AGE         |
| > 9\                              | > kubernetes ClusterIP 10.96.0.1  |
| > 10                              | > \<none\> 443/TCP 57s            |
|                                   | > web-app-service ClusterIP       |
|                                   | > 10.110.70.144 \<none\> 80/TCP   |
|                                   | > 46s                             |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> Now create an ingress to create access

+-----------------------------------+-----------------------------------+
| 1\                                | > cat \<\<EOF \| k apply -f -\    |
| 2\                                | > apiVersion:                     |
| 3\                                | > networking.k8s.io/v1\           |
| 4\                                | > kind: Ingress\                  |
| 5\                                | > metadata:\                      |
| 6\                                | > name: web-app-ingress\          |
| 7\                                | > annotations:\                   |
| 8\                                | > nginx.ingr                      |
| 9\                                | ess.kubernetes.io/rewrite-target: |
| 10 11 12 13 14 15 16 17 18 19 20  | > /\$1\                           |
|                                   | > spec:\                          |
|                                   | > rules:\                         |
|                                   | > - host: web-app.info\           |
|                                   | > http:\                          |
|                                   | > paths:\                         |
|                                   | > - path: /\                      |
|                                   | > pathType: Prefix\               |
|                                   | > backend:\                       |
|                                   | > service:\                       |
|                                   | > name: web-app-service\          |
|                                   | > port:\                          |
|                                   | > number: 80\                     |
|                                   | > EOF                             |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> This will create an ingress that will create a connection outside of
> the cluster with web-app.info as the host name that will direct all

connections to port 80 of web-app-service service that will then forward
this to port 80 of the deployment for forwarding to one of the replicas

> for connection.

+-----------------------+-----------------------+-----------------------+
|   ------------------  |                       |                       |
|   kubectl get         |                       |                       |
|   ingress             |                       |                       |
|   ------------------  |                       |                       |
|                       |                       |                       |
|   ------------------  |                       |                       |
+=======================+=======================+=======================+
|   ------------------  |                       | > ![](vertop          |
|   NAME CLASS HOSTS    |                       | al_c4f4baa402e647588e |
|   ADDRESS PORTS AGE   |                       | cb2a507c21de28/media/ |
|   ------------------  |                       | image142.png){width=" |
|                       |                       | 1.9652777777777777in" |
|   ------------------  |                       | > height="3           |
|                       |                       | .9305555555555554in"} |
+-----------------------+-----------------------+-----------------------+
|                       |                       | > ![](vertop          |
| --------------------- |                       | al_c4f4baa402e647588e |
|   web-app-ingress     |                       | cb2a507c21de28/media/ |
|   \<none\>            |                       | image142.png){width=" |
|   http://web-app.info |                       | 1.9652777777777777in" |
|   80 2m28s            |                       | > height="3           |
|                       |                       | .9305555555555554in"} |
| --------------------- |                       |                       |
|                       |                       |                       |
|                       |                       |                       |
| --------------------- |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Ensure that the       |                       | > ![](vertop          |
| Ingress addon is      |                       | al_c4f4baa402e647588e |
| enabled in Minikube.  |                       | cb2a507c21de28/media/ |
|                       |                       | image142.png){width=" |
|                       |                       | 1.9652777777777777in" |
|                       |                       | > height="3           |
|                       |                       | .9305555555555554in"} |
+-----------------------+-----------------------+-----------------------+
|   ------------------  |                       | > ![](vertop          |
|   minikube addons     |                       | al_c4f4baa402e647588e |
|   enable ingress      |                       | cb2a507c21de28/media/ |
|   ------------------  |                       | image142.png){width=" |
|                       |                       | 1.9652777777777777in" |
|   ------------------  |                       | > height="3           |
|                       |                       | .9305555555555554in"} |
+-----------------------+-----------------------+-----------------------+
| This command enables  |                       | > ![](vertop          |
| the NGINX Ingress     |                       | al_c4f4baa402e647588e |
| Controller in your    |                       | cb2a507c21de28/media/ |
| Minikube cluster.     |                       | image142.png){width=" |
|                       |                       | 1.9652777777777777in" |
| Obtain the IP address |                       | > height="3           |
| of your Minikube      |                       | .9305555555555554in"} |
| cluster.              |                       |                       |
+-----------------------+-----------------------+-----------------------+
|   ------------------  |                       | > ![](vertop          |
|   minikube ip         |                       | al_c4f4baa402e647588e |
|   ------------------  |                       | cb2a507c21de28/media/ |
|                       |                       | image142.png){width=" |
|   ------------------  |                       | 1.9652777777777777in" |
|                       |                       | > height="3           |
|                       |                       | .9305555555555554in"} |
+-----------------------+-----------------------+-----------------------+
| This will return the  |                       |                       |
| IP address of your    |                       |                       |
| Minikube cluster.     |                       |                       |
|                       |                       |                       |
| Add an entry to your  |                       |                       |
| hosts file for        |                       |                       |
| web-app.info to the   |                       |                       |
| Minikube IP.          |                       |                       |
+-----------------------+-----------------------+-----------------------+
| 1                     | +------------------+  |                       |
|                       | | > echo           |  |                       |
|                       | | > \"\$(minikube  |  |                       |
|                       | | > ip)            |  |                       |
|                       | | > web-app.info\" |  |                       |
|                       | | > \| sudo tee -a |  |                       |
|                       | | > /etc/hosts     |  |                       |
|                       | +==================+  |                       |
|                       | +------------------+  |                       |
+-----------------------+-----------------------+-----------------------+

> This step is necessary because you\'ve specified web-app.info as the
> host in your Ingress resource.
>
> Now you should be able to access your application by opening a web
> browser and navigating to: http://web-app.info If everything is set up
> correctly, you should see the NGINX welcome page.
>
> If you\'re unable to access the application, try the following:\
> Check Ingress status kubectl get ingress , ensure that the ADDRESS
> field is populated with an IP address.
>
> Verify ingress kubectl get pods -n ingress-nginx , make sure the
> Ingress Controller pod is running.
>
> Check ingress logs looking for ERRORS kubectl logs -n ingress-nginx
> \$(kubectl get pods -n ingress-nginx -o name) (this can be run in
> seperate parts kubectl get pods -n ingress-nginx -o name then run
> kubectl logs -n ingress-nginx with the ingress) Last resort you can
> try port forwarding. kubectl port-forward svc/web-app-service 8080:80
> , now access the application at http://localhost:8080 .
>
> Remember that Minikube is running inside a VM, so network access can
> sometimes be tricky depending on your setup. The methods described
> above should work in most cases, but you might need to adjust based on
> your specific environment
>
> **Kubernetes RBAC and Security Concepts**

+-----------------------------------+-----------------------------------+
| > 1\                              | +------------------------------+  |
| > 2\                              | | > +\-\-\-\-\-                |  |
| > 3\                              | | \-\-\-\-\-\-\-\-\-\-\-\-\-\- |  |
| > 4\                              | | \-\-\-\-\-\-\-\-\-\-\-\-\-\- |  |
| > 5\                              | | \-\-\-\-\-\-\-\-\-\-\-\-\-\- |  |
| > 6\                              | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
| > 7\                              | +==============================+  |
| > 8\                              | +------------------------------+  |
| > 9                               |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| Kubernetes Cluster \|   |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \|                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \|                         |  |
|                                   | | > +\-\-\-\-\-\-\-\-\-        |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
|                                   | | > +\-\-\-\-\-\-\-\-\-\-\-\-  |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
|                                   | | > \|                         |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \| RBAC Objects \| \|   |  |
|                                   | | > Security Contexts \| \|    |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \|                      |  |
|                                   | | > +\-                        |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
|                                   | | > \| \|                      |  |
|                                   | | > +\-\-\-\-\-\-              |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
|                                   | | > \| \|                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \| \| Roles \| \| \| \| |  |
|                                   | | > Pod Security \| \| \|      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \| \| (Namespaced) \|   |  |
|                                   | | > \| \| \| Context \| \| \|  |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \|                      |  |
|                                   | | > +\-                        |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
|                                   | | > \| \| \| - User/Group \|   |  |
|                                   | | > \| \|                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------+-----------------------+-----------------------+
| 10                    |                       | > \| \| \| \| \| \| - |
|                       |                       | > SELinux \| \| \|    |
+=======================+=======================+=======================+
| 11                    |                       | > \| \| v \| \| \| -  |
|                       |                       | > RunAsUser \| \| \|  |
+-----------------------+-----------------------+-----------------------+
| 12                    |                       | > \| \|               |
|                       |                       | > +\-\-\-\-\          |
|                       |                       | -\-\-\-\-\-\-\-\-\--+ |
|                       |                       | > \| \| \| -          |
|                       |                       | > Capabilities \| \|  |
|                       |                       | > \|                  |
+-----------------------+-----------------------+-----------------------+
| 13                    |                       | > \| \| \|            |
|                       |                       | > RoleBindings \| \|  |
|                       |                       | > \|                  |
|                       |                       | >                     |
|                       |                       |  +\-\-\-\-\-\-\-\-\-\ |
|                       |                       | -\-\-\-\-\-\-\-\-\--+ |
|                       |                       | > \| \|               |
+-----------------------+-----------------------+-----------------------+
| 14                    |                       | > \| \| \|            |
|                       |                       | > (Namespaced) \| \|  |
|                       |                       | > \| \| \| \|         |
+-----------------------+-----------------------+-----------------------+
| 15                    |                       | > \| \|               |
|                       |                       | > +\-\-\-\-\          |
|                       |                       | -\-\-\-\-\-\-\-\-\--+ |
|                       |                       | > \| \| v \| \|       |
+-----------------------+-----------------------+-----------------------+
| 16                    |                       | > \| \| \| \|         |
|                       |                       | >                     |
|                       |                       |  +\-\-\-\-\-\-\-\-\-\ |
|                       |                       | -\-\-\-\-\-\-\-\-\--+ |
|                       |                       | > \| \|               |
+-----------------------+-----------------------+-----------------------+
| 17                    |                       | > \| \|               |
|                       |                       | > +\-\-\-\-\          |
|                       |                       | -\-\-\-\-\-\-\-\-\--+ |
|                       |                       | > \| \| \| Container  |
|                       |                       | > Security \| \| \|   |
+-----------------------+-----------------------+-----------------------+
| 18                    |                       | > \| \| \|            |
|                       |                       | > ClusterRoles \| \|  |
|                       |                       | > \| \| Context \| \| |
|                       |                       | > \|                  |
+-----------------------+-----------------------+-----------------------+
| 19                    |                       | > \| \| \|(Cluster-   |
|                       |                       | > Wide)\| \| \| \| -  |
|                       |                       | > RunAsNonRoot \| \|  |
|                       |                       | > \|                  |
+-----------------------+-----------------------+-----------------------+
| 20                    |                       | > \| \|               |
|                       |                       | > +\-\-\-\-\          |
|                       |                       | -\-\-\-\-\-\-\-\-\--+ |
|                       |                       | > \| \| \| -          |
|                       |                       | > ReadOnlyRootFS \|   |
|                       |                       | > \| \|               |
+-----------------------+-----------------------+-----------------------+
| 21                    |                       | > \| \| \| \| \| \| - |
|                       |                       | > Privileged \| \| \| |
+-----------------------+-----------------------+-----------------------+
| 22                    |                       | > \| \| v \| \|       |
|                       |                       | >                     |
|                       |                       |  +\-\-\-\-\-\-\-\-\-\ |
|                       |                       | -\-\-\-\-\-\-\-\-\--+ |
|                       |                       | > \| \|               |
+-----------------------+-----------------------+-----------------------+
| 23                    |                       | > \| \|               |
|                       |                       | > +\-\-\-\-\          |
|                       |                       | -\-\-\-\-\-\-\-\-\--+ |
|                       |                       | > \| \| \| \|         |
+-----------------------+-----------------------+-----------------------+
| 24                    |                       | > \| \| \|            |
|                       |                       | > ClusterRole- \| \|  |
|                       |                       | > +\-\-\-\-\-         |
|                       |                       | \-\-\-\-\-\-\-\-\-\-\ |
|                       |                       | -\-\-\-\-\-\-\-\-\--+ |
|                       |                       | > \|                  |
+-----------------------+-----------------------+-----------------------+
| 25                    |                       | > \| \| \| Bindings   |
|                       |                       | > \| \| \|            |
+-----------------------+-----------------------+-----------------------+
| 26                    |                       | > \| \| \|            |
|                       |                       | > (Cluster-wide)\| \| |
|                       |                       | > \|                  |
+-----------------------+-----------------------+-----------------------+
| 27                    |                       | > \| \|               |
|                       |                       | > +\-\-\-\-\          |
|                       |                       | -\-\-\-\-\-\-\-\-\--+ |
|                       |                       | > \| \|               |
+-----------------------+-----------------------+-----------------------+
| 28                    |                       | > \| \| \| \|         |
+-----------------------+-----------------------+-----------------------+
| 29                    |                       | > \|                  |
|                       |                       | > +\-\-               |
|                       |                       | \-\-\-\-\-\-\-\-\-\-\ |
|                       |                       | -\-\-\-\-\-\-\-\-\--+ |
|                       |                       | > \|                  |
+-----------------------+-----------------------+-----------------------+
| 30                    |                       | > \| \|               |
+-----------------------+-----------------------+-----------------------+
| 31                    |                       | > \|                  |
|                       |                       | > +\                  |
|                       |                       | -\-\-\-\-\-\-\-\-\-\- |
|                       |                       | \-\-\-\-\-\-\-\-\-\-\ |
|                       |                       | -\-\-\-\-\-\-\-\-\-\- |
|                       |                       | \-\-\-\-\-\-\-\-\-\-\ |
|                       |                       | -\-\-\-\-\-\-\-\-\--+ |
|                       |                       | > \|                  |
+-----------------------+-----------------------+-----------------------+
| 32                    |                       | > \| \| Network       |
|                       |                       | > Policies \| \|      |
+-----------------------+-----------------------+-----------------------+
| 33                    |                       | > \| \|               |
|                       |                       | > +                   |
|                       |                       | \-\-\-\-\-\-\-\-\-\-\ |
|                       |                       | -\-\-\-\-\-\-\-\-\--+ |
|                       |                       | > +\-                 |
|                       |                       | \-\-\-\-\-\-\-\-\-\-\ |
|                       |                       | -\-\-\-\-\-\-\-\-\--+ |
|                       |                       | > \| \|               |
+-----------------------+-----------------------+-----------------------+
| 34                    |                       | > \| \| \| Ingress    |
|                       |                       | > Rules \| \| Egress  |
|                       |                       | > Rules \| \| \|      |
+-----------------------+-----------------------+-----------------------+
| 35                    |                       | > \| \| \| \| \| \|   |
|                       |                       | > \| \|               |
+-----------------------+-----------------------+-----------------------+
| 36                    |                       | > \| \| \| - From:    |
|                       |                       | > (sources) \| \| -   |
|                       |                       | > To: (destinations)  |
|                       |                       | > \| \| \|            |
+-----------------------+-----------------------+-----------------------+
| 37                    |                       | > \| \| \| - Ports \| |
|                       |                       | > \| - Ports \| \| \| |
+-----------------------+-----------------------+-----------------------+
| 38                    |                       | > \| \|               |
|                       |                       | > +                   |
|                       |                       | \-\-\-\-\-\-\-\-\-\-\ |
|                       |                       | -\-\-\-\-\-\-\-\-\--+ |
|                       |                       | > +\-                 |
|                       |                       | \-\-\-\-\-\-\-\-\-\-\ |
|                       |                       | -\-\-\-\-\-\-\-\-\--+ |
|                       |                       | > \| \|               |
+-----------------------+-----------------------+-----------------------+
| 39                    |                       | > \| \| \| \|         |
+-----------------------+-----------------------+-----------------------+
| 40                    |                       | > \|                  |
|                       |                       | > +\                  |
|                       |                       | -\-\-\-\-\-\-\-\-\-\- |
|                       |                       | \-\-\-\-\-\-\-\-\-\-\ |
|                       |                       | -\-\-\-\-\-\-\-\-\-\- |
|                       |                       | \-\-\-\-\-\-\-\-\-\-\ |
|                       |                       | -\-\-\-\-\-\-\-\-\--+ |
|                       |                       | > \|                  |
+-----------------------+-----------------------+-----------------------+
| 41                    |                       | > \| \|               |
+-----------------------+-----------------------+-----------------------+
| 42                    |                       | > +\-\-\-\-\-\-\-\-\  |
|                       |                       | -\-\-\-\-\-\-\-\-\-\- |
|                       |                       | \-\-\-\-\-\-\-\-\-\-\ |
|                       |                       | -\-\-\-\-\-\-\-\-\-\- |
|                       |                       | \-\-\-\-\-\-\-\-\-\-\ |
|                       |                       | -\-\-\-\-\-\-\-\-\--+ |
+-----------------------+-----------------------+-----------------------+
| ![](vertopal_         | > RBAC Objects:       |                       |
| c4f4baa402e647588ecb2 |                       |                       |
| a507c21de28/media/ima |                       |                       |
| ge143.png){width="4.1 |                       |                       |
| 666666666666664e-2in" |                       |                       |
| height="4.16          |                       |                       |
| 66666666666664e-2in"} |                       |                       |
+-----------------------+-----------------------+-----------------------+
| ![](vertopal          |                       | > Roles and           |
| _c4f4baa402e647588ecb |                       | > RoleBindings        |
| 2a507c21de28/media/im |                       | > (namespaced)        |
| age144.png){width="5. |                       |                       |
| 555555555555555e-2in" |                       |                       |
| height="4.16          |                       |                       |
| 66666666666664e-2in"} |                       |                       |
+-----------------------+-----------------------+-----------------------+
| ![](vertopal          |                       | > ClusterRoles and    |
| _c4f4baa402e647588ecb |                       | > ClusterRoleBindings |
| 2a507c21de28/media/im |                       | > (cluster-wide)      |
| age145.png){width="5. |                       |                       |
| 555555555555555e-2in" |                       |                       |
| height="5.5           |                       |                       |
| 55555555555555e-2in"} |                       |                       |
+-----------------------+-----------------------+-----------------------+

> These objects define who can access what resources and perform what
> actions.
>
> ![](converted/media/image146.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}Security Contexts:
>
> ![](converted/media/image147.png){width="5.555555555555555e-2in"
> height="5.555555555555555e-2in"}Pod Security Context: Applies to all
> containers in a pod
>
> ![](converted/media/image148.png){width="5.555555555555555e-2in"
> height="5.555555555555555e-2in"}Container Security Context: Specific
> to individual containers\
> These define privilege and access control settings for pods and
> containers.
>
> ![](converted/media/image149.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Network Policies:
>
> ![](converted/media/image150.png){width="5.555555555555555e-2in"
> height="5.555555555555555e-2in"}Ingress Rules: Control incoming
> traffic to pods
>
> ![](converted/media/image151.png){width="5.555555555555555e-2in"
> height="4.1666666666666664e-2in"}Egress Rules: Control outgoing
> traffic from pods\
> These act as a virtual firewall for your Kubernetes cluster.
>
> The diagram shows how these components interact within the Kubernetes
> cluster to provide a comprehensive security model. RBAC controls
> access to Kubernetes API resources, Security Contexts manage the
> runtime security settings for pods and containers, and Network
> Policies control the network traffic between pods and external sources
>
> **Role-Based Access Control (RBAC)**
>
> ![](converted/media/image152.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Regulates access to resources based
> on the roles of individual users.
>
> ![](converted/media/image153.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Key objects: Role, ClusterRole,
> RoleBinding, ClusterRoleBinding.\
> Example: Creating a role that allows reading pods:

+-----------------------------------+-----------------------------------+
| > 1\                              | +------------------------------+  |
| > 2\                              | | > apiVersion:                |  |
| > 3\                              | | >                            |  |
| > 4\                              | | rbac.authorization.k8s.io/v1 |  |
| > 5\                              | +==============================+  |
| > 6\                              | +------------------------------+  |
| > 7\                              |                                   |
| > 8\                              | +------------------------------+  |
| > 9                               | | > kind: Role                 |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > metadata:                  |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > namespace: default         |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > name: pod-reader           |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > Rules:                     |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \- apiGroups: \[\"\"\]     |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > resources: \[\"pods\"\]    |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > verbs: \[\"get\",          |  |
|                                   | | > \"watch\", \"list\"\]      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **Security Contexts**
>
> ![](converted/media/image154.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Define privilege and access control
> settings for Pods or Containers.
>
> ![](converted/media/image155.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Can set UID, GID, capabilities, and
> other security parameters.
>
> **Network Policies**
>
> ![](converted/media/image156.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Specify how groups of pods are
> allowed to communicate with each other and other network endpoints.
>
> ![](converted/media/image157.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Act as a virtual firewall for your
> Kubernetes cluster.
>
> **Exercise:**
>
> Deploying a Configurable Web ApplicationIn this exercise, we\'ll
> create a simple web application that reads its configuration from a
>
> ConfigMap. We\'ll then deploy it to Kubernetes and expose it using a
> Service and Ingress.
>
> This exercise demonstrates:
>
> 1\. Creating and using ConfigMaps
>
> 2\. Deploying a web application with Kubernetes
>
> 3\. Exposing the application using a Service and Ingress
>
> 4\. Injecting configuration into a container using environment
> variables
>
> 5\. Mounting ConfigMap data as a volume
>
> 6\. Updating configuration and seeing the changes reflected in the
> application
>
> ![](converted/media/image158.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}**Step 1:** Create a ConfigMap
>
> First, let\'s create a ConfigMap with some configuration data:

+-----------------------------------+-----------------------------------+
| > 1\                              | +------------------------------+  |
| > 2\                              | | > cat \<\<EOF \| kubectl     |  |
| > 3\                              | | > apply -f -                 |  |
| > 4\                              | +==============================+  |
| > 5\                              | +------------------------------+  |
| > 6\                              |                                   |
| > 7\                              | +------------------------------+  |
| > 8\                              | | > apiVersion: v1             |  |
| > 9                               | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > kind: ConfigMap            |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > metadata:                  |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > name: webapp-config        |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > data:                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > BACKGROUND_COLOR:          |  |
|                                   | | > \"#f0f0f0\"                |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > MESSAGE: \"Welcome to our  |  |
|                                   | | > configurable web app!\"    |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > EOF                        |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
| 1\                                | +------------------------------+  |
| 2\                                | | > +\-\-\-\-\-\-\-\-\-\-      |  |
| 3\                                | | \-\-\-\-\-\-\-\-\-\-\-\-\-\- |  |
| 4\                                | | \-\-\-\-\-\-\-\-\-\-\-\-\-\- |  |
| 5\                                | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
| 6\                                | +==============================+  |
| 7\                                | +------------------------------+  |
| 8\                                |                                   |
| 9\                                | +------------------------------+  |
| 10                                | | > \| Kubernetes Cluster \|   |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \|                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \|                         |  |
|                                   | | > +\-\-\-                    |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\-\- |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\-\- |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
|                                   | | > \|                         |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \| ConfigMap \| \|      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \| Name: webapp-config  |  |
|                                   | | > \| \|                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \| Data: \| \|          |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \|                      |  |
|                                   | | > +\-\-\-\-\-\-\-\-\-\-\-    |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\-\- |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
|                                   | | > \| \|                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \| \| Key \| Value \|   |  |
|                                   | | > \| \|                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \|                      |  |
|                                   | | > +\-\-\-\-\-\-\-\-\-\-      |  |
|                                   | | \-\-\-\-\-\-\-\--+\-\-\-\-\- |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
|                                   | | > \| \|                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 11 12 13 14 15 16 17 18 19 20   | +------------------------------+  |
|                                   | | > \| \| \| BACKGROUND_COLOR  |  |
|                                   | | > \| \"#f0f0f0\" \| \| \|    |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \|                      |  |
|                                   | | > +\-\-\-\-\-\-\-\-\-\-      |  |
|                                   | | \-\-\-\-\-\-\-\--+\-\-\-\-\- |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
|                                   | | > \| \|                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \| \| MESSAGE \|        |  |
|                                   | | > \"Welcome to our \| \| \|  |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \| \| \| configurable   |  |
|                                   | | > \| \| \|                   |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \| \| \| web app!\" \|  |  |
|                                   | | > \| \|                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \|                      |  |
|                                   | | > +\-\-\-\-\-\-\-\-\-\-      |  |
|                                   | | \-\-\-\-\-\-\-\--+\-\-\-\-\- |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
|                                   | | > \| \|                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \| \| \|                |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \|                         |  |
|                                   | | > +\-\-\-                    |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\-\- |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\-\- |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
|                                   | | > \|                         |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \|                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > +\-\-\-\-\-\-\-\-\-\-      |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\-\- |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\-\- |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> This diagram shows:
>
> 1\. The overall Kubernetes cluster environment.
>
> 2\. Within the cluster, a ConfigMap named \"webapp-config\" is
> created.
>
> 3\. The ConfigMap contains two key-value pairs:
>
> ![](converted/media/image159.png){width="5.555555555555555e-2in"
> height="5.555555555555555e-2in"}BACKGROUND_COLOR: \"#f0f0f0\"
>
> ![](converted/media/image160.png){width="5.555555555555555e-2in"
> height="5.555555555555555e-2in"}MESSAGE: \"Welcome to our configurable
> web app!\"
>
> The diagram illustrates how the ConfigMap stores configuration data as
> key-value pairs, which can be used by applications running in the
> cluster. This ConfigMap could be mounted as a volume or used as
> environment variables in a Pod, allowing the application to access
> these configuration values at runtime.
>
> ![](converted/media/image161.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}**Step 2:** Create a Deployment\
> Now, let\'s create a Deployment for our web application. We\'ll use a
> simple Nginx image and inject our configuration as environment
> variables:

+-----------------------------------+-----------------------------------+
| 1\                                | > cat \<\<EOF \| kubectl apply -f |
| 2\                                | > -\                              |
| 3\                                | > apiVersion: apps/v1\            |
| 4\                                | > kind: Deployment\               |
| 5\                                | > metadata:\                      |
| 6\                                | > name: webapp\                   |
| 7\                                | > spec:\                          |
| 8\                                | > replicas: 2\                    |
| 9\                                | > selector:\                      |
| 10 11 12 13 14 15 16 17 18 19 20  | > matchLabels:\                   |
| 21 22 23 24 25 26 27 28 29 30     | > app: webapp\                    |
|                                   | > template:\                      |
|                                   | > metadata:\                      |
|                                   | > labels:\                        |
|                                   | > app: webapp\                    |
|                                   | > spec:\                          |
|                                   | > containers:\                    |
|                                   | > - name: webapp\                 |
|                                   | > image: nginxtest\               |
|                                   | > ports:\                         |
|                                   | > - containerPort: 80\            |
|                                   | > envFrom:\                       |
|                                   | > - configMapRef:\                |
|                                   | > name: webapp-config\            |
|                                   | > volumeMounts:\                  |
|                                   | > - name: config\                 |
|                                   | > mountPath:                      |
|                                   | > /usr/share/nginx/html\          |
|                                   | > volumes:\                       |
|                                   | > - name: config\                 |
|                                   | > configMap:\                     |
|                                   | > name: webapp-content            |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 31 32 33 34                     | +------------------------------+  |
|                                   | | > items:                     |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \- key: index.html         |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > path: index.html           |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > EOF                        |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
| 1\                                | > +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- |
| 2\                                | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
| 3\                                | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- |
| 4\                                | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
| 5\                                | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
| 6\                                | > \| Kubernetes Cluster \| \| \|  |
| 7\                                | > \|                              |
| 8\                                | > +\-\-\-\-\-\-\-                 |
| 9\                                | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
| 10 11 12 13 14 15 16 17 18 19 20  | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- |
| 21 22 23 24 25 26 27 28 29 30 31  | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
| 32 33 34 35 36 37 38 39 40 41 42  | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
| 43 44                             | > \| \| \| Deployment: webapp \|  |
|                                   | > \| \| \| \| \| \| \|            |
|                                   | >                                 |
|                                   |  +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \| \| \| \| ReplicaSet (2    |
|                                   | > replicas) \| \| \| \| \| \| \|  |
|                                   | > \| \| \| \| \|                  |
|                                   | > +\-\-\-\                        |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \| \| \| \| \| \| Pod 1 \|   |
|                                   | > \| \| \| \| \| \| \|            |
|                                   | > +\-\-\-\-\-\-\-\-               |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \| \| \| \| \| \| \| \|      |
|                                   | > Container: webapp. \| \| \| \|  |
|                                   | > \| \| \| \| \| \| \| \| \| \|   |
|                                   | > \| \| \| \| \| \| Image:        |
|                                   | > nginx:alpine \| \| \| \| \| \|  |
|                                   | > \| \| \| \| Port: 80 \| \| \|   |
|                                   | > \| \| \| \| \| \| \| \| \| \|   |
|                                   | > \| \| \| \| \| \| \| EnvFrom:   |
|                                   | > \| \| \| \| \| \| \| \| \| \|   |
|                                   | > ConfigMap: webapp-config \| \|  |
|                                   | > \| \| \| \| \| \| \| \| \| \|   |
|                                   | > \| \| \| \| \| \| \| \|         |
|                                   | > VolumeMount: \| \| \| \| \| \|  |
|                                   | > \| \| \| \| Name: config \| \|  |
|                                   | > \| \| \| \| \| \| \| \|         |
|                                   | > MountPath:                      |
|                                   | > /usr/share/nginx/html \| \| \|  |
|                                   | > \| \| \| \| \| \|               |
|                                   | > +\-\-\-\-\-\-\-\-               |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \| \| \| \| \| \| \| \| \|   |
|                                   | > \| \| \| \| \| \|               |
|                                   | > +\-\-\-\-\-\-\-\-               |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \| \| \| \| \| \| \| \|      |
|                                   | > Volume: config \| \| \| \| \|   |
|                                   | > \| \| \| \| \| ConfigMap:       |
|                                   | > webapp-config \| \| \| \| \| \| |
|                                   | > \| \| \| \| Key: index.html \|  |
|                                   | > \| \| \| \| \| \| \| \| \|      |
|                                   | > Path: index.html \| \| \| \| \| |
|                                   | > \| \| \| \|                     |
|                                   | > +\-\-\-\-\-\-\-\-               |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \| \| \| \| \| \| \| \| \|   |
|                                   | > \| \| \| \| \|                  |
|                                   | > +\-\-\-\                        |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \| \| \| \| \| \| \| \| \|   |
|                                   | > \| \|                           |
|                                   | > +\-\-\-\                        |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \| \| \| \| \| \| Pod 2 \|   |
|                                   | > \| \| \| \| \| \| \| (Same      |
|                                   | > structure as Pod 1) \| \| \| \| |
|                                   | > \| \| \|                        |
|                                   | > +\-\-\-\                        |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \| \| \| \| \| \| \| \| \|   |
|                                   | > \|                              |
|                                   | >                                 |
|                                   |  +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \| \| \| \| \| \|            |
|                                   | > +\-\-\-\-\-\-\-                 |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \| \|                        |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
+-----------------------------------+-----------------------------------+

> This diagram illustrates:
>
> 1\. The overall Kubernetes Deployment named \"webapp\".\
> 2. The ReplicaSet managing 2 replicas (Pods).
>
> 3\. The structure of each Pod, including:
>
> ![](converted/media/image162.png){width="5.555555555555555e-2in"
> height="5.555555555555555e-2in"}The container named \"webapp\" using
> the nginx:alpine image.
>
> ![](converted/media/image163.png){width="5.555555555555555e-2in"
> height="5.555555555555555e-2in"}The container port 80 exposed.
>
> ![](converted/media/image164.png){width="5.555555555555555e-2in"
> height="5.555555555555555e-2in"}Environment variables loaded from the
> ConfigMap \"webapp-config\".
>
> ![](converted/media/image165.png){width="5.555555555555555e-2in"
> height="5.555555555555555e-2in"}A volume mount for the
> \"/usr/share/nginx/html\" path.
>
> 4\. The volume configuration, which mounts the \"index.html\" key from
> the \"webapp-config\" ConfigMap.

The diagram shows how the Deployment manages multiple identical Pods,
each containing a container with the specified configuration. It

also illustrates the use of ConfigMaps for both environment variables
and file mounting, demonstrating how Kubernetes can inject

configuration data into containers.

> ![](converted/media/image166.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}**Step 3:** Create a ConfigMap for
> the HTML content
>
> Let\'s create another ConfigMap to hold our HTML content:

+-----------------------------------+-----------------------------------+
| 1\                                | > cat \<\<EOF \| kubectl apply -f |
| 2\                                | > -\                              |
| 3\                                | > apiVersion: v1\                 |
| 4\                                | > kind: ConfigMap\                |
| 5\                                | > metadata:\                      |
| 6\                                | > name: webapp-content\           |
| 7\                                | > data:\                          |
| 8\                                | > index.html: \|\                 |
| 9\                                | > \<!DOCTYPE html\>\              |
| 10 11 12 13 14 15 16 17 18 19 20  | > \<html\>\                       |
| 21                                | > \<head\>\                       |
|                                   | > \<title\>Configurable Web       |
|                                   | > App\</title\>\                  |
|                                   | > \<style\>\                      |
|                                   | > body { background-color:        |
|                                   | > \\\${BACKGROUND_COLOR};         |
|                                   | > font-family: Arial, sans-serif; |
|                                   | > } \</style\>\                   |
|                                   | > \</head\>\                      |
|                                   | > \<body\>\                       |
|                                   | > \<h1\>\\\${MESSAGE}\</h1\>\     |
|                                   | > \<p\>This page is served by     |
|                                   | > Nginx and configured using      |
|                                   | > Kubernetes ConfigMaps.\</p\>    |
|                                   | > \</body\>\                      |
|                                   | > \</html\>\                      |
|                                   | > EOF                             |
+===================================+===================================+
| 1\                                | > +\-\-\-\-\                      |
| 2\                                | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- |
| 3\                                | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
| 4\                                | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
| 5\                                | > \| Kubernetes Cluster \| \| \|  |
| 6\                                | > \|                              |
| 7\                                | > +\-\-\-\-\-\-\-\-\-\-\-\-\-     |
| 8\                                | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
| 9\                                | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
| 10 11 12 13 14 15 16 17 18 19 20  | > \| \| \| ConfigMap:             |
| 21 22 23                          | > webapp-config \| \| \| \| \| \| |
|                                   | > \| \| Data: \| \| \| \|         |
|                                   | > BACKGROUND_COLOR: \"#f0f0f0\"   |
|                                   | > \| \| \| \| MESSAGE: \"Welcome  |
|                                   | > to our configurable\...\" \| \| |
|                                   | > \|                              |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\-     |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \| \| \|                     |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\-     |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \| \| ConfigMap:             |
|                                   | > webapp-content \| \| \| \| \|   |
|                                   | > \| \| \| Data: \| \| \| \|      |
|                                   | > index.html: (HTML content) \|   |
|                                   | > \| \| \| - Uses                 |
|                                   | > \${BACKGROUND_COLOR} \| \| \|   |
|                                   | > \| - Uses \${MESSAGE} \| \| \|  |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\-     |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \| \| \|                     |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\-     |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \| \| Deployment: webapp \|  |
|                                   | > \| \| \| \| \|                  |
+-----------------------------------+-----------------------------------+

![](converted/media/image172.png){width="0.9583333333333334in"
height="0.16666666666666666in"}

+-----------------------------------+-----------------------------------+
| > 24 25 26 27 28 29 30 31 32 33   | > \| \|                           |
| > 34 35 36 37 38 39 40 41 42 43   | > +\-\-\-\-\-\-\-                 |
| > 44 45 46 47 48                  | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \| \| \| \| Pod \| \| \| \|  |
|                                   | > \| \|                           |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\  |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \| \| \| \| \| \| Container: |
|                                   | > webapp \| \| \| \| \| \| \| \|  |
|                                   | > \| \| \| \| \| \| \| \| -       |
|                                   | > Image: nginx:alpine \| \| \| \| |
|                                   | > \| \| \| \| - Port: 80 \| \| \| |
|                                   | > \| \| \| \| \| \| \| \| \| \|   |
|                                   | > \| \| \| EnvFrom: \| \| \| \|   |
|                                   | > \| \| \| \| ConfigMap:          |
|                                   | > webapp-config \| \| \| \| \| \| |
|                                   | > \| \| \| \| \| \| \| \| \| \|   |
|                                   | > VolumeMount: \| \| \| \| \| \|  |
|                                   | > \| \| Name: config \| \| \| \|  |
|                                   | > \| \| \| \| MountPath:          |
|                                   | > /usr/share/\... \| \| \| \| \|  |
|                                   | > \| \|                           |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\  |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \| \| \| \| \| \| \| \| \|   |
|                                   | > \| \|                           |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\  |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \| \| \| \| \| \| Volume:    |
|                                   | > config \| \| \| \| \| \| \| \|  |
|                                   | > ConfigMap: webapp-content \| \| |
|                                   | > \| \| \| \| \| \| Key:          |
|                                   | > index.html \| \| \| \| \| \| \| |
|                                   | > \| Path: index.html \| \| \| \| |
|                                   | > \| \| \|                        |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\  |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \| \| \| \|                  |
|                                   | > +\-\-\-\-\-\-\-                 |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \| \|                        |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\-     |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|                              |
|                                   | > +\-\-\-\-\                      |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> This updated diagram now includes:
>
> 1\. The original webapp-config ConfigMap with BACKGROUND_COLOR and
> MESSAGE . 2. The new webapp-content ConfigMap containing the
> index.html template. 3. The Deployment and Pod structure, showing how
> these ConfigMaps are used: webapp-config is used as environment
> variables (EnvFrom).
>
> ![](converted/media/image167.png){width="1.0138888888888888in"
> height="0.1527777777777778in"}webapp-content is mounted as a volume,
> providing the index.html file.
>
> The new webapp-content ConfigMap contains an HTML template that uses
> the \${BACKGROUND_COLOR} and \${MESSAGE} variables. These variables
> will be replaced with the actual values from the webapp-config
> ConfigMap when the page is served.This setup allows for a dynamic,
> configurable web application where:
>
> ![](converted/media/image168.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}The content of the page (HTML
> structure) is defined in one ConfigMap ( webapp-content ).
>
> ![](converted/media/image169.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}The configuration values (background
> color and message) are defined in another ConfigMap ( webapp-config ).
>
> ![](converted/media/image170.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}The Nginx container serves the HTML
> content, with the variables replaced by the actual configuration
> values.
>
> This separation of concerns makes it easy to update either the content
> template or the configuration values independently, providing
> flexibility in managing your web application\'s appearance and
> content.
>
> ![](converted/media/image171.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}**Step 4:** Create a Service\
> Now, let\'s create a Service to expose our Deployment:

+-----------------------------------+-----------------------------------+
| > 1\                              | +------------------------------+  |
| > 2\                              | | > cat \<\<EOF \| kubectl     |  |
| > 3\                              | | > apply -f -                 |  |
| > 4\                              | +==============================+  |
| > 5\                              | +------------------------------+  |
| > 6\                              |                                   |
| > 7\                              | +------------------------------+  |
| > 8\                              | | > apiVersion: v1             |  |
| > 9                               | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > kind: Service              |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > metadata:                  |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > name: webapp-service       |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > spec:                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > selector:                  |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > app: webapp                |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > ports:                     |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 10 11 12 13                     | +------------------------------+  |
|                                   | | > \- protocol: TCP           |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > port: 80                   |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > targetPort: 80             |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > EOF                        |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
| 1\                                | > +\-\-\-                         |
| 2\                                | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
| 3\                                | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- |
| 4\                                | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+\ |
| 5\                                | > \| Kubernetes Cluster \|\       |
| 6\                                | > \| \|\                          |
| 7\                                | > \|                              |
| 8\                                | > +\-\-\-\-\-\-\-\-\-\-\-\-       |
| 9\                                | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
| 10 11 12 13 14 15 16 17 18 19 20  | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
| 21 22 23 24 25 26 27 28 29 30 31  | > \|\                             |
| 32 33 34 35 36 37 38 39 40 41 42  | > \| \| ConfigMap: webapp-config  |
| 43 44 45 46 47 48 49 50 51 52 53  | > \| \|\                          |
|                                   | > \| \| \| \|\                    |
|                                   | > \| \| Data: \| \|\              |
|                                   | > \| \| BACKGROUND_COLOR:         |
|                                   | > \"#f0f0f0\" \| \|\              |
|                                   | > \| \| MESSAGE: \"Welcome to our |
|                                   | > configurable\...\" \| \|\       |
|                                   | > \|                              |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-       |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > \| \|\                          |
|                                   | > \|                              |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-       |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > \| \| ConfigMap: webapp-content |
|                                   | > \| \|\                          |
|                                   | > \| \| \| \|\                    |
|                                   | > \| \| Data: \| \|\              |
|                                   | > \| \| index.html: (HTML         |
|                                   | > content) \| \|\                 |
|                                   | > \| \| - Uses                    |
|                                   | > \${BACKGROUND_COLOR} \| \|\     |
|                                   | > \| \| - Uses \${MESSAGE} \| \|\ |
|                                   | > \|                              |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-       |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > \| \|\                          |
|                                   | > \|                              |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-       |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > \| \| Deployment: webapp \| \|\ |
|                                   | > \| \| \| \|\                    |
|                                   | > \| \|                           |
|                                   | > +\-\-\-\-\-\-                   |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \|\                          |
|                                   | > \| \| \| Pod \| \| \|\          |
|                                   | > \| \| \|                        |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\  |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \| \|\                       |
|                                   | > \| \| \| \| Container: webapp   |
|                                   | > \| \| \| \|\                    |
|                                   | > \| \| \| \| \| \| \| \|\        |
|                                   | > \| \| \| \| - Image:            |
|                                   | > nginx:alpine \| \| \| \|\       |
|                                   | > \| \| \| \| - Port: 80 \| \| \| |
|                                   | > \|\                             |
|                                   | > \| \| \| \| \| \| \| \|\        |
|                                   | > \| \| \| \| EnvFrom: \| \| \|   |
|                                   | > \|\                             |
|                                   | > \| \| \| \| ConfigMap:          |
|                                   | > webapp-config \| \| \| \|\      |
|                                   | > \| \| \| \| \| \| \| \|\        |
|                                   | > \| \| \| \| VolumeMount: \| \|  |
|                                   | > \| \|\                          |
|                                   | > \| \| \| \| Name: config \| \|  |
|                                   | > \| \|\                          |
|                                   | > \| \| \| \| MountPath:          |
|                                   | > /usr/share/\... \| \| \| \|\    |
|                                   | > \| \| \|                        |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\  |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \| \|\                       |
|                                   | > \| \| \| \| \| \|\              |
|                                   | > \| \| \|                        |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\  |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \| \|\                       |
|                                   | > \| \| \| \| Volume: config \|   |
|                                   | > \| \| \|\                       |
|                                   | > \| \| \| \| ConfigMap:          |
|                                   | > webapp-content \| \| \| \|\     |
|                                   | > \| \| \| \| Key: index.html \|  |
|                                   | > \| \| \|\                       |
|                                   | > \| \| \| \| Path: index.html \| |
|                                   | > \| \| \|\                       |
|                                   | > \| \| \|                        |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\  |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \| \|\                       |
|                                   | > \| \|                           |
|                                   | > +\-\-\-\-\-\-                   |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \|\                          |
|                                   | > \|                              |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-       |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > \| \|\                          |
|                                   | > \|                              |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-       |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > \| \| Service: webapp-service   |
|                                   | > \| \|\                          |
|                                   | > \| \| \| \|\                    |
|                                   | > \| \| Selector: app: webapp \|  |
|                                   | > \|\                             |
|                                   | > \| \| Port: 80 -\> targetPort:  |
|                                   | > 80 \| \|                        |
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| 54 55                             | > \|                              |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-       |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > +\-\-\                          |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> This updated diagram now includes:
>
> 1\. The original webapp-config ConfigMap with BACKGROUND_COLOR and
> MESSAGE .
>
> 2\. The webapp-content ConfigMap containing the index.html template.
>
> 3\. The Deployment and Pod structure, showing how these ConfigMaps are
> used.
>
> 4\. The new webapp-service Service, which:
>
> ![](converted/media/image173.png){width="5.555555555555555e-2in"
> height="5.555555555555555e-2in"}Selects Pods with the label app:
> webapp
>
> ![](converted/media/image174.png){width="5.555555555555555e-2in"
> height="5.555555555555555e-2in"}Exposes port 80 and forwards traffic
> to the Pods\' port 80
>
> The Service acts as a stable network endpoint for the Pods created by
> the Deployment. It provides:
>
> ![](converted/media/image175.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Load balancing: Distributes incoming
> traffic across all Pods matching the selector.
>
> ![](converted/media/image176.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Service discovery: Provides a stable
> IP address and DNS name for the set of Pods.
>
> ![](converted/media/image177.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}Port mapping: Maps the Service port
> (80) to the target port on the Pods (also 80 in this case).
>
> This Service allows other components within the cluster (or external
> to the cluster, depending on the Service type) to access the webapp
> Pods without needing to know the individual Pod IP addresses. It adds
> a layer of abstraction that enhances the scalability and flexibility
> of your application.The flow of traffic would typically be:External
> Request -\> Service (webapp-service) -\> Pod (webapp) -\> Container
> (nginx:alpine)This setup allows you to scale your Deployment (adding
> or removing Pods) without changing how other components interact with
> your webapp, as they will always communicate through the Service.
>
> ![](converted/media/image36.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}**Step 5:** Create an Ingress\
> If your cluster has an Ingress controller, you can create an Ingress
> resource:

+-----------------------------------+-----------------------------------+
| 1\                                | > cat \<\<EOF \| kubectl apply -f |
| 2\                                | > -\                              |
| 3\                                | > apiVersion:                     |
| 4\                                | > networking.k8s.io/v1\           |
| 5\                                | > kind: Ingress\                  |
| 6\                                | > metadata:\                      |
| 7\                                | > name: webapp-ingress\           |
| 8\                                | > annotations:\                   |
| 9\                                | > nginx.ingr                      |
| 10 11 12 13 14 15 16 17 18 19 20  | ess.kubernetes.io/rewrite-target: |
|                                   | > /\                              |
|                                   | > spec:\                          |
|                                   | > rules:\                         |
|                                   | > - host: webapp.example.com\     |
|                                   | > http:\                          |
|                                   | > paths:\                         |
|                                   | > - path: /\                      |
|                                   | > pathType: Prefix\               |
|                                   | > backend:\                       |
|                                   | > service:\                       |
|                                   | > name: webapp-service\           |
|                                   | > port:\                          |
|                                   | > number: 80\                     |
|                                   | > EOF                             |
+===================================+===================================+
| > 1\                              | +------------------------------+  |
| > 2\                              | | > +\-\-\-\-\-\-\-\-\-\-      |  |
| > 3\                              | | \-\-\-\-\-\-\-\-\-\-\-\-\-\- |  |
| > 4\                              | | \-\-\-\-\-\-\-\-\-\-\-\-\-\- |  |
| > 5\                              | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
| > 6\                              | +==============================+  |
| > 7\                              | +------------------------------+  |
| > 8\                              |                                   |
| > 9                               | +------------------------------+  |
|                                   | | > \| Kubernetes Cluster \|   |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \|                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \|                         |  |
|                                   | | > +\-\-\-                    |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\-\- |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\-\- |  |
|                                   | | \-\-\-\-\-\-\-\-\-\-\-\-\--+ |  |
|                                   | | > \|                         |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \| ConfigMap:           |  |
|                                   | | > webapp-config \| \|        |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \| \| \|                |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \| Data: \| \|          |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \| BACKGROUND_COLOR:    |  |
|                                   | | > \"#f0f0f0\" \| \|          |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \| \| MESSAGE: \"Welcome   |  |
|                                   | | > to our configurable\...\"  |  |
|                                   | | > \| \|                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 10 11 12 13 14 15 16 17 18 19   | > \|                              |
| > 20 21 22 23 24 25 26 27 28 29   | > +\-\-\-\-\-\-\-\-\-\-\-\-       |
| > 30 31 32 33 34 35 36 37 38 39   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
| > 40 41 42 43 44 45 46 47 48 49   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
| > 50 51 52 53 54 55 56 57 58 59   | > \|\                             |
| > 60 61 62 63                     | > \| \|\                          |
|                                   | > \|                              |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-       |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > \| \| ConfigMap: webapp-content |
|                                   | > \| \|\                          |
|                                   | > \| \| \| \|\                    |
|                                   | > \| \| Data: \| \|\              |
|                                   | > \| \| index.html: (HTML         |
|                                   | > content) \| \|\                 |
|                                   | > \| \| - Uses                    |
|                                   | > \${BACKGROUND_COLOR} \| \|\     |
|                                   | > \| \| - Uses \${MESSAGE} \| \|\ |
|                                   | > \|                              |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-       |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > \| \|\                          |
|                                   | > \|                              |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-       |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > \| \| Deployment: webapp \| \|\ |
|                                   | > \| \| \| \|\                    |
|                                   | > \| \|                           |
|                                   | > +\-\-\-\-\-\-                   |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \|\                          |
|                                   | > \| \| \| Pod \| \| \|\          |
|                                   | > \| \| \|                        |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\  |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \| \|\                       |
|                                   | > \| \| \| \| Container: webapp   |
|                                   | > \| \| \| \|\                    |
|                                   | > \| \| \| \| \| \| \| \|\        |
|                                   | > \| \| \| \| - Image:            |
|                                   | > nginx:alpine \| \| \| \|\       |
|                                   | > \| \| \| \| - Port: 80 \| \| \| |
|                                   | > \|\                             |
|                                   | > \| \| \| \| \| \| \| \|\        |
|                                   | > \| \| \| \| EnvFrom: \| \| \|   |
|                                   | > \|\                             |
|                                   | > \| \| \| \| ConfigMap:          |
|                                   | > webapp-config \| \| \| \|\      |
|                                   | > \| \| \| \| \| \| \| \|\        |
|                                   | > \| \| \| \| VolumeMount: \| \|  |
|                                   | > \| \|\                          |
|                                   | > \| \| \| \| Name: config \| \|  |
|                                   | > \| \|\                          |
|                                   | > \| \| \| \| MountPath:          |
|                                   | > /usr/share/\... \| \| \| \|\    |
|                                   | > \| \| \|                        |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\  |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \| \|\                       |
|                                   | > \| \| \| \| \| \|\              |
|                                   | > \| \| \|                        |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\  |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \| \|\                       |
|                                   | > \| \| \| \| Volume: config \|   |
|                                   | > \| \| \|\                       |
|                                   | > \| \| \| \| ConfigMap:          |
|                                   | > webapp-content \| \| \| \|\     |
|                                   | > \| \| \| \| Key: index.html \|  |
|                                   | > \| \| \|\                       |
|                                   | > \| \| \| \| Path: index.html \| |
|                                   | > \| \| \|\                       |
|                                   | > \| \| \|                        |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\  |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \| \|\                       |
|                                   | > \| \|                           |
|                                   | > +\-\-\-\-\-\-                   |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \| \|\                          |
|                                   | > \|                              |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-       |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > \| \|\                          |
|                                   | > \|                              |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-       |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > \| \| Service: webapp-service   |
|                                   | > \| \|\                          |
|                                   | > \| \| \| \|\                    |
|                                   | > \| \| Selector: app: webapp \|  |
|                                   | > \|\                             |
|                                   | > \| \| Port: 80 -\> targetPort:  |
|                                   | > 80 \| \|\                       |
|                                   | > \|                              |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-       |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > \| \|\                          |
|                                   | > \|                              |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-       |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > \| \| Ingress: webapp-ingress   |
|                                   | > \| \|\                          |
|                                   | > \| \| \| \|\                    |
|                                   | > \| \| Host: webapp.example.com  |
|                                   | > \| \|\                          |
|                                   | > \| \| Path: / \| \|\            |
|                                   | > \| \| Backend:                  |
|                                   | > webapp-service:80 \| \|\        |
|                                   | > \|                              |
|                                   | > +\-\-\-\-\-\-\-\-\-\-\-\-       |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
|                                   | > \|\                             |
|                                   | > +\-\-\                          |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- |
|                                   | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ |
|                                   | -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+ |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> This updated diagram now includes:
>
> 1\. The original webapp-config ConfigMap with BACKGROUND_COLOR and
> MESSAGE . 2. The webapp-content ConfigMap containing the index.html
> template.
>
> 3\. The Deployment and Pod structure, showing how these ConfigMaps are
> used.
>
> 4\. The webapp-service Service that exposes the Pods.
>
> 5\. The new webapp-ingress Ingress resource, which:

+-----------------------------------+-----------------------------------+
| ![](vertopal_c4f4baa402e647588    | > Routes traffic for the host     |
| ecb2a507c21de28/media/image178.pn | > webapp.example.com\             |
| g){width="5.555555555555555e-2in" | > Directs all paths ( / ) to the  |
| height="5.555555555555555e-2in"}  | > webapp-service on port 80       |
+===================================+===================================+
| ![](vertopal_c4f4baa402e647588    |                                   |
| ecb2a507c21de28/media/image179.pn |                                   |
| g){width="5.555555555555555e-2in" |                                   |
| height="5.555555555555555e-2in"}  |                                   |
+-----------------------------------+-----------------------------------+
|                                   |                                   |
+-----------------------------------+-----------------------------------+

> The Ingress resource acts as an entry point for external traffic into
> the cluster. It provides:

+-----------------------------------+-----------------------------------+
| ![](vertopal_c4f4baa402e647588e   | > Host-based routing: It routes   |
| cb2a507c21de28/media/image180.png | > traffic based on the            |
| ){width="4.1666666666666664e-2in" | > webapp.example.com hostname.    |
| height="4.1666666666666664e-2in"} | >                                 |
|                                   | > Path-based routing: In this     |
|                                   | > case, all paths ( / ) are       |
|                                   | > routed to the backend service.  |
|                                   | >                                 |
|                                   | > Integration with the Ingress    |
|                                   | > Controller: The                 |
|                                   | > nginx.ingr                      |
|                                   | ess.kubernetes.io/rewrite-target: |
|                                   | > / annotation is specific to the |
|                                   | > NGINX                           |
+===================================+===================================+
| ![](vertopal_c4f4baa402e647588e   |                                   |
| cb2a507c21de28/media/image181.png |                                   |
| ){width="4.1666666666666664e-2in" |                                   |
| height="5.555555555555555e-2in"}  |                                   |
+-----------------------------------+-----------------------------------+
| ![](vertopal_c4f4baa402e647588e   |                                   |
| cb2a507c21de28/media/image182.png |                                   |
| ){width="4.1666666666666664e-2in" |                                   |
| height="4.1666666666666664e-2in"} |                                   |
+-----------------------------------+-----------------------------------+

> Ingress Controller, indicating that the path should be rewritten to /
> when forwarding to the backend.
>
> The flow of traffic would now be:External Request -\> Ingress
> Controller -\> Ingress (webapp-ingress) -\> Service (webapp-service)
> -\> Pod
>
> (webapp) -\> Container (nginx:alpine)This setup allows you to:
>
> 1\. Access your application from outside the cluster using a domain
> name ( webapp.example.com ).
>
> 2\. Potentially host multiple applications on the same IP address
> using different hostnames.
>
> 3\. Implement more complex routing rules if needed (e.g., routing
> different paths to different services).
>
> Remember to ensure that:
>
> ![](converted/media/image183.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}The Ingress Controller is installed
> in your cluster.
>
> ![](converted/media/image184.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}The DNS for webapp.example.com is
> configured to point to your cluster\'s external IP.
>
> ![](converted/media/image141.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Any necessary TLS certificates are
> configured if you want to enable HTTPS.
>
> This Ingress resource completes the basic setup of a web application
> in Kubernetes, providing a full path for external traffic to reach
> your
>
> containerized application.
>
> ![](converted/media/image185.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Step 6: Verify the deployment
>
> Check if all resources are created and running:

  -----------------------------------------------------------------------
  kubectl get configmaps
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

  -----------------------------------------------------------------------
  kubectl get deployments
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

  -----------------------------------------------------------------------
  kubectl get pods
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

  -----------------------------------------------------------------------
  kubectl get services
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

+-----------------------------------+-----------------------------------+
|                                   |   ------------------------------  |
|                                   |   kubectl get ingress             |
|                                   |   ------------------------------  |
|                                   |                                   |
|                                   |   ------------------------------  |
+===================================+===================================+
| > 1\                              | > kubectl get configmaps\         |
| > 2\                              | > NAME DATA AGE\                  |
| > 3\                              | > kube-root-ca.crt 1 21m\         |
| > 4\                              | > webapp-config 2 18m\            |
| > 5                               | > webapp-content 1 13m            |
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 6\                              | > kubectl get deployments\        |
| > 7\                              | > NAME READY UP-TO-DATE AVAILABLE |
| > 8\                              | > AGE\                            |
| > 9                               | > webapp 2/2 2 2 11m              |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 10\                             | > kubectl get pods\               |
| > 11\                             | > NAME READY STATUS RESTARTS AGE  |
| > 12\                             | > webapp-756448c658-8h5lz 1/1     |
| > 13\                             | > Running 0 7m26s                 |
| > 14                              | > webapp-756448c658-b6gnr 1/1     |
|                                   | > Running 0 7m33s                 |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 15\                             | > kubectl get services\           |
| > 16\                             | > NAME TYPE CLUSTER-IP            |
| > 17\                             | > EXTERNAL-IP PORT(S) AGE         |
| > 18                              | > kubernetes ClusterIP 10.96.0.1  |
|                                   | > \<none\> 443/TCP 22m            |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| 19                                | > webapp-service ClusterIP        |
|                                   | > 10.107.192.80 \<none\> 80/TCP   |
|                                   | > 5m20s                           |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 20                              |                                   |
+===================================+===================================+
| 21                                | > kubectl get ingress             |
+-----------------------------------+-----------------------------------+
| 22                                | > NAME CLASS HOSTS ADDRESS PORTS  |
|                                   | > AGE                             |
+-----------------------------------+-----------------------------------+
| 23                                | > webapp-ingress \<none\>         |
|                                   | > webapp.example.com 80 3m52s     |
+-----------------------------------+-----------------------------------+
| ![](vertopal_c4f4baa402e647588e   | > **Step 7:** Access the          |
| cb2a507c21de28/media/image186.png | > application                     |
| ){width="4.1666666666666664e-2in" |                                   |
| height="4.1666666666666664e-2in"} |                                   |
+-----------------------------------+-----------------------------------+

> If you\'re using Minikube, you can use port-forwarding to access the
> application:

  -----------------------------------------------------------------------
  kubectl port-forward service/webapp-service 8080:80
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

Then open a web browser and go to http://localhost:8080 .If you\'re
using an Ingress, add the following to your /etc/hosts file:

  -----------------------------------------------------------------------
  echo \"127.0.0.1 web-app.info\" \| sudo tee -a /etc/hosts
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

> Then access the application at http://webapp.example.com .
>
> ![](converted/media/image187.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}**Step 8:** Modify the configuration
>
> Let\'s change the background color and message:

  -----------------------------------------------------------------------
  kubectl edit configmap webapp-config
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

> Change the BACKGROUND_COLOR to \"#e0e0e0\" and the MESSAGE to
> \"Updated configuration!\" .
>
> ![](converted/media/image188.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}**Step 9:** Restart the Deployment to
> pick up the new configuration

+-----------------------------------+-----------------------------------+
|                                   |   ------------------------------  |
|                                   |   kubectl rollout restart         |
|                                   |   deployment webapp               |
|                                   |   ------------------------------  |
|                                   |                                   |
|                                   |   ------------------------------  |
+===================================+===================================+
| ![](vertopal_c4f4baa402e647588e   | **Step 10:** Access the           |
| cb2a507c21de28/media/image189.png | application again to see the      |
| ){width="4.1666666666666664e-2in" | changes                           |
| height="5.555555555555555e-2in"}  |                                   |
+-----------------------------------+-----------------------------------+

> **Day 5: Working with local K8s options**
>
> **Docker Images in kind**
>
> **Building a custom Docker image**
>
> ![](converted/media/image190.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}Create a Dockerfile for your
> application.
>
> ![](converted/media/image191.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Build the image: docker build -t
> your-image:tag .
>
> **Loading the image into kind cluster**
>
> ![](converted/media/image192.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}Use the command: kind load
> docker-image your-image:tag
>
> ![](converted/media/image193.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}This copies the image from your local
> Docker daemon into the kind cluster.
>
> **Limitations and workarounds for Docker-in-Docker scenarios**
>
> ![](converted/media/image194.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}kind runs Kubernetes inside Docker,
> which can complicate building images inside the cluster.
>
> ![](converted/media/image117.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Workaround: Use kaniko or buildkit
> for in-cluster builds.
>
> **Creating deployments with custom images**

+-----------------------------------+-----------------------------------+
| ![](vertopal_c4f4baa402e647588e   | > Create a deployment YAML file   |
| cb2a507c21de28/media/image195.png | > (e.g., deployment.yaml )        |
| ){width="4.1666666666666664e-2in" | > referencing your custom image:  |
| height="5.555555555555555e-2in"}  |                                   |
+===================================+===================================+
| 1                                 | +------------------------------+  |
|                                   | | > apiVersion: apps/v1        |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+-----------------------------------+-----------------------------------+
| 2                                 | > kind: Deployment                |
+-----------------------------------+-----------------------------------+
| 3                                 | > metadata:                       |
+-----------------------------------+-----------------------------------+
| 4                                 | > name: your-app                  |
+-----------------------------------+-----------------------------------+
| 5                                 | > spec:                           |
+-----------------------------------+-----------------------------------+
| 6                                 | > replicas: 1                     |
+-----------------------------------+-----------------------------------+
| 7                                 | > selector:                       |
+-----------------------------------+-----------------------------------+
| 8                                 | > matchLabels:                    |
+-----------------------------------+-----------------------------------+
| 9                                 | > app: your-app                   |
+-----------------------------------+-----------------------------------+
| 10                                | > template:                       |
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| 11                                | +------------------------------+  |
|                                   | | > metadata:                  |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
| 12                                | > labels:                         |
+-----------------------------------+-----------------------------------+
| 13                                | > app: your-app                   |
+-----------------------------------+-----------------------------------+
| 14                                | > spec:                           |
+-----------------------------------+-----------------------------------+
| 15                                | > containers:                     |
+-----------------------------------+-----------------------------------+
| 16                                | > \- name: your-app               |
+-----------------------------------+-----------------------------------+
| 17                                | > image: your-image:tag           |
+-----------------------------------+-----------------------------------+
| 18                                | > imagePullPolicy: Never          |
+-----------------------------------+-----------------------------------+
| ![](vertopal_c4f4baa402e647588e   | > Apply the deployment: kubectl   |
| cb2a507c21de28/media/image196.png | > apply -f deployment.yaml        |
| ){width="4.1666666666666664e-2in" |                                   |
| height="4.1666666666666664e-2in"} |                                   |
+-----------------------------------+-----------------------------------+

> **Working with Images in Minikube**
>
> Minikube provides several options for working with Docker images:
>
> **Using the Host Docker Daemon**
>
> ![](converted/media/image197.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Configure your terminal to use
> Minikube\'s Docker daemon:

+-----------------------------------+-----------------------------------+
|                                   |   ------------------------------  |
|                                   |   eval \$(minikube docker-env)    |
|                                   |   ------------------------------  |
|                                   |                                   |
|                                   |   ------------------------------  |
+===================================+===================================+
| ![](vertopal_c4f4baa402e647588e   | Build your image. It will now be  |
| cb2a507c21de28/media/image198.png | available to Minikube without     |
| ){width="4.1666666666666664e-2in" | additional steps.                 |
| height="4.1666666666666664e-2in"} |                                   |
+-----------------------------------+-----------------------------------+

> **Loading Images into Minikube**
>
> ![](converted/media/image199.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}If you\'ve built the image using your
> host\'s Docker daemon:

+-----------------------------------+-----------------------------------+
|                                   |   ------------------------------  |
|                                   |   minikube image load             |
|                                   |   your-image:tag                  |
|                                   |   ------------------------------  |
|                                   |                                   |
|                                   |   ------------------------------  |
+===================================+===================================+
| ![](vertopal_c4f4baa402e647588e   | This copies the image from your   |
| cb2a507c21de28/media/image200.png | local Docker daemon into          |
| ){width="4.1666666666666664e-2in" | Minikube.                         |
| height="4.1666666666666664e-2in"} |                                   |
+-----------------------------------+-----------------------------------+

> **Creating Deployments with Custom Images**

+-----------------------------------+-----------------------------------+
| ![](vertopal_c4f4baa402e647588e   | > Create a deployment YAML file   |
| cb2a507c21de28/media/image201.png | > (e.g., deployment.yaml )        |
| ){width="4.1666666666666664e-2in" | > referencing your custom image:  |
| height="4.1666666666666664e-2in"} |                                   |
+===================================+===================================+
| 1                                 | > apiVersion: apps/v1             |
+-----------------------------------+-----------------------------------+
| 2                                 | > kind: Deployment                |
+-----------------------------------+-----------------------------------+
| 3                                 | > metadata:                       |
+-----------------------------------+-----------------------------------+
| 4                                 | > name: your-app                  |
+-----------------------------------+-----------------------------------+
| 5                                 | > spec:                           |
+-----------------------------------+-----------------------------------+
| 6                                 | > replicas: 1                     |
+-----------------------------------+-----------------------------------+
| 7                                 | > selector:                       |
+-----------------------------------+-----------------------------------+
| 8                                 | > matchLabels:                    |
+-----------------------------------+-----------------------------------+
| 9                                 | > app: your-app                   |
+-----------------------------------+-----------------------------------+
| 10                                | > template:                       |
+-----------------------------------+-----------------------------------+
| 11                                | > metadata:                       |
+-----------------------------------+-----------------------------------+
| 12                                | > labels:                         |
+-----------------------------------+-----------------------------------+
| 13                                | > app: your-app                   |
+-----------------------------------+-----------------------------------+
| 14                                | > spec:                           |
+-----------------------------------+-----------------------------------+
| 15                                | > containers:                     |
+-----------------------------------+-----------------------------------+
| 16                                | > \- name: your-app               |
+-----------------------------------+-----------------------------------+
| 17                                | > image: your-image:tag           |
+-----------------------------------+-----------------------------------+
| 18                                | > imagePullPolicy: IfNotPresent   |
+-----------------------------------+-----------------------------------+
| ![](vertopal_c4f4baa402e647588e   | > Apply the deployment: kubectl   |
| cb2a507c21de28/media/image202.png | > apply -f deployment.yaml        |
| ){width="4.1666666666666664e-2in" |                                   |
| height="4.1666666666666664e-2in"} |                                   |
+-----------------------------------+-----------------------------------+

> **Minikube-Specific Features**
>
> **Built-in Docker Registry**
>
> Minikube includes a built-in Docker registry. To use it:
>
> ![](converted/media/image203.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}Enable the registry addon:

  -----------------------------------------------------------------------
  minikube addons enable registry
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

> ![](converted/media/image204.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Push your image to the Minikube
> registry:

  ---------------------------------------------------------------------------------------------------------------------------------------
                                                                                                      docker push \$(minikube
                                                                                                      ip):5000/your-image:tag
  --------------------------------------------------------------------------------------------------- -----------------------------------
  ![](converted/media/image205.png){width="4.1666666666666664e-2in"   Update your deployment to use the
  height="4.1666666666666664e-2in"}                                                                   registry image:

  ---------------------------------------------------------------------------------------------------------------------------------------

  -----------------------------------------------------------------------
  image: localhost:5000/your-image:tag
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

**Direct Image Building**

> ![](converted/media/image206.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Minikube can build images directly
> using its Docker daemon:

+-----------------------------------+-----------------------------------+
|                                   |   ------------------------------  |
|                                   |   minikube image build -t         |
|                                   |   your-image:tag .                |
|                                   |   ------------------------------  |
|                                   |                                   |
|                                   |   ------------------------------  |
+===================================+===================================+
| ![](vertopal_c4f4baa402e647588e   | This builds the image inside      |
| cb2a507c21de28/media/image207.png | Minikube, making it immediately   |
| ){width="4.1666666666666664e-2in" | available for use.                |
| height="5.555555555555555e-2in"}  |                                   |
+-----------------------------------+-----------------------------------+

**Monitoring and Troubleshooting**

> ![](converted/media/image208.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Check if your pods are running:

+-----------------------------------+-----------------------------------+
|                                   |   ------------------------------  |
|                                   |   kubectl get pods                |
|                                   |   ------------------------------  |
|                                   |                                   |
|                                   |   ------------------------------  |
+===================================+===================================+
| ![](vertopal_c4f4baa402e647588e   | If pods are not in the            |
| cb2a507c21de28/media/image209.png | \"Running\" state, check the      |
| ){width="4.1666666666666664e-2in" | logs:                             |
| height="4.1666666666666664e-2in"} |                                   |
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
|                                   |   ------------------------------  |
|                                   |   kubectl logs \<pod-name\>       |
|                                   |   ------------------------------  |
|                                   |                                   |
|                                   |   ------------------------------  |
+===================================+===================================+
| ![](vertopal_c4f4baa402e647588e   | For more detailed                 |
| cb2a507c21de28/media/image210.png | troubleshooting, use:             |
| ){width="4.1666666666666664e-2in" |                                   |
| height="5.555555555555555e-2in"}  |                                   |
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
|                                   |   ------------------------------  |
|                                   |   kubectl describe pod            |
|                                   |   \<pod-name\>                    |
|                                   |   ------------------------------  |
|                                   |                                   |
|                                   |   ------------------------------  |
+===================================+===================================+
| ![](vertopal_c4f4baa402e647588e   | To access the Minikube Docker     |
| cb2a507c21de28/media/image211.png | daemon logs:                      |
| ){width="4.1666666666666664e-2in" |                                   |
| height="5.555555555555555e-2in"}  |                                   |
+-----------------------------------+-----------------------------------+

  -----------------------------------------------------------------------
  minikube logs
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

**Cleaning Up**

To remove unused images and free up space:

  -----------------------------------------------------------------------
  minikube image rm your-image:tag
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

By following these steps, you can effectively work with custom Docker
images in your Minikube cluster, allowing you to develop and test

your Kubernetes deployments locally. Minikube offers more flexibility in
terms of image handling compared to kind, making it a popular

choice for local Kubernetes development.

**Best Practices**

> 1\. Use meaningful tags for your images, preferably based on git
> commit hashes or semantic versioning.
>
> 2\. When updating your application, build a new image with a new tag,
> then update your deployment to use the new image tag.
>
> 3\. For production-like setups, consider using a private Docker
> registry. Minikube can be configured to pull from private registries.
>
> Week 2: Service Mesh Concepts and Python
>
> **Day 1-2: Service Mesh**

**Fundamentals**

> **Core concepts of service mesh**
>
> ![](converted/media/image212.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}A dedicated infrastructure layer for
> handling service-to-service communication.
>
> ![](converted/media/image213.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Provides features like service
> discovery, load balancing, encryption, observability, traceability,
> authentication, and authorization.
>
> **Problems service meshes solve**
>
> ![](converted/media/image214.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}Complexity in microservices
> communication
>
> ![](converted/media/image215.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Lack of observability in distributed
> systems
>
> ![](converted/media/image216.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}Inconsistent security policies across
> services
>
> ![](converted/media/image217.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Difficulty in implementing resilience
> patterns (circuit breaking, retries)
>
> **Evolution of ingress**
>
> ![](converted/media/image218.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}From simple L7 load balancers to
> advanced API gateways
>
> ![](converted/media/image219.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Integration with service mesh for
> consistent policy enforcement

**Service Mesh Architecture**\
A service mesh consists of two primary components: the data plane and
the control plane.

**Data Plane**\
The data plane is composed of a network of lightweight proxies,
typically deployed as sidecars alongside each service instance. These
proxies intercept and manage all network traffic to and from the
service.

**Example:**\
Let\'s consider a simple e-commerce application with three
microservices: Product, Order, and Payment. In a service mesh, each
instance of these services would have a sidecar proxy deployed alongside
it:

+-----------------------------------+-----------------------------------+
| > 1\                              | +------------------------------+  |
| > 2\                              | | > Product Service + Sidecar  |  |
| > 3                               | | > Proxy                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > Order Service + Sidecar    |  |
|                                   | | > Proxy                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > Payment Service + Sidecar  |  |
|                                   | | > Proxy                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

When the Order service needs to communicate with the Payment service,
the request goes through the following path: 1. Order service -\>
Order\'s sidecar proxy\
2. Order\'s sidecar proxy -\> Payment\'s sidecar proxy\
3. Payment\'s sidecar proxy -\> Payment service\
This allows the mesh to control and observe all inter-service
communication.

**Control Plane**\
The control plane manages and configures the proxies to enforce
policies, collect telemetry, and handle service discovery.

**Example:**\
Using Istio as an example, the control plane consists of several
components:

> ![](converted/media/image220.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Pilot: Handles service discovery and
> traffic management
>
> ![](converted/media/image221.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Citadel: Manages security and access
> policies

![](converted/media/image222.png){width="4.1666666666666664e-2in"
height="4.1666666666666664e-2in"}Galley: Validates configuration and
distributes it to other components\
The control plane would configure the sidecar proxies to implement
specific routing rules, such as:

+-----------------------------------+-----------------------------------+
| 1\                                | > apiVersion:                     |
| 2\                                | > networking.istio.io/v1alpha3\   |
| 3\                                | > kind: VirtualService\           |
| 4\                                | > metadata:\                      |
| 5\                                | > name: payment-route\            |
| 6\                                | > spec:\                          |
| 7\                                | > hosts:\                         |
| 8\                                | > - payment\                      |
| 9\                                | > http:\                          |
| 10 11 12 13 14 15 16 17           | > - route:\                       |
|                                   | > - destination:\                 |
|                                   | > host: payment\                  |
|                                   | > subset: v1\                     |
|                                   | > weight: 90\                     |
|                                   | > - destination:\                 |
|                                   | > host: payment\                  |
|                                   | > subset: v2\                     |
|                                   | > weight: 10                      |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> This configuration would route 90% of traffic to version 1 of the
> Payment service and 10% to version 2, enabling canary deployments or
> A/B testing.
>
> Here is an example using Linkerd\'s control plane. This is simpler and
> consists of fewer components compared to Istio. The main components
> are:
>
> 1\. Destination: Handles service discovery and provides configuration
> to proxies
>
> 2\. Identity: Manages security and certificate issuance for mTLS
>
> 3\. Proxy Injector: Injects the Linkerd proxy as a sidecar
>
> For traffic splitting in Linkerd, you would use either a TrafficSplit
> resource (if using the SMI extension) or an HTTPRoute resource (which
> is the preferred method going forward).\
> Here\'s an example using HTTPRoute:

+-----------------------------------+-----------------------------------+
| 1\                                | > text\                           |
| 2\                                | > apiVersion:                     |
| 3\                                | > policy.linkerd.io/v1beta2\      |
| 4\                                | > kind: HTTPRoute\                |
| 5\                                | > metadata:\                      |
| 6\                                | > name: payment-route\            |
| 7\                                | > namespace: your-namespace\      |
| 8\                                | > spec:\                          |
| 9\                                | > parentRefs:\                    |
| 10 11 12 13 14 15 16 17 18 19 20  | > - name: payment\                |
|                                   | > kind: Service\                  |
|                                   | > group: core\                    |
|                                   | > port: 8080\                     |
|                                   | > rules:\                         |
|                                   | > - backendRefs:\                 |
|                                   | > - name: payment-v1\             |
|                                   | > port: 8080\                     |
|                                   | > weight: 90\                     |
|                                   | > - name: payment-v2\             |
|                                   | > port: 8080\                     |
|                                   | > weight: 10                      |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> 21
>
> This configuration would achieve the same result as the Istio example,
> routing 90% of traffic to version 1 of the Payment service and 10% to
> version 2.
>
> **Key Features and Use Cases**
>
> **Service Discovery and Load Balancing**
>
> Service meshes provide dynamic service discovery and intelligent load
> balancing.
>
> **Example:**\
> In our e-commerce application, if we scale the Payment service to
> three instances, the service mesh would automatically discover these
> instances and distribute traffic among them. It could use advanced
> load balancing algorithms like least connections or weighted
> round-robin.
>
> **Traffic Management**
>
> Service meshes offer fine-grained control over traffic routing.
>
> **Example:**\
> Implementing a canary release for the Product service:

+-----------------------------------+-----------------------------------+
| > 1\                              | > apiVersion:                     |
| > 2\                              | > networking.istio.io/v1alpha3\   |
| > 3\                              | > kind: VirtualService\           |
| > 4                               | > metadata:\                      |
|                                   | > name: product-canary            |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| 5\                                | > spec:\                          |
| 6\                                | > hosts:\                         |
| 7\                                | > - product\                      |
| 8\                                | > http:\                          |
| 9\                                | > - match:\                       |
| 10 11 12 13 14 15 16 17 18 19 20  | > - headers:\                     |
|                                   | > user-agent:\                    |
|                                   | > regex: \".\*Chrome.\*\"\        |
|                                   | > route:\                         |
|                                   | > - destination:\                 |
|                                   | > host: product\                  |
|                                   | > subset: v2\                     |
|                                   | > - route:\                       |
|                                   | > - destination:\                 |
|                                   | > host: product\                  |
|                                   | > subset: v1                      |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> This configuration routes all traffic from Chrome browsers to version
> 2 of the Product service, while all other traffic goes to version 1.
>
> With Linkerd use HTTPRoute resource to define the traffic splitting:

+-----------------------------------+-----------------------------------+
| 1\                                | > text\                           |
| 2\                                | > apiVersion:                     |
| 3\                                | > policy.linkerd.io/v1beta2\      |
| 4\                                | > kind: HTTPRoute\                |
| 5\                                | > metadata:\                      |
| 6\                                | > name: product-canary\           |
| 7\                                | > namespace: your-namespace\      |
| 8\                                | > spec:\                          |
| 9\                                | > parentRefs:\                    |
| 10 11 12 13 14 15 16 17 18 19 20  | > - name: product\                |
| 21 22 23                          | > kind: Service\                  |
|                                   | > group: core\                    |
|                                   | > port: 8080\                     |
|                                   | > rules:\                         |
|                                   | > - matches:\                     |
|                                   | > - headers:\                     |
|                                   | > - name: user-agent\             |
|                                   | > regex: \".\*Chrome.\*\"\        |
|                                   | > backendRefs:\                   |
|                                   | > - name: product-v2\             |
|                                   | > port: 8080\                     |
|                                   | > - backendRefs:\                 |
|                                   | > - name: product-v1\             |
|                                   | > port: 8080                      |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> 24
>
> This configuration routes all traffic from Chrome browsers to version
> 2 of the Product service, while all other traffic goes to version 1.
> For more advanced canary deployments, you can use tools like Flagger
> with Linkerd. Flagger automates the process of creating new Kubernetes
> resources, watching metrics, and incrementally sending users to the
> new version.
>
> Here\'s an example of how you might set up a Flagger canary for the
> Product service:

+-----------------------------------+-----------------------------------+
| > 1\                              | +------------------------------+  |
| > 2\                              | | > text                       |  |
| > 3\                              | +==============================+  |
| > 4\                              | +------------------------------+  |
| > 5\                              |                                   |
| > 6\                              | +------------------------------+  |
| > 7\                              | | > apiVersion:                |  |
| > 8                               | | > flagger.app/v1beta1        |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > kind: Canary               |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > metadata:                  |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > name: product              |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > namespace: test            |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > spec:                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > targetRef:                 |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 9\                              | > apiVersion: apps/v1\            |
| > 10\                             | > kind: Deployment\               |
| > 11\                             | > name: product\                  |
| > 12\                             | > service:\                       |
| > 13\                             | > port: 8080\                     |
| > 14\                             | > analysis:\                      |
| > 15\                             | > interval: 30s\                  |
| > 16\                             | > threshold: 5\                   |
| > 17\                             | > maxWeight: 50\                  |
| > 18\                             | > stepWeight: 5\                  |
| > 19\                             | > metrics:\                       |
| > 20\                             | > - name: success-rate\           |
| > 21\                             | > threshold: 99\                  |
| > 22\                             | > interval: 1m\                   |
| > 23\                             | > - name: latency\                |
| > 24\                             | > threshold: 500\                 |
| > 25                              | > interval: 1m                    |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> 26

This configuration sets up a canary deployment that gradually increases
traffic to the new version while monitoring success rate and latency.

> **Observability**\
> Service meshes provide detailed insights into service-to-service
> communication.
>
> **Example:**\
> Using Istio with Prometheus and Grafana, you can visualize request
> volume, latency, and error rates for each service. You might see a
> dashboard showing:
>
> ![](converted/media/image223.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Request rate for Product service: 100
> requests/second
>
> ![](converted/media/image224.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}95th percentile latency for Order
> service: 250ms
>
> ![](converted/media/image225.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Error rate for Payment service: 0.1%
>
> This level of observability helps quickly identify and troubleshoot
> issues in the distributed system.
>
> Linkerd provides similar observability capabilities to Istio, there
> are some differences in how it implements and presents these
> features. 1. Using the Linkerd CLI:

  -----------------------------------------------------------------------
  linkerd viz stat deploy -n your-namespace
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

> This command would show you a table with metrics for each deployment,
> including:
>
> ![](converted/media/image226.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}Success rate
>
> ![](converted/media/image227.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}Request per second (RPS)
>
> ![](converted/media/image228.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Latency (P50, P95, P99)\
> 2. Using the Linkerd dashboard:\
> You can access it by running:

  -----------------------------------------------------------------------
  linkerd viz dashboard
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

> In the dashboard, you would see:
>
> ![](converted/media/image229.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Request rate for Product service: 100
> req/sec
>
> ![](converted/media/image230.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}95th percentile latency for Order
> service: 250ms
>
> ![](converted/media/image231.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Success rate for Payment service:
> 99.9% (which is equivalent to a 0.1% error rate)
>
> **Security**\
> Service meshes can enforce mutual TLS (mTLS) encryption and
> fine-grained access policies.
>
> **Example:**\
> Enforcing mTLS between all services:

+-----------------------------------+-----------------------------------+
| > 1\                              | +------------------------------+  |
| > 2\                              | | > apiVersion:                |  |
| > 3\                              | | > security.istio.io/v1beta1  |  |
| > 4\                              | +==============================+  |
| > 5\                              | +------------------------------+  |
| > 6\                              |                                   |
| > 7\                              | +------------------------------+  |
| > 8                               | | > kind: PeerAuthentication   |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > metadata:                  |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > name: default              |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > namespace: istio-system    |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > spec:                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > mtls:                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > mode: STRICT               |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> This configuration ensures all inter-service communication is
> encrypted and authenticated.
>
> Linkerd automatically enables mTLS for all meshed services by default,
> so you don\'t need to explicitly configure it. However, if you want to
> ensure that only mTLS traffic is allowed, you can use Linkerd\'s
> authorization policies.
>
> **Challenges and Best Practices**
>
> While service meshes offer numerous benefits, they also introduce
> complexity and potential performance overhead.
>
> **Performance Considerations**
>
> The additional network hops introduced by sidecar proxies can increase
> latency. It\'s crucial to benchmark your application with and without
> the service mesh to understand the performance impact.
>
> **Best Practice:**Start with a subset of your services in the mesh and
> gradually expand as you become more comfortable with the technology
> and its impact on your system.
>
> **Complexity Management**
>
> Service meshes add another layer to your infrastructure, which can
> increase operational complexity.
>
> **Best Practice:**Invest time in your training.
>
> **Monitoring and Troubleshooting**
>
> While service meshes provide extensive observability, the volume of
> data can be overwhelming.
>
> **Best Practice:**Define clear Service Level Objectives (SLOs) and set
> up alerts based on these. Use distributed tracing to debug complex
> issues across services.
>
> In conclusion, service meshes offer powerful capabilities for managing
> microservices architectures, but they require careful planning and
> implementation. By understanding the core concepts and following best
> practices, organizations can leverage service meshes to build more
> resilient, observable, and secure distributed systems.
>
> **Day 3-4: Python for Kubernetes**
>
> **Python basics review (if needed)**
>
> **Data Types**
>
> Python has several built-in data types:

+-----------------------------------+-----------------------------------+
| ![](vertopal_c4f4baa402e647588e   | > **Numeric**: int, float,        |
| cb2a507c21de28/media/image232.png | > complex\                        |
| ){width="4.1666666666666664e-2in" | > **Sequence**: list, tuple,      |
| height="4.1666666666666664e-2in"} | > range\                          |
|                                   | > **Text**: str\                  |
| ![](vertopal_c4f4baa402e647588e   | > **Mapping**: dict\              |
| cb2a507c21de28/media/image233.png | > **Set**: set, frozenset\        |
| ){width="4.1666666666666664e-2in" | > **Boolean**: bool               |
| height="4.1666666666666664e-2in"} |                                   |
|                                   |                                   |
| ![](vertopal_c4f4baa402e647588e   |                                   |
| cb2a507c21de28/media/image234.png |                                   |
| ){width="4.1666666666666664e-2in" |                                   |
| height="4.1666666666666664e-2in"} |                                   |
|                                   |                                   |
| ![](vertopal_c4f4baa402e647588e   |                                   |
| cb2a507c21de28/media/image235.png |                                   |
| ){width="4.1666666666666664e-2in" |                                   |
| height="4.1666666666666664e-2in"} |                                   |
|                                   |                                   |
| ![](vertopal_c4f4baa402e647588e   |                                   |
| cb2a507c21de28/media/image236.png |                                   |
| ){width="4.1666666666666664e-2in" |                                   |
| height="4.1666666666666664e-2in"} |                                   |
|                                   |                                   |
| ![](vertopal_c4f4baa402e647588e   |                                   |
| cb2a507c21de28/media/image237.png |                                   |
| ){width="4.1666666666666664e-2in" |                                   |
| height="4.1666666666666664e-2in"} |                                   |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> Example:
>
> **Numeric Types**
>
> int (Integer)

+-----------------------------------+-----------------------------------+
| > 1\                              | +------------------------------+  |
| > 2\                              | | > age = 30                   |  |
| > 3\                              | +==============================+  |
| > 4                               | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > year = 2024                |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > temperature = -5           |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > x = 5                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> float (Floating-point)

+-----------------------------------+-----------------------------------+
| > 1\                              | +------------------------------+  |
| > 2\                              | | > pi = 3.14159               |  |
| > 3\                              | +==============================+  |
| > 4                               | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > weight = 68.5              |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > temperature = -2.8         |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > y = 3.14                   |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> complex

+-----------------------------------+-----------------------------------+
| 1\                                | +------------------------------+  |
| 2                                 | | > z = 3 + 4j                 |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > w = complex(2, -3)         |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **Sequence Types**
>
> list

+-----------------------------------+-----------------------------------+
| > 1\                              | > fruits = \[\"apple\",           |
| > 2\                              | > \"banana\", \"cherry\"\]\       |
| > 3                               | > numbers = \[1, 2, 3, 4, 5\]\    |
|                                   | > mixed = \[1, \"two\", 3.0, \[4, |
|                                   | > 5\]\]                           |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> tuple

+-----------------------------------+-----------------------------------+
| > 1\                              | > coordinates = (10, 20)\         |
| > 2\                              | > rgb = (255, 0, 128)\            |
| > 3                               | > person = (\"John\", 30,         |
|                                   | > \"London\")                     |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> range

+-----------------------------------+-----------------------------------+
| 1\                                | +------------------------------+  |
| 2                                 | | > numbers = range(5) \# 0,   |  |
|                                   | | > 1, 2, 3, 4                 |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > even_numbers = range(0,    |  |
|                                   | | > 10, 2) \# 0, 2, 4, 6, 8    |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **Text Type**
>
> str (String)

+-----------------------------------+-----------------------------------+
| > 1\                              | +------------------------------+  |
| > 2\                              | | > name = \"Alice\"           |  |
| > 3\                              | +==============================+  |
| > 4                               | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > message = \'Hello,         |  |
|                                   | | > World!\'                   |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > multiline = \"\"\"This is  |  |
|                                   | | > a                          |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > multiline string.\"\"\"    |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **Mapping Type**
>
> dict (Dictionary)

+-----------------------------------+-----------------------------------+
| 1\                                | > person = {\"name\": \"Bob\",    |
| 2                                 | > \"age\": 25, \"city\":          |
|                                   | > \"Manchester\"}\                |
|                                   | > scores = {                      |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------+-----------------------+-----------------------+
| 3                     | }                     | +------------------+  |
|                       |                       | | > \"Alice\": 95, |  |
|                       |                       | +==================+  |
|                       |                       | +------------------+  |
+=======================+=======================+=======================+
| 4                     |                       | > \"Bob\": 87,        |
+-----------------------+-----------------------+-----------------------+
| 5                     |                       | > \"Charlie\": 92     |
+-----------------------+-----------------------+-----------------------+
| 6                     |                       |                       |
+-----------------------+-----------------------+-----------------------+

> **Set Types**
>
> set

+-----------------------------------+-----------------------------------+
| 1\                                | > unique_numbers = {1, 2, 3, 4,   |
| 2                                 | > 5}\                             |
|                                   | > fruits = {\"apple\",            |
|                                   | > \"banana\", \"cherry\"}         |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> frozenset

+-----------------------------------+-----------------------------------+
| 1                                 | > immutable_set = frozenset(\[1,  |
|                                   | > 2, 3, 4, 5\])                   |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **Boolean Type**
>
> bool

+-----------------------------------+-----------------------------------+
| > 1\                              | +------------------------------+  |
| > 2\                              | | > is_raining = True          |  |
| > 3                               | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > has_licence = False        |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > is_adult = age \>= 18      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> Here are some examples of how these data types can be used in
> practice:

+-----------------------------------+-----------------------------------+
| > 1\                              | > \# Calculating area of a        |
| > 2\                              | > circle\                         |
| > 3\                              | > radius = 5.0\                   |
| > 4                               | > area = pi \* radius\*\*2\       |
|                                   | > print(f\"The area of the circle |
|                                   | > is {area:.2f} square units\")   |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 5\                              | > \# Working with lists\          |
| > 6\                              | > fruits.append(\"orange\")\      |
| > 7\                              | > print(f\"The second fruit is    |
| > 8                               | > {fruits\[1\]}\")                |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 9\                              | > \# Using a dictionary\          |
| > 10\                             | > print(f\"{person\[\'name\'\]}   |
| > 11                              | > is {person\[\'age\'\]} years    |
|                                   | > old and lives in                |
|                                   | > {person\[\'city\'\]}\")         |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 12\                             | > \# Set operations\              |
| > 13\                             | > a = {1, 2, 3, 4}\               |
| > 14\                             | > b = {3, 4, 5, 6}\               |
| > 15\                             | > print(f\"Union: {a \| b}\")\    |
| > 16\                             | > print(f\"Intersection: {a &     |
| > 17                              | > b}\")                           |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 18\                             | > \# Boolean logic\               |
| > 19\                             | > if is_adult and not             |
| > 20\                             | > is_raining:\                    |
| > 21                              | > print(\"Let\'s go for a         |
|                                   | > walk!\")                        |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> These examples demonstrate the basic usage of each data type. Remember
> that Python is dynamically typed, meaning you don\'t need to
>
> declare the type of a variable explicitly. The interpreter infers the
> type based on the value assigned to it.
>
> **[Control Structures]{.underline}**
>
> **If-else statements**:

+-----------------------------------+-----------------------------------+
| 1                                 | > if x \> 0:                      |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 2\                              | +------------------------------+  |
| > 3\                              | | > print(\"Positive\")        |  |
| > 4\                              | +==============================+  |
| > 5\                              | +------------------------------+  |
| > 6                               |                                   |
|                                   | +------------------------------+  |
|                                   | | > elif x \< 0:               |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > print(\"Negative\")        |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > else:                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > print(\"Zero\")            |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **For loops**:

+-----------------------------------+-----------------------------------+
| 1\                                | > for i in range(5):\             |
| 2                                 | > print(i)                        |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **While loops**:

+-----------------------------------+-----------------------------------+
| > 1\                              | +------------------------------+  |
| > 2\                              | | > count = 0                  |  |
| > 3\                              | +==============================+  |
| > 4                               | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > while count \< 5:          |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > print(count)               |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > count += 1                 |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **[Functions]{.underline}**

+-----------------------------------+-----------------------------------+
| 1\                                | > def greet(name):\               |
| 2                                 | > return f\"Hello, {name}!\"      |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 3\                              | > message = greet(\"Alice\")\     |
| > 4\                              | > print(message)                  |
| > 5                               |                                   |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **[Classes]{.underline}**

+-----------------------------------+-----------------------------------+
| > 1\                              | > class Dog:\                     |
| > 2\                              | > def \_\_init\_\_(self, name):\  |
| > 3                               | > self.name = name                |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 4\                              | > def bark(self):\                |
| > 5\                              | > return f\"{self.name} says      |
| > 6                               | > Woof!\"                         |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 7\                              | > my_dog = Dog(\"Buddy\")\        |
| > 8\                              | > print(my_dog.bark())            |
| > 9                               |                                   |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **Python Package Management**
>
> **pip**
>
> pip is the standard package manager for Python. It allows you to
> install and manage additional packages that are not part of the Python
> standard library.
>
> **Installing a package:**

+-----------------------------------+-----------------------------------+
| 1                                 | > python3 -m pip install requests |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **Upgrading a package:**

+-----------------------------------+-----------------------------------+
| 1                                 | > python3 -m pip install          |
|                                   | > \--upgrade requests             |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **Python Virtual Environments**\
> Virtual environments are isolated Python environments that allow you
> to install packages for specific projects without affecting your
> system-wide Python installation.
>
> **Creating a virtual environment:**

+-----------------------------------+-----------------------------------+
| 1                                 | > python3 -m venv .venv           |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

![](converted/media/image242.png){width="1.4166666666666667in"
height="0.16666666666666666in"}![](converted/media/image243.png){width="1.6527777777777777in"
height="0.16666666666666666in"}![](converted/media/image244.png){width="1.4722222222222223in"
height="0.1527777777777778in"}

> **Activating a virtual environment:On Unix or MacOS:**

+-----------------------------------+-----------------------------------+
| 1                                 | > source .venv/bin/activate       |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> On Windows:

+-----------------------------------+-----------------------------------+
| 1                                 | > .venv\\Scripts\\activate        |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **Installing packages in a virtual environment:**\
> Once activated, you can use pip to install packages, and they will be
> isolated to this environment.

+-----------------------------------+-----------------------------------+
| 1                                 | > pip install requests            |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **Deactivating a virtual environment:**

+-----------------------------------+-----------------------------------+
| 1                                 | > deactivate                      |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **Creating a requirements file:**\
> To share your project\'s dependencies, you can create a
> requirements.txt file:

+-----------------------------------+-----------------------------------+
| 1                                 | > pip freeze \> requirements.txt  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **Installing from a requirements file:**

+-----------------------------------+-----------------------------------+
| 1                                 | > pip install -r requirements.txt |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> Remember, it\'s a good practice to use virtual environments for each
> of your Python projects to avoid conflicts between package versions.
> Explore
>
> **Kubernetes Python client library**
>
> ![](converted/media/image108.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}Installation: pip install kubernetes\
> This will allow Authentication and configuration, Creating, reading,
> updating, and deleting Kubernetes resources
>
> **Simple Python scripts for Kubernetes interaction**
>
> Here is an example to;
>
> ![](converted/media/image238.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Listing pods in a namespace
>
> ![](converted/media/image239.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}Creating and managing deployments
>
> ![](converted/media/image240.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Watching for changes in resources\
> Example script to list pods:
>
> Create a virtual env\
> python3 -m venv .venv\
> source .venv/bin/activate\
> pip install kubernetes

+-----------------------------------+-----------------------------------+
| ![](vertopal_c4f4baa402e647588e   | > Create testscript.py            |
| cb2a507c21de28/media/image241.png |                                   |
| ){width="4.1666666666666664e-2in" |                                   |
| height="4.1666666666666664e-2in"} |                                   |
+===================================+===================================+
| 1                                 | > **from** kubernetes **import**  |
|                                   | > client, config                  |
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 2\                              | > config.load_kube_config()\      |
| > 3\                              | > v1 = client.CoreV1Api()         |
| > 4                               |                                   |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 5\                              | > pods =                          |
| > 6\                              | > v1.list_pod                     |
| > 7\                              | _for_all_namespaces(watch=False)\ |
| > 8                               | > **for** pod **in** pods.items:\ |
|                                   | > **print**(f\"{pod.metadata.na   |
|                                   | mespace}\\t{pod.metadata.name}\") |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

![](converted/media/image247.png){width="1.4166666666666667in"
height="0.16666666666666666in"}

> python3 testscript.py\
> If running minikube the output may look like this

+-----------------------------------+-----------------------------------+
| 1\                                | +------------------------------+  |
| 2\                                | | > default debug-env          |  |
| 3\                                | +==============================+  |
| 4\                                | +------------------------------+  |
| 5\                                |                                   |
| 6\                                | +------------------------------+  |
| 7\                                | | > default                    |  |
| 8\                                | | > webapp-6988595754-qnkqp    |  |
| 9\                                | +==============================+  |
| 10 11                             | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > default                    |  |
|                                   | | > webapp-6d989cd746-8wgzs    |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > default                    |  |
|                                   | | > webapp-cf544bc7c-24zpb     |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > kube-system                |  |
|                                   | | > coredns-7db6d8ff4d-t46mv   |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > kube-system etcd-minikube  |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > kube-system                |  |
|                                   | | > kube-apiserver-minikube    |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > kube-system                |  |
|                                   | | > kube                       |  |
|                                   | | -controller-manager-minikube |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > kube-system                |  |
|                                   | | > kube-proxy-jkgd5           |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > kube-system                |  |
|                                   | | > kube-scheduler-minikube    |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > kube-system                |  |
|                                   | | > storage-provisioner        |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> You now have the basics to interact with a kubernetes cluster via
> python. Link:

  -------------------------------------------------------------------------------------------------------------------------------------
  ![](converted/media/image245.png){width="0.11388888888888889in"   GitHub - kubernetes-client/python:
  height="0.11249890638670167in"}                                                                   Official Python client library for
                                                                                                    kubernetes
  ------------------------------------------------------------------------------------------------- -----------------------------------

  -------------------------------------------------------------------------------------------------------------------------------------

> **Day 5: Helm Basics**

**Helm\'s Purpose and Architecture**\
Helm is a package manager for Kubernetes that simplifies the deployment
and management of applications. It allows you to define, install, and
upgrade even the most complex Kubernetes applications.

  ------------------------------------------------------------------------------------------------------------------------------------
  ![](converted/media/image246.png){width="0.1388888888888889in"   Helm Essentials in Under an Hour
  height="0.1111111111111111in"}                                                                   
  ------------------------------------------------------------------------------------------------ -----------------------------------

  ------------------------------------------------------------------------------------------------------------------------------------

**Key Components:**

> 1\. **Helm Client**: The command-line tool used to create, package,
> and manage charts.
>
> 2\. **Charts**: Packages of pre-configured Kubernetes resources.\
> 3. **Releases**: Instances of a chart running in a Kubernetes cluster.

**Creating and Structure of a Helm Chart**\
Let\'s create a chart and examine its structure:\
You will have needed to

+-----------------------------------+-----------------------------------+
| 1\                                | +------------------------------+  |
| 2                                 | | > helm create mychart        |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > cd mychart                 |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

The chart structure:

+-----------------------------------+-----------------------------------+
| 1\                                | +------------------------------+  |
| 2\                                | | > mychart/                   |  |
| 3\                                | +==============================+  |
| 4\                                | +------------------------------+  |
| 5\                                |                                   |
| 6\                                | +------------------------------+  |
| 7\                                | | > Chart.yaml \# Metadata     |  |
| 8\                                | | > about the chart            |  |
| 9\                                | +==============================+  |
| 10                                | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > values.yaml \# Default     |  |
|                                   | | > configuration values       |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > charts/ \# Directory for   |  |
|                                   | | > chart dependencies         |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > templates/ \# Directory    |  |
|                                   | | > for template files         |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > deployment.yaml            |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > service.yaml               |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > ingress.yaml               |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \_helpers.tpl \# Template  |  |
|                                   | | > helpers                    |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > .helmignore \# Patterns to |  |
|                                   | | > ignore when packaging      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

**Chart.yaml Example:**

+-----------------------------------+-----------------------------------+
| 1\                                | +------------------------------+  |
| 2                                 | | > apiVersion: v2             |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > name: mychart              |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 3\                              | > description: A Helm chart for   |
| > 4\                              | > Kubernetes\                     |
| > 5\                              | > type: application\              |
| > 6                               | > version: 0.1.0\                 |
|                                   | > appVersion: \"1.16.0\"          |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **values.yaml Example:**

+-----------------------------------+-----------------------------------+
| 1                                 | > replicaCount: 1                 |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 2\                              | > image:\                         |
| > 3\                              | > repository: nginx\              |
| > 4\                              | > pullPolicy: IfNotPresent\       |
| > 5\                              | > tag: \"\"                       |
| > 6                               |                                   |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 7\                              | > service:\                       |
| > 8\                              | > type: ClusterIP\                |
| > 9\                              | > port: 80                        |
| > 10                              |                                   |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 11\                             | > ingress:\                       |
| > 12\                             | > enabled: false                  |
| > 13                              |                                   |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **Deploying Applications with Helm**
>
> To install a chart:

+-----------------------------------+-----------------------------------+
| 1                                 | > helm install myrelease          |
|                                   | > ./mychart                       |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> To customize values during installation:

+-----------------------------------+-----------------------------------+
| 1                                 | > helm install myrelease          |
|                                   | > ./mychart \--set                |
|                                   | > service.type=LoadBalancer       |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> Or using a custom values file:

+-----------------------------------+-----------------------------------+
| 1                                 | > helm install myrelease          |
|                                   | > ./mychart -f custom-values.yaml |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **Advanced Helm Concepts**
>
> **Hooks**
>
> Hooks allow you to intervene at certain points in a release\'s
> lifecycle. Here\'s an example of a pre-install hook:

+-----------------------------------+-----------------------------------+
| 1\                                | > apiVersion: batch/v1\           |
| 2\                                | > kind: Job\                      |
| 3\                                | > metadata:\                      |
| 4\                                | > name: {{ .Release.Name          |
| 5\                                | > }}-pre-install-job\             |
| 6\                                | > annotations:\                   |
| 7\                                | > \"helm.sh/hook\": pre-install\  |
| 8\                                | > spec:\                          |
| 9\                                | > template:\                      |
| 10 11 12 13 14                    | > spec:\                          |
|                                   | > containers:\                    |
|                                   | > - name: pre-install-job\        |
|                                   | > image: busybox\                 |
|                                   | > command: \[\'sh\', \'-c\',      |
|                                   | > \'echo Pre-install job          |
|                                   | > running\'\]                     |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > restartPolicy: Never       |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **Dependencies**\
> You can define dependencies in the Chart.yaml file:

+-----------------------------------+-----------------------------------+
| 1                                 | > dependencies:                   |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 2\                              | > \- name: apache\                |
| > 3\                              | > version: 1.2.3\                 |
| > 4                               | > repository:                     |
|                                   | > h                               |
|                                   | ttps://charts.bitnami.com/bitnami |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> Then, update dependencies:

+-----------------------------------+-----------------------------------+
| 1                                 | > helm dependency update          |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **Templating**
>
> Helm uses Go templates. Here\'s an example of a template using
> conditionals and loops:

+-----------------------------------+-----------------------------------+
| 1\                                | > apiVersion: apps/v1\            |
| 2\                                | > kind: Deployment\               |
| 3\                                | > metadata:\                      |
| 4\                                | > name: {{ .Release.Name          |
| 5\                                | > }}-deployment\                  |
| 6\                                | > spec:\                          |
| 7\                                | > replicas: {{                    |
| 8\                                | > .Values.replicaCount }}\        |
| 9\                                | > selector:\                      |
| 10 11 12 13 14 15 16 17 18 19 20  | > matchLabels:\                   |
| 21 22 23 24 25 26                 | > app: {{ .Chart.Name }}\         |
|                                   | > template:\                      |
|                                   | > metadata:\                      |
|                                   | > labels:\                        |
|                                   | > app: {{ .Chart.Name }}\         |
|                                   | > spec:\                          |
|                                   | > containers:\                    |
|                                   | > - name: {{ .Chart.Name }}\      |
|                                   | > image: \"{{                     |
|                                   | > .Values.image.repository }}:{{  |
|                                   | > .Values.image.tag }}\" ports:\  |
|                                   | > - containerPort: 80\            |
|                                   | > {{- if .Values.env }}\          |
|                                   | > env:\                           |
|                                   | > {{- range \$key, \$value :=     |
|                                   | > .Values.env }}\                 |
|                                   | > - name: {{ \$key }}\            |
|                                   | > value: {{ \$value \| quote }}\  |
|                                   | > {{- end }}\                     |
|                                   | > {{- end }}                      |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **Creating Helm Charts with Python Templates**\
> While Helm natively uses Go templates, you can use Python to generate
> Helm charts dynamically.
>
> **Using Jinja2 for Templating**
>
> Here\'s an example of using Jinja2 to generate a Kubernetes manifest:

+-----------------------------------+-----------------------------------+
| 1                                 | > from jinja2 import Template     |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 2\                              | > template = Template(\"\"\"\     |
| > 3\                              | > apiVersion: apps/v1\            |
| > 4\                              | > kind: Deployment\               |
| > 5\                              | > metadata:\                      |
| > 6\                              | > name: {{ name }}-deployment\    |
| > 7\                              | > spec:\                          |
| > 8\                              | > replicas: {{ replicas }}\       |
| > 9\                              | > selector:\                      |
| > 10\                             | > matchLabels:\                   |
| > 11\                             | > app: {{ name }}\                |
| > 12\                             | > template:                       |
| > 13                              |                                   |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 14 15 16 17 18 19 20 21 22 23   | > metadata:\                      |
|                                   | > labels:\                        |
|                                   | > app: {{ name }}\                |
|                                   | > spec:\                          |
|                                   | > containers:\                    |
|                                   | > - name: {{ name }}\             |
|                                   | > image: {{ image }}\             |
|                                   | > ports:\                         |
|                                   | > - containerPort: {{ port }}\    |
|                                   | > \"\"\")                         |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 24 25 26 27 28 29 30            | > rendered = template.render(\    |
|                                   | > name=\"myapp\",\                |
|                                   | > replicas=3,\                    |
|                                   | > image=\"nginx:latest\",\        |
|                                   | > port=80\                        |
|                                   | > )                               |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| 31 32                             | > print(rendered)                 |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **Generating Kubernetes Manifests Dynamically**
>
> You can use Python to read configuration from various sources and
> generate Helm charts:
>
> 1 import yaml
>
> 2 from jinja2 import Template

+-----------------------------------+-----------------------------------+
| > 3\                              | > def generate_chart(config):\    |
| > 4\                              | > \# Load templates\              |
| > 5\                              | > deployment_template =           |
| > 6\                              | > Template(open(\'tem             |
| > 7                               | plates/deployment.yaml\').read()) |
|                                   | > service_template =              |
|                                   | > Template(open(\'                |
|                                   | templates/service.yaml\').read()) |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 8\                              | > \# Render templates\            |
| > 9\                              | > deployment =                    |
| > 10\                             | > d                               |
| > 11                              | eployment_template.render(config) |
|                                   | > service =                       |
|                                   | > service_template.render(config) |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 12\                             | > \# Combine rendered templates\  |
| > 13\                             | > chart =                         |
| > 14                              | > f\"{                            |
|                                   | deployment}\\n\-\--\\n{service}\" |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> 15
>
> 16 return chart

+-----------------------------------+-----------------------------------+
| > 17\                             | > \# Read configuration\          |
| > 18\                             | > with open(\'app_config.yaml\',  |
| > 19\                             | > \'r\') as f:\                   |
| > 20                              | > config = yaml.safe_load(f)      |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 21\                             | > \# Generate chart\              |
| > 22\                             | > chart = generate_chart(config)  |
| > 23                              |                                   |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 24\                             | > \# Write chart to file\         |
| > 25\                             | > with                            |
| > 26\                             | > open(\'generated_chart.yaml\',  |
| > 27                              | > \'w\') as f: f.write(chart)     |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **Integrating with CI/CD Pipelines**
>
> You can incorporate this Python-based chart generation into your CI/CD
> pipeline:

+-----------------------------------+-----------------------------------+
| > 1\                              | > \# Example GitLab CI job\       |
| > 2\                              | > generate_helm_chart:\           |
| > 3\                              | > stage: build\                   |
| > 4                               | > script:                         |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 5\                              | +------------------------------+  |
| > 6\                              | | > \- pip install pyyaml      |  |
| > 7\                              | | > jinja2                     |  |
| > 8\                              | +==============================+  |
| > 9                               | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \- python                  |  |
|                                   | | > generate_chart.py          |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > artifacts:                 |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > paths:                     |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \- generated_chart.yaml    |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> This job would generate the Helm chart as part of your CI/CD process,
> allowing for dynamic chart creation based on your application\'s
>
> needs.These examples demonstrate how to create more complex Helm
> charts, use advanced features, and even integrate Python for
>
> dynamic chart generation.
>
> Week 3: Istio Deep Dive
>
> **Day 1: Istio Basics**
>
> **Installing Istio on your Kubernetes cluster**
>
> **Download Istio**

  -------------------------------------------------------------------------------------------------------------------------------------
  ![](converted/media/image248.png){width="0.11249890638670167in"   Getting Started
  height="0.1125in"}                                                                                
  ------------------------------------------------------------------------------------------------- -----------------------------------

  -------------------------------------------------------------------------------------------------------------------------------------

> Mac can use brew brew install istionctl
>
> **Install Istio**
>
> istio provides a demo for testing and learning:

+-----------------------+-----------------------+-----------------------+
| ![](vertopal_         | > It installs more    |                       |
| c4f4baa402e647588ecb2 | > components than the |                       |
| a507c21de28/media/ima | > default profile,    |                       |
| ge141.png){width="4.1 | > including:          |                       |
| 666666666666664e-2in" |                       |                       |
| height="4.16          |                       |                       |
| 66666666666664e-2in"} |                       |                       |
|                       |                       |                       |
| ![](vertopal_         |                       |                       |
| c4f4baa402e647588ecb2 |                       |                       |
| a507c21de28/media/ima |                       |                       |
| ge249.png){width="4.1 |                       |                       |
| 666666666666664e-2in" |                       |                       |
| height="4.16          |                       |                       |
| 66666666666664e-2in"} |                       |                       |
|                       |                       |                       |
| ![](vertopal_         |                       |                       |
| c4f4baa402e647588ecb2 |                       |                       |
| a507c21de28/media/ima |                       |                       |
| ge250.png){width="4.1 |                       |                       |
| 666666666666664e-2in" |                       |                       |
| height="4.16          |                       |                       |
| 66666666666664e-2in"} |                       |                       |
|                       |                       |                       |
| ![](vertopal_         |                       |                       |
| c4f4baa402e647588ecb2 |                       |                       |
| a507c21de28/media/ima |                       |                       |
| ge251.png){width="4.1 |                       |                       |
| 666666666666664e-2in" |                       |                       |
| height="4.16          |                       |                       |
| 66666666666664e-2in"} |                       |                       |
+=======================+=======================+=======================+
|                       | ![](vertopal          | > Istiod (the Istio   |
|                       | _c4f4baa402e647588ecb | > control plane)      |
|                       | 2a507c21de28/media/im |                       |
|                       | age252.png){width="5. |                       |
|                       | 555555555555555e-2in" |                       |
|                       | height="5.5           |                       |
|                       | 55555555555555e-2in"} |                       |
+-----------------------+-----------------------+-----------------------+
|                       | ![](vertopal          | > Ingress gateway     |
|                       | _c4f4baa402e647588ecb |                       |
|                       | 2a507c21de28/media/im |                       |
|                       | age253.png){width="5. |                       |
|                       | 555555555555555e-2in" |                       |
|                       | height="5.5           |                       |
|                       | 55555555555555e-2in"} |                       |
+-----------------------+-----------------------+-----------------------+
|                       | ![](vertopal          | > Egress gateway      |
|                       | _c4f4baa402e647588ecb |                       |
|                       | 2a507c21de28/media/im |                       |
|                       | age254.png){width="5. |                       |
|                       | 555555555555555e-2in" |                       |
|                       | height="5.5           |                       |
|                       | 55555555555555e-2in"} |                       |
+-----------------------+-----------------------+-----------------------+
|                       | > It enables a set of |                       |
|                       | > features that are   |                       |
|                       | > suitable for        |                       |
|                       | > demonstrating       |                       |
|                       | > Istio\'s            |                       |
|                       | > capabilities.       |                       |
|                       | >                     |                       |
|                       | > It has higher       |                       |
|                       | > resource            |                       |
|                       | > requirements than   |                       |
|                       | > the minimal or      |                       |
|                       | > default profiles.   |                       |
|                       | >                     |                       |
|                       | > It\'s not           |                       |
|                       | > recommended for     |                       |
|                       | > production use due  |                       |
|                       | > to its expanded     |                       |
|                       | > feature set and     |                       |
|                       | > resource usage.     |                       |
+-----------------------+-----------------------+-----------------------+

  -----------------------------------------------------------------------
  istioctl install \--set profile=demo -y
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

> **Enable automatic sidecar injection**

  -----------------------------------------------------------------------
  kubectl label namespace default istio-injection=enabled
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

> **Istio\'s architecture and core components**
>
> **Control Plane**
>
> istiod: Combines Pilot, Citadel, and Galley into a single binaryPilot:
> Service discovery and traffic management
>
> **Data Plane**
>
> Envoy proxy: Sidecar container deployed alongside each service
>
> **Addons**

+-----------------------------------+-----------------------------------+
| ![](vertopal_c4f4baa402e647588e   | > Prometheus: Metrics collection\ |
| cb2a507c21de28/media/image255.png | > Grafana: Metrics visualization\ |
| ){width="4.1666666666666664e-2in" | > Jaeger or Zipkin: Distributed   |
| height="4.1666666666666664e-2in"} | > tracing\                        |
|                                   | > Kiali: Service mesh             |
| ![](vertopal_c4f4baa402e647588e   | > visualization                   |
| cb2a507c21de28/media/image256.png |                                   |
| ){width="4.1666666666666664e-2in" |                                   |
| height="4.1666666666666664e-2in"} |                                   |
|                                   |                                   |
| ![](vertopal_c4f4baa402e647588e   |                                   |
| cb2a507c21de28/media/image257.png |                                   |
| ){width="4.1666666666666664e-2in" |                                   |
| height="4.1666666666666664e-2in"} |                                   |
|                                   |                                   |
| ![](vertopal_c4f4baa402e647588e   |                                   |
| cb2a507c21de28/media/image258.png |                                   |
| ){width="4.1666666666666664e-2in" |                                   |
| height="4.1666666666666664e-2in"} |                                   |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **Deploying applications with Istio sidecar injection**
>
> 1\. Create a sample application deployment YAML
>
> 2\. Apply the deployment: kubectl apply -f sample-app.yaml
>
> 3\. Verify sidecar injection: kubectl get pods
>
> You should see two containers per pod (app + istio-proxy)
>
> **Day 2: Istio Traffic Management**
>
> **Exploring Istio\'s traffic management features**
>
> Virtual Services: Define routing rules for traffic

+-----------------------------------+-----------------------------------+
| 1\                                | > apiVersion:                     |
| 2\                                | > networking.istio.io/v1alpha3\   |
| 3\                                | > kind: VirtualService\           |
| 4\                                | > metadata:\                      |
| 5\                                | > name: reviews-route\            |
| 6\                                | > spec:\                          |
| 7\                                | > hosts:\                         |
| 8\                                | > - reviews\                      |
| 9\                                | > http:\                          |
| 10 11 12 13 14 15 16 17           | > - route:\                       |
|                                   | > - destination:\                 |
|                                   | > host: reviews\                  |
|                                   | > subset: v1\                     |
|                                   | > weight: 75\                     |
|                                   | > - destination:\                 |
|                                   | > host: reviews\                  |
|                                   | > subset: v2\                     |
|                                   | > weight: 25                      |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> Destination Rules: Define policies that apply after routing

+-----------------------------------+-----------------------------------+
| 1\                                | +------------------------------+  |
| 2\                                | | > apiVersion:                |  |
| 3\                                | | >                            |  |
| 4\                                | | networking.istio.io/v1alpha3 |  |
| 5\                                | +==============================+  |
| 6\                                | +------------------------------+  |
| 7\                                |                                   |
| 8\                                | > kind: DestinationRule\          |
| 9\                                | > metadata:\                      |
| 10 11 12 13                       | > name: reviews-destination\      |
|                                   | > spec:\                          |
|                                   | > host: reviews\                  |
|                                   | > subsets:\                       |
|                                   | > - name: v1\                     |
|                                   | > labels:\                        |
|                                   | > version: v1\                    |
|                                   | > - name: v2\                     |
|                                   | > labels:                         |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > version: v2                |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> Gateways: Manage inbound and outbound traffic for the mesh
>
> **Implementing canary deployments and A/B testing**
>
> 1\. Use VirtualService to split traffic between versions\
> 2. Gradually adjust weights to increase traffic to new version\
> 3. Monitor metrics to ensure new version performs as expected
>
> **Istio\'s load balancing and circuit breaking capabilities**
>
> Load Balancing: Configure in DestinationRule

+-----------------------------------+-----------------------------------+
| > 1\                              | > spec:\                          |
| > 2\                              | > trafficPolicy:\                 |
| > 3                               | > loadBalancer:                   |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 4                               | > simple: ROUND_ROBIN             |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> Circuit Breaking: Define in DestinationRule

+-----------------------------------+-----------------------------------+
| > 1\                              | +------------------------------+  |
| > 2\                              | | > spec:                      |  |
| > 3\                              | +==============================+  |
| > 4\                              | +------------------------------+  |
| > 5\                              |                                   |
| > 6                               | +------------------------------+  |
|                                   | | > trafficPolicy:             |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > outlierDetection:          |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > consecutiveErrors: 5       |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > interval: 5s               |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > baseEjectionTime: 30s      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **Day 3: Istio Security and Observability**
>
> **Istio\'s security features**
>
> **mTLS (Mutual TLS)**
>
> ![](converted/media/image259.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Enable cluster-wide: kubectl apply -f
> istio-1.x.x/samples/security/strict-mtls.yaml
>
> ![](converted/media/image260.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}Verify: istioctl x authz check
> \<pod-name\>
>
> **Authorization Policies**

+-----------------------------------+-----------------------------------+
| 1\                                | +------------------------------+  |
| 2\                                | | > apiVersion:                |  |
| 3\                                | | > security.istio.io/v1beta1  |  |
| 4\                                | +==============================+  |
| 5\                                | +------------------------------+  |
| 6\                                |                                   |
| 7\                                | +------------------------------+  |
| 8\                                | | > kind: AuthorizationPolicy  |  |
| 9\                                | +==============================+  |
| 10                                | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > metadata:                  |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > name: allow-read           |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > spec:                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > action: ALLOW              |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > rules:                     |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \- to:                     |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \- operation:              |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > methods: \[\"GET\"\]       |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **Exploring Istio\'s observability stack**
>
> **Prometheus**
>
> ![](converted/media/image261.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}Access dashboard: istioctl dashboard
> prometheus
>
> ![](converted/media/image262.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}Query metrics using PromQL
>
> **Grafana**
>
> ![](converted/media/image263.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Access dashboard: istioctl dashboard
> grafana
>
> ![](converted/media/image264.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}Explore pre-configured Istio
> dashboards
>
> **Kiali**
>
> ![](converted/media/image265.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Access dashboard: istioctl dashboard
> kiali
>
> ![](converted/media/image266.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Visualize service mesh topology and
> health
>
> **Jaeger/Zipkin**

+-----------------------------------+-----------------------------------+
| ![](vertopal_c4f4baa402e647588e   | > Access Jaeger UI: istioctl      |
| cb2a507c21de28/media/image267.png | > dashboard jaeger Analyze        |
| ){width="4.1666666666666664e-2in" | > distributed traces              |
| height="5.555555555555555e-2in"}  |                                   |
|                                   |                                   |
| ![](vertopal_c4f4baa402e647588e   |                                   |
| cb2a507c21de28/media/image268.png |                                   |
| ){width="4.1666666666666664e-2in" |                                   |
| height="5.555555555555555e-2in"}  |                                   |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

![](converted/media/image271.png){width="0.5972222222222222in"
height="0.16666666666666666in"}

**Day 4-5: Deploying a Sample Application with Istio**

**Objective**

Deploy a simple web application with Istio sidecar injection and
implement basic traffic routing.

**Prerequisites**

> ![](converted/media/image269.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Kubernetes cluster set up
>
> ![](converted/media/image270.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}Istio installed with demo profile\
> kubectl and istioctl configured

**Enable Istio Sidecar Injection**

First, let\'s enable Istio sidecar injection for the default namespace:

+-----------------------------------+-----------------------------------+
| 1                                 | > kubectl label namespace default |
|                                   | > istio-injection=enabled         |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

The command is used to enable automatic Istio sidecar injection for the
default namespace in a Kubernetes cluster.

Key points about this command:

> 1\. Namespace-level control: By labeling a namespace, you\'re enabling
> Istio sidecar injection for all pods created in that namespace, unless
> overridden at the pod level.
>
> 2\. Automatic injection: When a namespace has this label, the Istio
> sidecar (Envoy proxy) will be automatically injected into all new pods
> deployed in that namespace.
>
> 3\. Existing workloads: This label only affects new pods. Existing
> workloads will need to be redeployed to get the sidecar injected. 4.
> Override option: Even with this namespace-level setting, individual
> pods can opt out of injection using the sidecar.istio.io/inject:
> \"false\" annotation.
>
> 5\. Verification: After applying this label, you can verify it worked
> by deploying a new pod in the namespace and checking for the presence
> of the istio-proxy container.
>
> 6\. Reversibility: You can disable injection for the namespace by
> changing the label value to disabled or removing the label entirely.

**Deploy a Sample Application**

Create a file named sample-app.yaml with the following content:

+-----------------------------------+-----------------------------------+
| 1\                                | > text\                           |
| 2\                                | > apiVersion: apps/v1\            |
| 3\                                | > kind: Deployment\               |
| 4\                                | > metadata:\                      |
| 5\                                | > name: myapp\                    |
| 6\                                | > spec:\                          |
| 7\                                | > replicas: 2\                    |
| 8\                                | > selector:\                      |
| 9\                                | > matchLabels:\                   |
| 10 11 12 13 14 15 16 17 18 19     | > app: myapp\                     |
|                                   | > template:\                      |
|                                   | > metadata:\                      |
|                                   | > labels:\                        |
|                                   | > app: myapp\                     |
|                                   | > version: v1\                    |
|                                   | > spec:\                          |
|                                   | > containers:\                    |
|                                   | > - name: myapp\                  |
|                                   | > image: nginx:1.14.2             |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 20 21 22 23 24 25 26 27 28 29   | > ports:\                         |
| > 30 31 32                        | > - containerPort: 80\            |
|                                   | > \-\--\                          |
|                                   | > apiVersion: v1\                 |
|                                   | > kind: Service\                  |
|                                   | > metadata:\                      |
|                                   | > name: myapp\                    |
|                                   | > spec:\                          |
|                                   | > selector:\                      |
|                                   | > app: myapp\                     |
|                                   | > ports:\                         |
|                                   | > - port: 80\                     |
|                                   | > targetPort: 80                  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------------------------------------------+
| > 33                                                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

> Deploy the application:

+-----------------------------------+-----------------------------------+
| 1\                                | > bash\                           |
| 2                                 | > kubectl apply -f                |
|                                   | > sample-app.yaml                 |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------------------------------------------+
| > 3                                                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

> Verify the deployment:

+-----------------------------------+-----------------------------------+
| 1\                                | > bash\                           |
| 2                                 | > kubectl get pods                |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------------------------------------------+
| > 3                                                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

> You should see two containers per pod (app + istio-proxy), indicating
> successful sidecar injection.
>
> **Create a Virtual Service**
>
> Create a file named virtual-service.yaml :

+-----------------------------------+-----------------------------------+
| 1\                                | > text\                           |
| 2\                                | > apiVersion:                     |
| 3\                                | > networking.istio.io/v1alpha3\   |
| 4\                                | > kind: VirtualService\           |
| 5\                                | > metadata:\                      |
| 6\                                | > name: myapp-route\              |
| 7\                                | > spec:\                          |
| 8\                                | > hosts:\                         |
| 9\                                | > - myapp\                        |
| 10 11 12 13                       | > http:\                          |
|                                   | > - route:\                       |
|                                   | > - destination:\                 |
|                                   | > host: myapp\                    |
|                                   | > subset: v1                      |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------------------------------------------+
| > 14                                                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

> Apply the Virtual Service:

+-----------------------------------+-----------------------------------+
| 1\                                | > bash\                           |
| 2                                 | > kubectl apply -f                |
|                                   | > virtual-service.yaml            |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------------------------------------------+
| > 3                                                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

> **Create a Destination Rule**
>
> Create a file named destination-rule.yaml :

+-----------------------------------+-----------------------------------+
| 1\                                | > text\                           |
| 2\                                | > apiVersion:                     |
| 3\                                | > networking.istio.io/v1alpha3\   |
| 4\                                | > kind: DestinationRule\          |
| 5\                                | > metadata:\                      |
| 6\                                | > name: myapp-destination\        |
| 7\                                | > spec:\                          |
| 8\                                | > host: myapp\                    |
| 9\                                | > subsets:\                       |
| 10 11                             | > - name: v1\                     |
|                                   | > labels:\                        |
|                                   | > version: v1                     |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------------------------------------------+
| > 12                                                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

> Apply the Destination Rule:

+-----------------------------------+-----------------------------------+
| 1\                                | > bash\                           |
| 2                                 | > kubectl apply -f                |
|                                   | > destination-rule.yaml           |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------------------------------------------+
| > 3                                                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

> **Test the Routing**
>
> To test the routing, we\'ll need to access the application. For
> simplicity, let\'s use port-forwarding:

+-----------------------------------+-----------------------------------+
| 1\                                | > bash\                           |
| 2                                 | > kubectl port-forward            |
|                                   | > service/myapp 8080:80           |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------------------------------------------+
| > 3                                                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

> Now, in another terminal, you can access the application:

+-----------------------------------+-----------------------------------+
| 1\                                | > bash\                           |
| 2                                 | > curl http://localhost:8080      |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------------------------------------------+
| > 3                                                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

> You should see the nginx welcome page.
>
> **Implement Canary Deployment**
>
> Let\'s update our application to version 2. Create a file named
> sample-app-v2.yaml :

+-----------------------------------+-----------------------------------+
| 1\                                | > text\                           |
| 2\                                | > apiVersion: apps/v1\            |
| 3\                                | > kind: Deployment\               |
| 4\                                | > metadata:\                      |
| 5\                                | > name: myapp-v2\                 |
| 6\                                | > spec:\                          |
| 7\                                | > replicas: 1\                    |
| 8\                                | > selector:\                      |
| 9\                                | > matchLabels:\                   |
| 10 11 12 13 14 15 16 17 18        | > app: myapp\                     |
|                                   | > version: v2\                    |
|                                   | > template:\                      |
|                                   | > metadata:\                      |
|                                   | > labels:\                        |
|                                   | > app: myapp\                     |
|                                   | > version: v2\                    |
|                                   | > spec:\                          |
|                                   | > containers:                     |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 19\                             | > \- name: myapp\                 |
| > 20\                             | > image: nginx:1.16.0\            |
| > 21\                             | > ports:\                         |
| > 22                              | > - containerPort: 80             |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------------------------------------------+
| > 23                                                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

> Deploy version 2:

+-----------------------------------+-----------------------------------+
| 1\                                | > bash\                           |
| 2                                 | > kubectl apply -f                |
|                                   | > sample-app-v2.yaml              |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------------------------------------------+
| > 3                                                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

> Update the virtual-service.yaml to split traffic:

+-----------------------------------+-----------------------------------+
| 1\                                | > text\                           |
| 2\                                | > apiVersion:                     |
| 3\                                | > networking.istio.io/v1alpha3\   |
| 4\                                | > kind: VirtualService\           |
| 5\                                | > metadata:\                      |
| 6\                                | > name: myapp-route\              |
| 7\                                | > spec:\                          |
| 8\                                | > hosts:\                         |
| 9\                                | > - myapp\                        |
| 10 11 12 13 14 15 16 17 18        | > http:\                          |
|                                   | > - route:\                       |
|                                   | > - destination:\                 |
|                                   | > host: myapp\                    |
|                                   | > subset: v1\                     |
|                                   | > weight: 75\                     |
|                                   | > - destination:\                 |
|                                   | > host: myapp\                    |
|                                   | > subset: v2\                     |
|                                   | > weight: 25                      |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> 19
>
> Update the destination-rule.yaml :

+-----------------------------------+-----------------------------------+
| 1\                                | > text\                           |
| 2\                                | > apiVersion:                     |
| 3\                                | > networking.istio.io/v1alpha3\   |
| 4\                                | > kind: DestinationRule\          |
| 5\                                | > metadata:\                      |
| 6\                                | > name: myapp-destination\        |
| 7\                                | > spec:\                          |
| 8\                                | > host: myapp\                    |
| 9\                                | > subsets:\                       |
| 10 11 12 13 14                    | > - name: v1\                     |
|                                   | > labels:\                        |
|                                   | > version: v1\                    |
|                                   | > - name: v2\                     |
|                                   | > labels:\                        |
|                                   | > version: v2                     |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------------------------------------------+
| > 15                                                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

> Apply the updated configurations:

+-----------------------------------+-----------------------------------+
| > 1\                              | > bash\                           |
| > 2\                              | > kubectl apply -f                |
| > 3                               | > virtual-service.yaml\           |
|                                   | > kubectl apply -f                |
|                                   | > destination-rule.yaml           |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------------------------------------------+
| > 4                                                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

> Now, when you access the application, 75% of the traffic will go to v1
> and 25% to v2.
>
> **Conclusion**\
> In this lesson, we\'ve deployed a sample application with Istio,
> implemented basic traffic routing, and set up a canary deployment.
> This demonstrates some of Istio\'s core traffic management
> capabilities. In a real-world scenario, you would monitor the
> performance of both versions and gradually adjust the traffic split
> until you\'re confident in the new version\'s performance.Remember to
> clean up your resources after the lesson:

+-----------------------------------+-----------------------------------+
| > 1\                              | > bash\                           |
| > 2\                              | > kubectl delete -f               |
| > 3\                              | > sample-app.yaml\                |
| > 4\                              | > kubectl delete -f               |
| > 5                               | > sample-app-v2.yaml\             |
|                                   | > kubectl delete -f               |
|                                   | > virtual-service.yaml\           |
|                                   | > kubectl delete -f               |
|                                   | > destination-rule.yaml           |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------------------------------------------+
| > 6                                                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

> This lesson provides a practical introduction to Istio\'s traffic
> management features. For more advanced scenarios, you could explore
> features like fault injection, circuit breaking, and more complex
> routing rules.
>
> Week 4: Linkerd and Practical Applications
>
> **Day 1: Linkerd Basics**
>
> **Installing Linkerd on your Kubernetes cluster**
>
> **Install CLI**

  -------------------------------------------------------------------------------------------------------------------------------------
  ![](converted/media/image272.png){width="0.11249890638670167in"   Installing Linkerd
  height="0.1125in"}                                                                                
  ------------------------------------------------------------------------------------------------- -----------------------------------

  -------------------------------------------------------------------------------------------------------------------------------------

> Again Mac can use brew

  -----------------------------------------------------------------------
  curl -sL https://run.linkerd.io/install \| sh
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

  -----------------------------------------------------------------------
  export PATH=\$PATH:\$HOME/.linkerd2/bin
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

> **Validate cluster**

  -----------------------------------------------------------------------
  linkerd check \--pre
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

> **Install Linkerd**

  -----------------------------------------------------------------------
  linkerd install \| kubectl apply -f -
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

> **Linkerd\'s architecture and core components**
>
> **Control Plane**
>
> ![](converted/media/image273.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}controller: Manages and configures
> proxy instances
>
> ![](converted/media/image274.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}destination: Service discovery and
> load balancing
>
> ![](converted/media/image275.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}identity: Certificate management for
> mTLS
>
> **Data Plane**
>
> linkerd-proxy: Ultra-lightweight proxy (written in Rust)
>
> **Add-ons**
>
> ![](converted/media/image276.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Grafana: Metrics visualization
>
> ![](converted/media/image277.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Prometheus: Metrics collection
>
> **Linkerd Features**
>
> **Traffic management capabilities**
>
> Traffic Split:

+-----------------------------------+-----------------------------------+
| 1\                                | +------------------------------+  |
| 2\                                | | > apiVersion:                |  |
| 3\                                | | > split.smi-spec.io/v1alpha1 |  |
| 4\                                | +==============================+  |
| 5\                                | +------------------------------+  |
| 6\                                |                                   |
| 7\                                | +------------------------------+  |
| 8\                                | | > kind: TrafficSplit         |  |
| 9\                                | +==============================+  |
| 10 11                             | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > metadata:                  |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > name: web-split            |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > spec:                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > service: web-svc           |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > backends:                  |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \- service: web-v1         |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > weight: 500m               |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > \- service: web-v2         |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > weight: 500m               |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> Retries and Timeouts: Configured via annotations
>
> **Linkerd\'s observability and security features**
>
> ![](converted/media/image278.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Automatic mTLS:\
> Enabled by default for all meshed servicesb.
>
> ![](converted/media/image279.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Metrics:\
> Access via CLI or Grafana dashboards

+-----------------------------------+-----------------------------------+
| 1                                 | +------------------------------+  |
|                                   | | > linkerd stat deployment    |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
| ![](vertopal_c4f4baa402e647588e   | > Live Traffic View:              |
| cb2a507c21de28/media/image280.png |                                   |
| ){width="4.1666666666666664e-2in" |                                   |
| height="4.1666666666666664e-2in"} |                                   |
+-----------------------------------+-----------------------------------+
| 1                                 | +------------------------------+  |
|                                   | | > linkerd viz top            |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+-----------------------------------+-----------------------------------+
| ![](vertopal_c4f4baa402e647588e   | > Traffic Inspection:             |
| cb2a507c21de28/media/image281.png |                                   |
| ){width="4.1666666666666664e-2in" |                                   |
| height="4.1666666666666664e-2in"} |                                   |
+-----------------------------------+-----------------------------------+
| 1                                 | +------------------------------+  |
|                                   | | > linkerd tap                |  |
|                                   | | > deployment/your-deployment |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+-----------------------------------+-----------------------------------+

> **Day 2-4: Hands-on Exercise**
>
> **Deploying and Managing emojivoto with Linkerd**

+-----------------------------------+-----------------------------------+
| > Sheet here                      | > Linkerd in a Minikube           |
|                                   | > environment                     |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **Deploy the emojivoto sample application**

+-----------------------------------+-----------------------------------+
| 1                                 | > curl -sL                        |
|                                   | > htt                             |
|                                   | ps://run.linkerd.io/emojivoto.yml |
|                                   | > \| kubectl apply -f -           |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> This command downloads the emojivoto application manifest and applies
> it to your Kubernetes cluster. Verify the deployment:

+-----------------------------------+-----------------------------------+
| 1                                 | > kubectl get pods -n emojivoto   |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **Inject Linkerd into the application**

+-----------------------------------+-----------------------------------+
| 1                                 | > kubectl get -n emojivoto deploy |
|                                   | > -o yaml \| linkerd inject - \|  |
|                                   | > kubectl apply -f -              |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> This command retrieves all deployments in the emojivoto namespace,
> injects the Linkerd sidecar, and reapplies the configuration. Verify
> the injection:

+-----------------------------------+-----------------------------------+
| 1                                 | > kubectl get pods -n emojivoto   |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> You should now see two containers per pod (the application container
> and the Linkerd proxy).
>
> **Observe traffic**

+-----------------------------------+-----------------------------------+
| 1                                 | > linkerd -n emojivoto stat       |
|                                   | > deploy                          |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> This command shows real-time metrics for your deployments, including
> success rate, requests per second, and latency.
>
> **Visualize the service mesh**

+-----------------------------------+-----------------------------------+
| 1                                 | > linkerd viz dashboard           |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> This opens the Linkerd dashboard in your default browser. Explore the
> various sections to see detailed metrics, topology, and live calls.
>
> **Implement a traffic split for canary deployment**
>
> First, let\'s create a new version of the voting service:

+-----------------------------------+-----------------------------------+
| 1\                                | > cat \<\<EOF \| kubectl apply -f |
| 2\                                | > -\                              |
| 3\                                | > apiVersion: apps/v1\            |
| 4\                                | > kind: Deployment\               |
| 5\                                | > metadata:\                      |
| 6\                                | > name: voting-v2\                |
| 7\                                | > namespace: emojivoto\           |
| 8\                                | > spec:\                          |
| 9\                                | > replicas: 1\                    |
| 10 11 12 13 14 15 16 17 18 19 20  | > selector:\                      |
| 21 22 23 24 25 26 27              | > matchLabels:\                   |
|                                   | > app: voting-svc\                |
|                                   | > version: v2\                    |
|                                   | > template:\                      |
|                                   | > metadata:\                      |
|                                   | > labels:\                        |
|                                   | > app: voting-svc\                |
|                                   | > version: v2\                    |
|                                   | > spec:\                          |
|                                   | > containers:\                    |
|                                   | > - name: voting-svc\             |
|                                   | > image:                          |
|                                   | > bu                              |
|                                   | oyantio/emojivoto-voting-svc:v11\ |
|                                   | > env:\                           |
|                                   | > - name: GRPC_PORT\              |
|                                   | > value: \"8080\"\                |
|                                   | > ports:\                         |
|                                   | > - containerPort: 8080\          |
|                                   | > EOF                             |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> Now, create a TrafficSplit to gradually shift traffic:

+-----------------------------------+-----------------------------------+
| 1\                                | +------------------------------+  |
| 2\                                | | > bash                       |  |
| 3\                                | +==============================+  |
| 4\                                | +------------------------------+  |
| 5\                                |                                   |
| 6\                                | +------------------------------+  |
| 7\                                | | > cat \<\<EOF \| kubectl     |  |
| 8\                                | | > apply -f -                 |  |
| 9\                                | +==============================+  |
| 10                                | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > apiVersion:                |  |
|                                   | | > split.smi-spec.io/v1alpha2 |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > kind: TrafficSplit         |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > metadata:                  |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > name: voting-split         |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > namespace: emojivoto       |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > spec:                      |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > service: voting-svc        |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > backends:                  |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| > 11 12 13 14 15                  | > \- service: voting\             |
|                                   | > weight: 900m\                   |
|                                   | > - service: voting-v2\           |
|                                   | > weight: 100m\                   |
|                                   | > EOF                             |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------------------------------------------+
| > 16                                                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

> This configuration sends 90% of traffic to the original version and
> 10% to the new version.
>
> **Observe the traffic split**

+-----------------------------------+-----------------------------------+
| 1                                 | > linkerd -n emojivoto stat       |
|                                   | > deploy voting voting-v2         |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> You should see traffic being split between the two versions according
> to the weights specified in the TrafficSplit resource.
>
> **Gradually increase traffic to the new version**
>
> As you gain confidence in the new version, you can update the
> TrafficSplit to increase traffic to v2:

+-----------------------------------+-----------------------------------+
| 1\                                | +------------------------------+  |
| 2\                                | | > cat \<\<EOF \| kubectl     |  |
| 3\                                | | > apply -f -                 |  |
| 4\                                | +==============================+  |
| 5\                                | +------------------------------+  |
| 6\                                |                                   |
| 7\                                | > apiVersion:                     |
| 8\                                | > split.smi-spec.io/v1alpha2\     |
| 9\                                | > kind: TrafficSplit\             |
| 10 11 12 13 14                    | > metadata:\                      |
|                                   | > name: voting-split\             |
|                                   | > namespace: emojivoto\           |
|                                   | > spec:\                          |
|                                   | > service: voting-svc\            |
|                                   | > backends:\                      |
|                                   | > - service: voting\              |
|                                   | > weight: 500m\                   |
|                                   | > - service: voting-v2\           |
|                                   | > weight: 500m                    |
|                                   |                                   |
|                                   | +------------------------------+  |
|                                   | | > EOF                        |  |
|                                   | +==============================+  |
|                                   | +------------------------------+  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> This updates the split to 50/50 between the two versions.
>
> **Monitor the canary deployment**
>
> Use the Linkerd dashboard or CLI to monitor the performance of both
> versions:

+-----------------------------------+-----------------------------------+
| 1\                                | > bash\                           |
| 2                                 | > linkerd -n emojivoto stat       |
|                                   | > deploy voting voting-v2         |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------------------------------------------+
| > 3                                                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

> Keep an eye on success rates, latency, and request volumes to ensure
> the new version is performing as expected.
>
> **Conclusion**
>
> In this hands-on exercise, you\'ve:
>
> 1\. Deployed the emojivoto sample application
>
> 2\. Injected Linkerd into the application
>
> 3\. Observed traffic using Linkerd\'s CLI and dashboard
>
> 4\. Implemented a canary deployment using TrafficSplit
>
> 5\. Monitored the performance of both versions during the canary
> rollout
>
> This exercise demonstrates Linkerd\'s key features for traffic
> management and observability, providing a practical introduction to
> service
>
> mesh concepts and canary deployments.

**Day 5: Service Mesh Comparison**

**Comparing Istio, Linkerd, and other service mesh solutions**

**Istio**

> ![](converted/media/image282.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}Pros: Feature-rich, powerful traffic
> management
>
> ![](converted/media/image283.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}Cons: Complex, resource-intensive

**Linkerd**

> ![](converted/media/image284.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}Pros: Lightweight, simple, fast
>
> ![](converted/media/image285.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Cons: Fewer advanced features

**Consul Connect**

> ![](converted/media/image286.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Pros: Integrates well with HashiCorp
> ecosystem
>
> ![](converted/media/image287.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Cons: Less mature as a full service
> mesh

**NGINX Service Mesh**

> ![](converted/media/image288.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Pros: Builds on familiar NGINX
> technology
>
> ![](converted/media/image289.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Cons: Relatively new, smaller
> community

**When to choose one service mesh over another**

> ![](converted/media/image290.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Choose Istio for complex,
> feature-rich requirements
>
> ![](converted/media/image291.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Choose Linkerd for simplicity and
> performance
>
> ![](converted/media/image292.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}Consider Consul Connect if already
> using HashiCorp tools
>
> ![](converted/media/image293.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}NGINX Service Mesh if familiar with
> NGINX and need basic mesh features

Week 5: Practical Project

**Designing and implementing a microservices application**

> 1\. Create 3-4 simple microservices (e.g., frontend, backend,
> database) 2. Containerize each service with Docker\
> 3. Create Kubernetes manifests for each service

**Deploying the application using Helm**

> 1\. Create a Helm chart for the entire application\
> 2. Use subchart for each microservice\
> 3. Define configurable values in values.yaml

**Implementing service mesh features**

> 1\. Choose either Istio or Linkerd based on your preference\
> 2. Implement traffic routing between service versions\
> 3. Set up mTLS between services\
> 4. Configure observability (metrics, tracing)

**Creating Python scripts for automation**

> 1\. Script to deploy/update the Helm release\
> 2. Script to check service health and metrics\
> 3. Script to perform canary deployments

This comprehensive deep dive covers the entire 4-week training plan,
providing a solid foundation in Kubernetes, service mesh technologies,
and related tools. Remember to practice hands-on with each concept and
refer to official documentation for the most up-to-date information.

> **Additional Resources and Best Practices**
>
> ![](converted/media/image294.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Throughout the training, refer to
> official documentation for each technology
>
> ![](converted/media/image295.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Join community forums or discussion
> groups for each technology
>
> ![](converted/media/image296.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Consider working on a personal
> project that incorporates all these technologies
>
> ![](converted/media/image297.png){width="4.1666666666666664e-2in"
> height="4.1666666666666664e-2in"}Explore real-world use cases and
> examples
>
> ![](converted/media/image298.png){width="4.1666666666666664e-2in"
> height="5.555555555555555e-2in"}Practice hands-on exercises daily
>
> **Tips for Successful Service Mesh Adoption**
>
> 1\. Start your service mesh journey early to allow your knowledge to
> grow organically as your microservices landscape evolves. 2. Avoid
> common design and implementation pitfalls by thoroughly understanding
> each technology.
>
> 3\. Leverage your service mesh as the mission control of your
> multi-cloud microservices landscape.
>
> 4\. Consider starting with a sample project to evaluate which service
> mesh solution you prefer before standardizing across all services. 5.
> Use service mesh as a \'bridge\' while decomposing monolithic
> applications into microservices.
>
> 6\. Implement service mesh incrementally, starting with the components
> you need most.

By following this training plan, you\'ll gain a solid foundation in
service mesh concepts, Kubernetes, Helm, and Python, with practical
experience in both Istio and Linkerd. Remember to adapt the pace and
depth of each topic based on your prior knowledge and learning speed.

Tools

+---------+---------+---------+---------+---------+---------+---------+
| k9s :   |         | ![](    | K9s: a  |         |         |         |
|         |         | vertopa | Kub     |         |         |         |
|         |         | l_c4f4b | ernetes |         |         |         |
|         |         | aa402e6 | Cluster |         |         |         |
|         |         | 47588ec | Man     |         |         |         |
|         |         | b2a507c | agement |         |         |         |
|         |         | 21de28/ | Tool    |         |         |         |
|         |         | media/i |         |         |         |         |
|         |         | mage299 |         |         |         |         |
|         |         | .png){w |         |         |         |         |
|         |         | idth="0 |         |         |         |         |
|         |         | .125in" |         |         |         |         |
|         |         | he      |         |         |         |         |
|         |         | ight="6 |         |         |         |         |
|         |         | .944444 |         |         |         |         |
|         |         | 4444444 |         |         |         |         |
|         |         | 45e-2in |         |         |         |         |
|         |         | "}![](v |         |         |         |         |
|         |         | ertopal |         |         |         |         |
|         |         | _c4f4ba |         |         |         |         |
|         |         | a402e64 |         |         |         |         |
|         |         | 7588ecb |         |         |         |         |
|         |         | 2a507c2 |         |         |         |         |
|         |         | 1de28/m |         |         |         |         |
|         |         | edia/im |         |         |         |         |
|         |         | age300. |         |         |         |         |
|         |         | png){wi |         |         |         |         |
|         |         | dth="0. |         |         |         |         |
|         |         | 1125in" |         |         |         |         |
|         |         | heig    |         |         |         |         |
|         |         | ht="0.1 |         |         |         |         |
|         |         | 125in"} |         |         |         |         |
+=========+=========+=========+=========+=========+=========+=========+
|         | ![]     |         |         |         |         |         |
|         | (vertop |         |         |         |         |         |
|         | al_c4f4 |         |         |         |         |         |
|         | baa402e |         |         |         |         |         |
|         | 647588e |         |         |         |         |         |
|         | cb2a507 |         |         |         |         |         |
|         | c21de28 |         |         |         |         |         |
|         | /media/ |         |         |         |         |         |
|         | image30 |         |         |         |         |         |
|         | 1.png){ |         |         |         |         |         |
|         | width=" |         |         |         |         |         |
|         | 0.11111 |         |         |         |         |         |
|         | 1111111 |         |         |         |         |         |
|         | 1111in" |         |         |         |         |         |
|         | heig    |         |         |         |         |         |
|         | ht="6.9 |         |         |         |         |         |
|         | 4444444 |         |         |         |         |         |
|         | 4444445 |         |         |         |         |         |
|         | e-2in"} |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
| kubectl |         |         |         | ![](    |         |         |
| :       |         |         |         | vertopa |         |         |
|         |         |         |         | l_c4f4b |         |         |
|         |         |         |         | aa402e6 |         |         |
|         |         |         |         | 47588ec |         |         |
|         |         |         |         | b2a507c |         |         |
|         |         |         |         | 21de28/ |         |         |
|         |         |         |         | media/i |         |         |
|         |         |         |         | mage106 |         |         |
|         |         |         |         | .png){w |         |         |
|         |         |         |         | idth="0 |         |         |
|         |         |         |         | .113888 |         |         |
|         |         |         |         | 8888888 |         |         |
|         |         |         |         | 8889in" |         |         |
|         |         |         |         | hei     |         |         |
|         |         |         |         | ght="0. |         |         |
|         |         |         |         | 1124989 |         |         |
|         |         |         |         | 0638670 |         |         |
|         |         |         |         | 167in"} |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         |         | ![](    |         | >       |         |
|         |         |         | vertopa |         | Install |         |
|         |         |         | l_c4f4b |         |         |         |
|         |         |         | aa402e6 |         |         |         |
|         |         |         | 47588ec |         |         |         |
|         |         |         | b2a507c |         |         |         |
|         |         |         | 21de28/ |         |         |         |
|         |         |         | media/i |         |         |         |
|         |         |         | mage302 |         |         |         |
|         |         |         | .png){w |         |         |         |
|         |         |         | idth="0 |         |         |         |
|         |         |         | .113887 |         |         |         |
|         |         |         | 7952755 |         |         |         |
|         |         |         | 9055in" |         |         |         |
|         |         |         | hei     |         |         |         |
|         |         |         | ght="0. |         |         |         |
|         |         |         | 1138888 |         |         |         |
|         |         |         | 8888888 |         |         |         |
|         |         |         | 889in"} |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+


<img src="img/authors/geeky.jpg" width="40"/>