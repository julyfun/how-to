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

⭐️⭐️ NTU | https://arxiv.org/html/2610.12369v1

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20261015200126855.png)

通过文本记录 环境状态, 机器人状态 和 任务状态. dojo 刷到 70.

## When Do Discrete Actions Make Good Continuous Controllers? (84)

⭐️⭐️⭐️⭐️ Zeji Yi, Guanya Shi, CMU | https://www.alphaxiv.org/abs/2610.20429

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20261016180730842.png)


本文发现 paligemma 直接接动作头，flow 离散 > flow 连续 > regression 离散 > regression 连续 ... (robocasa SR)

为了让离散动作协调，用 flow 调节 logits + 逐渐随机确定采样. CFG 能降低 token ambiguity 和动作分散度，但是 GT coverage 也会减小.

另外，tokenize 过程中注入几何先验还不如 uniform bin.
