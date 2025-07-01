---
title: unit3-01_stable_diffusion_introduction
date: 2025-06-20 18:38:58
tags: ["notes", "julyfun", "技术学习", "diffusion-models-class"]
---
## Pipeline 的职责是?

pipe:
- unet
- vae
- text_encoder
- image_encoder
- feature_extractor
- tokenizer (is a nn.Module without params)
- scheduler
- safety_checker ?
