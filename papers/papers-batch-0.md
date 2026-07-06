---
title: "papers batch 0"
date: 2026-06-28 21:55:00
tags: ["papers"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

合并图片：https://small.im/zh-hans/merge-images

## Video Language Planning
[Gemini 3.1 Pro] 提出结合 VLM 和文本到视频模型进行树搜索的 VLP 算法来实现长视距机器人视觉动作规划 | MIT，Yilun Du，Yilun Du
https://video-language-planning.github.io/ | https://hjfy.top/arxiv/2310.10625 | https://www.alphaxiv.org/abs/2310.10625 |
https://github.com/video-language-planning/vlp_code
|-|-|-|-|-|

VLP 通过前向树搜索结合两种模型，先由 VLM 生成候选动作的文本指令并利用视频模型预测对应的执行短视频，最后再由 VLM
充当启发式函数来评估以找出最优的长视距视觉执行计划。

纯视觉生成和启发式评估缺乏显式的物理约束，生成的计划偶尔会出现物体瞬移或消失等物理不一致错误。

## π₀.₇ MEM-Style memory

## FiLM

把 cond 投影成 x per-channel 的 scale 和 bias.

```python
x: (B, C, D) cond: (B, cond_dim)
#      ╰ channels
cond = linear(cond) # (B, 2, C)
scale, bias = cond[:, 0, ...].reshape('b c -> b c 1'), cond[:, 1, ...].reshape('b c -> b c 1')
x = scale * x + bias
```
