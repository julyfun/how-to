---
title: "Basic Robot Papers for Beginners"
date: 2026-09-22 18:59:40
tags: ["26", "09"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

- [x] 基础
    - [x] CLIP | 21.1 通过直接匹配图-文编码来训练
    - [x] DINO | 21.4 以 EMA & 全局视图的教师与局部视图学生进行自蒸馏
    - [x] BLIP | 22.1  在 CLIP 基础上添加 decoder 看图生文本
    - [x] SigLIP | 23.3 将 CLIP 的 softmax 损失改为 sigmoid 二分类损失提升训练效率
    - [x] LLaVA | 23.4 将 CLIP 投影到 LLM 空间并进行问答训练
    - [x] QwenVL | 23.8 将 CLIP 通过 256 learnable-queries cross-attn 变换到 LLM 空间
- [x] VLA
    - [x] OpenVLA | 24.6 用 VLM 的 next-token-prediction 输出离散动作
    - [x] pi0 | 24.10 推出 MoT & FM & zero-padding 大规模预训练范式
    - [x] pi05 | 25.4 预训练扩充 CE/互联网，离散动作预训练，subtask 作为辅助损失和 CoT
    - [x] SmolVLA | 25.6 裁剪 MoT 并交错使用 CA 和 SA 以让模型更轻量化
    - [x] pi06 | 25.11 稀疏 RL 训练进度估计器给数据打 0/1 advantage 作为 VLA condition
- [ ] WM
    - [x] EnerVerse | 25.11 稀疏自回归扩散训练 Unet-VM，中间层 latent 作为 AE cross-attn kv
    - [x] DreamDojo | 26.2 LAPA 式提取 WM 预训练 Ego 所需的 latent action condition 并将 WM 用于其他policy择优
    - [x] Ctrl-World (for IL) | 26.3 WM simulator rollout + 人工选择后训练数据
    - [ ] PlaNet ?
    - [x] Sora
    - [x] V-JEPA
    - [x] Wan
- [ ] WM for RL
    - [ ] Dreamer to Control
    - [ ] Dreamer V3
    - [ ] World-Env
- [ ] Cascaded WAM
    - [ ] 显式
        - [ ] AVDC ?
        - [ ] UniPi https://www.alphaxiv.org/abs/2302.00111
        - [ ] VLP https://www.alphaxiv.org/abs/2401.05577
    - [ ] 隐式
        - [x] VPP | 24.12 微调 SVD 并 query UNet 的中间特征交给 AE
        - [x] LAPA | 25.5 训练 latent action encoder 获取 pretraining condition
        - [ ] MWM https://www.alphaxiv.org/abs/2603.07799
- [ ] Joint WAM
    - [ ] 扩散
        - [x] Motus | 25.12 VM/VLM/AE 三专家 MoT
        - [x] Lingbot-va | 26.1 自回归交错去噪 video chunk/action chunk
        - [x] Cosmos | 26.1 单一 Cosmos 直接去噪 proprio/action/img/value token，不用投影直接广播
        - [x] DreamZero | 26.2 单一 WAN 去噪 img/action token，带 action decoder
        - [x] DiT4DiT | 26.3 非 MoT & 带 diffusion shift & action_to_video_only 的实践
        - [x] FastWAM | 26.3 video gen 仅作为辅助任务
        - [ ] MotuBrain
    - [x] Query-based (ACT-like)
        - [x] VLA-JEPA | 26.2 query latent action 并在 JEPA 空间监督从而 leverage human video
- [ ] 数据工作
    - [ ] EgoRecovery 26.7 | 提取动作意图
- [ ] VLA Framework
    - [ ] FLuxVLA
    - [x] RLinf
    - [x] StarVLA

TODO
- [ ] MMLab 的 EGOWILD2DEX https://mmlab.hk/egowild2dex/
- 9/23 推荐的五六篇文章 https://shuiyuan.sjtu.edu.cn/t/topic/506513/350
