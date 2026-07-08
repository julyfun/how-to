---
title: "papers batch 7"
date: 2026-07-08 14:29:34
tags: ["papers"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

to read.

## UniVLA: Learning to Act Anywhere with Task-centric Latent Actions
[Gemini 3.1 Pro] 通过潜在动作模型从视频中提取以任务为中心的潜在动作并在 DINO 特征空间中结合语言指令进行泛化策略训练 | 👤 The University of Hong Kong, Qingwen Bu, Hongyang Li | - | [📃 2505.06111](https://hjfy.top/arxiv/2505.06111) | [✨](https://www.alphaxiv.org/abs/2505.06111) | [📂](https://github.com/OpenDriveLab/UniVLA) |

提出了用于跨具身学习的框架 UniVLA。该方法不直接依赖带动作标注的数据，而是通过潜在动作模型从各种视频（包括人类视频）中提取以任务为中心的潜在动作表示。为了过滤任务无关的动态，它在 DINO 特征空间内结合语言指令建立潜在动作模型，预训练后的通用策略只需通过轻量的潜在动作解码器即可高效部署到各种异构机器人上。

## Video Language Planning
[Gemini 3.1 Pro] 提出结合 VLM 和文本到视频模型进行树搜索的 VLP 算法来实现长视距机器人视觉动作规划 | MIT，Yilun Du，Yilun Du
https://video-language-planning.github.io/ | https://hjfy.top/arxiv/2310.10625 | https://www.alphaxiv.org/abs/2310.10625 |
https://github.com/video-language-planning/vlp_code
|-|-|-|-|-|

VLP 通过前向树搜索结合两种模型，先由 VLM 生成候选动作的文本指令并利用视频模型预测对应的执行短视频，最后再由 VLM
充当启发式函数来评估以找出最优的长视距视觉执行计划。

纯视觉生成和启发式评估缺乏显式的物理约束，生成的计划偶尔会出现物体瞬移或消失等物理不一致错误。
