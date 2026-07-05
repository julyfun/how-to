---
title: "papers batch 5"
date: 2026-06-30 20:49:49
tags: ["papers"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

## Behavior Prompting Policy: Demonstrations as Prompts for Manipulation (35)
⭐️⭐️⭐️ 将一次性演示作为 in-context 任务提示 | 👤 Stanford, Austin Patel, Shuran Song | [🦾](https://behavior-prompting.github.io) | [📃 2606.30457](https://hjfy.top/arxiv/2606.30457) | [✨](https://www.alphaxiv.org/abs/2606.30457) | [💻](https://github.com/real-stanford/behavior_prompting) |

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20260705173413639.png)

Recap: 众所周知，diffusion policy 使用 obs_encoder(obs) 获得 global_cond 并直接 FiLM 调制 UNet 中的多层 x.

本文仅需在上述 obs_encoder 内部 cross-attn 一条演示下采样得到的 `[enc(rgb), mlp(propio), mlp(action)]`，实现了 1. infer-time 指定折叠方式（训练时见过多种折叠方式）; 2. infer-time 指定绘制数字（训练时未见过的数字）。实验发现需要训练数据多样性高时才能很好地 steering，当然，还是无法跨 action primitive 的.

这篇文章 abs:
1. We study Bahavior Propmting.
2. To enable this, we present contributions in algo, data and evaluation.
3. For algo, we.. For data we identify that .. is the primer driver **and introduce iPhUMI**.

## SOE: Sample-Efficient Robot Policy Self-Improvement via On-Manifold Exploration (36)
⭐️⭐️⭐️ 在更低维度的 observation latent 上随机扰动来让 Policy 探索 | 👤 上海交通大学, Yang Jin, Chuan Wen、Cewu Lu |
[🦾](https://ericjin2002.github.io/SOE) | [📃 2509.19292](https://hjfy.top/arxiv/2509.19292) | [✨](https://www.alphaxiv.org/abs/2509.19292) | - |

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20260705172947006.png)

将 DP 的 observation z 压缩到更低维度的 latent 训练编解码[1]，随后 infer 时对实际 observation z 编码 -> 扰动 -> 解码来生成新的且符合 on-manifold z，从而让 action 能安全高效地 RFT 探索[2].

1. latent 编解码的训练目标为 `max_θ I(A; Z) - β I(Z; O)`（互信息在代码中通过 KL 散度实现）.
2. RFT 探索很简单，就是生成多条候选轨迹，通过执行结果或人工筛选保留加入数据集，本质上是纯 IL.

## FTP-1: A Generalist Foundation Tactile Policy Across Tactile Sensors for Contact-Rich Manipulation
[Gemini 3.1 Pro] FTP-1 将异构触觉信号统一编码并交由独立的触觉专家处理，首次实现了跨传感器泛化的通用触觉基座策略 | 👤 Tsinghua University, Chengbo
Yuan, Yang Gao | [🦾](https://ftp1-policy.github.io/) | [📃 2606.13102](https://hjfy.top/arxiv/2606.13102) |
[✨](https://www.alphaxiv.org/abs/2606.13102) | [💻](-) |

FTP-1 基于 Pi0.5 架构将多模态触觉信号按功能区编码为统一的形态感知 token，这些 token 会直接交由独立的触觉专家处理。负责输出动作的流匹配专家通过交叉注
意力融合这些触觉特征，大规模预训练后不仅在接触丰富任务中表现更优，甚至能直接泛化到未见过的触觉硬件。

FTP-1 当前主要受限于触觉数据规模，且面临新机器人的动作空间适配成本较高的问题，同时触觉 token 化仍依赖于人工设计的功能区映射规则。
