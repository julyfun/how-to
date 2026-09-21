---
title: "models README"
date: 2026-09-21 15:57:27
tags: ["papers", "models"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

## AdaLN

fm/diffusion

```python
class AdaLN:
    def __init__(self, hidden_dim, cond_dim):
        self.norm = LayerNorm( hidden_dim, elementwise_affine=False )
        self.to_scale_shift = Linear( cond_dim, 2 * hidden_dim )

    def forward(self, x, cond):
        # x:    [batch, tokens, hidden_dim], cond: [batch, cond_dim]
        scale, shift = split( self.to_scale_shift(cond), num_splits=2 )

        # 扩展到每个 token
        scale = scale[:, None, :]
        shift = shift[:, None, :]

        x_norm = self.norm(x)
        return (1.0 + scale) * x_norm + shift
```
t⟶TimeEmbedding(t)⟶MLP⟶AdaLN modulation⟶(γ,β)