---
title: "I Installed Arch Linux"
date: 2025-01-01 00:28:40
tags: ["25", "01"]
author: "julyfun-4070s-ubuntu2204"
os: "Linux julyfun-4070s-ubuntu 6.8.0-90-generic #91~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Thu Nov 20 15:20:45 UTC 2 x86_64 x86_64 x86_64 GNU/Linux"
assume-you-know: [computer]
confidence: 2
---

`lsblk`

[q] iso

- [x] uninstall ubuntu

[q] 压缩卷时可压缩空间远小于实际剩余空间? 
- [not-ok] 磁盘管理，右键属性，优化
- [not-ok] https://blog.csdn.net/Rained_99/article/details/54023914
- [ok] DiskGenius (橙色图标)，右键 C 盘，调整大小。然后会自动压缩 -> 重启 -> 分区 -> 重启.

[q] UEFI & GRUB

[q] `加载内核和initramfs` initramfs?

[q] NVME ssd vs other? [a]

order:
1.  **硬件上电** -> **UEFI/BIOS**（固件自检并初始化硬件）
2.  **引导程序**（Bootloader，如GRUB、systemd-boot、Windows Boot Manager） -> **加载内核与initramfs**到内存
3.  **内核**（Kernel，如vmlinuz、ntoskrnl.exe） -> **解压并挂载initramfs**作为临时根文件系统
4.  **initramfs中的/init脚本** -> **执行硬件探测、加载关键驱动模块**（如磁盘、文件系统、解密驱动） -> **挂载真正的根文件系统**（`/`）
5.  **内核切换到真实根文件系统** -> **启动第一个用户空间进程**（Linux：`systemd`（PID 1）或`init`；Windows：`smss.exe`）
6.  **第一个用户进程** -> **启动核心系统服务与守护进程**（Linux：由systemd启动各种`.service`；Windows：由smss.exe启动`csrss.exe`, `wininit.exe`等）
7.  **系统服务** -> **启动登录管理器/图形界面**（Linux：`gdm`, `sddm`等；Windows：`winlogon.exe`）
8.  **用户登录** -> **启动用户会话与桌面环境**（Linux：`gnome-shell`, `plasma`等；Windows：`explorer.exe`）
9.  **桌面环境/Shell** -> **用户可以执行应用程序**（如`firefox`, `notepad.exe`）

[q] 如果我要写内核模块，C语言，如何暴露接口给用户态程序
- [a]
