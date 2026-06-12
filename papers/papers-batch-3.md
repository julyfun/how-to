---
title: "papers batch 3"
date: 2026-06-11 20:32:05
tags: ["papers"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

## DreamZero (21)
- https://hjfy.top/arxiv/2602.15922 | https://dreamzero0.github.io | agibot + NVIDIA | Seonghyeon Ye + Joel Jang

与 cosmos policy 稍有不同, video backbone (Wan2.1，冻结) 用作编码器而单一 DiT（可学习）从 noise 中解码出 flow v. DiT 利用 kv cache 实现了历史观测.

demo 亮点是 agibot-G1 穿鞋带以及 unseen 地前进按电梯按钮. 附录中有 train-infer 的 attn mask 设计和 infer 加速等不错的资料.

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20260611232213721.png)

## EgoScale (22)
- ⭐️⭐️⭐️ https://hjfy.top/arxiv/2602.16710 : https://www.alphaxiv.org/abs/2602.16710 | https://research.nvidia.com/labs/gear/egoscale/ | NVIDIA | Ruijie Zhang + Linxin Fan

20000 小时数据灵巧手操作预训练，mid-training 和 post-training 实践。模型架构
- 预训练：解冻所有模块，包括 VLM(GROOT N1)，vision encoder，DiT 动作专家等，纯 RGB 数据用现成工具解算手部姿态和手腕轨迹，其中有 829 小时 vision pro 准确手腕+手部数据.
- mid-training: 对同样的任务同时采集 30 条人类轨迹和 5 条机器人轨迹（50h人类 + 4h机器人，都使用 vive tracker + manus 手套）
- post-training: 特定任务的机器人数据. 如果进行了 mid-trainig 则冻结视觉编码器，否则不冻结.

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20260612225719448.png)

这个 demo 比较精彩，用 sharpa hand 实现了使用电动螺丝刀、试管吸液和双指拧瓶盖.

## LIFT: yi wang (23)

将预训练的 pi0.5 的 action expert 复制一份参数作为 learnable force expert，提供 1 秒的 force kv history. 通过 teleop online dagger 训练 force expert. LIFT 并非为了 contact-rich 场景设计，而是证明后训练阶段才引入 force 仍然是有价值的。不过 multi-task 能力还未开发（pi0.5 本身在这些任务上也不怎么 multitask）.

## Moto: Latent Motion Token as the Bridging Language for Learning Robot Manipulation from Videos

## Motus: A Unified Latent Action World Model
- tri-mot (VLM 用于理解指令 + video gen model + action expert)

## WorldVLA

## SimpleVLA

## Forcy policy

## VLA-JEPA
- https://hjfy.top/arxiv/2602.10098

## dit4dit yy硕推荐

## Latent Policy Steering 光流

## LAPA: 早期提出 FDM 和 IDM 模型

## End-to-end training of deep visuomotor policies 四大神仙

## UniVLA: 提出了一种两阶段的训练来更好地提取 Latent Action

关于 latent-action pretraining drifting 的问题值得看看.

https://yipko.com/posts/work/pi0.7/

- offline: Conservative q-learning for offline reinforcement learning. 惩罚 OOD 动作
