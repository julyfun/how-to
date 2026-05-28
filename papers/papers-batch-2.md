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
递归学习..
- ?Q-chunking

## GreenVLA
- https://hjfy.top/arxiv/2602.00919
有很多训练 trick，包括5阶段课程学习、质量指标筛选（公开数据集质量表）. 然而，demo 没有什么新东西。

## GuidedVLA: ybw
一句话：给 pi0 action token 加手工设计的 auxiliary tasks.
- 让 action tokens 的 q 去 attend `depth_proj(depth_enc(img))` 的 kv 得到 y1
- 从 action tokens 学习新的 q 以及从 concat(image tokens, action tokens) 学习新的 kv 用于:
  - 计算 这里 qk 的 attn score，这个 score 和 GT attn mask patchify 得到 obj_loss (ground truth 由其他 grounding 模型生成)
  - 以及产生 pred_skill(one-hot，类似于 "pick" "place" "hold" 分类)，计算额外 skill_loss. 这里也会得到 y2 y3
  - action tokens += linear(concat(y1, y2, y3))
  - (代码中被称为 control_qkv)
- 以上带门控
- 以上给 action expert 的指定层去做，代码默认 [9, 10, 11, 12]  (pi0 expert 一共 18 层)

关于 control net
```python
output = original_attention(x) + # 这里是纯 pi0 的
  linear(control_attention(x)) # 只不过这里 linear 初始化为 0 防止初始就让老模型乱掉
```

## Interleave-VLA: fcx

```patch
 # 输入包含当前观测图像、交错的图文指令及机器人状态
 # 使用 <BOI>/<EOI> 特殊 Token 标识指令中的参考图像
-instr_tokens = tokenizer.encode("把那个蓝色的带条纹的勺子放到盘子里") # 常规 VLA
+instr_tokens = tokenizer.encode(f"把 <BOI>{crop_img}<EOI> 放到盘子里") # 本方法，操作者在GUI手动框选目标
 obs_tokens = visual_encoder(current_observation)
 # 将观测、交错指令和本体感受状态拼接为统一序列
 input_seq = concat(obs_tokens, instr_tokens, robot_state)
 # VLA 模型直接生成连续动作序列
 actions = VLA_Model.predict(input_seq)
```

```mermaid
flowchart LR
    img["Observation Images<br/>(B, n_cam=3, H=224, W=224, C=3)"] --> siglip["PaliGemma Image Encoder(SigLIP)"]
    instr_img["Instruction Images (Crops/Web/Sketch)<br/>(B, n_imgs, 224, 224, 3)"]:::highlight --> siglip
    txt["Interleaved Tokens (Text + BOI/EOI)<br/>(B, max_len=N)"]:::highlight --> tok["Gemma Tokenizer + Special Tokens"]:::highlight
    siglip --> obs_vis["Observation Tokens<br/>(B, 3*256=768, D=2048)"]
    siglip --> instr_vis["Instruction Visual Tokens<br/>(B, n*256, D=2048)"]:::highlight
    tok --> textemb["Text Embeddings<br/>(B, N, D=2048)"]
    instr_vis --> inter_instr["Interleaved Instruction Embeddings<br/>(Text Tokens & Visual Tokens Mix)"]:::highlight
    textemb --> inter_instr
    obs_vis --> prefix["Prefix Tokens (Obs + Interleaved Instr)<br/>(B, seq_len, D=2048)"]:::highlight
    inter_instr --> prefix
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

    classDef highlight fill:#ffff00,stroke:#333,stroke-width:2px;
```

## Implicit RDP
- https://hjfy.top/arxiv/2512.10946

```python
# slow #1: cache slow context once for one action chunk
slow_obs_1 = {
    img:      img_slow[S-1:S+1],               # (B,2,3,360,640), slow history: 2 frames
    tcp_pose: tcp_slow[S-1:S+1],               # (B,2,6). S: slow 时间轴上的时间索引
}
slow_kv_1 = SlowEncoder(slow_obs_1)            # (B,~100,768)
noise_1 = randn(B,16,13)                       # cached initial noise for this chunk
# infer #1
fast_obs = wrench_fast[F0:F_cur+1+l]           # 多个 fast steps，覆盖 slow history 到当前控制步
fast_kv = FastGRU(fast_obs)                    # (B,L1,768) L1 就是 len(wrench_fast[F0:F_cur+1+l])
x = DDIM(noise_1[:, :L1], slow_kv_1, fast_kv)  # (B,L1,13)
execute(x[:, -1, :6])                          # execute tcp pose only. :6 是因为后面是 auxiliary.
# infer #2
fast_obs = wrench_fast[F0:F_cur+2+l]           # 多个 fast steps，覆盖 slow history 到当前控制步，并追加新 force
fast_kv = FastGRU(fast_obs)                    # (B,L1+1,768)
x = DDIM(noise_1[:, :L2], slow_kv_1, fast_kv)  # (B,L1+1,13)
execute(x[:, -1, :6])
# infer #3 ...

# slow #2: update slow context, start a new chunk
slow_obs_2 = {
    img:      img_slow[S:S+2],                 # next 2 slow frames
    tcp_pose: tcp_slow[S:S+2],
}
slow_kv_2 = SlowEncoder(slow_obs_2)
noise_2 = randn(B,16,13)
# new chunk infer #1
fast_obs = wrench_fast[F1:F_cur2+1+l]          # 多个 fast steps，覆盖新的 slow history 到当前控制步
fast_kv = FastGRU(fast_obs)
x = DDIM(noise_2[:, :L1], slow_kv_2, fast_kv)
execute(x[:, -1, :6])
```
