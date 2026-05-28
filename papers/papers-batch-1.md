---
title: "Papers batch 1"
date: 2025-01-01 23:10:53
tags: ["papers"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

## RT-2
- https://hjfy.top/arxiv/2307.15818
和 OpenVLA 同属一派，将 VLM 的最后 256 个 token id 分配给动作，直接将 x, y, z, yaw, pitch, roll, gripper 划分为 256 个离散桶，七个动作维度共享 token id 并通过位置区分语义，直接拼接丢给 VLM 输出隐状态，一个 head 解码出 id 再映射回动作空间. 缺点是离散化和自回归导致的精度不够.

TODO: 数据集这一块儿有空可以再看看.

## World Model for Robot Learning: A Comprehensive Survey
- https://hjfy.top/arxiv/2605.00080

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20260520212623754.png)

## Fast-WAM (Yuanet al., 2026)
- https://hjfy.top/arxiv/2603.16666
可被视为该家族中的一个混合点：它采用具有共享注意力的 Transformer 混合体骨干网络 及耦合的视频与动作分支，但结论认为主要优势可能更多来自训练期间的视频协同训练，而非推理阶段 的显式未来想象。在这些变体中，视频分支越来越不再被视为需要忠实渲染的输出，而是被看作一种预 测性潜在过程，其隐状态用于指导动作生成.

```mermaid
flowchart LR
    video["Training Video<br/>(B, 3, T=33, H=224, W=448)"] --> vae["Wan VAE Encode"]
    vae --> z0["Video Latents z_0<br/>(B, 48, T_lat=9, 28, 56)"]
    z0 --> zv["Add Flow Noise<br/>sample t_v, eps_v"]
    zv --> vpre["Video Expert pre_dit<br/>patchify + 3D RoPE"]

    prompt["Task Prompt / Cached Text<br/>(B, L=128, D=4096)"] --> ctx["Text Context"]
    state["Robot State<br/>(B, T, D_state=8)"] --> prop["proprio_encoder<br/>as 1 state token"]
    prop --> ctx
    ctx --> vpre

    action["GT Actions a_0<br/>(B, T_act=32, A=7)"] --> za["Add Flow Noise<br/>sample t_a, eps_a"]
    za --> apre["Action Expert pre_dit<br/>Linear(A -> 1024) + 1D RoPE"]
    ctx --> apre

    vpre --> vt["Video Tokens<br/>(B, S_v=3528, D_v=3072)"]
    apre --> at["Action Tokens<br/>(B, 32, D_a=1024)"]
    vt --> mot["MoT Mixed Transformer<br/>30 layers shared masked self-attn"]
    at --> mot
    mask["Mask<br/>video->video causal<br/>action->first-frame video + action"] --> mot

    mot --> vpost["Video post_dit<br/>unpatchify"]
    mot --> apost["Action post_dit<br/>Linear(1024 -> A)"]
    vpost --> pv["Predicted video velocity<br/>(B, 48, T_lat', 28, 56)"]
    apost --> pa["Predicted action velocity<br/>(B, 32, 7)"]

    zv --> vtgt["Target video velocity"]
    za --> atgt["Target action velocity"]
    pv --> vloss["Video FM Loss"]
    vtgt --> vloss
    pa --> aloss["Action FM Loss"]
    atgt --> aloss
    vloss --> total["Total Loss<br/>lambda_v * L_video + lambda_a * L_action"]
    aloss --> total
```

## Lingbot-va
- https://hjfy.top/arxiv/2601.21998
- [ok] 自回归扩散
    - [ok] "对统一序列施加因果注意力掩码，确保预测的视觉状态和动作命令均受先前状态的约束"

```python
obs0 -> VAE -> z0

infer #1 (frame_st_id=0):
  1) flow denoise video chunk [z0_anchor, z1_hat]   # 2帧，不是(z1,z2)两个未来
     - 第0帧 init_latent=z0
     - 第1帧才是预测的未来 latent
  2) flow denoise action chunk [a_grp0(16步), a_grp1(16步)]  # 共32步
     - 条件：cache(空) + 刚预测的 video chunk
execute #1（第一轮特殊）:
  start_idx=1 -> 跳过 a_grp0，只执行 a_grp1 的 16 步
  每 4 步收一次 obs -> key_frame_list（约 4 个真实 obs）
compute_kv_cache #1:
  clear_pred_cache()          # 删掉 z_hat、a_hat，不是“替换某几帧”
  real_z = VAE(key_frame_list)
  若 frame_st_id==0: cat(init_latent=z0, real_z)
  real_a = preprocess(executed action chunk)
  写入 cache（is_pred=False）

infer #2:
  预测下一个 chunk [z2_hat, z3_hat] + [a_grp2, a_grp3]
  条件：cache 里的 real history
execute #2 起:
  start_idx=0 -> 执行完整 32 步
  每 4 步收 obs -> key_frame_list（约 8 个）
compute_kv_cache #2:
  再次 clear_pred_cache()
  追加新的 real_z / real_a
```

