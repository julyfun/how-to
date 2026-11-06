---
title: "papers batch 15"
date: 2026-11-04 17:52:54
tags: ["papers"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 27.0.0 Darwin Kernel Version 27.0.0: Tue Aug 11 21:02:59 PDT 2026; root:xnu-13432.1.9~1/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

## EgoSteer (117)

⭐️⭐️ PKU AI, yifan zhong, yandong yang |https://egosteer.github.io/

demo 有手叠盒子，还挺好看的（睿研 RY-H2 6DOF）
- 提出了 EgoSmith 流水线，据说很快.
- 架构：qwen-vla 加上一个 wm expert 预测未来 dinov3，这是纯粹的辅助任务.
- 支持 dagger & 一些非常 trivial 的对齐技巧

## AIRoA-0 (118)

⭐️ AIRoA, 11/2 | https://a-0.airoa.io/ | https://www.alphaxiv.org/abs/2611.03815

<img src="https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20261105160140745.png"/>

不演了，我们就是 pi05！作者用 YUBI[1] 采集了 1.6wh 纯 UMI 数据，无任何本体数据，直接 pi05 + subtask 辅助 loss + 后训练额外当前阶段分类头. 但是这个 demo 简直拉完了，无限单手 pick and place.

1. YUBI: Quest3 手柄+头显定位。

## RoboScope Kit (119)

dengke wu, 赵波 | https://www.alphaxiv.org/abs/2611.03850

加速 robotwin 仿真评测. 1.5x - 4.5x. 主要 trick 是代码调度.

## worldbridge (120)

京东 jun cen, duo zheng | https://www.alphaxiv.org/abs/2610.40748


