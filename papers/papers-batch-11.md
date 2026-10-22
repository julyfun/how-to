---
title: "papers batch 11"
date: 2026-10-15 19:40:22
tags: ["papers"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 27.0.0 Darwin Kernel Version 27.0.0: Tue Aug 11 21:02:59 PDT 2026; root:xnu-13432.1.9~1/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

## Embodied Turing Machines (83)

⭐️⭐️ NTU 南洋理工 | https://arxiv.org/html/2610.12369v1

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20261015200126855.png)

通过文本记录 环境状态, 机器人状态 和 任务状态. dojo 刷到 70.

## When Do Discrete Actions Make Good Continuous Controllers? (84)

⭐️⭐️⭐️⭐️ 离散动作或许不劣于连续. Zeji Yi, Guanya Shi, CMU | https://www.alphaxiv.org/abs/2610.20429

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20261016180730842.png)

本文发现 paligemma 直接接动作头，flow 离散 > flow 连续 > regression 离散 > regression 连续 ... (robocasa SR)

为了让离散动作协调，用 flow 调节 logits + 逐渐随机确定采样. CFG 能降低 token ambiguity 和动作分散度，但是 GT coverage 也会减小.

另外，tokenize 过程中注入几何先验（如 FAST 编码）还不如 uniform bin.

## 智元 CEL (85)

⭐️⭐️⭐️

96 台机器人共享经验，失败时用 s-dtw / vlm 等方式寻找接近的成功片段并提高其 sft 权重. 该方法称为 FERT.

FERT 需要人在旁边打 01 标，但是不加数据.

## UniWAM (86)

港科大 & 欧拉万象 | https://www.alphaxiv.org/abs/2610.02054

Motus 架构 (VLM + WAN + AE).

后训练非常非常 hack. Latent 随机 0-50% 扰动，生成 A2A (从随机噪声开始生成下一段动作，而是把机器人刚执行过的动作片段加少量噪声作为生成起点，η=0.02)

libero plus 92, robotwin c2r 68.

## VAM (87)

wenye yu | https://www.alphaxiv.org/abs/2610.22368

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20261022012815404.png)

动机大概是解决 recap 离线迭代太慢以及观测歧义问题. 本文将 trainer 改为 online，并且 value history 会经过 GRU 输入给 VLA.

replay buffer 混合了离线 sft，dagger 和真机 rollout 数据。advantage FM 根据本轮 `H步 td advantage[1]` 的 70% 分位数打 01 优势标签.

1. `r[t:t+H] + gamma^H*(1 - d_t)V(s_(t+H)) - V(s_t)`

## Phoenix (88)

无界动力 | https://openphoenix-team.github.io/Phoenix-pages/

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20261022013811864.png)

MWA 变体，ILA 变体和 PhysCanvas 变体. MWA 刷到 dojo 真机榜一（无仿真），c2r 72. libero plus 94.

5w 小时 EGO + teleop + UMI 数据.

ILA 有触觉. PhysCanvas 模拟器.

## n0-twam (89)

FDU & NeoteAI | https://www.alphaxiv.org/abs/2607.23783

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20261022211730229.png)

触觉有独立 expert. 另外会输出预测触觉，并输入给 ae

触觉编码为自己提出的 Neoforce，初始化为 DINOv2，触觉 -> 三轴表面力图(3, H, W) -> 力觉信息.

在 UniVTAC 和 NeoSim 上. 点数挺高. 真机点数和 pi05 差不多.

## OneWM (90)


