---
title: "285-hw4 LLM RL"
date: 2026-07-07 20:32:24
tags: ["技术学习", "285"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

## 回忆提纲
补全 GRPO 和 GE-REINFORCE.
```python
for step in range(cfg.steps)  | 📂 hw4/hw4/train.py
├── task.sample_train_batch(...)
├── sampler.rollout(...)  | 📂 hw4/hw4/rollout/hf_sampler.py
├── 给每条 completion 打 reward
├── compute_group_advantages(...)  | group 内相对优势
└──  for ppo_epoch in range(cfg.ppo_epochs)
    └── for minibatch in iter_minibatches(...)
        ├── ratio = exp(new_logp - old_logprobs)
        ├── PPO clip objective + KL
        └── backward / optimizer.step()
```

