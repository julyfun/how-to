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

这个 demo 比较精彩，用 sharpa hand 实现了使用电动螺丝刀、试管吸液和双指拧瓶盖.

## Moto: Latent Motion Token as the Bridging Language for Learning Robot Manipulation from Videos

## Motus: A Unified Latent Action World Model
- tri-mot (VLM 用于理解指令 + video gen model + action expert)

## WorldVLA

## SimpleVLA

## Forcy policy

## LIFT
- yi wang

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
