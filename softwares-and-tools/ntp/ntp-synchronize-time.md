---
reliability: "[20% (author), 0 / 0 (visitor)]"
language: "Chinese"
os: "Darwin floriandeMacBook-Air.local 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1 20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64"
author: "Julyfun MacOS14.5 M1"
suppose-you-know: [computer]
date: 2024-05-23
title: "ntp synchronize time"
---

# ntp synchronize time

> by Yutong.Li @slack

117. 研究院局域网NTP同步指北：

研究院路由器（IP地址：10.53.21.1）一并提供时间同步服务

## 设置同步源：

### Linux（以Ubuntu为例）

首先安装ntp服务：

```
shell
sudo apt-get install -y ntp
```

编辑`/etc/ntp.conf`，添加一行

在Debian系统上该配置文件位于`/etc/ntpsec/ntp.conf`

server 10.53.21.1 iburst

如果不需要和其他时间服务器同步，注释其他的以`pool`、`server`开头的服务器配置

重启ntp服务，以便生效

shell
sudo systemctl restart ntp

注意：可能需要检查系统有没有运行systemd-timesyncd服务，这是系统自带的较为简单的时间同步服务，如果不需要则禁用

### Windows

在具有管理员权限的PowerShell终端中，执行：

shell
w32tm /config /manualpeerlist:10.53.21.1 /syncfromflags:manual /reliable:yes /update

依次执行下列命令重启NTP服务

shell
net stop w32time
net start w32time

## 检查同步质量

### Linux

使用`ntpq -p`确认同步质量

shell
➜  ~ ntpq -p
     remote                                   refid      st t when poll reach   delay   offset   jitter
=======================================================================================================
+10.53.21.1                              17.253.84.251    2 u    8   64    1   5.8984  -0.1837   1.8213

以下是对参数的解释：

- delay：这是往返到远程服务器的延迟，即5.8984毫秒。
- offset：这是本地系统时间与远程服务器时间的差值，即-0.1837毫秒。这个值越小，说明时间同步越准确。
- jitter：这是本地系统时间的抖动，即1.8213毫秒。这个值越小，说明时间同步越稳定。

### Windows

使用`w32tm /query /status`确认

```
shell
➜  ~ w32tm /query /status
Leap 指示符: 0(无警告)
层次: 3 (次引用 - 与(S)NTP 同步)
精度: -23 (每刻度 119.209ns)
根延迟: 0.0596580s
根分散: 7.7647534s
引用 ID: 0x0A351501 (源 IP:  10.53.21.1)
上次成功同步时间: 2024/5/18 19:24:32
源: 10.53.21.1
轮询间隔: 10 (1024s)
```

## 常见数值

无线网络中，同步误差在10ms左右

有线网络中，同步误差在100us左右 （已编辑） 

