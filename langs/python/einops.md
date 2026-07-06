---
title: "einops"
date: 2026-07-06 23:34:47
tags: ["langs", "python"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

```python
We don't write:
    y = x.transpose(0, 2, 3, 1)
We write comprehensible code:
    y = rearrange(x, 'b c h w -> b h w c')
Also:
    rearrange(ims, "b h w c -> h (b w) c").shape
    rearrange(ims, "(b1 b2) h w c -> b1 b2 h w c ", b1=2).shape
    reduce(ims, "b h w c -> h w c", "mean") # Average overbatch
   reduce(ims, "b h w c -> h w", "min")
```

