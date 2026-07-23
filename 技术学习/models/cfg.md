---
title: "cfg"
date: 2025-01-01 17:45:53
tags: ["技术学习", "models"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

Classifer Guidance:

```python
# 1. 网络正常去噪，预测当前步的纯净轨迹或噪声
pred_tau = unet(noisy_tau, history_obs, step_k)
# 2. 将预测轨迹送入可导的代价函数计算 Cost (必须 Autograd)
cost = task_cost_function(pred_tau)
# 3. 对输入的高维轨迹求梯度 (告诉它往哪里微调能降低 Cost)
grad = autograd.grad(outputs=cost, inputs=noisy_tau)
# 4. 在标准去噪更新的基础上，叠加上梯度引导项. 比如 scale 是 0.01 ~ 0.05
next_noisy_tau = ddpm_step(pred_tau, noisy_tau) - scale * grad
```

CFG:

```python
# 1. 带条件前向：比如输入 prompt="walk forward"
pred_cond = unet(noisy_tau, condition="walk forward", step_k)
# 2. 无条件前向：将条件置空 prompt="" (Drop-out)
pred_uncond = unet(noisy_tau, condition="", step_k)
# 3. 计算 CFG 放大后的预测值 (不使用任何 Autograd 梯度)
# scale > 1 (比如 7.5)，将预测推向更符合条件的方向
pred_final = pred_uncond + scale * (pred_cond - pred_uncond)
# 4. 用最终预测值进行标准的去噪更新
next_noisy_tau = ddpm_step(pred_final, noisy_tau)
```

