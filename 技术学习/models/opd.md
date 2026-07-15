---
title: "OPD"
date: 2025-01-01 21:04:59
tags: ["技术学习", "models"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

思路：让 teacher 在 student 真实 rollout 的轨迹上去纠正分布.

普通蒸馏：
```python
for traj, y_teacher in offline_dataset: # x: (b, L)int. y_teacher (b, L)int.
    loss = KL(student(traj), teacher(traj)) # 一次性输出 len 个 dist. 需要一些 mask.
```

OPD (on-policy distillation):
```python
for prompt in prompts: # x: (b, prompt_len)
    traj = student.generate(prompt) # (b, L)
    loss = KL(student(cat(prompt, traj)), teacher(cat(prompt, traj))) # 需要一些 mask.
```
