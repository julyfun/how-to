---
title: Layer Norm
date: 2025-11-09 21:15:01
tags:
  - notes
  - julyfun
  - 技术学习
  - models
author: julyfun-4070s-ubuntu2204
os: "Linux julyfun-4070s-ubuntu 6.8.0-87-generic #88~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Tue Oct 14 14:03:14 UTC 2 x86_64 x86_64 x86_64 GNU/Linux"
assume-you-know:
  - computer
confidence: 2
---

LN: 只要是特征就视为一个分布内，做归一化。
- 图像 (b, c, h, w): 一个 sample 的 (c, h, w) 归一化
- emb: (b, length, dimension)：一个 emb 内做归一化 (d, )

BN:
- 图像 (b, c, h, w): 一个 channel 内归一化 (b, h, w)
- emb: 刚好和 LN 相反，认为 emb 一个维度是一个分布，(b, l, d) 的 (b, l) 内归一化 内归一化

