---
title: "papers batch 5"
date: 2026-06-30 20:49:49
tags: ["papers"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

## Behavior Prompting Policy: Demonstrations as Prompts for Manipulation
⭐️⭐️⭐️ 将一次性演示作为 in-context 任务提示 [Stanford, Austin Patel, Shuran Song]

| 🦾 https://behavior-prompting.github.io | 📃 https://hjfy.top/arxiv/2606.30457 | ✨ https://www.alphaxiv.org/abs/2606.30457 | 💻 https://github.com/real-stanford/behavior_prompting |
|-|-|-|-|

recap: diffusion policy 使用 obs_encoder(obs) 获得 global_cond 并直接 FiLM 调制 UNet 中的多层 x.

本文仅需在上述 obs_encoder 内部 cross-attn 一条演示下采样得到的 `[enc(rgb), mlp(propio), mlp(action)]`，实现了 1. infer-time 指定折叠方式（训练时见过多种折叠方式）; 2. infer-time 指定绘制数字（训练时未见过的数字）。实验发现需要训练数据多样性高时才能很好地 steering，当然，还是无法跨 action primitive 的.

这篇文章 abs 比我们写的好多了:
1. We study Bahavior Propmting.
2. To enable this, we present contributions in algo, data and evaluation.
3. For algo, we.. For data we identify that .. is the primer driver **and introduce iPhUMI**.
