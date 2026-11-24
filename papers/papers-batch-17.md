---
title: "papers batch 17"
date: 2026-11-18 15:56:20
tags: ["papers"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 27.0.0 Darwin Kernel Version 27.0.0: Tue Aug 11 21:02:59 PDT 2026; root:xnu-13432.1.9~1/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

## Robometer (133)

⭐️⭐️⭐️ 南加州 Anthony Liang, Jesse Zhang | https://www.alphaxiv.org/abs/2603.02115

通用进度模型。用 100w eps，在 t/T 进度监督的基础上构造偏好监督，即同一任务的两条轨迹判断哪条轨迹更好（通过失败轨迹、倒放和错配任务自动构造数据）.

基模: Qwen-VL-4B-Instruct. 实验先用 IQL 训练 critic 然后 SAC-DSRL 微调 pi0. 不过任务也是比较简单. 基本就是 pick and place & singletask.

## WiTac (134)

## 下面补充老文章的索引

## Behavior Generation with Latent Actions (135)

⭐️⭐️⭐️ 首尔大学 & 纽约大学，Pinto 组 | https://www.alphaxiv.org/abs/2403.03181

提出了 VQ-Bet，通过 RVQ 离散化动作，transformer 一个头预测它们的 logits，另一个直接回归连续偏移量保证动作精确.

## Robomimic (136)

danfei xu, feifei li | https://www.alphaxiv.org/abs/2108.03298

2021，纯视觉输入，mujoco 仿真，按数据质量划分不同 track...

## A Careful Examination of ... LBM (137)

⭐️⭐️⭐️ 丰田 TRI | https://www.alphaxiv.org/pdf/2507.05331

用一个 from scratch 的较大 DP 验证了预训练 scaling，包括成功率提升以及后训练所需数据减少 (3-5x less). 任务比较难包含组装任务，相对来说比较 solid.

不过论文没有深入拆解具体的表征或因果机制，主要证据仍是 SR.

## SERL (138)

jianlan luo, chelsea finn, sergey levine, UCB | https://www.alphaxiv.org/abs/2401.16013

本文贡献是提供了 Sample Efficient 软件框架，基于 RLPD（SAC，且采样时一半来自 replay buffer 一半来自示范数据）同时补充了视觉成功判别器，自动复位，阻抗控制器和并发执行动作和训练. 没有 BC 损失.

## Hil-SERL (139)

jianlan luo, sergey levine, UCB | https://www.alphaxiv.org/pdf/2410.21845

SERL + 人工纠正. 即使是人工纠正数据，也使用成功判别器给奖励. 仍然没有 BC 损失.

任务变难了一点.

## GR-RL (140)

yunfei li, yonghui wu, 字节 | https://www.alphaxiv.org/abs/2512.01801

离线阶段用 TD3 + BC 训练 critic，丢弃其 actor，然后对 VLA 进行 DSRL. 对数据镜像对称相当于数据量翻倍，这个我尝试过感觉有点 dirty work.

## 一些遥操作方法

- GELLO: 小臂同构
- OPEN TEACH: VR 手势控制各种机械臂
