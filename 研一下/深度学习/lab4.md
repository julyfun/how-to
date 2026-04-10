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

 - (\epsilon_{\text{guided}})：引导后的噪声预测，用它来做反向采样更新。
- (\epsilon_\theta(x_t,t))：扩散模型（参数为 (\theta)）在时间步 (t) 对当前噪声图 (x_t) 的原始噪声预测。
- (x_t)：第 (t) 步的带噪图像（latent/像素都可，看模型定义）。
- (t)：扩散时间步。
- (s)：guidance strength / scale，引导强度超参数。
- (\sigma_t)：与时间步 (t) 对应的噪声尺度（由噪声调度器决定）。
- (\nabla_{x_t})：对 (x_t) 求梯度。
- (\log p_\phi(y|x_t,t))：分类器（参数 (\phi)）在给定 (x_t,t) 时，对目标类别 (y) 的对数概率。
- (p_\phi(y|x_t,t))：分类器输出的类别后验概率。
- (y)：你希望生成结果符合的目标类别标签。
- (\phi)：外部分类器参数。
- (\theta)：扩散模型参数。

```python
# x_t: [B, C, H, W]
# t:   [B] or scalar timestep
# y:   [B] target class ids
# s: guidance scale (float)
# sigma_t: noise scale at timestep t (float or tensor broadcastable to x_t)

x_t = x_t.detach().requires_grad_(True)

# 扩散模型给原始噪声预测
with torch.no_grad():
    eps = unet(x_t, t)  # epsilon_theta(x_t, t)

# 3) 外部分类器给类别分数（需要梯度）
logits = classifier(x_t, t)              # [B, num_classes]
log_probs = F.log_softmax(logits, dim=-1)
# 每个样本目标类log p
selected = log_probs[torch.arange(x_t.size(0), device=x_t.device), y]  
obj = selected.sum()  # 标量，便于 autograd

# 4) 求 grad = ∇_{x_t} log p(y|x_t,t)
grad = torch.autograd.grad(obj, x_t, only_inputs=True)[0]
eps_guided = eps - s * sigma_t * grad
with torch.no_grad():
    x_prev = ddpm_step(x_t.detach(), eps_guided.detach(), t)

x_t = x_prev
```

