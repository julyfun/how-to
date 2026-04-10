---
title: "Lab4"
date: 2025-01-01 10:34:48
tags: ["研一下", "深度学习"]
author: "Julyfun MacOS14.5 M1"
os: "Darwin floriandeMacBook-Air.local 25.2.0 Darwin Kernel Version 25.2.0: Tue Nov 18 21:09:55 PST 2025; root:xnu-12377.61.12~1/RELEASE_ARM64_T8103 arm64"
assume-you-know: [computer]
confidence: 2
---

- data to
- opt zero
- get output
- loss

```python
for batch_idx, (data, _) in enumerate(train_loader):
    data = data.to(device)
    optimizer_vae.zero_grad()
    recon_batch, mu, logvar = vae(data)
    loss = vae_loss(recon_batch, data, mu, logvar)
    loss.backward()
    optimizer_vae.step()
```
