---
title: "papers batch 7: CE Pretraining"
date: 2026-07-08 14:29:34
tags: ["papers"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

## Qwen-RobotManip Technical Report: Alignment Unlocks Scale for Robotic Manipulation Foundation Models (51)

https://hjfy.top/arxiv/2606.17846

### dataset
1. OXE, DROID, RDT-1B,
2. MANO 转换 EGO
    - visual: SAM3 + Propainter + Mujoco
    - 手部高频噪声： Savitzky–G 滤波
    - 最优化找 base
    - 下采样
3. VL co-training
    - 思维链 ECoT 数据. infer 时动作专家会 cross-attend 这些表示.
### 架构
1. 不是 MoT 而是 cascaded，DiT 每层 cross-attend VLM 最后一层
    - 推理 4 步.
2. 表示: 29 * 2 + 预留 22
    - state 用 absolute. 6d rot.
    - action 用 relative EE pose, absolute joint. 3d 旋转向量

## Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization (52)
⭐️⭐️⭐️ 直接用 WM 编码 ICL | 👤 Robbyant, Jiaming Zhou, Yinghao Xu 和 Junwei Liang | [🌐](https://robbyant-research.github.io/Zero-WAM/) | [📃 2608.26103](https://hjfy.top/arxiv/2608.26103) | [✨](https://www.alphaxiv.org/abs/2608.26103) | [📂](https://github.com/robbyant-research/Zero-WAM)

![](https://raw.githubusercontent.com/robbyant-research/Zero-WAM/gh-pages/static/images/paper/framework-v1.0.webp)

结构和 lingbot-va 一致。ICL 通过直接 WM 编码 human video，并使用 height-axis RoPE offset 区分.

预训练 ICL 加入了 aux tasks (named FTP): 额外多预测几个 video chunk，从而避免模型忽略 ICL video.

此外，本文预训练采样时按任务而不是轨迹采样，避免同一任务权重过高. 仿真 ablation 表明，仅仅这一 sampling 策略就在未见任务上比 lingbotva 提了 20 个点.

> demo 是 inserting 任务.

## Learning to Act While Waiting: RL Finetuning of Generalist Robot Policies Under Inference Latency (53)

⭐️⭐️⭐️ 对于异步推理，改进 DSRL 让 AE 获得更多信息 | 👤 Siemens、UC Berkeley、Microsoft、ETH Zurich, Brian Zhu, Sergey Levine | [🌐](https://async-rl-intermediate-information.github.io/) | [📃 2608.23831](https://hjfy.top/arxiv/2608.23831) | [✨](https://www.alphaxiv.org/abs/2608.23831) | 📂 -

![](https://arxiv.org/html/2608.23831v2/body/figures/approach_diagram.png)

本文改进 DSRL[1]，1. 将异步中必然要执行[2]的 a 作为 DSRL 的条件，2. 如上图，在噪声真正给 AE 使用之前的新 obs/state 也可以拿来作为条件. 最后与 RTC 结合一下。实验基于 pi0 上改动，发现能提升 SR.

局限显然是假定 VLM-AE 模型且 VLM 无需噪声.

1. DSRL，输入 obs/state，输出噪声，交给冻结的 AE 去噪并执行得到 reward. 去噪视为黑盒，故解决了 diffusion 难以 RL 的问题.
2. 这个 a 的长度应该是一个人定的缓冲区长度，这个缓冲区只需覆盖 vla 最大可能延迟.

> 呃我印象中 pi0 MoT diffusion 没法拆成上面这两个时间段的吧.

# --- AI ---

## Qwen-RobotManip Technical Report: Alignment Unlocks Scale for Robotic Manipulation Foundation Models

GPT-5 通过统一状态动作表示、相机坐标系末端动作和行为上下文，将多机器人数据及人类视频扩展为可训练的通用 VLA 模型 | 👤 Qwen Team, Haoqi Yuan, Xiong-Hui Chen | [🌐](https://qwen.ai/blog?id=qwen-robotmanip) | [📃 2606.17846](https://hjfy.top/arxiv/2606.17846) | [✨](https://www.alphaxiv.org/abs/2606.17846) | [📂](https://github.com/QwenLM/Qwen-RobotManip)

![主模型架构图](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/Qwen-RobotManip-method.png)

论文针对不同机器人形态、关节动作、坐标系和数据采集方式不一致导致 VLA 难以从大规模数据泛化的问题，提出 Qwen-RobotManip。复现时使用 Qwen3.5-4B 作为视觉语言骨干，将每个机械臂编码为 29 维槽位并组成双臂 80 维状态动作向量，对缺失自由度使用二值掩码，再用相机坐标系末端位姿增量和 Camera Positional Encoding 对齐运动，接入 10 层 flow-matching DiT 动作专家，按机器人数据和视觉语言数据 9:1 联合预训练，最后在目标机器人数据上做动作监督微调。

人类视频部分通过 MANO 手部关键点重定向到平行夹爪，用 SAM3 和 ProPainter 移除人手，再用 MuJoCo 逆运动学渲染 15 种机器人形态，生成约 24,808 小时合成机器人示范。论文的主要结论是 OOD 场景比 LIBERO 或 RoboTwin 的 IID 测试更能区分预训练质量，相机坐标系末端动作有助于跨机器人迁移；局限是合成视频存在重定向和修复误差，OOD 评测仍以仿真为主，当前仓库也没有发布模型权重。

## DexUMI: Using Human Hand as the Universal Manipulation Interface for Dexterous Manipulation

[GPT-5] 用定制外骨骼记录可执行的机器人手关节动作，再将视频中的人手修复成目标机器人手 | 👤 Columbia University, Mengda Xu, Shuran Song | [🌐](https://dex-umi.github.io/) | [📃 2505.21864](https://hjfy.top/arxiv/2505.21864) | [✨](https://www.alphaxiv.org/abs/2505.21864) | [📂](https://github.com/real-stanford/DexUMI)

![DexUMI 系统总览](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/DexUMI-Teaser.png)

论文要解决人手示范与机器人手之间的关节运动和视觉差异。复现时先针对目标机器人手优化并打印可穿戴外骨骼，在关节处安装编码器并在指尖安装触觉传感器，固定腕部相机采集人手操作视频、关节角和触觉数据，再用 SAM2 分割人手与外骨骼并用光流修复背景，最后用 DINO-V2 提取视觉特征并训练 Diffusion Policy，输出机器人腕部相对动作和手指相对动作。

每种目标手都需要重新设计外骨骼，视觉修复仍有分割遗漏、模糊和光照不一致问题。相对手指动作比绝对动作更能容忍映射误差，触觉主要帮助被手遮挡的接触任务。

## DEXOP: A Device for Robotic Transfer of Dexterous Human Manipulation

[GPT-5] 用机械连杆让人手直接驱动带触觉传感器的被动机器人手，采集可直接训练机器人的示范数据 | 👤 MIT, Hao-Shu Fang, Pulkit Agrawal | [🌐](https://dex-op.github.io/) | [📃 2509.04441](https://hjfy.top/arxiv/2509.04441) | [✨](https://www.alphaxiv.org/abs/2509.04441) | 📂 -

![DEXOP 系统总览](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/DEXOP-overview.png)

论文提出一种被称为 perioperation 的采集方式。复现时制作与目标机器人手协同设计的被动外骨骼，通过连杆同步人手和被动机器人手，在手指、手掌和腕部安装视觉触觉传感器，采集双腕相机、触觉图像和关节状态，再用 ACT 进行行为克隆，输出机械臂关节增量和机器人手绝对关节位置。

DEXOP 的数据与真实机器人在运动学、视觉和触觉配置上高度一致，因此基本不需要视觉后处理。当前系统仍受外骨骼制造误差、标定误差和机器人手自由度限制，实验中加入少量遥操作数据用于校准。

## WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time
[indexed] 通过自监督视频预测将人类视频吸收到冻结 WAM 的轻量级记忆中，实现测试时训练和策略引导 | 👤 Peking University, Yusen Feng, He Wang | [🌐]- | [📃 2607.06988](https://hjfy.top/arxiv/2607.06988) | [✨](https://www.alphaxiv.org/abs/2607.06988) | [📂]- |

支持训练时录制 ego 视频引导 wam 到新任务或用户偏好，不是海量 kv 而是 fast-weight MLP.

see also: https://github.com/ImChong/Robotics_Notebooks/blob/main/wiki/entities/paper-wam-ttt-human-video-test-time-steering.md

to read:

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
