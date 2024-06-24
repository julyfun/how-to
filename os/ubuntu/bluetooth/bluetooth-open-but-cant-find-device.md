---
reliability: "[35% (author), 0 / 0 (visitor)]"
date: 2024-06-24
language: "Chinese"
os: "Darwin 192.168.124.17 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1 20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64"
author: "Julyfun MacOS14.5 M1"
suppose-you-know: [computer]
keywords: []
---

# Bluetooth open but cant find device

ref: https://blog.51cto.com/u_14193285/5985919

```
sudo hciconfig hci0 down && \ #关闭蓝牙设备 
sudo rmmod btusb && \ #卸载蓝牙模块 
sudo modprobe btusb && \ #重加载蓝牙模块 
sudo rfkill unblock bluetooth && \ #解锁蓝牙设备 
sudo hciconfig hci0 up && \ #开启蓝牙设备 
sudo systemctl restart bluetooth #重启蓝牙服务
```

我这边做到 `hci0 up` 就无法继续了，但是没关系，关机 30s 后恢复，蓝牙就正常工作了。

