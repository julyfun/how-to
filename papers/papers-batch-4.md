---
title: "papers batch 4"
date: 2026-06-22 14:41:38
tags: ["papers"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

## InSpire (27)
⭐️⭐️ 同济 Ji Zhang, Jingkuan Song | https://koorye.github.io/Inspire/ | https://arxiv.org/pdf/2505.13888

在 Pi0 基础上直接对 VLM 输入“物体在哪里” 作为 aux task 并且也会把输出结果直接再次输入 VLM.

## MEM (28)
⭐️⭐️⭐️ PI 团队

直接复制一个 pi0.5 的 VLM 作为 system 2 来做 text-level 长时序总结，而 system 1 改用 video 输入达到短时序能力.

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20260622151337338.png)

## LAPA (29)
⭐️⭐️⭐️ https://hjfy.top/arxiv/2410.11758

自监督在相邻帧训练 IDM -> latent_token -> FDM 模型，作为 VLM 的 pretraining label.

3 步训练:
1. 自监督利用互联网视频训练一个 encoder: (x1, x2) -> z（VQ 离散化）和 decoder: (x1, z) -> x2，这类似于 IDM 和 FDM. 这里 x1 和 x2 相差 T 帧.
2. 监督 Latent Pretraining: 利用上面模型打 label，然后给 VLM 接入一个新的 latent head，输入 x, l 输出 z
3. Action FT: 给 VLM 接入 action head，输入 x, l 输出 action

当然，对于 ego 视频来说画面的变化无法实际上完全用 z 解释，因素还有视角变化和物体运动等，因此这一套自监督不算很完备.

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20260622183820532.png)

## DreamVLA (30)
⭐️⭐️ 上交 wenyao zhang, EIT Xin Jin |  https://hjfy.top/arxiv/2507.04447

相比普通 WM，本文预测的不是 video latent 而是自定义的 world latent，train-time tasks 包括未来的动态区域、深度、DINO-V2 emb 等. infer-time 使用此 world latent 作为 action query 的 kv.

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20260622195900612.png)

## Lingbot-VLA (31)
⭐️⭐️ https://hjfy.top/arxiv/2601.18692

在 pi0 基础上使用了 FSDP 和 FlexAttention 提升吞吐量，增加了 learnable depth query -> [VLM (attend to image token)] -> [a new proj] -> depth token 的监督，并增大数据到 20000h.

## MemoryWAM: Efficient World Action Modeling with Persistent Memory (32)
⭐️⭐️⭐️ 用近期帧、起始帧和 gist tokens 来压缩长期记忆 [香港中文大学，Sizhe Yang，Huazhe Xu]

| <https://yangsizhe.github.io/MemoryWAM/> | https://hjfy.top/arxiv/2606.20562 | https://www.alphaxiv.org/abs/2606.20562 | <https://github.com/yangsizhe/MemoryWAM> |
|-|-|-|-|

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20260628223306877.png)

1. 所有帧共享 8 个 learnable gist query embedding，这样就可以每帧留下 8 个 gist embed 和对应 kv cache.（完整视觉 token 是 120 个）.
2. 滑动窗口完整视觉 token
3. 起始帧完整视觉 token

其他结构则是 Pi-like Video DiT + action expert DiT.

## DiT4DiT (33)
⭐️⭐️ [YY 硕]
| https://hjfy.top/arxiv/2603.10448 |
|-|

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20260629144114755.png)

一种正常的 Joint WAM. demo 是全身控制而论文中并没有提及，实际上代码中直接封装了 Nvidia GR00T-WholeBodyControl

## GEN-1: Scaling Embodied Foundation Models to Mastery
[Gemini 3.1 Pro] GEN-1 进一步扩展了无机器人数据预训练的具身模型，在简单物理任务上实现了 99% 成功率和 3 倍执行速度。 | Generalist AI, Generalist Team https://generalistai.com/blog/gen-1 | - | - | -
|-|-|-|-|-|

GEN-1 完全使用人类穿戴设备数据进行大规模预训练，并引入了 Harmonic Reasoning 推理技术。它在部署时仅需 1 小时机器人数据进行微调，即可在折叠盒子等简单任务上达到 99% 成功率和 3 倍执行速度。这证明了无机器人数据预训练结合少量微调的路线是可行的。

它目前仅在简单任务上展示了高成功率。模型涌现的即兴恢复能力有时会导致不符合预期的物理动作，这表明具身模型也需要研发对齐方法。

## Generating Robot Hands from Human Demonstrations
[Gemini 3.1 Pro] 利用人类手指运动轨迹，通过逆运动学直接优化并生成机器手硬件设计 | <加州大学圣地亚哥分校，Sha Yi，Xiaolong Wang> | <https://yswhynot.github.io/generating-robot-hands/> | https://hjfy.top/arxiv/2606.20549 | https://www.alphaxiv.org/abs/2606.20549
|-|-|-|-|-|

本文将逆运动学作为固定策略，联合优化机器手硬件参数和关节轨迹以拟合人类手指的运动轨迹。为了加速搜索，本文训练了一个 RL actor
来输出硬件设计和关节初始值，随后再用梯度下降进行微调。可以用来参考如何将人类运动数据用于机器人的形态协同设计。
本文目前只优化拇指和食指的指尖位置，没有考虑全手接触和受力情况，且 3D 打印的结构在承受高负载时容易损坏。

## RLinf: Flexible and Efficient Large-scale Reinforcement Learning via Macro-to-Micro Flow Transformation
[Gemini 3.1 Pro] 提出 M2Flow 范式解耦逻辑工作流与物理调度，构建高灵活度的大规模强化学习并行训练系统 | 清华大学, Chao Yu, Yu Wang | https://hjfy.top/arxiv/2509.15965 | https://www.alphaxiv.org/abs/2509.15965 | https://github.com/RLinf/RLinf
|-|-|-|-|-|

RLinf 允许开发者直接用代码定义大模型强化学习组件交互，随后系统会自动分析性能并搜索出最优的时空流水线配置。它在底层原生支持自动上下文切换和自适应通信机制，复现时可以直接运
行官方开源框架来训练模型。

系统采用的动态规划调度强依赖基于多项式外推的预先性能剖析，这种预估方式在极端动态长尾负载下可能产生时间计算误差，进而降低自动分配流水线的实际并行效率。
