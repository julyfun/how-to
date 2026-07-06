---
title: "My Notations"
date: 2026-07-06 11:06:44
tags: ["26", "07"]
author: "Julyfun MacOS14.5 M1"
os: "Darwin floriandeMacBook-Air.local 25.2.0 Darwin Kernel Version 25.2.0: Tue Nov 18 21:09:55 PST 2025; root:xnu-12377.61.12~1/RELEASE_ARM64_T8103 arm64"
assume-you-know: [computer]
confidence: 2
---

## 绘制 mermaid flowchart
- 可训练模型用 `node[[]]`，数据用 `node([])`，非可学习模块 `node[]`. train-time 如有冻结模块用🧊标识. 如果是 +/concat 等操作符直接写 +/concat 等.
- 文字简洁，用 `<br>` 换行，数据带上形状以及项目最默认配置的具体数值, e.g. (B=8, seq_len=50, D=1024)
- 非 fully attention 可标出谁提供 q/k/v，对于 q 可标出其 attend 目标，简述. fully attention 省略之.
- 画出重要模块，如 Embedding, RoPE, expert, FM, proj, MLP, loss，省略 layer norm 等不重要模块.

## flowchart-like chain
例子: raw action -> [Linear] -> action tokens -> [some module] -> some data

其中，数据不用包裹，可学习模块用 [] 包裹起来.
