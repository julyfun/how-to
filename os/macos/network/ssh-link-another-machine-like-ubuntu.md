---
type: verified
language: "Chinese"
os: "Darwin floriandeMacBook-Air.local 22.5.0 Darwin Kernel Version 22.5.0: Mon Apr 24 20:53:44 PDT 2023; root:xnu-8796.121.2~5/RELEASE_ARM64_T8103 arm64"
author: "Julyfun MacOS13.4 M1"
suppose-you-know: [computer]
date: 2024-04-10
title: SSH Link Another Machine like Ubuntu
tags: []
---

# SSH Link Another Machine like Ubuntu

两台机器加入同一个局域网，注意不要连桥接网络（比如校园网）。

在 MacOS 13.4 上，按住 option 右键点击菜单 - 网络图标，可以直接看到你被分配的 ipv4 地址。

在 Ubuntu 上，通过 Settings -> Wifi 点击设置也可以看到 ipv4 地址。

直接 ssh 该地址，注意使用机器上已有的用户名。

