---
title: ssh
date: 2024-01-15 01:10:05
tags: ["softwares-and-tools", "docker"]
---
## 用 ssh 连接 docker 容器？

in the container:

```
apt install openssh-server
service ssh start

```
useradd nvidia
usermod -aG sudo nvidia
```

然后你在本机 `docker inspect <container> | grep "IPAddress"` 

下面要做什么就很显然了。

## 在 VSCode 中使用容器中的 clangd

用 Remote-ssh 插件链接这个容器

然后在左边插件栏目里对 ssh 的容器下载 clangd 插件

新建一个 1.cpp 然后打开这个 cpp，vscode 会提示你下载 clangd-server.

## docker 容器查看 usb 列表

sudo apt install usbutils

lsusb

居然这样就可以捏。

