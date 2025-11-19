---
title: "Flow vs Diffusion"
date: 2025-11-19 10:46:56
tags: ["notes", "julyfun", "25", "10"]
author: "Julyfun MacOS14.5 M1"
os: "Darwin floriandeMacBook-Air.local 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1 20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64"
assume-you-know: [computer]
confidence: 2
---

```python
# x0: [B, C, H, W]  real image in [-1,1] or [0,1]
t = sample_uniform_t(batch_size)
alpha_t = get_alpha(t)                      # precomputed schedule
eps = torch.randn_like(x0)                  # Gaussian noise

# forward noising
xt = (alpha_t.sqrt() * x0 +
      (1 - alpha_t).sqrt() * eps)

pred_eps = model(xt, t)                     # predict noise

loss = ((pred_eps - eps)**2).mean()
```

```python
# x0: [B, C, H, W]
t = sample_uniform_t(batch_size)
x1 = torch.randn_like(x0)                   # Gaussian prior

# forward interpolation
xt = (1 - t) * x0 + t * x1

# true velocity
v_true = x1 - x0

pred_v = model(xt, t)                       # predict velocity

loss = ((pred_v - v_true)**2).mean()
```
