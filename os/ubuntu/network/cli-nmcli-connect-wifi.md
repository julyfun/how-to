---
reliability: "[60% (author), 0 / 0 (visitor)]"
date: 2024-05-08
language: "Chinese"
os: "Darwin floriandeMacBook-Air.local 22.5.0 Darwin Kernel Version 22.5.0: Mon Apr 24 20:53:44 PDT 2023; root:xnu-8796.121.2~5/RELEASE_ARM64_T8103 arm64"
author: "Julyfun MacOS13.4 M1"
suppose-you-know: [computer]
keywords: [wifi, network]
---

# Cli (nmcli) connect wifi

ref: https://blog.csdn.net/kdongyi/article/details/84557708

```
sudo apt-get install nmcli
# 查看设备
sudo nmcli dev

# 开启 wifi
sudo nmcli r wifi on

# 扫描 wifi
sudo nmcli dev wifi

sudo nmcli dev wifi connect "wifi名" password "密码"
```

