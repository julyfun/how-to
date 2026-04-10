---
title: "Lab4"
date: 2025-01-01 10:34:48
tags: ["研一下", "深度学习"]
author: "Julyfun MacOS14.5 M1"
os: "Darwin floriandeMacBook-Air.local 25.2.0 Darwin Kernel Version 25.2.0: Tue Nov 18 21:09:55 PST 2025; root:xnu-12377.61.12~1/RELEASE_ARM64_T8103 arm64"
assume-you-know: [computer]
confidence: 2
---

六步走
- data to
- opt zero
- forward
- loss
- backward
- opt step

```python
for batch_idx, (data, _) in enumerate(train_loader):
    data = data.to(device)
    optimizer_vae.zero_grad()
    recon_batch, mu, logvar = vae(data)
    loss = vae_loss(recon_batch, data, mu, logvar)
    loss.backward()
    optimizer_vae.step()
```

### 💡 Discussion: VAE
**Question 1: Why do the generated digits from the VAE look somewhat blurry compared to real MNIST images?**
> 特征在数字特征之间了

**Question 2: What would happen if we remove the KL-divergence term from the loss?**
> 让我试试. 生成了非常糟糕的结果
![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/202604101048993.webp)

### 💡 Discussion: GAN
**Question 1: Why do GANs generate sharper images than VAEs?**
> 

**Question 2: What is "Mode Collapse"? (You might even observe it in your output grid)**
>  

依托

