---
title: "Let's establish a common language"
date: 2026-10-10 23:36:28
tags: ["26", "09"]
author: "4070s wsl julyfun"
os: "Linux DESKTOP-VDB57PP 5.15.153.1-microsoft-standard-WSL2+ #2 SMP Sun Oct 27 22:02:06 CST 2024 x86_64 x86_64 x86_64 GNU/Linux"
assume-you-know: [computer]
confidence: 2
---

```mermaid
flowchart TD
  pytorch --> Linear --> MLP --> CNN --> RNN
  MLP --> softmax --> regression --> auto-regression
  Linear --> forward-backward-optimizer --> MLP & SGD
  SGD --> AdamW
  MLP --> RL[RL, see 285-0]
  transformer --> gradient-clipping
  nn.Parameter --> embedding --> image-patch
  CNN --> image-patch --> patch-embedding --> vision-transformer
  pytorch --> nn.Parameter --> Linear
  CNN --> attention --> transformer --> vision-transformer --> DINO
  embedding --> token-tokenizer --> transformer --> decoder-only-transformer
  encoder-decoder --> transformer
  transformer --> auto-regression
  CNN --> AE --> VAE --> encoder-decoder --> flow-matching --> diffusion
  flow-matching --> latent
  diffusion & latent --> Stable-Diffusion
```

try:

```mermaid
flowchart TD
    %% level 0
    pytorch
    %% level 1
    pytorch --> Linear & MLP & regression & nn.Parameter & weights & forward-backward-optimizer
    %% level 2
    MLP --> CNN & RNN
    %% level 3
    nn.Parameter --> embedding & image-patch & patch-embedding
    CNN --> image-patch
    %% level 4
    CNN --> attention
    transformer
    %% level 5
    attention --> transformer --> vision-transformer
```
