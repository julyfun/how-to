---
reliability: "[20% (author), 0 / 0 (visitor)]"
date: 2024-06-26
language: "zh-hans"
os: "Darwin 192.168.124.17 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1 20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64"
author: "Julyfun MacOS14.5 M1"
suppose-you-know: [computer]
keywords: []
---

# Can't boot after installing nvidia driver

Save your computer!

## Env:

- win 10
- GTX 1660 Ti
- 华硕主板

## Save

- del 进入 bios，Advanced Mode -> Boot -> Secure Boot -> 选择 Windows UEFI，Standard，重启
- 如果没有变化就多重启几次
- 继续启动，进入安全模式 https://jingyan.baidu.com/article/6b97984db5c2975da2b0bfd4.html
- 安全模式重新启动，进入设备管理器卸载显卡（测试可勾选删除驱动软件）
- 重启成功！

