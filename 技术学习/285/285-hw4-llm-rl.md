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
├── sampler.rollout(...)  | 对每个 prompt 生成多个 completion 作为一个 group | 📂 hw4/hw4/rollout/hf_sampler.py
├── 给每条 completion 打 reward
├── compute_group_advantages(...)  | group 内相对 advantage
├── 上述所有 rollout 制作成 minimatch
└──  for ppo_epoch in range(cfg.ppo_epochs)
    └── for minibatch in iter_minibatches(...)
        ├── ratio = exp(new_logp - old_logprobs)
        ├── PPO clip objective + KL
        └── backward / optimizer.step()
```

## format_copy
输入字符串，输出 `<answer>输入</answer>`.

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/merged-image.png)

## math_hard

## Answer questions

### 1. Approximate KL

### 2. Implementation

按照 pdf 建议的顺序补全了 8 个函数.

one bug or confusion point: 写 GRPO 的时候我发现 GRPO loss 的量纲和 GR-REINFORCE loss 似乎不同，后者具有平凡 PG surrogate 的 `-logprob * adv`，而前者是 `-(logprob_new - logprob_old).exp() * adv`. 后来询问发现 GRPO 也是正确的 surrogate.

### 4. GRPO ablation on format_copy

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/merged-image-2.png)
