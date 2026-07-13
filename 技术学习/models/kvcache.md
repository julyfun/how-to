---
title: "kvcache"
date: 2025-01-01 11:33:17
tags: ["技术学习", "models"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

KV cache 时，每次输入给模型的是新
token，形状是 token id (b=1, L=1)，embedding 后才是 (b=1, L=1,
D)；不会把 hidden state 在 D 维或输入序列上 concat 后再整段
forward。

惯例流程是：

1. 首次 prefill：

   input_ids: (1, prompt_len)
   每层算出整段 prompt 的 k, v，存成 cache。

2. 后续 decode 每一步：

   input_ids: (1, 1)，只包含最新 token。
   每层只对这个新 token 计算新的 q, k, v。

3. attention 时：

   q 是当前 token 的 query，shape 类似 (1, heads, 1, d_k)。
   k, v 会和历史 cache 在 seq_len 维 concat：

k_all = torch.cat([past_k, new_k], dim=-2)
v_all = torch.cat([past_v, new_v], dim=-2)

然后做：

attn = q @ k_all.transpose(-1, -2)
out = attn @ v_all

所以 concat 每层
attention 内部的 k/v：

```
当前层输入 x:      (B=1, L=1, D)
当前 q/k/v:        (1, H, L=1, d_k)
cached k/v:        (1, H, T, d_k)
concat 后 k/v:     (1, H, T+1, d_k)
attention 输出:    (1, H, L=1, d_k)
合并 heads 后:     (1, L=1, D)
进入下一层:        (1, L=1, D)
```

外部接口：

```python
logits, new_cache = lm.forward(
    input_ids=current_token_ids,      # (1, 1)
    token_positions=current_position, # (1,) 或 (1, 1)
    past_kv=past_kv,
    use_cache=True,
)
```

每层返回更新后的 (k_all, v_all)，组成一个 list：

```python
past_kv = [
    (layer0_k, layer0_v),
    (layer1_k, layer1_v),
    ...
]
```
