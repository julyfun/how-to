---
title: "VAE 和 VQ-VAE"
date: 2025-01-01 20:34:14
tags: ["25", "01"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

```python
# VAE 伪代码
1  x = input_image
2  mu, logvar = Encoder(x)
3  z = mu + exp(0.5 * logvar) * eps # eps ~ N(0, I)
4  x_hat = Decoder(z)

5  loss_recon = reconstruction_loss(x_hat, x)
6  loss_kl = KL(q(z|x) || N(0, I))

# 然后 VQ-VAE：
1  x = input_image
2  z_e = Encoder(x)
3  z_q = argmin_{z in codebook} distance(z_e, z) # 在 codebook 里找离 z_e 最近的向量
4  x_hat = Decoder(z_q)

5  loss_recon = reconstruction_loss(x_hat, x)
6  loss_codebook = || stop_grad(z_e) - z_q ||^2
7  loss_commit = || z_e - stop_grad(z_q) ||^2
8  loss = loss_recon + loss_codebook + beta * loss_commit
```
