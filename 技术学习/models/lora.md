---
title: "LoRA"
date: 2025-01-01 16:43:13
tags: ["技术学习", "models"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

假设原始线性层权重是：

W: [1000, 2000]   # out_features=1000, in_features=2000

LoRA rank r=16 时，会训练两个小矩阵：

A: [16, 2000]
B: [1000, 16]

前向时原来是：

y = W x

加 LoRA 后变成：

y = W x + scale * B(Ax)

其中：

scale = lora_alpha / r = 32 / 16 = 2

