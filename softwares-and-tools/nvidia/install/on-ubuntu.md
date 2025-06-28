---
reliability: "[0% (author), 0 / 0 (visitor)]"
language: "zh-hans"
os: "Darwin floriandeMacBook-Air.local 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1 20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64"
author: "Julyfun MacOS14.5 M1"
suppose-you-know: [computer]
date: 2024-06-28
title: "on ubuntu"
---

# on ubuntu

- Ref: https://blog.csdn.net/qq_30468723/article/details/107531062
- Ref: https://blog.csdn.net/qq_42887760/article/details/126903100
- Ref: https://blog.csdn.net/xiaosongshine/article/details/115720887
- Arch kde ref: https://www.skyone.host/2024/archlinux-plasma-faq

- 清华源
- 装 555.run（不含 cuda，不是 developer 搜索的是 google 搜 nvidia drivers download）
- 装 kde。原因是，为了装驱动需进入文本界面关闭 gui 服务，但 gdm 不能直接关不然文本界面都没了，至少得装个 lightdm，那不如直接先装 sddm 的 kde 吧
- Kde 装好了 reboot
- 进文本界面 systemctl status sddm 正常，gdm 没开
- sudo /etc/init.d/sddm stop 直接进入了一个底层的终端，没法动，重启
- 那就 sudo telinit 3
- sudo service sddm stop ok!!
- ./NVIDIA.run 说找不到 cc ，重启
- sudo apt install gcc g++ make 还真没装
- sudo ./NVIDIA.run
- ok 现在它在加了两个 blacklist， /usr/lib 下和 /etc 重启下要删掉
- 重启需要进 tty，如果你卡住了就 ctrl + alt + F2 之类的进 tty，运行 /.run
- 这次要求关 Secure mode，那就重启并关闭并重启
- 在 ./run 说找不到 pkg-config，但是能继续安装
- 重启后进入桌面，但是桌面缩放错误，什么东西都特别大，完全操作不了~
- 试试 https://www.skyone.host/2024/archlinux-plasma-faq 中的 nvidia-drm，重启
- 缩放还是一样答辩
- sudo dpkg-reconfigure gdm3  ，虽然说 gdm3 服务 inactive 但是还是切换成功
- 重启发现桌面正常，甚至有 nvidia-smi，那好吧直接在 gdm 下开发看看

