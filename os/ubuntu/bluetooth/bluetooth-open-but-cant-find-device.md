---
reliability: "[35% (author), 0 / 0 (visitor)]"
language: "Chinese"
os: "Darwin 192.168.124.17 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1 20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64"
author: "Julyfun MacOS14.5 M1"
suppose-you-know: [computer]
date: 2024-06-24
title: "Bluetooth open but cant find device"
---

# Bluetooth open but cant find device

## Try this first

```
sudo rmmod btusb
sleep 1
sudo modprobe btusb
```

## If failed, try:

ref: https://blog.51cto.com/u_14193285/5985919

```
# 关闭蓝牙设备 
sudo hciconfig hci0 down
# 卸载蓝牙模块 
sudo rmmod btusb
# 重加载蓝牙模块 
sudo modprobe btusb
# 解锁蓝牙设备 
sudo rfkill unblock bluetooth
# 开启蓝牙设备 
sudo hciconfig hci0 up 
#重启蓝牙服务
sudo systemctl restart bluetooth
```

我这边做到 `hci0 up` 就无法继续了，但是没关系，关机 30s 后恢复，蓝牙就正常工作了。

> 下午又挂了！而且上面方法没用了！

试试这个，又成功启动了：

https://blog.csdn.net/Insight__/article/details/132777714

```
# 卸载并重新加载btusb内核模块（支持蓝牙设备的内核模块）
sudo rmmod btusb
sleep 1
sudo modprobe btusb

# 安装蓝牙工具和工具包
# 使用apt安装blueman蓝牙管理工具
sudo apt install blueman
# 使用apt-get安装blue-utils蓝牙实用工具
sudo apt-get install blue-utils
# 使用apt-get安装bluez蓝牙套件的所有相关包
sudo apt-get install bluez*
 
# 3、启动蓝牙服务
sudo service bluetooth start
 
# 4、重新解除蓝牙设备的阻止
# 阻止蓝牙设备
rfkill block bluetooth
# 解除对蓝牙设备的阻止
rfkill unblock bluetooth 
```

> this cmd verified to be effective on 24.6.25
>
> this cmd verified to be effective on 24.6.25 again, the rmmod and modprobe is enough
>
> this cmd verified to be effective on 24.6.27 again, the rmmod and modprobe is enough
>
> this cmd verified to be effective on 24.9.9 on linux, the rmmod and modprobe is enough

