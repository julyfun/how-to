---
title: unit3-01_stable_diffusion_introduction
date: 2025-06-20 18:38:58
tags: ["notes", "julyfun", "技术学习", "diffusion-models-class"]
---

## Stable Diffusion Pipeline 的职责是?

说白了 unet 预测的就是 vae 的 latent.

pipe:
- unet
- vae
- text_encoder
- image_encoder
- feature_extractor
- tokenizer (is a nn.Module without params)
- scheduler
- safety_checker ?

```mermaid
graph
    text --> t(tokenizer & text_encoder) --> e[text_embedding]
    e --> unet(unet)
    n["noisy_latents (4, 64, 64)"] --> unet
    timestep --> unet
    unet --> p["noise prediction (4, 64, 64)"]
    p --> v_d(vae decoder)
```
