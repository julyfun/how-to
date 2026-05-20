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

[todo]

```
# ========== 超参 ==========
A = 7                    # 动作维数 (x,y,z, roll,pitch,yaw, gripper)；可选 +1 terminate
K = 256                  # 每维 bin 数
V = tokenizer.vocab_size # 原 VLM 词表大小，不扩表

# 占用词表末尾 K 个「最少用」token（OpenVLA/RT-2 惯例）
action_token_begin = V - (K + 1)   # +1 对齐 np.digitize 的 [1..K] 下标

# 连续值 -> bin 下标 -> token id
bins = linspace(a_min, a_max, K)           # K-1 个区间，K 个边界
bin_centers = (bins[:-1] + bins[1:]) / 2
def cont_to_token_ids(a_cont):             # a_cont: [B, A] 或 [B, T, A]
    a_clip = clip(a_cont, a_min, a_max)
    # digitize 得到 [1..K]；与 OpenVLA 一致
    bin_idx = digitize(a_clip, bins)       # [B, (T,) A]
    token_ids = V - bin_idx                # 映射到 vocab 尾部
    return token_ids                       # 各维可重复同一 token_id，靠位置区分
def token_ids_to_cont(token_ids):
    bin_idx = V - token_ids
    bin_idx = clip(bin_idx - 1, 0, K - 2)  # 落到 bin_centers 下标
    return bin_centers[bin_idx]

# ========== 训练：拼进同一条自回归序列 ==========
# 例： [vision_tokens] + [text_tokens] + [action_tokens]
# 动作在文本里常写成 "128 45 ..." 或直接喂 token_ids
vision_tok = encode_image(img)             # [B, Nv]
text_tok   = tokenize(instruction)         # [B, Nt]，这里是整数类型，Nt 是 seq_len
act_tok    = cont_to_token_ids(a_cont)     # [B, A]  单步；或 [B, T*A] 多步展平
# teacher forcing：预测下一个 token（含动作段）
seq_in  = cat([vision_tok, text_tok, act_tok[:, :-1]], dim=1)   # 若单步 A 维，[:-1] 即前 A-1 维
seq_tgt = cat([ignore,      ignore,     act_tok],        dim=1)   # 仅动作位置算 loss
# RT-2 默认 embedding 要训练
h = VLM_Transformer(seq_in, images=img)    # 或 cross-attn 把 vision 当 context
logits = LM_Head(h)                        # [B, L, V]  与文本共用 head

# 只在动作 token 位置算 CE（其余位置 mask=-100）
loss_mask = (positions in action_span)
loss = cross_entropy(
    logits[loss_mask].reshape(-1, V),
    seq_tgt[loss_mask].reshape(-1),
)
# 可选：把非动作 logits 在动作步 mask 掉，只允许预测 [action_token_begin+1 .. V-1]
# logits[..., :action_token_begin+1] = -inf

# ========== 推理：自回归生成固定 A 个动作 token ==========
context = cat([vision_tok, text_tok], dim=1)
act_pred_ids = []
for i in range(A):
    h = VLM_Transformer(context, images=img)
    logits = LM_Head(h[:, -1:, :])       # 最后一个位置
    # 限制在动作词表子集（尾部 K 个 id）
    logits[..., :action_token_begin + 1] = -inf
    next_id = argmax(logits, dim=-1)     # [B, 1]
    act_pred_ids.append(next_id)
    context = cat([context, next_id], dim=1)
act_pred_ids = stack(act_pred_ids, dim=1)  # [B, A]
a_pred = token_ids_to_cont(act_pred_ids)   # [B, A] 连续控制量

核心就是：把每个动作维度量化成离散 bin，转成 token 序列，用语言建模同款 CE loss
训练，再反量化回控制量。
```

