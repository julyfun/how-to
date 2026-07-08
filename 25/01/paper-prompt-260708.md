---
title: "paper prompt 260708"
date: 2026-07-08 14:30:59
tags: ["25", "01", "deprecated"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

本文 deprecated，因为 AI 不太能遵循.

---

使用 arxiv api 阅读论文. 若有难以理解的内容请阅读开源代码.

请你简洁地给出代码复现视角的有序步骤.例 1（增量工作）：
1. 拿出 pi0 代码.
2. 对 pi0 action expert 的中间层加 depth auxiliary task.

例 2（增量工作）:
1. 拿出 diffusion policy 代码
2. 实现手机端与 policy 主机通信，并 AR 渲染轨迹
3. 根据轨迹执行动作，发现动作错误直接采集纠正轨迹
4. 纠正轨迹直接传输到主机立即微调 policy.

常见基础模型:
- WAM, video DiT + action DiT
- VLA: pi0 或 pi0.5 之一. VLM + action flow-matching(action expert)
- Diffusion Policy 或 ACT

保持极简. 文章通常都有大量凑字数内容，或者给简单的核心方法添加过多包装，谨慎识别并提取易懂的 core idea. 增量工作指出4个以内增量，非增量工作仅保留8个以内重要模块.

除了官方模型名或论文名里的斜杠，尽量不用斜杠，写清楚语义：

- 表示并列用 `和` 或 `、`。
- 表示选择用 `或`。
- 表示解释用 `i.e.`、`也即`。
- 表示包含关系用 `包括`。
- 别名用括号.
