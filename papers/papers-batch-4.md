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

自监督在相邻帧训练 IDM -> latent_token -> FDM 模型，作为 VLM 的 pretraining label.

3 步训练:
1. 自监督利用互联网视频训练一个 encoder: (x1, x2) -> z（VQ 离散化）和 decoder: (x1, z) -> x2，这类似于 IDM 和 FDM. 这里 x1 和 x2 相差 T 帧.
2. 监督 Latent Pretraining: 利用上面模型打 label，然后给 VLM 接入一个新的 latent head，输入 x, l 输出 z
3. Action FT: 给 VLM 接入 action head，输入 x, l 输出 action

当然，对于 ego 视频来说画面的变化无法实际上完全用 z 表示，因素还有视角变化和物体运动等，因此这一套自监督不算很完备.

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20260622183820532.png)
