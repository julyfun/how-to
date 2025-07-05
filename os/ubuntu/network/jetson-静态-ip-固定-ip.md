---
reliability: 20% (author)
os: 'Darwin floriandeMacBook-Air.local 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1
  20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64'
author: Julyfun MacOS14.5 M1
assume-you-know:
- computer
date: 2025-01-05
title: jetson 静态 ip 固定 ip
tags: ["os", "ubuntu", "network"]
---
# jetson 静态 ip 固定 ip

ref: https://www.cnblogs.com/cc1784380709/p/17601331.html

先插网线，连接任意一台电脑，然后通过小电脑主机或者无线 ssh 输入命令:


```
sudo nmcli c mod Wired\ connection\ 1 ipv4.address 192.168.2.245/24 ipv4.gateway 192.168.2.1 ipv4.dns 8.8.8.8 ipv4.method manual # 设置 ip 地址  网关  以及 静态地址
sudo nmcli c up Wired\ connection\ 1 # 将设置的地址生效
```

> worked for jetson nano.

