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

⭐️⭐️ PKU AI, yifan zhong, yandong yang |https://egosteer.github.io/ | https://www.alphaxiv.org/abs/2607.09701

demo 有手叠盒子，还挺好看的（睿研 RY-H2 6DOF）
- 提出了 EgoSmith 流水线，据说很快.
- 架构：qwen-vla 加上一个 wm expert 预测未来 dinov3，这是纯粹的辅助任务.
- 支持 dagger & 一些非常 trivial 的对齐技巧. 所谓 steer 就是“让 ego 数据对灵巧手有用”

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

c2r 有 73.4%. 预训练是 ego + 真机 + 仿真，滑动窗口+历史抽帧; IDM 注意力; 采用 `Action Forcing`: 一块 action chunk 中不同的 action token 加不同的噪声来训练...

## delta flow (121)

Kuangji Zuo, Jianfei Yang, NTU 南洋理工 | https://www.alphaxiv.org/abs/2610.15794

将 A2A 思路引用到 V2V. 应用到不同的架构上，可以 inference only. 发现对于 pi05, imagewam, fastwam 都能提点. (libero-plus only)

顺便发现对于 imagewam 这个图像编辑策略，动作到 model 进行梯度截断可以提升 +5 PSNR. 另外还认为稀疏预测更好.

## Reinforcement Learning Enables.. (122)

ETHZ 苏黎世 | https://www.alphaxiv.org/abs/2611.06905 | https://lasgroup.github.io/generalist-improvement/

用了各种 RL 方法；其中 OGPO 是一种引导 flow 向高 critic 价值的方法.

OGPO > BoN (Best of N, using critic Q) > SFT

## Should the Action Expert Train the VLM (123)

NVIDIA, boyi li | https://www.alphaxiv.org/abs/2611.05249

从结论上论文认为 VLM 至少得有一路动作监督，token 和梯度哪一路都行，两路都断掉的时候最差；有动作 token 的时候，从头一起训的话不隔离还是更好一些

## When the Simulator Fails, Not the Policy (124)

Tsinghua, alex zhou & yongchao chen | https://www.alphaxiv.org/abs/2610.41857

本文通过审计插件评估了 robotwin 等仿真器的碰撞穿透 bug. `在 RoboTwin 2.0（PhysX 5.3.1）中，相距 1–2 cm 的碰撞体被误报为约 2 cm 的穿透，接触求解器随之在单步内以数米每秒的速度将其弹出。` 修复以后成功率提高.

"把 PhysX 5.3.1 源码里的那 1 个错误阈值常量改掉，89% 提高到了 98%，异常弹出回合由 12/100 降为 0"
