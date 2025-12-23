---
title: "I Installed Arch Linux"
date: 2025-01-01 00:28:40
tags: ["25", "01"]
author: "julyfun-4070s-ubuntu2204"
os: "Linux julyfun-4070s-ubuntu 6.8.0-90-generic #91~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Thu Nov 20 15:20:45 UTC 2 x86_64 x86_64 x86_64 GNU/Linux"
assume-you-know: [computer]
confidence: 2
---

## 回忆提纲
- 禁用服务
- 设置时钟
- 分区和格式化
- 挂载 （为了待会儿能够 pacstrap /mnt base linux linux-firmware）
    - [wtf] mount /dev/nvmexn1pn /mnt/boot # 这里挂载的得是 EFI 分区（256MB 那个），别挂你的 btrfs 分区
- pacstrap 给 /mnt 安装系统 (联网) 以及 fish-shell
- 生成 fstab
- 切到 /mnt，配置时区、locale 等
- pacman 安装 grub
- ok

## recall

`lsblk`

[q] iso

- [x] uninstall ubuntu

[q] 压缩卷时可压缩空间远小于实际剩余空间? 
- [not-ok] 磁盘管理，右键属性，优化
- [not-ok] https://blog.csdn.net/Rained_99/article/details/54023914
- [ok] DiskGenius (橙色图标)，右键 C 盘，调整大小。然后会自动压缩 -> 重启 -> 分区 -> 重启.

[q] UEFI & GRUB

[q] `加载内核和initramfs` initramfs?

[q] NVME ssd vs other? [re]

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

`free -h`

[q] Btrfs? [a] B-Tree filesystem. like zfs. ext4 超级进化版

`fdisk -l`

[q] mount zstd? [a] 进程读取/写入硬盘数据居然可以压缩. [ai] 一个 100KB 的文本文件实际在硬盘上可能只占 30-50KB 的空间

[q] dev 为啥要 mount 才能操作啊，和链接有啥区别 [a] 设备文件不是普通文件，没有文件结构，尝试直接读取会失败或得到原始二进制

[q] 这分成两个子卷啥意思，有何必要，而且这俩不是包含关系吗 [a] 这样 /home 和非 /home 位于两个子卷。且重装系统可以不覆盖 /home

[q] 每个子卷内部是连续地址吗 [a] 而是高度分散的（交错存储，数据块组）

[q] pacstrap [re]

[q] fstab? [a] genfstab 会智能扫描当前 /mnt 下的挂载情况，并生成对应的 fstab 配置，以后启动都这样挂载. 你刚 /mnt 是临时挂载的，重启就没了.

[note] /boot 就是 EFI 分区!!

[err] `boot vmlinuz-linux must be readable / The image may not be complete.` [sol] 我是挂载错分区了，退回格式化那一步.

[err] mount -t -o subvol.. 时 fsconfig() failed: No such file or directory [sol] 你忘记前面还有 mount 了

[err] pacstrap `file not found: /etc/vconsole.conf` [sol] echo "KEYMAP=us" > /mnt/etc/vconsole.conf

[done]

