---
title: "papers batch 7"
date: 2026-07-08 14:29:34
tags: ["papers"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

to read.

## Why Does Action Chunking Improve Behavioral Cloning Performance in Robotic Control?
[Gemini 3.1 Pro] 发现 action chunking 的有效性主要源于隐式集成效应，因此提出将其显式实例化为随机延迟策略集成。 | 👤 Politecnico di Milano, Filippo Lazzati, Sergey Levine | [🌐](https://action-chunking.github.io) | [📃 2608.02547](https://hjfy.top/arxiv/2608.02547) | [✨](https://www.alphaxiv.org/abs/2608.02547) | [📂-]() |

本文旨在解释 action chunking 为何在模仿学习中有效，推翻了时间一致性和表征学习等传统解释假设。作者发现动作分块的性能优势主要来自预测多样化时间关系所带来的隐式集成效应。复现这篇论文的方法是独立训练多个具有不同观察延迟步数的单步预测策略，并在推理阶段对它们的动作输出取平均，这样就能达到甚至超越原版动作分块的性能。

作者在讨论中得出一个有趣结论：当机器人控制频率较高（如 50-60Hz）时延迟策略将无法匹敌动作分块的性能。这可能与人类真实反应频率较低有关，说明在此种高频设定下动作序列的时间一致性仍然不可或缺。

## UniVLA: Learning to Act Anywhere with Task-centric Latent Actions
[Gemini 3.1 Pro] 通过潜在动作模型从视频中提取以任务为中心的潜在动作并在 DINO 特征空间中结合语言指令进行泛化策略训练 | 👤 The University of Hong Kong, Qingwen Bu, Hongyang Li | - | [📃 2505.06111](https://hjfy.top/arxiv/2505.06111) | [✨](https://www.alphaxiv.org/abs/2505.06111) | [📂](https://github.com/OpenDriveLab/UniVLA) |

提出了用于跨具身学习的框架 UniVLA。该方法不直接依赖带动作标注的数据，而是通过潜在动作模型从各种视频（包括人类视频）中提取以任务为中心的潜在动作表示。为了过滤任务无关的动态，它在 DINO 特征空间内结合语言指令建立潜在动作模型，预训练后的通用策略只需通过轻量的潜在动作解码器即可高效部署到各种异构机器人上。

## Video Language Planning
[Gemini 3.1 Pro] 提出结合 VLM 和文本到视频模型进行树搜索的 VLP 算法来实现长视距机器人视觉动作规划 | MIT，Yilun Du，Yilun Du
https://video-language-planning.github.io/ | https://hjfy.top/arxiv/2310.10625 | https://www.alphaxiv.org/abs/2310.10625 |
https://github.com/video-language-planning/vlp_code
|-|-|-|-|-|

VLP 通过前向树搜索结合两种模型，先由 VLM 生成候选动作的文本指令并利用视频模型预测对应的执行短视频，最后再由 VLM
充当启发式函数来评估以找出最优的长视距视觉执行计划。

纯视觉生成和启发式评估缺乏显式的物理约束，生成的计划偶尔会出现物体瞬移或消失等物理不一致错误。

## GR00T N1: An Open Foundation Model for Generalist Humanoid Robots
[Gemini 3.1 Pro] GR00T N1 采用双系统架构并混合真实、合成与人类视频数据进行预训练 | 👤 NVIDIA, Scott Reed, Linxi Fan | [🌐](https://developer.nvidia.com/isaac/gr00t) | [📃 2503.14734](https://hjfy.top/arxiv/2503.14734) | [✨](https://www.alphaxiv.org/abs/2503.14734) | [📂](https://github.com/NVlabs/GR00T) |

GR00T N1 包含作为系统二的 Eagle-2 视觉语言模型和作为系统一的扩散 Transformer，两者通过交叉注意力机制结合，在包含人类视频、神经生成轨迹和真实机器人数据的异构数据集上联合端到端训练。

实验表明利用视频生成模型合成的神经轨迹进行协同训练，可以显著提升模型在真实世界小样本微调时的表现。
