---
title: "papers batch 2"
date: 2026-05-25 17:59:48
tags: ["papers"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

## ALOE:
递归
- ?Q-chunking

## GreenVLA
- https://hjfy.top/arxiv/2602.00919
有很多训练 trick，包括5阶段课程学习、质量指标筛选（公开数据集质量表）. 然而，demo 没有什么新东西。

## GuidedVLA
- 让 action tokens 的 q 去 attend `depth_proj(depth_enc(img))` 的 kv 得到 y，然后 action tokens += y
- 从 action tokens 学习新的 qkv 用于产生 pred_obj_mask(ground truth 由其他 grounding 模型生成) 和 pred_skill(one-hot，类似于 "pick" "place" "hold" 分类)，计算额外 skill_loss 和 obj_mask_loss
  - 代码中被称为 control_qkv
- 以上带门控

关于 control net
```python
output = original_attention(x) + # 这里是纯 pi0 的
  linear(control_attention(x)) # 只不过这里 linear 初始化为 0 防止初始就让老模型乱掉
```
