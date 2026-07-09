---
title: "einops and einx"
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

and einx:

```python
z = einx.id("a (b c) -> (b a) c", x, b=2)             # Permute and (un)flatten axes
z = einx.id("b (q + k) -> b q, b k", x, q=2)          # Split
z = einx.id("b c, -> b (c + 1)", x, 42)               # Append number to each channel
z = einx.sum("a [b]", x)                              # Sum-reduction along second axis
z = einx.flip("... (g [c])", x, c=2)                  # Flip pairs of values along the last axis
z = einx.mean("b [...] c", x)                         # Spatial mean-pooling
z = einx.multiply("a..., b... -> (a b)...", x, y)     # Kronecker product
z = einx.sum("b (s [ds])... c", x, ds=(2, 2))         # Sum-pooling with 2x2 kernel
z = einx.add("a, b -> a b", x, y)                     # Outer sum
z = einx.dot("a [b], [b] c -> a c", x, y)             # Matrix multiplication
z = einx.get_at("b [h w] c, b i [2] -> b i c", x, y)  # Gather values at coordinates
```
