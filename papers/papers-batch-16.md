---
title: "papers batch 16"
date: 2026-11-06 22:17:52
tags: ["papers"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 27.0.0 Darwin Kernel Version 27.0.0: Tue Aug 11 21:02:59 PDT 2026; root:xnu-13432.1.9~1/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

## Reweight (125)

⭐️⭐️ Chenwei Wang, Zhongliang Jiang, HKU & TeleAI | https://www.alphaxiv.org/pdf/2609.13851

用后训练机器人示范检索 egodex 中的人类数据，通过 levr 流水线加入后训练，检索直接使用最优传输 + 简单 vision-action 编码. 人类视频权重 = 0.5.

ablation 做了组成权重，编码器，以及人类视频权重 alpha.

## open-humanwam (126)

⭐️⭐️⭐️ juncheng ma, daquan zhou, PKU & NUS 新加坡国立 | https://www.alphaxiv.org/abs/2611.06817

用开源纯 ego 数据 50kh 预训练，取得 68.8% 的 c2r. 没有用 intern 也是很神奇. 其中，goal 分支使用了机器人数据预训练.

不管是 vanilla 还是 goal，后训练数据增强都很强，鉴定为 patchwam 2.0. 两个分支也都使用了 egopro 三视角中训练，不然论文认为后训练直接加腕部相机会损害 OOD 泛化. 真机依旧非常简单，没怎么调好；但是有一定 zero-shot 能力！

帮我们做了诸多消融，动作表示等，我们来具体看看，尽管过于依赖 robotwin 了... 之后可以在 dojo 上验证:

- 数据多样性（这个数值是斜率，每增加 10 倍数据小时的 twin 成功率百分点）

| 评估设置 | 扩展任务与场景多样性 | 固定多样性 |
|---|---:|---:|
| Clean | 4.82 | 2.80 |
| Scene-OOD | 16.54 | 11.81 |
| Random | 11.91 | 7.41 |

- 跨数据源动作对齐

| 设置 | Clean | Scene-OOD | Random |
|---|---:|---:|---:|
| 对齐 | 77.5 | 52.2 | 26.4 |
| 未对齐 | 72.0 | 43.2 | 18.0 |

- Ego 动作监督（预训练 20k 步）

| 设置 | Clean | Scene-OOD | Random |
|---|---:|---:|---:|
| 50% 视频时长有动作标注 | 75.2 | 34.8 | 16.3 |
| 纯视频（无动作监督） | 70.4 | 13.0 | 3.6 |

- 注意力与动作表示（无数据增强）

| 注意力设置 | 动作表示 | Clean | Scene-OOD | Random |
|---|---|---:|---:|---:|
| IA(fastwam) | 相对动作 | 76.28 | 46.36 | 22.40 |
| Mutual | 相对动作 | 81.28 | 57.96 | 32.92 |
| IDM | 相对动作 | 83.56 | 58.08 | 27.56 |
| Mutual | 绝对相机系 | 84.88 | 61.12 | 30.68 |
| IDM | 绝对相机系 | 88.48 | 62.00 | 28.56 |

- Optional-IDM（同时训练）

| 推理时 | Clean | Scene-OOD | Random |
|---|---:|---:|---:|
| 只看首帧 | 73.44 | 48.44 | 23.40 |
| 动作看视频 | 81.96 | 57.04 | 28.04 |

- 动作专家初始化（有数据增强, 1000h ego 预训练）

| 初始化方式 | Clean | Scene-OOD | Random |
|---|---:|---:|---:|
| 随机初始化 | 90.28 | 83.92 | 54.12 |
| Wan2.2 权重初始化 | 89.56 | 83.20 | 51.52 |

- 多视角输入（IDM）

| 输入设置 | EgoPro 中间训练 | Clean | Scene-OOD | Random |
|---|---|---:|---:|---:|
| 单视角 | 无 | 88.48 | 62.00 | 28.56 |
| 多视角条件输入 | 无 | 90.56 | 59.52 | 29.08 |
| 多视角预测 | 无 | 89.84 | 56.28 | 26.16 |
| 多视角条件输入 | 有 | 90.28 | 61.20 | 30.68 |
| 多视角预测 | 有 | 88.72 | 58.80 | 27.36 |

- Goal 混合数据采样（真实机器人 hard-task 成功率）

| 采样方式 | 总数据量 | 成功率 |
|---|---:|---:|
| 固定总量，机器人/人类样本按比例采样 | 60.6k 小时 | 19% |
| 每批机器人与人类样本各半 | 60.6k 小时 | 27% |

- Goal 是否加入 Ego 数据（RoboTwin 零样本平均成功率）

| 预训练数据 | 平均成功率 |
|---|---:|
| 仅机器人数据 | 11.48% |
| 人机混合数据 | 13.94% |

- 样本效率实验

| Ego 预训练数据 | 每任务机器人示范数 | Clean | Random |
|---|---:|---:|---:|
| 无 Ego | 10 | 34.5% | — |
| 500 小时 | 10 | 44.2% | 4.1% |
| 5,000 小时 | 10 | 50.1% | 8.3% |

那他的 vanilla 和 goal 分别得做 idm 和 mutual 实验才有说服力吧（变量仅为 idm & mutual)，做了么，没做。

### 关于 goal

- 推理的时候需要用 GPT5.5 + GPT Image 2.5 生成目标图像... 非常的特权信息.
- goal condition 如何注入 wam? 就是直接在 token 维度拼接，加可学习的 goal embedding.

### IDM 变种

- video 前向一次还是多次，
- t=0.9 的 action 是看 t= 0.9 的 video 还是前向到终点的 video ?

本文 IDM 的 video 是前向多次，然后固定，action 只看终点的 video.

## praxis-1 (127)

纽约 runway | https://runway.com/research/praxis-1-video-pretraining-to-robot-control

本文表示 praxis 模型在世界模型中训练取得了收益，并将开放权重. 其架构略微不同于 mot, 其 AE 是 cross-attn VM 特征的.

然后他这个 attn map 很奇怪，看似是 LLM-like 的，和 jiarui battle 了一下，带历史的话效率会高很多. (1 个监督 vs L 个监督).

## RoboTTT (128)

```python
W = W0  # 本层、本条序列的初始快速权重

for t in range(seq_len):
    q, k, v = project_qkv(h2[:, t])       # 第 t 个时间步的表示
    W_next = W - lr * grad(loss(f_W(k), v))  # W_next = W_t，由 W_{t-1} 更新
    z[:, t] = f_W_next(q)                 # 用更新后的 W_t 读取
    W = W_next                            # 传给下一个时间步：W_{t+1} 的起点

h3 = h2 + tanh(alpha) * z
```

- yanwei 的SWAM
- 4d-hof
- lingbot-touch
