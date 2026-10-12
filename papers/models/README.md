---
title: "models README"
date: 2025-01-01 15:57:27
tags: ["papers", "models"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

## AdaLN

fm/diffusion 常用

```python
flow step t -> t_emb -> [MLP] -> [Linear] inside Ada -> split as γ,β
x = (1.0 + γ) * layer_norm(x) + β
```

## CD

一致性蒸馏的目的是让 student 具有 从任意噪声时刻直接一步映射到干净样本 的能力，而 teacher 通常需要多步迭代去噪才能得到干净样本。

方法则是 “通过相邻时刻的一致性约束”.

```python
s, t = sample_adjacent_times()                  # t < s. time=0 is noise => time=1 is clean.
x_t = add_noise(x0, noise(), t)
x_s = x_t + (s - t) * teacher(x_t, t)           # 教师做一步 Euler 求解
target = stop_grad(ema(x_s, s))
loss = distance(student(x_t, t), target)
optimize(student, loss); update_ema(ema, student)
```
