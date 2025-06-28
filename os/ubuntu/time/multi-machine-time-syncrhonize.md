---
reliability: "[20% (author), 0 / 0 (visitor)]"
language: "Chinese"
os: "Darwin floriandeMacBook-Air.local 22.5.0 Darwin Kernel Version 22.5.0: Mon Apr 24 20:53:44 PDT 2023; root:xnu-8796.121.2~5/RELEASE_ARM64_T8103 arm64"
author: "Julyfun MacOS13.4 M1"
suppose-you-know: [computer]
date: 2024-05-08
title: "Multi machine time syncrhonize"
---

# Multi machine time syncrhonize

ref: https://blog.csdn.net/weixin_44684139/article/details/109844106

## 服务器 Ubuntu 20.04 nuc

```
sudo apt install ntp
sudo vim /etc/ntp.conf
```

文件最后写入：

```
restrict 192.168.43.0 mask 255.255.255.0 nomodify notrap # 将前三位改成你的子网
server 127.127.1.0 # local clock
fudge 127.127.1.0 stratum 10
```

重启 ntp 服务：

```
sudo /etc/init.d/ntp restart
```

## 客户端通过网线连接服务器

使用 ifconfig, `nmcli dev` 和设置查看是否连接正确。实践时，重启 ntp 服务之后两台机子的时间就同步了。

如果不同步，请继续参考 ref。

## Problem

- restart 服务后依然没有同步：试试看 reboot

