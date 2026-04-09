---
title: "Robot Transformer Basics"
date: 2025-01-01 14:58:22
tags: ["25", "01"]
author: "Julyfun MacOS14.5 M1"
os: "Darwin floriandeMacBook-Air.local 25.2.0 Darwin Kernel Version 25.2.0: Tue Nov 18 21:09:55 PST 2025; root:xnu-12377.61.12~1/RELEASE_ARM64_T8103 arm64"
assume-you-know: [computer]
confidence: 2
---

## FiLM

使用 txt token => MLP 的输出缩放 img token

```python
img = image_encoder(image)                  # [B, N, D]  visual tokens
txt = text_encoder(text)                    # [B, L, D]  text tokens

gamma_beta = film_mlp(txt.mean(1))          # [B, 2D] 这里 mean 把一句话平均为一个 token
gamma, beta = gamma_beta.chunk(2, dim=-1)   # [B, D], [B, D]
img = gamma.unsqueeze(1) * img + beta.unsqueeze(1)   # FiLM on image tokens

x = torch.cat([img, txt], dim=1)            # [B, N+L, D]
x = transformer(x)                          # cross-modal interaction
out = head(x[:, 0] or x.mean(1))            # cls / pooling
```

## 更现代的（把现成 LLM Transformer 当作 fusion 主干）

