---
title: "Microduck"
date: 2026-10-22 20:02:49
tags: ["26", "10"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 27.0.0 Darwin Kernel Version 27.0.0: Tue Aug 11 21:02:59 PDT 2026; root:xnu-13432.1.9~1/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

- [ ] 相机和 tof 大概看一下
- [ ] 电源 5v
- [ ] 扬声器
- [ ] 螺丝之类的

## 在线可视化零件
https://nowpop.art/cad/v/Pop3D-ZVP4B.g3d

## 购买列表
1. [x] 舵机x15
2. [ ] 主控 Radxa
3. [ ] 存储卡 microSD
4. [ ] USB-C 1m
5. [ ] Robot HAT C1
6. [ ] 40针低矮排母
7. [ ] ID200 身体姿态板
8. [ ] 1转4 DC Hub
9. [ ] 广角相机
10. [ ] 8x8 测距模块
11. [ ] ToF 四芯连线
12. [ ] 扬声器
13. [ ] NP-F550 电池
14. [ ] 双槽 USB 充电器
15. [ ] 电池触点板
16. [ ] 莲花头触点
17. [ ] 红黑主电源线
18. [ ] X3P 舵机线
19. [ ] 黑色绝缘胶带
20. [ ]

## 电控通信

1. 物理层（电平 / 电气）：TTL、RS485、RS232、差分、单端；规定电压、布线、驱动能力
2. 链路 / 帧层（串行收发规则）：UART（起止位、波特率、校验）；RS485 只是物理层，本身不带帧定义，通常承载 UART 帧
3. 上层协议（包语义）：Modbus（常跑在 UART/485 上）

额外几个你关心的放旁边：

- GPIO：硬件引脚资源，不属于通信栈；可以输出普通高低电平、PWM（调制信号，无帧）
- PWM：信号调制方式，不是协议，跑在 GPIO 上
- USB：一整套完整栈（物理 + 链路 + 协议），和 UART 不是一套

一句话层级：UART 是帧协议，RS485 是物理介质，UART 可以跑在 TTL 或 RS485 物理层上。
