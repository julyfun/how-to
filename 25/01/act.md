---
title: "act"
date: 2025-01-01 10:53:07
tags: ["25", "01"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

一句话：state 和 image 通过 transformer encoder 作为 kv memory 提供给 decoder hidden（初始值为 0，带可学习位置编码），decoder hidden 通过 cross-attn memory 生成最终 action. act 还引入了 vae 来自监督重建 GT-action，原文声称是为了建模人类数据的 mutli-modality 防止输出平均.

这里的 vae-encoder 是一个 BERT 风格的 transformer encoder. 输入为 `[[cls], [joint state], [action seq]]`，经过四层 self-attn 最终只取 [cls] 并 Linear 得到 z. 而 policy transformer encoder 则没有 [cls].

## General

```
                       Transformer
                       推理时不使用 VAE.
                       (acts as VAE decoder
                        during training)
                      ┌───────────────────────┐
                      │             Outputs   │
                      │                ▲      │
                      │     ┌─K───►┌───────┐  │
     ┌──────┐         │     │      │Transf.│  │
     │      │         │     ├─V───►│decoder│  │
┌────┴────┐ │         │     │      │       │  │
│         │ │         │ ┌───┴───┬─►│       │  │
│ VAE     │ │         │ │       │  └───────┘  │
│ encoder │ │         │ │Transf.│             │
│         │ │         │ │encoder│             │
└───▲─────┘ latent    │ │       │             │
    │       │         │ └▲──▲─▲─┘             │
    │       │         │  │  │ │               │
  inputs    └─────────┼──┘  │ image emb.(use resnet backbone)
    │                 │   qpos emb.(No action emb.)
action&qpos emb.      └───────────────────────┘

where latent: (b, 512)
```

## 其他
- is_pad 是什么：考虑到有些采样动作长度不足 chunk_size，其对应位置 is_pad 为 true 且 input 由复制产生且不会被注意（已验证）
- decoder_pos_embed 是什么：形状是 [50, 8, 512], 是固定长度 (`num_queries`) 的学习参数，代表 `num_queries`个“查询槽位”，每个槽位询问一个动作。

## Train
```mermaid
flowchart TD
    qpos(["qpos<br/>(B=8, state_dim=14)"]) --> qemb[["qpos Embedding / proj<br/>14 -> D=512"]]
    action(["GT Actions<br/>(B=8, chunk_size=50, action_dim=14)"]) --> aemb[["action Embedding<br/>14 -> D=512"]]
    cls[["cls_embed<br/>(B=8, 1, D=512)"]] --> encin(["VAE tokens<br/>(seq_len=52, B=8, D=512)"])
    qemb --> encin
    aemb --> encin
    encin --> vae[["VAE Transformer Encoder<br/>ACTEncoder"]]
    vae --> dist[["latent proj MLP<br/>mu, logvar"]]
    dist --> z(["sample latent z<br/>(B=8, latent_dim=512)"])
    dist --> kl["KL Loss"]

    img(["Images<br/>(B=8, n_cam=3, C=3, H=480, W=640)"]) --> norm["Image Normalize<br/>ImageNet mean/std"]
    norm --> backbone[["ResNet Backbone<br/>feature D=512"]]
    backbone --> feat(["Image Features<br/>(B=8, D=512, H=15, W=60)<br/>900 tokens"])

    z --> zproj[["latent_input_proj<br/>512 -> 512"]]
    qpos --> stateproj[["input_proj_robot_state<br/>14 -> 512"]]
    zproj --> addtok(["Extra Tokens<br/>(2, B=8, D=512)<br/>latent + qpos"])
    stateproj --> addtok
    feat --> src(["Encoder src<br/>(seq_len=902, B=8, D=512)"])
    addtok --> src

    src --> venc[["Transformer Encoder<br/>vision + state + latent"]]
    query[["decoder_pos_embed<br/>num_queries=50, D=512"]] --> tgt(["Decoder tgt zeros<br/>(50, B=8, D=512)"])
    tgt --> dec[["Transformer Decoder<br/>cross-attn to memory"]]
    query --> dec
    venc --> mem(["memory<br/>(902, B=8, D=512)"])
    mem --> dec
    dec --> hs(["Action Tokens<br/>(B=8, 50, D=512)"])

    hs --> ahead[["action_head / proj<br/>512 -> 14"]]
    hs --> phead[["is_pad_head / proj<br/>512 -> 1"]]
    ahead --> ahat(["Pred Actions<br/>(B=8, 50, 14)"])
    phead --> phat(["Pred is_pad<br/>(B=8, 50, 1)"])

    action --> recon["Masked L1 Loss"]
    ispad(["is_pad mask<br/>(B=8, 50)"]) --> recon
    ahat --> recon
    phat --> padloss["Pad / auxiliary loss"]
    ispad --> padloss
    recon --> total(["Total Loss<br/>L1 + kl_weight * KL"])
    kl --> total
    padloss --> total
```

## Infer
```mermaid
flowchart TD
    qpos(["qpos<br/>(B=8, state_dim=14)"]) --> stateproj[["input_proj_robot_state<br/>14 -> 512"]]
    img(["Images<br/>(B=8, n_cam=3, C=3, H=480, W=640)"]) --> norm["Image Normalize<br/>ImageNet mean/std"]
    norm --> backbone[["ResNet Backbone<br/>feature D=512"]]
    backbone --> feat(["Image Features<br/>(B=8, D=512, H=15, W=60)<br/>900 tokens"])

    zero(["zero latent<br/>(B=8, latent_dim=512)"]) --> zproj[["latent_input_proj<br/>512 -> 512"]]
    zproj --> addtok(["Extra Tokens<br/>(2, B=8, D=512)<br/>latent + qpos"])
    stateproj --> addtok

    feat --> src(["Encoder src<br/>(seq_len=902, B=8, D=512)"])
    addtok --> src
    src --> enc[["Transformer Encoder<br>多层 selfattn + FFN"]]
    enc --> mem(["memory<br/>(902, B=8, D=512)"])

    query[["decoder_pos_embed<br/>num_queries=50, D=512"]] --> tgt(["Decoder tgt zeros<br/>(50, B=8, D=512)"])
    tgt --> dec[["Transformer Decoder<br/>cross-attn to memory"]]
    query --> dec
    mem --> dec

    dec --> hs(["Action Tokens<br/>(B=8, 50, D=512)"])
    hs --> ahead[["action_head / proj<br/>512 -> 14"]]
    hs --> phead[["is_pad_head / proj<br/>512 -> 1"]]
    ahead --> ahat(["Pred Action Chunk<br/>(B=8, horizon=50, action_dim=14)"])
    phead --> phat(["Pred is_pad<br/>(B=8, 50, 1)"])
    ahat --> exec["Execute / temporal aggregation<br/>next action(s)"]
```

## 其中 decoder QKV
```mermaid
flowchart TD
    tgt(["Decoder tgt zeros<br>(全 0 tensor)<br>(T=50, B=8, D=512)"])
    query[["decoder_pos_embed<br>表明 query 位置.<br>是 learnable embedding.<br>(T=50, 1, D=512)"]] --> selfqk["+"]
    tgt --> selfqk
    selfqk --> selfq(["Self-attn Q/K<br/>(50, B=8, 512)"])
    tgt --> selfv(["Self-attn V<br/>(50, B=8, 512)"])
    selfq --> selfattn[["self_attn<br>WTF??这不是全 0 吗"]]
    selfv --> selfattn
    selfattn --> x1(["Decoder hidden<br/>(50, B=8, 512)"])

    x1 --> crossqadd["+"]
    query --> crossqadd
    crossqadd --> crossq(["Cross-attn Q<br/>(50, B=8, 512)"])

    mem(["memory<br/>(encoder_out)<br/>(S=902, B=8, D=512)"]) --> crosskadd["+"]
    pos(["encoder_pos_embed<br>2D Sine<br>(S=902, B=8, D=512)"]) --> crosskadd
    crosskadd --> crossk(["Cross-attn K<br/>(902, B=8, 512)"])
    mem --> crossv(["Cross-attn V<br/>(902, B=8, 512)"])

    crossq --> crossattn[["cross-attn<br>memory不变<br>每层 self-attn + cross memory + FFN"]]
    crossk --> crossattn
    crossv --> crossattn
    crossattn --> ff[["MLP<br/>512 -> feedforward -> 512"]]
    ff --> out(["decoder_out<br/>(50, B=8, D=512)"])
```