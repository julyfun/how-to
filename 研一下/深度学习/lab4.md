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
> 因为对抗损失过度逼近高频细节
> 而 VAE 用了 KL，如果高频细节过多，KL 损失就大

**Question 2: What is "Mode Collapse"? (You might even observe it in your output grid)**
> 只学会了其中集中样式。因为判别器也不判多样性。

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/202604101101441.webp)

### 💡 Discussion: Diffusion Models
**Question 1: What exactly does `num_inference_steps` do?**
> 调节生成单步走多少

**Question 2: What is `guidance_scale` (Classifier-Free Guidance / CFG)?**
> 就是对 prompt 的权重（放大条件信号）
> Classifier-Free 的原理：每步做两个预测，uncond 和 prompt-conditioned，然后 diffusion 走的方向取个加权.
> Use-classifer 方法：用分类器梯度引导

$epsilon.alt_"guided" = epsilon.alt_theta (x_t , t) - s dot.op sigma_t nabla_(x_t) log p_phi.alt (y | x_t , t)$

其中 s 是 guidance strength（类似 scale）。

