---
title:  "So You Want to Build Your Own Linux Distro"
subtitle: "From ‘slightly cursed Ubuntu remix’ to full Linux From Scratch"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/so-you-want-to-build-your-own-linux-distro.jpg"
date: 2026-04-26
tags: linux distro buildroot LFS devops
---

## So You Want to Build Your Own Linux Distro

Building your own Linux distro sounds like a mad scientist project, and in fairness, it is. It’s also one of the few exercises that genuinely teaches you how Linux fits together, end to end — kernel, init, libc, package format, bootloader, the lot.

This is the tutorial I wish I’d had when I first tried it: three paths, all with commands you can actually paste, versions you can pin, and the gotchas that cost me an evening so they don’t cost you one.

A small honesty note before we start. I’ve built and re-built the live-build and Buildroot examples below; they work on Debian 12 (bookworm) and a Raspberry Pi 4 respectively. The LFS section walks you through the [LFS 12.x book](https://www.linuxfromscratch.org/lfs/) — I’ll show you the shape of it and the bits that trip people up, but the book is the source of truth and the only sensible way to actually build it. I’m not pretending I compiled the universe between paragraphs.

---

## Step 0: What Are You Actually Building?

“Make my own distro” is one phrase covering at least four different projects:

- **A custom live ISO** — Debian/Ubuntu plus your tools, configs, branding. Boots from USB, optionally installs. This is what most people actually want when they say “distro”. **Effort: a weekend.**
- **An appliance image** — a tiny, single-purpose OS for a router, kiosk, sensor, or Pi. Tens of MB, not GB. Ships on hardware. **Effort: a weekend to a couple of weeks, depending on hardware quirks.**
- **A from-source system** — Linux From Scratch. You compile every package yourself. Educational, slow, beautiful, occasionally infuriating. **Effort: a long weekend if you’re fast and lucky, a fortnight of evenings if you’re mortal.**
- **A managed downstream distro** — your own apt repo or OSTree stream that real users update from. This is a product, not a project, and it’s mostly the “how do updates work?” problem. **Effort: ongoing, forever.**

Pick the smallest version that solves your actual problem. You can always graduate.

What you’ll need on the host for everything below:

- A Linux box (Debian 12, Ubuntu 24.04, or Fedora 41+ all fine). 8 GB RAM minimum, 16 GB comfortable. 50 GB of free disk. An SSD if you value your sanity.
- `git`, `build-essential`, `qemu-system-x86`, `qemu-system-arm`, `xz-utils`, `bc`, `flex`, `bison`, `libssl-dev`, `libelf-dev`, `cpio`.
- A little patience for compiler output you’ll never read.

```bash
sudo apt update
sudo apt install -y git build-essential qemu-system-x86 qemu-system-arm \
    xz-utils bc flex bison libssl-dev libelf-dev cpio rsync wget
```

---

## Path 1: Remix Debian with `live-build`

This is the path most people actually want. You get a bootable hybrid ISO (USB or DVD), pre-loaded with your packages, your dotfiles, your wallpaper, and your slightly opinionated firewall defaults. It boots live and can also install to disk if you include `debian-installer`.

`live-build` is the official Debian toolchain for this. Ubuntu’s `live-build` is similar but a fork; the example below targets Debian 12 (bookworm). Cubic is a friendlier GUI wrapper if you want to click through it instead — under the hood it does the same things.

### 1.1 Install the tooling

```bash
sudo apt install -y live-build live-boot live-config debootstrap squashfs-tools \
    xorriso isolinux syslinux-common memtest86+
```

### 1.2 Set up the project

Pick a working directory. I’ll use `~/distro/blinderlinux`.

```bash
mkdir -p ~/distro/blinderlinux
cd ~/distro/blinderlinux
lb config \
  --distribution bookworm \
  --architectures amd64 \
  --binary-images iso-hybrid \
  --debian-installer live \
  --archive-areas "main contrib non-free non-free-firmware" \
  --apt-indices false \
  --memtest memtest86+ \
  --bootappend-live "boot=live components quiet splash hostname=blinder username=blinder"
```

`lb config` writes a `config/` directory full of stub files. You don’t have to understand all of them yet; you just need to know which ones to edit.

What the flags actually buy you:

- `--distribution bookworm` — Debian 12. Swap for `trixie` if you want to live on Debian 13.
- `--archive-areas "... non-free-firmware"` — without this, your laptop’s wifi card won’t come up. Ask me how I know.
- `--debian-installer live` — adds a “Install” menu entry that uses the live system as the installer source. Drop it for live-only USBs.
- `--bootappend-live` — kernel cmdline for the live session. The `username` and `hostname` here are what you’ll see at the prompt.

### 1.3 Pick your packages

Make a package list. The filename matters: `.list.chroot` means “install in the live filesystem”.

```bash
mkdir -p config/package-lists
cat > config/package-lists/blinder.list.chroot <<'EOF'
# baseline
sudo
openssh-server
curl
wget
git
vim
tmux
htop

# the actual reason we built this
nmap
tcpdump
wireshark
john
hashcat
hydra
sqlmap
gobuster
ffuf
seclists

# devops bits
docker.io
docker-compose
kubectl
helm
ansible

# desktop, if you want one
task-xfce-desktop
firefox-esr
EOF
```

If you don’t want a desktop, drop the last block and add `--bootappend-live "... text"` to start in TTY mode.

### 1.4 Bake in your config files

Anything under `config/includes.chroot/` is copied verbatim into the live filesystem at the matching path. So:

```bash
mkdir -p config/includes.chroot/etc/skel
cat > config/includes.chroot/etc/skel/.bashrc <<'EOF'
export EDITOR=vim
alias ll='ls -lah --color=auto'
alias k='kubectl'
PS1='\[\e[35m\]\u@blinder\[\e[0m\]:\w\$ '
EOF

mkdir -p config/includes.chroot/etc/sudoers.d
cat > config/includes.chroot/etc/sudoers.d/90-blinder <<'EOF'
blinder ALL=(ALL) NOPASSWD: ALL
EOF
chmod 440 config/includes.chroot/etc/sudoers.d/90-blinder
```

For branding (wallpaper, plymouth theme, MOTD), drop files in the matching path under `config/includes.chroot/`. For example:

```bash
mkdir -p config/includes.chroot/usr/share/backgrounds/blinder
cp ~/Pictures/blinder-wallpaper.png \
   config/includes.chroot/usr/share/backgrounds/blinder/default.png
```

### 1.5 Hooks for the things files can’t do

Hooks are shell scripts run inside the chroot during the build. Use them when “drop a file” isn’t enough — enabling services, generating SSH host keys, locking accounts, that kind of thing.

```bash
mkdir -p config/hooks/normal
cat > config/hooks/normal/9000-blinder.hook.chroot <<'EOF'
#!/bin/sh
set -e

# enable services
systemctl enable ssh
systemctl enable docker

# regen ssh host keys on first boot, not at build
rm -f /etc/ssh/ssh_host_*
cat > /etc/systemd/system/regen-ssh-host-keys.service <<'UNIT'
[Unit]
Description=Regenerate SSH host keys on first boot
ConditionPathExists=!/etc/ssh/ssh_host_ed25519_key
Before=ssh.service

[Service]
Type=oneshot
ExecStart=/usr/bin/ssh-keygen -A

[Install]
WantedBy=multi-user.target
UNIT
systemctl enable regen-ssh-host-keys.service

# minimal firewall
apt-get install -y ufw
ufw default deny incoming
ufw default allow outgoing
ufw allow 22/tcp
echo y | ufw enable || true
EOF
chmod +x config/hooks/normal/9000-blinder.hook.chroot
```

The naming convention matters: `NNNN-name.hook.chroot` runs in the chroot, `.hook.binary` runs against the final image. Numeric prefix sets order.

### 1.6 Build it

```bash
sudo lb build 2>&1 | tee build.log
```

First build takes 20–40 minutes depending on your bandwidth and how much you stuffed into the package list. Subsequent builds, with the local cache warm, take 5–10. Output is `live-image-amd64.hybrid.iso` in the project root.

### 1.7 Boot the result before you trust it

```bash
qemu-system-x86_64 \
  -enable-kvm \
  -m 4096 \
  -smp 4 \
  -cdrom live-image-amd64.hybrid.iso \
  -boot d \
  -display gtk
```

You should land at a Debian live boot menu. Pick the live entry, log in as `blinder` (no password), confirm your tools are installed, sshd is up, and `ufw status` shows the rules you wanted. If anything is off, fix the config, then:

```bash
sudo lb clean
sudo lb build
```

### 1.8 Common live-build gotchas

- **`lb build` halts on a missing package.** Almost always a typo or a package that exists in `main` but you didn’t enable `contrib`/`non-free`. Re-run `lb config` with the right `--archive-areas`.
- **No wifi on real hardware.** You forgot `non-free-firmware`. Add it, rebuild.
- **Docker doesn’t start in the live session.** Live images run with overlay roots; the default `overlay2` storage driver tries to stack overlay-on-overlay and fails. In a hook, write `/etc/docker/daemon.json` with `{"storage-driver": "vfs"}` for the live image. Slow but it boots.
- **ISO boots in QEMU but not on bare metal.** Almost always the BIOS/UEFI mode mismatch. `iso-hybrid` is the right binary image type for both, but check the target machine’s firmware setting.
- **First boot is slow because of `ssh-keygen -A`.** That’s fine — that’s the regen service doing its job.

---

## Path 2: Buildroot for an Appliance or Pi

Buildroot is a different beast. It’s not a remix; it’s a build system that produces a tailored, tiny rootfs from source. Ten to fifty MB, no apt, no systemd unless you ask for it. Perfect for embedded boxes, Pi-based appliances, and anything where you want to know every binary on the disk.

This walkthrough targets a Raspberry Pi 4 (64-bit). The same project tree builds for qemu-arm if you don’t have a Pi handy.

### 2.1 Get Buildroot

Pin a version. Buildroot does an LTS release every February and a regular release every quarter; LTS is the right pick unless you need a brand new package.

```bash
cd ~/distro
git clone https://gitlab.com/buildroot.org/buildroot.git
cd buildroot
git checkout 2025.02.x   # current LTS at time of writing — check tags
```

### 2.2 Use an external tree, not the buildroot directory

This is the single most important Buildroot habit. **Never edit anything inside `buildroot/`.** All your customisations go in a separate “BR2_EXTERNAL” tree, so you can `git pull` Buildroot updates without merge hell.

```bash
mkdir -p ~/distro/blinder-br/{configs,board,package}
cd ~/distro/blinder-br

cat > external.desc <<'EOF'
name: BLINDER
desc: Blinder appliance external tree
EOF

cat > Config.in <<'EOF'
source "$BR2_EXTERNAL_BLINDER_PATH/package/blinder-firstboot/Config.in"
EOF

cat > external.mk <<'EOF'
include $(sort $(wildcard $(BR2_EXTERNAL_BLINDER_PATH)/package/*/*.mk))
EOF
```

### 2.3 Start from a defconfig

Buildroot ships defconfigs for hundreds of boards. For Pi 4 64-bit:

```bash
cd ~/distro/buildroot
make BR2_EXTERNAL=$HOME/distro/blinder-br raspberrypi4_64_defconfig
```

That seeds `.config`. Tweak it interactively:

```bash
make menuconfig
```

The bits worth flipping for a real appliance:

- **Toolchain → C library → glibc** unless size matters more than compatibility (then musl).
- **System configuration → Init system → systemd** if you want it; otherwise BusyBox init is fine and tiny.
- **System configuration → Root password** — set it now. Default is empty, which is awful.
- **Target packages → Networking applications → openssh, dropbear, dhcpcd, wpa_supplicant**.
- **Filesystem images → ext4 root filesystem** and **squashfs** if you want a read-only rootfs with overlay.

Save when done. Save the config back into your external tree so it’s versioned:

```bash
make BR2_DEFCONFIG=$HOME/distro/blinder-br/configs/blinder_defconfig savedefconfig
```

Next time anyone clones your tree:

```bash
make BR2_EXTERNAL=$HOME/distro/blinder-br blinder_defconfig
```

### 2.4 A custom package, properly

Pretend you want a tiny first-boot service that resizes the rootfs and writes a unique machine ID. Two files do it.

```bash
mkdir -p ~/distro/blinder-br/package/blinder-firstboot
cat > ~/distro/blinder-br/package/blinder-firstboot/Config.in <<'EOF'
config BR2_PACKAGE_BLINDER_FIRSTBOOT
    bool "blinder-firstboot"
    help
      First-boot script: resize rootfs, generate machine-id.
EOF

cat > ~/distro/blinder-br/package/blinder-firstboot/blinder-firstboot.mk <<'EOF'
################################################################################
# blinder-firstboot
################################################################################

BLINDER_FIRSTBOOT_VERSION = 1.0
BLINDER_FIRSTBOOT_SITE = $(BR2_EXTERNAL_BLINDER_PATH)/package/blinder-firstboot/src
BLINDER_FIRSTBOOT_SITE_METHOD = local

define BLINDER_FIRSTBOOT_INSTALL_TARGET_CMDS
    $(INSTALL) -D -m 0755 $(@D)/firstboot.sh \
        $(TARGET_DIR)/usr/sbin/firstboot.sh
    $(INSTALL) -D -m 0644 $(@D)/firstboot.service \
        $(TARGET_DIR)/usr/lib/systemd/system/firstboot.service
endef

define BLINDER_FIRSTBOOT_INSTALL_INIT_SYSTEMD
    $(INSTALL) -D -m 0644 $(@D)/firstboot.service \
        $(TARGET_DIR)/usr/lib/systemd/system/firstboot.service
    mkdir -p $(TARGET_DIR)/etc/systemd/system/multi-user.target.wants
    ln -sf ../../../../usr/lib/systemd/system/firstboot.service \
        $(TARGET_DIR)/etc/systemd/system/multi-user.target.wants/firstboot.service
endef

$(eval $(generic-package))
EOF
```

Then drop a real `firstboot.sh` and `firstboot.service` in `package/blinder-firstboot/src/`. After enabling the package in `menuconfig`, it’s baked into every image.

### 2.5 Rootfs overlays for static config

For one-off files (network config, MOTD, your CA cert), an overlay directory is faster than a package.

```bash
mkdir -p ~/distro/blinder-br/board/rpi4/rootfs-overlay/etc
echo "blinder-pi" > ~/distro/blinder-br/board/rpi4/rootfs-overlay/etc/hostname
```

Tell Buildroot where it is via menuconfig:

```
System configuration → Root filesystem overlay directories →
    $(BR2_EXTERNAL_BLINDER_PATH)/board/rpi4/rootfs-overlay
```

### 2.6 Build

```bash
cd ~/distro/buildroot
make
```

First build: 30–90 minutes depending on your CPU and the package count. Subsequent builds are minutes. Output lands in `output/images/`:

- `Image` — the kernel
- `bcm2711-rpi-4-b.dtb` — device tree for Pi 4
- `rootfs.ext4` — the root filesystem
- `sdcard.img` — a complete bootable SD image (this is the one you flash)

### 2.7 Boot the result

For a real Pi:

```bash
sudo dd if=output/images/sdcard.img of=/dev/sdX bs=4M conv=fsync status=progress
sync
```

Replace `/dev/sdX` with your SD card. Get this wrong and you’ll overwrite your laptop. Read it twice.

For qemu-arm (handier for iteration), use a Buildroot defconfig with QEMU support: `qemu_aarch64_virt_defconfig` instead of the Pi one. Then:

```bash
qemu-system-aarch64 \
  -M virt -cpu cortex-a72 -m 1024 -smp 2 \
  -kernel output/images/Image \
  -drive file=output/images/rootfs.ext4,if=none,format=raw,id=hd0 \
  -device virtio-blk-device,drive=hd0 \
  -append "root=/dev/vda console=ttyAMA0" \
  -nographic
```

You’ll get a serial console boot. Log in as root with the password you set. `Ctrl-A x` to quit qemu.

### 2.8 Common Buildroot gotchas

- **You edited a file in `buildroot/`.** It’ll get clobbered. Move it to your external tree.
- **`make clean` doesn’t do what you think.** It nukes `output/`, including downloaded sources. For a quick rebuild of one package, `make <pkg>-rebuild`. For a full clean, `make distclean` (slower, but consistent).
- **The image works in qemu but not on the Pi.** The defconfig matters: `raspberrypi4_64_defconfig` for the 4, not the same for the 5. Check the right defconfig for your board.
- **First boot hangs at “Waiting for /dev/mmcblk0p2”.** Almost always a too-small SD image. Resize via a `BR2_ROOTFS_POST_IMAGE_SCRIPT` or expand on first boot.
- **You changed `.config` by hand and lost it.** That’s why you save it back to `configs/blinder_defconfig` after every meaningful change.

---

## Path 3: Linux From Scratch (the real one)

LFS is the “compile every package by hand” path. It takes a fortnight of evenings if you’re mortal, and you’ll learn more about Linux than any book or course can teach you. The [LFS book](https://www.linuxfromscratch.org/lfs/view/stable/) is the actual tutorial — it has exact commands, exact patches, exact md5sums. What I’ll do here is the meta-tutorial: the shape of it, the parts that catch people out, and how to not waste a week.

### 3.1 What you’re actually building

LFS produces a minimal, bootable Linux system using only source code. No package manager, no graphical environment, no network manager. Roughly 800 MB of system, built from ~80 source tarballs over ~30 hours of compile time on a decent laptop.

After LFS, [BLFS (Beyond LFS)](https://www.linuxfromscratch.org/blfs/) layers desktops, browsers, and services on top. [ALFS (Automated LFS)](https://www.linuxfromscratch.org/alfs/) lets you script the whole thing once you’ve done it manually and want to reproduce it.

### 3.2 Host requirements

LFS provides a [`version-check.sh`](https://www.linuxfromscratch.org/lfs/view/stable/chapter02/hostreqs.html) script. Run it on your build host before you do anything else. It checks gcc, make, bash, perl, etc. are all new enough.

Other prep:

- A dedicated partition or LVM volume of at least 30 GB, formatted ext4. You can use a loopback file for the first attempt to keep your laptop intact.
- A dedicated unprivileged build user, conventionally `lfs`, with a sanitised environment (the book’s `~/.bash_profile` and `~/.bashrc` are not optional — they prevent host pollution from leaking into your toolchain).

```bash
# As root, set up the partition and user
mount /dev/sdY1 /mnt/lfs
useradd -s /bin/bash -m -k /dev/null lfs
chown -v lfs /mnt/lfs
su - lfs
```

### 3.3 The phases, in order

LFS chapters group into phases. You will spend a different amount of pain on each.

1. **Prepare host (ch. 2–4)** — partition, user, env, sources tarball.
2. **Cross toolchain (ch. 5)** — build binutils-pass1, gcc-pass1, linux headers, glibc, libstdc++. This is the most fragile part. If something fails here, **stop and fix it**. Compounding errors downstream will eat your weekend.
3. **Cross-compile temporary tools (ch. 6)** — m4, ncurses, bash, coreutils, etc., all linked against the new toolchain.
4. **Enter the chroot (ch. 7)** — at this point `/mnt/lfs` is self-hosting enough that you `chroot` into it and continue from inside.
5. **Build the final system (ch. 8)** — every package, properly, in the order the book gives. This is the long bit. Don’t reorder. Don’t skip patches.
6. **System configuration (ch. 9)** — fstab, hostname, network, locale, /etc/hosts.
7. **Kernel and bootloader (ch. 10)** — `make menuconfig` for the kernel, GRUB to boot it.
8. **Reboot, log in, feel something (ch. 11)** — that’s your distro.

### 3.4 The four mistakes that cost everyone a day

- **Skipping the version-check.** A host gcc that’s too new or too old produces a temporary toolchain that subtly miscompiles glibc later. Run the script.
- **Not using the recommended `~/.bash_profile`.** Without it, your temporary build picks up `/usr/lib` from the host. You end up with an LFS that links against the host’s libc and crashes the moment you boot it standalone.
- **Running `make -j$(nproc)` for `glibc` install.** Some packages (glibc’s `make install`, for one) have race conditions in their install rules. Use `make` (no `-j`) for installs.
- **Editing the kernel `.config` without reading what’s on.** The book gives you a working baseline. Trim later, once you’ve booted once.

### 3.5 How long is this actually going to take?

Realistic on a modern laptop with `MAKEFLAGS='-j8'`:

| Phase | Hands-on | Wall-clock |
|-------|----------|------------|
| Host prep | 30 min | 30 min |
| Cross toolchain (ch. 5) | 1 hr | 2–3 hr |
| Temporary tools (ch. 6) | 1 hr | 2–3 hr |
| Chroot setup (ch. 7) | 30 min | 30 min |
| Final system (ch. 8) | 4–6 hr | 10–18 hr |
| System config (ch. 9) | 1 hr | 1 hr |
| Kernel + GRUB (ch. 10) | 1 hr | 2 hr |
| Total | ~10 hr | 18–28 hr |

Set up `tmux` (see [The Tool That Makes Your Terminal Feel Like a Cockpit](https://geekyblinder.co.uk/#/2026/12/20/Tmux-The-Tool-That-Makes-Your-Terminal-Feel-Like-a-Cockpit) when it publishes) and treat it as background work over a long weekend.

### 3.6 When you’re ready, [the book](https://www.linuxfromscratch.org/lfs/view/stable/) is the only thing you should be following

I can’t reproduce the LFS book in a blog post, and you shouldn’t want me to — it’s 350+ pages and gets revised every six months. Bookmark it, work top-to-bottom, and when something fails, the [LFS errata page](https://www.linuxfromscratch.org/lfs/errata/) is where the fixes live.

---

## Cross-Cutting: Hardening, Updates, and Reproducibility

Three things matter regardless of path.

### Hardening

Whichever route you took, you can bake in:

- **Minimal package set.** Every package is attack surface. If you don’t need `telnet`, `rsh`, `nfs-server`, don’t install them. live-build and Buildroot make this trivial; LFS makes it the default.
- **Kernel hardening.** KASLR on, `CONFIG_SLAB_FREELIST_HARDENED`, `CONFIG_SLAB_FREELIST_RANDOM`, lockdown mode, module signing. The [Kernel Self-Protection Project](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project) wiki has a current recommended config.
- **MAC layer.** AppArmor on Debian/Ubuntu remixes (it’s already there, just enable profiles). SELinux on RHEL-flavoured. On Buildroot/LFS, decide before you build — bolting it on later is annoying.
- **Sane defaults.** No empty root password (Buildroot default — change it). UFW or nftables enabled with deny-incoming. SSH key-only. Auto-updates on, or a clear update story (see below).
- **Threat model the thing.** Who’s using it, where, against whom? A pentest-USB and a kiosk for a public lobby have very different threat models. Don’t pretend they don’t.

### Updates: the actual hard problem

This is the bit most “build a distro” tutorials skip, and it’s where real distros live or die.

- **Live ISO, refreshed periodically.** Easy. You rebuild the ISO every month, users re-flash a USB. Fine for training/event use. Useless for fleets.
- **apt repo of your own.** You build, sign, and host packages. `reprepro` or `aptly` are the tools. You inherit Debian’s security-update cadence for the base. You become responsible for everything you’ve added on top, including CVE patching and signing.
- **Image-based updates (A/B partitions).** Two root partitions, swap-and-reboot atomic upgrades, automatic rollback on boot failure. [Mender](https://mender.io/), [RAUC](https://rauc.io/), or [SWUpdate](https://sbabic.github.io/swupdate/) for the orchestration. This is what serious appliances do.
- **OSTree / image-based desktops.** [rpm-ostree](https://coreos.github.io/rpm-ostree/) (Fedora Silverblue) and [bootc](https://github.com/containers/bootc) are where Linux desktop is heading. Atomic upgrades, easy rollback, declarative state. Worth a look if you’re going to maintain this for years.

Pick a story before you ship. Distros without an update story become liabilities the day after the first CVE drops.

### Reproducibility

If you can’t rebuild last month’s image and get the same bytes (or close to it), you don’t really know what you shipped.

- **Pin versions.** Debian release codename, Buildroot tag, LFS book version, kernel commit.
- **Vendor your sources.** Either a local mirror or hashes in your build system.
- **Script everything.** `live-build` configs go in git. Buildroot external tree goes in git. Even your LFS notes go in git.
- **Stamp the image.** `/etc/blinder-release` with build date, git commit, and config hash. Future-you will thank present-you when something boots weirdly and you have no idea which version it is.

---

## Iteration: How to Not Lose a Weekend

Three habits I’ve learnt the slow way.

- **Test in a VM first, every single build.** QEMU boot in a script that runs after every successful build. Catches 80% of regressions in 30 seconds.
- **Keep a known-good image.** When you’ve got a build that boots and works, copy the ISO/image to a `known-good/` directory with the date. When the next build won’t boot at 1am, you’ve got something to compare against.
- **Commit between every change.** `live-build` and Buildroot configs are tiny. Commit per tweak. `git bisect` will find the change that broke boot in five minutes.

---

## Final Thought

Building your own distro won’t impress anyone at the pub. It will, quietly, change how you read every other Linux thing for the rest of your career — kernel panics, container layers, cloud-init quirks, package-manager weirdness. You stop seeing Linux as a thing that came from somewhere and start seeing it as a thing you assemble.

Start with `live-build` if you want a USB you can hand to a colleague on Monday. Reach for Buildroot if your distro is really firmware. Climb LFS once, slowly, when you’ve got a fortnight and a good chair.

Either way, the next time someone says “just install Ubuntu,” you’ll know exactly how much that sentence is hiding.

<img src="img/authors/geeky.jpg" width="40"/>
