---
title: "Robot Transformer Basics"
date: 2025-01-01 14:58:22
tags: ["25", "01"]
author: "Julyfun MacOS14.5 M1"
os: "Darwin floriandeMacBook-Air.local 25.2.0 Darwin Kernel Version 25.2.0: Tue Nov 18 21:09:55 PST 2025; root:xnu-12377.61.12~1/RELEASE_ARM64_T8103 arm64"
assume-you-know: [computer]
confidence: 2
---

> "使用 Image Encoder 以及 Text Encoder 并使用 FiLM 进行 Fusion 后用 Transformer 处理的模型"
用高度凝练的几行 pytorch 伪代码告诉我这里的写法。尤其是  film 和如何后续采用 transformer 处理

## FiLM
来自 RT1

使用 txt token => MLP 的输出缩放 img token

```python
# img: [B, C, H, W], txt_ids: [B, L]
v = ImageEncoder(img)                    # [B, Nv, D]   (视觉 token)
t = TextEncoder(txt_ids).mean(1)         # [B, Dt]      (文本全局语义)

gamma, beta = Linear(t).chunk(2, dim=-1) # 各 [B, D]
v_film = v * (1 + gamma[:, None, :]) + beta[:, None, :]   # FiLM: feature-wise affine

x = torch.cat([CLS.expand(B,1,D), v_film], dim=1)         # [B, 1+Nv, D]
h = TransformerEncoder(x)                                  # [B, 1+Nv, D]
y = Head(h[:, 0])                                          # 用 CLS 做下游预测
```

## 更现代的（把现成 LLM Transformer 当作 fusion 主干）
```python
v = VisionEncoder(img)                               # [B, Nv, Dv]
v_tok = VisionProjector(v)                           # [B, Nv, D]  对齐到 LLM 维度

t_tok = LLM.embed_tokens(text_ids)                   # [B, Nt, D]
x = torch.cat([BOV, v_tok, EOV, t_tok], dim=1)       # 视觉+语言统一序列（Fusion in LLM）

h = LLM.transformer(x, causal_mask=True)             # 统一 Transformer 融合
a_logits = ActionHead(h[:, -Na:, :])                 # 取动作位置 hidden state
a = sample_or_argmax(a_logits)                       # 自回归/并行输出离散动作 token

如果动作是连续量，也常见：
a = MLP(h[:, -1, :])   # 直接回归 7DoF/控制量
```

## 预测 attn map
来自 RT1

就是你能想到的最简单的自主加权. （每个 token 自己算自己对 m 个结果的权重，权重和为 1）

```
# x: [B, N, D]  (N个输入token)
attn_logits = MLP(x)                      # [B, N, M]   -> 每个token对M个map的打
分
attn = torch.softmax(attn_logits, dim=1)  # 在token维归一化: 每张map覆盖N个token

# 用每张attention map对token做加权汇聚
# x_out[b,m,d] = sum_n attn[b,n,m] * x[b,n,d]
x_out = torch.einsum('bnm,bnd->bmd', attn, x)   # [B, M, D]
```

## RT-2 离散动作 token

```python
# RT-2: 连续动作 → 词表尾部 K 个 token，同一 VLM 自回归 CE
act_ids = V - digitize(clip(a, a_min, a_max), K_bins)     # [B, A]
seq = cat([vision_tok, text_tok, act_ids[:, :-1]], dim=1)
h = VLM_Transformer(seq, images=img)
loss = CE(LM_Head(h)[action_mask], act_ids)               # 仅动作位算 loss

# infer: 自回归 A 步，logits 尾部子集 argmax → bin_centers 反量化
context = cat([vision, text])
for _ in range(A):
    next_id = argmax(LM_Head(VLM(context)[:, -1:])[:, :, V-K:], -1)
    context = cat([context, next_id], dim=1)
a = bin_centers[V - stack(context[:, -A:]) - 1]
```

## pi0.5

```python
# π₀.₅: PaliGemma prefix + Action Expert suffix + flow matching
v = SigLIP(imgs)                                    # [B, Nv, D]
t = PaliGemma.embed(prompt_with_discrete_state)     # state 在文本里
prefix = cat([v, t])                                # 图文双向 (prefix-LM)
x_t, t = noise * t + actions * (1-t)                # flow 插值
suffix = Linear_in(x_t)          # [B, Na, D]. 编码到 token-embedding-space. 代码中叫做 action_in_proj
cond = MLP(sincos(t))                               # adaRMS 条件
# Gemma 内跑 suffix 的那条路是 Action Expert （expert 1，Gemma-300M）
(h_pre, h_suf) = DualGemma([prefix, suffix], mask=prefix_lm, adarms=[None, cond]) # 输出 hidden states
loss = MSE(Linear_out(h_suf[:, -Na:]), noise - actions)
# infer: cache prefix → Euler: x += dt * Linear_out(h_suf), t -= dt # 解码回动作空间 (flow 的速度场)
```