## RTC
```python
# H: (Prediction Horizon), M: 动作维度 (Action Dim), O: 观测维度
def rtc_inference(v_net, o_t, A_prev, d, s, n=5, beta=5):
    # o_t: 观测 [O], A_prev: 旧动作块的残余部分 [H, M] (已 pad0 至H长度)
    # d: 推理延迟 s: 执行步长 n: 迭代步数 beta: 引导项裁剪值
    A_tau = torch.randn((H, M))             # [H, M] 采样初始噪声
    W = compute_soft_mask(d, s, H)          # [H, 1] 软掩码权重，1 ~ 0递减
    for tau in np.linspace(0, 1, n):        # n 步流匹配迭代
        v = v_net(A_tau, o_t, tau)          # [H, M] 当前速度场预测
        # A_hat_1: [H, M] 预估当前步如果去噪完成后的最终动作轨迹
        A_hat_1 = A_tau + (1 - tau) * v
        # 计算带权重的 Inpainting 误差
        loss = 0.5 * (W * (A_prev - A_hat_1)**2).sum()  # 标量 Scalar
        # g: [H, M] 获取修正梯度，指引 A_tau 向 A_prev 靠拢
        g = torch.autograd.grad(loss, A_tau)[0]
        scale = min(beta, get_weight_scale(tau)) # get_weight_scale 是一个随 tau 递减的权重
        # A_tau: [H, M] 结合原始预测与裁剪后的引导项进行更新
        A_tau += (1/n) * (v + scale * g)
    return A_tau                            # [H, M] 平滑衔接的新动作块
```

## Pi0
```mermaid
flowchart LR
    img["Images<br/>(B, n_cam=3, H=224, W=224, C=3)"] --> siglip["PaliGemma Image Encoder(SigLIP)"]
    txt["Text Tokens<br/>(B, max_token_len=48)"] --> tok["Gemma Token Embedding"]
    siglip --> vis["Visual Tokens<br/>(B, 3*256=768, D=2048)"]
    tok --> textemb["Text Embeddings<br/>(B, 48, D=2048)"]
    vis --> prefix["Prefix Tokens<br/>(B, seq_len=816, D=2048)"]
    textemb --> prefix
    state["Robot State<br/>(B, action_dim=32)"] --> stateproj["state_proj"]
    noisy["Noisy Actions x_t<br/>(B, horizon=50, action_dim=32)"] --> actproj["action_in_proj"]
    time["Flow Time t<br/>(B,)"] --> timemlp["Time Embedding MLP"]
    stateproj --> statetok["State Token<br/>(B, 1, D=1024)"]
    actproj --> acttok["Action Tokens<br/>(B, 50, D=1024)"]
    timemlp --> timetok["Time Tokens<br/>(B, 50, D=1024)"]
    acttok --> mix["Action + Time Tokens<br/>(B, 50, D=1024)"]
    timetok --> mix
    statetok --> suffix["Suffix Tokens<br/>(B, seq_len=51, D=1024)"]
    mix --> suffix
    prefix --> pg["PaliGemma / Gemma 2B Expert"]
    suffix --> ae["Action Expert / Gemma 300M"]
    pg <--> shared["Shared Masked Self-Attn (qkv dim=256)"]
    ae <--> shared
    shared --> actout["action_out_proj"]
    actout --> vt["Predicted v_t<br/>(B, 50, action_dim=32)"]
    gt["Target u_t = noise - action<br/>(B, 50, action_dim=32)"] --> loss["Flow Matching Loss"]
    vt --> loss
```

```mermaid
flowchart LR
    img["Images<br/>(B, n_cam=3, H=224, W=224, C=3)"] --> siglip["PaliGemma Image Encoder(SigLIP)"]
    prompt["Task Prompt<br/>(string)"] --> format["Prompt Format<br/>Task: ..., State: ...;<br/>Action:"]
    rawstate["Raw / Normalized Robot State<br/>(B, action_dim=32)"] --> binstate["Digitize State<br/>256 bins over [-1, 1]"]
    binstate --> statestr["State String<br/>(e.g. '12 98 ...')"]
    statestr --> format
    format --> txt["Text + Discrete State Tokens<br/>(B, max_token_len=200)"]
    txt --> tok["Gemma Token Embedding"]

    siglip --> vis["Visual Tokens<br/>(B, 3*256=768, D=2048)"]
    tok --> textemb["Text/State Embeddings<br/>(B, 200, D=2048)"]
    vis --> prefix["Prefix Tokens<br/>(B, seq_len=968, D=2048)"]
    textemb --> prefix

    noisy["Noisy Actions x_t<br/>(B, horizon=50, action_dim=32)"] --> actproj["action_in_proj"]
    time["Flow Time t<br/>(B,)"] --> timemlp["Time MLP for adaRMSNorm"]

    actproj --> suffix["Suffix Action Tokens<br/>(B, seq_len=50, D=1024)"]
    timemlp --> adarms["adaRMSNorm condition<br/>(B, D=1024)"]

    prefix --> pg["PaliGemma / Gemma 2B Expert"]
    suffix --> ae["Action Expert / Gemma 300M"]
    adarms --> ae

    pg <--> shared["Shared Masked Self-Attn<br/>(qkv head_dim=256)"]
    ae <--> shared

    shared --> actout["action_out_proj"]
    actout --> vt["Predicted v_t<br/>(B, 50, action_dim=32)"]
    gt["Target u_t = noise - action<br/>(B, 50, action_dim=32)"] --> loss["Flow Matching Loss"]
    vt --> loss
```
