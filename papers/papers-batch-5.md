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

**图像型 (如 GelSight)**
- Tactile Image -> [Sensor-specific ViT] -> feature maps -> [Shared T3 Transformer] -> CLS token -> [LayerNorm] -> [MLP] -> Tactile Token

**阵列型 (如 Contactile)**
- Tactile Array -> [Fourier Encoding] -> expanded signal -> [3-layer CNN] -> spatial features -> [MLP] -> [LayerNorm] -> [MLP] -> Tactile Token

**状态型 (如 力/力矩)**
- Tactile State -> [Fourier Encoding] -> expanded signal -> [3-layer MLP] -> [LayerNorm] -> [MLP] -> Tactile Token

**空间对齐与聚合**
- Tactile Tokens -> [+ Shared Functional Area Embedding] -> MTTS Tokens -> [Tactile Expert]

## VGGT: Visual Geometry Grounded Transformer
[Gemini 3.1 Pro] VGGT 使用交替注意力的前向 Transformer，在单次前向传播中直接预测所有关键的 3D 场景属性 | 👤 牛津大学,Jianyuan Wang, David Novotny | [🦾](https://vgg-t.github.io/) | [📃2503.11651](https://hjfy.top/arxiv/2503.11651) |[✨](https://www.alphaxiv.org/abs/2503.11651) |[💻](https://github.com/facebookresearch/vggt) |

VGGT 首先使用 DINO 将输入图像转换为 token 并附加相机 token，接着交替使用帧内
自注意力和全局自注意力进行特征提取。模型通过专门的预测头直接输出相机参数、深
度图、点云图和特征图，从而消除了传统方法中耗时的几何后处理优化步骤。相比于
DUSt3R 只能处理图像对的情况，VGGT 可以同时处理数百张图像。

当前模型不支持鱼眼或全景图像，且在极端旋转或剧烈非刚性形变场景下性能会下降。

## UniDex: A Robot Foundation Suite for Universal Dexterous Hand Control from Egocentric Human Videos
[Gemini 3.1 Pro] UniDex 将人类视频重定向为机器人轨迹并提出统一动作空间 FAAS，训练出支持多种灵巧手的 3D VLA 模型。FTP 使用之. | 👤 清华大学, Gu Zhang, Huazhe Xu | [🦾](https://unidex-ai.github.io/) | [📃 2603.22264](https://hjfy.top/arxiv/2603.22264) | [✨](https://www.alphaxiv.org/abs/2603.22264) | [💻](https://github.com/unidex-ai/UniDex) |

UniDex 首先通过带人工微调的逆运动学将人类视频重定向为机器人轨迹，接着提出按功
能对齐关节的统一动作空间 FAAS，最后使用 Uni3D 编码单视角点云并结合 FAAS
动作空间，通过流匹配目标训练出支持多种灵巧手的 VLA 模型。

当前方法没有利用无动作标签的大规模第一人称视频，且重定向过程仍需要一定的人工
干预。
