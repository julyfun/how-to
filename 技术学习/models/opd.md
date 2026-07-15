---
title: "OPD"
date: 2025-01-01 21:04:59
tags: ["技术学习", "models"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

普通蒸馏：
```python
for x, y_teacher in offline_dataset: # x: (b, vocab). y_teacher (b, vocab).
    loss = KL(student(x), y_teacher) # next token.
    update(student, loss)
```

OPD (on-policy distillation):
```python
for x in prompts: # x: (b, L)
    traj = student.generate(x) # (b, L, vocab)
    for token_dist in traj: # (b, vocab)
        loss =
```
