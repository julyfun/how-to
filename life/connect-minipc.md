---
title: connect-minipc
date: 2024-01-15 01:10:05
tags: []
---
You type `ifconfig`.

如下是一个正常的小电脑的示例。

它的真实静态 ip 是 192.168.1.107，我给网口设置的地址是 192.168.1.1. 

netmask 必须是 255.255.255.0 哦，如果不是，你就在 Settings 里面 Wired 里面的设置设置好子网掩码，然后重新插拔网线，有时候不插拔就不刷新 netmask.

```
enx00e04c680fa9: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.1  netmask 255.255.255.0  broadcast 192.168.1.255
        inet6 fe80::dc3b:b7dd:e1fc:2252  prefixlen 64  scopeid 0x20<link>
        ether 00:e0:4c:68:0f:a9  txqueuelen 1000  (Ethernet)
        RX packets 7  bytes 1470 (1.4 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 20  bytes 2966 (2.9 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

