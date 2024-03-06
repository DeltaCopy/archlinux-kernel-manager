# Arch Linux Kernel Manager

A GTK4 Python application used to install/remove Linux kernels on an Arch based system.

# Official Kernels

The following Kernels are supported:

- linux
- linux-lts
- linux-zen
- linux-hardened
- linux-rt
- linux-rt-lts

![Official kernel](https://github.com/DeltaCopy/archlinux-kernel-manager-dev/assets/121581829/bb509540-47ae-4735-968b-89ac330eb9ee)

# Community based Kernels

Community based Kernels are also supported, as long as the necessary Pacman repositories are configured

- linux-xanmod
- linux-xanmod-lts
- linux-cachyos
- linux-ck
- linux-lts-tkg-bmq
- linux-lts-tkg-pds
- linux-lqx
- linux-ck
- linux-clear
- linux-amd
- linux-nitrous

![Community kernel](https://github.com/DeltaCopy/archlinux-kernel-manager-dev/assets/121581829/cfda3727-178f-4465-aa31-378bce630aee)

# Bootloader

After a successful install/removal of a kernel the relevant bootloader entries are updated.
By default, the application will use `bootctl` to distinguish which bootloader (Grub/systemd-boot) is currently being used.

## Grub

`grub-mkconfig` is run to update the grub.cfg file

## systemd-boot

`bootctl update` is run to update the systemd-boot entries

# Advanced settings

## Bootloader settings

The bootloader settings can be overridden using the Advanced settings window.

![Advanced settings](https://github.com/DeltaCopy/archlinux-kernel-manager-dev/assets/121581829/3002012c-a721-4b46-bdc0-c7d64f378050)

# Default configuration file

This file can be found inside `$HOME/.config/archlinux-kernel-manager`

```toml

title = "ArchLinux Kernel Manager Settings"

[kernels]

# Kernels which are sourced from the ALA (Arch Linux Archive) https://archive.archlinux.org
official = [
    { name = "linux", description = "The Linux kernel and modules (Stable)", headers = "linux-headers" },
    { name = "linux-lts", description = "The LTS Linux kernel and modules (Longterm)", headers = "linux-lts-headers" },
    { name = "linux-zen", description = "The Linux ZEN kernel and modules (Zen)", headers = "linux-zen-headers" },
    { name = "linux-hardened", description = "The Security-Hardened Linux kernel and modules (Hardened)", headers = "linux-hardened-headers" },
    { name = "linux-rt", description = "The Linux RT kernel and modules (Realtime)", headers = "linux-rt-headers" },
    { name = "linux-rt-lts", description = "The Linux RT LTS kernel and modules (Realtime Longterm)", headers = "linux-rt-lts-headers" },
]

# Kernels which are sourced from unofficial repositories, these won't work if you haven't updated your pacman configuration
# https://wiki.archlinux.org/title/Unofficial_user_repositories
community = [
    { name = "linux-xanmod", description = "The Linux kernel and modules with Xanmod patches", headers = "linux-xanmod-headers", repository = "chaotic-aur" },
    { name = "linux-xanmod-lts", description = "The Linux kernel and modules with Xanmod patches", headers = "linux-xanmod-lts-headers", repository = "chaotic-aur" },
    { name = "linux-amd", description = "Linux kernel aimed at the ZNVER4/MZEN4 AMD Ryzen CPU based hardware", headers = "linux-amd-headers", repository = "chaotic-aur" },
    { name = "linux-cachyos", description = "The Linux EEVDF-BORE scheduler Kernel by CachyOS with other patches and improvements kernel and modules", headers = "linux-cachyos-headers", repository = "chaotic-aur" },
    { name = "linux-ck", description = "The Linux kernel and modules with ck's hrtimer patches", headers = "linux-ck-headers", repository = "repo-ck" },
    { name = "linux-clear", description = "The Clear Linux kernel and modules", headers = "linux-clear-headers", repository = "chaotic-aur" },
    { name = "linux-lts-tkg-bmq", description = "The Linux-tkg kernel and modules", headers = "linux-lts-tkg-bmq-headers", repository = "chaotic-aur" },
    { name = "linux-tkg-pds", description = "The Linux-tkg kernel and modules", headers = "linux-tkg-pds-headers", repository = "chaotic-aur" },
    { name = "linux-lqx", description = "The Linux Liquorix kernel and modules", headers = "linux-lqx-headers", repository = "chaotic-aur" },
    { name = "linux-nitrous", description = "Modified Linux kernel optimized for Skylake and newer, compiled using clang", headers = "linux-nitrous-headers", repository = "chaotic-aur" },
]

# custom bootloader example
#[bootloader]
#name = "grub"
#grub_config = "/boot/grub/grub.cfg"

```

Further Kernels can be added using the same format.

When adding new community based un-official kernels, the repository name should match the one defined inside the pacman `/etc/pacman.conf` file under `[repo-name]`.
Further details on un-official kernels can be found on https://wiki.archlinux.org/title/Kernel#Unofficial_kernels

# Cache

Kernel data retrieved from the ALA is stored inside a toml based file inside `$HOME/.cache/archlinux-kernel-manager/kernels.toml`

This cached file is updated every 5 days to ensure the application is kept up to date with the latest kernels.
Clicking on Update inside Advanced Settings, will force the application to update the cache.

# Logs

Logs can be found inside `/var/log/archlinux-kernel-manager`