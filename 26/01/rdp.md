---
title: "RDP"
date: 2026-01-20 19:09:53
tags: ["26", "01"]
author: "julyfun arch y9000p"
os: "Linux archfun 6.18.5-arch1-1 #1 SMP PREEMPT_DYNAMIC Sun, 11 Jan 2026 17:10:53 +0000 x86_64 GNU/Linux"
assume-you-know: [computer]
confidence: 2
---

## Reactive Diffusion Policy (RDP) 网络结构

### 整体架构

RDP 采用慢-快（slow-fast）分层结构：

1. **Slow Policy (LDP - Latent Diffusion Policy)**：低频预测高级动作块
2. **Fast Policy (AT - Asymmetric Tokenizer)**：高频基于触觉/力反馈进行闭环调整

---

### Slow Policy (LDP) 部分

**输入**：
- RGB 图像（240×320，2帧 @ 12Hz）
- Tactile/Force embedding（PCA特征或6D wrench）
- Proprioception（机器人TCP位姿等）
- 频率：1-2 Hz（低频观测）

**网络结构**：
- 视觉编码器：ResNet18（MultiImageObsEncoder）
- Diffusion U-Net：1D U-Net，在潜在空间中预测动作块
- 输入维度：`(B, T, D_latent)`，其中 `T` 是下采样后的horizon

**输出**：
- Latent action chunk：`(B, horizon, latent_dim)`
- 例如：`(1, 8, 4)` 表示8个时间步，每个4维潜在动作

---

### Fast Policy (AT) 部分

**结构**：
- 编码器（Encoder）：1D-CNN 或 MLP，将 action chunk 编码到潜在空间
- 解码器（Decoder）：GRU，使用高频触觉/力信号解码动作

**训练时输入**：
- Action chunk：`(B, 32, action_dim)` @ 24Hz
- Tactile/Force embedding：`(B, 32, tactile_dim)` @ 24Hz

**推理时输入**：
- Latent action chunk：来自 Slow Policy
- 高频 Tactile/Force：`(B, T, tactile_dim)` @ 24-30Hz

**输出**：
- Action sequence：`(B, T, action_dim)`，例如 `(1, 32, 4)` 表示32步，每步4维动作（x, y, z, gripper）

---

## 训练流程图

```
┌─────────────────────────────────────────────────────────────┐
│                    Stage 1: 训练 AT (Fast Policy)            │
└─────────────────────────────────────────────────────────────┘

数据集 (24Hz)
  │
  ├─ Action Chunk: (B, 32, 4)  [32步动作序列]
  └─ Tactile/Force: (B, 32, d) [对应32步的触觉/力信号]
      │
      ▼
  ┌─────────────────┐
  │  AT Encoder     │  ← 只使用 Action Chunk
  │  (1D-CNN/MLP)   │
  └────────┬────────┘
           │
           ▼
    Latent Action: (B, 8, 4)  [下采样到8步]
           │
           ▼
  ┌─────────────────┐
  │  AT Decoder     │  ← 使用 Latent + Tactile/Force
  │  (GRU)          │
  └────────┬────────┘
           │
           ▼
    Reconstructed Action: (B, 32, 4)
           │
           ▼
    Loss: L1 Reconstruction + KL Penalty
           │
           ▼
    训练完成，保存 AT 模型


┌─────────────────────────────────────────────────────────────┐
│          Stage 2: 训练 LDP (Slow Policy)                    │
└─────────────────────────────────────────────────────────────┘

数据集 (12Hz 低频观测)
  │
  ├─ RGB Images: (B, 2, 3, 240, 320)
  ├─ Tactile/Force: (B, 2, d)
  ├─ Proprioception: (B, 2, ...)
  └─ Action Chunk: (B, 12, 4)  [12步动作序列]
      │
      ▼
  ┌─────────────────┐
  │  AT Encoder     │  ← 使用预训练的 AT Encoder (冻结)
  │  (冻结)         │
  └────────┬────────┘
           │
           ▼
    Latent Action: (B, 8, 4)
      │
      ▼
  ┌─────────────────┐
  │  Visual Encoder │  ← ResNet18
  │  (ResNet18)     │
  └────────┬────────┘
           │
           ▼
    Visual Features: (B, feature_dim)
      │
      ├─────────────────┐
      │                 │
      ▼                 ▼
  ┌─────────────────────────────────┐
  │  Diffusion U-Net (1D)           │
  │  - 输入: Noisy Latent Action    │
  │  - 条件: Visual Features        │
  │  - 输出: Predicted Noise        │
  └──────────────┬──────────────────┘
                 │
                 ▼
          Diffusion Loss (MSE)
                 │
                 ▼
           训练完成，保存 LDP 模型
```

---

## 推理流程图

```
┌─────────────────────────────────────────────────────────────┐
│                      推理循环 (实时)                         │
└─────────────────────────────────────────────────────────────┘

时间步 t (每 1/6 秒，即 6Hz)
  │
  ├─ 获取低频观测 (1-2Hz)
  │   ├─ RGB Images: (1, 2, 3, 240, 320)
  │   ├─ Tactile/Force: (1, 2, d)
  │   └─ Proprioception: (1, 2, ...)
  │
  ▼
┌─────────────────────────────────┐
│  Slow Policy (LDP)              │  ← 每 1-2 秒运行一次
│  - Visual Encoder               │
│  - Diffusion U-Net              │
│  - 采样潜在动作块                │
└────────────┬────────────────────┘
             │
             ▼
    Latent Action Chunk: (1, 8, 4)
             │
             │  存储到 Ensemble Buffer
             │
             ▼
┌─────────────────────────────────┐
│  Ensemble Buffer                │
│  - 存储 Latent Action Chunk     │
│  - 管理动作队列                  │
└────────────┬────────────────────┘
             │
             │  每 1/24 秒 (24Hz)
             │
             ▼
┌─────────────────────────────────┐
│  Fast Policy (AT Decoder)       │  ← 高频运行 (24-30Hz)
│  - 获取最新 Latent Action       │
│  - 获取最新 Tactile/Force       │
│  - GRU Decoder 解码             │
└────────────┬────────────────────┘
             │
             ▼
    Action: (1, 1, 4)  [单步动作]
             │
             ▼
    ┌─────────────────┐
    │  执行到机器人    │
    └─────────────────┘
             │
             │  循环继续...
             │
             ▼
    下一个时间步 (t+1)
```

---

## 关键设计要点

1. 非对称结构：编码器只用 action，解码器用 latent + tactile/force，使潜在空间保留高级策略，细节由触觉反馈决定。
2. 频率分离：Slow Policy 1-2Hz 建模复杂轨迹，Fast Policy 24-30Hz 实现闭环控制。
3. 相对轨迹：使用相对 TCP 位姿，便于学习通用反应策略。
4. Latency Matching：丢弃前几步动作以匹配推理和执行延迟，保证动作块间平滑过渡。

---

## 输入输出总结

| 组件 | 输入 | 输出 | 频率 |
|------|------|------|------|
| **Slow Policy (LDP)** | RGB图像 + Tactile/Force + Proprioception | Latent Action Chunk | 1-2 Hz |
| **Fast Policy (AT Decoder)** | Latent Action + 最新 Tactile/Force | Action (pose array) | 24-30 Hz |
| **最终输出** | - | Action Chunk: `(T, action_dim)` | 24 Hz |

其中 `action_dim` 通常是 4（单臂：x, y, z, gripper）或 8（双臂：x_l, y_l, z_l, x_r, y_r, z_r, gripper_l, gripper_r）。
