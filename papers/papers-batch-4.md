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
⭐️⭐️ 同济 Ji Zhang, Jingkuan Song | https://koorye.github.io/Inspire/

在 Pi0 基础上直接对 VLM 输入“物体在哪里” 作为 aux task 并且也会把输出结果直接再次输入 VLM.

## MEM (28)

⭐️⭐️⭐️ PI 团队

直接复制一个 pi0.5 的 VLM 作为 system 2 来做 text-level 长时序总结，而 system 1 改用 video 输入达到短时序能力.

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20260622151337338.png)

## LAPA (29)
⭐️⭐️⭐️ https://hjfy.top/arxiv/2410.11758

原始的 IDM 和 FDM 模型。

散步训练
1. 无监督利用互联网视频训练一个 encoder: (x1, x2) -> z（VQ 离散化）和 decoder: (x1, z) -> x2

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20260622183820532.png)