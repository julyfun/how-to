---
title: "ssh.old"
date: 2024-01-15 01:10:05
tags: []
---
## ssh-keys

in ~/.ssh/config:

```
Host docker2
    HostName 172.17.0.2
    User nvidia
```

```
ssh-copy-id docker2
```

输入一次密码，然后后面就不用密码了。

## 构建 ssh 内网 solution

搜搜 zero-tier

## linux 睡眠后无法链接 zero-tier ssh

reboot

## mac 睡眠后无法连接 zero-tier ssh

此时 linux 却可以连接。这时候我重启，连不上，等了几分钟然后就连上了。

clash-for-windows 应该是没影响的，测了一下。

