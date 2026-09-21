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
