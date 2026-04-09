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

