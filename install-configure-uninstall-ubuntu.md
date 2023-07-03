## Uninstall

1. F2 进入 BIOS，进入 Boot，把 Windows 移到最上面，Save and Exit
2. Win + R listpart 删除 Ubuntu 分区（由 15 GB 开头的“未知”分区）。给系统分区命名，然后用管理员打开记事本，打开其中文件资源管理器删除系统分区下 EFI 下 Ubuntu。

## Install

1. 买一个 U 盘
2. 下载 ubuntu-amd64.iso
3. 用 Rufus 软件把 U 盘变成启动盘
4. 计算机管理 -> C 盘压缩出 200 MB 作为 存放 Ubuntu EFI。另外开一个未知分区作为 Ubuntu 硬盘
5. 重启进入 BIOS，修改 Boot Mode 为 UEFI Only，然后把 U 盘放在 Windows 上面
6. 分区，200 MB 作为 efi ，剩下所有作为 `/`

## Configure to your style
