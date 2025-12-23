---
title: "VQ-VAE"
date: 2025-11-09 21:15:01
tags: ["notes", "julyfun", "技术学习", "models"]
author: "julyfun-4070s-ubuntu2204"
os: "Linux julyfun-4070s-ubuntu 6.8.0-87-generic #88~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Tue Oct 14 14:03:14 UTC 2 x86_64 x86_64 x86_64 GNU/Linux"
assume-you-know: [computer]
confidence: 2
---
see: https://kexue.fm/archives/6760

note:
- codebook 的目的是离散建模，以适用于 PixelCNN 这样的**分类**网络.
- 每个像素会映射到 codebook 中的一个，保留着位置结构。

```
训练:
x -> [Encoder (CNN)] -> z (m * m * d)
同时 PixelCNN 输入 z 的前 n 个，预测第 n + 1 个（建模 z 分布）
同时 z -> [Decoder CNN] -> x

生成:
PixelCNN 自回归生成 m * m * d 的矩阵 -> Decoder -> x
```
