---
title: "How to improve Lingbot-VLA-2.0 C2R - 预研"
date: 2026-09-28 21:25:41
tags: ["26", "09"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 27.0.0 Darwin Kernel Version 27.0.0: Tue Aug 11 21:02:59 PDT 2026; root:xnu-13432.1.9~1/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

## InternW0
1. 用了 3494h InternA1.
2. 架构上类似 AHA-WAM 修正过时视频 KV，并且用 DINOv3 编码当前帧
3. 小 ablation 发现预训练用 Ego cotraining 有效.

