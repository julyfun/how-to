---
title: "Microduck"
date: 2026-10-22 20:02:49
tags: ["26", "10"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 27.0.0 Darwin Kernel Version 27.0.0: Tue Aug 11 21:02:59 PDT 2026; root:xnu-13432.1.9~1/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

## 在线可视化零件
- https://nowpop.art/cad/v/Pop3D-ZVP4B.g3d
- 模型文件: https://github.com/7757/fanduck

## 购买列表
看腾讯文档. https://docs.qq.com/sheet/DWHVuV25QQ1hpY29C?tab=000001

买完以后我整个脑子都通透了，原来嵌入式这么简单...

## 电控通信

1. 物理层（电平 / 电气）：TTL、RS485、RS232、差分、单端；规定电压、布线、驱动能力
2. 链路 / 帧层（串行收发规则）：UART（起止位、波特率、校验）；RS485 只是物理层，本身不带帧定义，通常承载 UART 帧
3. 上层协议（包语义）：Modbus（常跑在 UART/485 上）

额外几个你关心的放旁边：

- GPIO：硬件引脚资源，不属于通信栈；可以输出普通高低电平、PWM（调制信号，无帧）
- PWM：信号调制方式，不是协议，跑在 GPIO 上
- USB：一整套完整栈（物理 + 链路 + 协议），和 UART 不是一套

一句话层级：UART 是帧协议，RS485 是物理介质，UART 可以跑在 TTL 或 RS485 物理层上。
