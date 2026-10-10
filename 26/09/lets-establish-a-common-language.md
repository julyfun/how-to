---
title: "Let's establish a common language"
date: 2026-10-10 23:36:28
tags: ["26", "09"]
author: "4070s wsl julyfun"
os: "Linux DESKTOP-VDB57PP 5.15.153.1-microsoft-standard-WSL2+ #2 SMP Sun Oct 27 22:02:06 CST 2024 x86_64 x86_64 x86_64 GNU/Linux"
assume-you-know: [computer]
confidence: 2
---

### Deep learning

```mermaid
flowchart TD
  pytorch --> Linear --> MLP --> CNN --> RNN
  MLP --> softmax --> regression --> auto-regression
  Linear --> forward-backward-optimizer --> MLP & SGD
  SGD --> AdamW
  MLP --> RL[RL, see 285-0]
  transformer --> gradient-clipping
  nn.Parameter --> embedding --> image-patch
  CNN --> ResNet --> image-patch --> patch-embedding --> vision-transformer
  pytorch --> nn.Parameter --> Linear
  CNN & embedding --> positional-embedding --> attention --> transformer --> vision-transformer --> DINO & MoT
  embedding --> token-tokenizer --> transformer --> decoder-only-transformer
  encoder-decoder --> transformer
  transformer --> auto-regression
  diffusion & transformer --> DiT
  CNN --> AE --> VAE --> encoder-decoder --> UNet --> flow-matching --> diffusion
  flow-matching --> latent
  diffusion & latent --> Stable-Diffusion
```

### Robot Policy Beginnner

```mermaid
flowchart TD
    flow-matching & diffusion & DINO & CLIP --> Diffusion-Policy --> TinyVLA --> Pi0 --> Pi05 --> Pi06 --> MEM
    Pi0 --> action-expert
    ACT-action-chunking & MoT & VLM --> Pi0
    Pi05 --> OpenWAM
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
