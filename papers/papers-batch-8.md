---
title: "papers batch 8"
date: 2026-08-04 14:12:00
tags: ["papers"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

# --- AI ---

## RoboTTT: Context Scaling for Robot Policies
[GPT-5] 用测试时更新的 fast weights 压缩 8K 步轨迹并保持固定推理成本 | 👤 NVIDIA、Stanford, Yunfan Jiang, Linxi “Jim” Fan | [🌐](https://research.nvidia.com/labs/gear/robottt/) | [📃 2607.15275](https://hjfy.top/arxiv/2607.15275) | [✨](https://www.alphaxiv.org/abs/2607.15275) | 📂 -

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/robotttt-model-arch.png)

RoboTTT 基于 GR00T N1.7，在 16 个 action DiT layer 的 attention 后各接一个 TTT layer。每层用两层 MLP 作为 fast model 并以自监督损失学习 K→V，再用更新后的 MLP 查询 Q。state、noisy action 和 16 个 register token 跨时间进入 TTT，register token 负责携带 VLM 信息。推理时 slow weights 冻结并将 fast weights 持续传给下一时刻。

训练时为每个 action chunk 独立采样 flow-matching 噪声并使用 TBPTT，避免显存随 8K 步历史增长。预训练使用 16 张 GB200 跑 30K steps，当前未发布代码。

## Faster-WAM: Efficient Inference-Time Future Conditioning for Robust World Action Models
[GPT-5] 保留一次生成的未来视觉表示并在部分 action 层复用，兼顾 OOD 鲁棒性和推理速度 | 👤 华中科技大学, Weiheng Zhao, Xinggang Wang | 🌐 - | [📃 2608.04404](https://hjfy.top/arxiv/2608.04404) | [✨](https://www.alphaxiv.org/abs/2608.04404) | [📂](https://github.com/hustvl/FasterWAM)

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/fasterwam-2608.04404-framework.png)

Faster-WAM 基于 Wan2.2-TI2V-5B，先编码当前观测并用高斯噪声初始化未来视频 token。video expert 仅运行一次并缓存不同深度的 future KV，Interval KV-Fusion 聚合相邻层的 KV。SparseMoT 只在选定的 action stage 注入缓存，其余层单独更新 action token。该缓存供 10 次 action denoising 复用并输出 32 步动作。

推理耗时 252.95 ms 是 Joint-WAM 的 2.21 倍速，但仍需运行 5B video expert 且交互层由人工指定。额外执行未来视频去噪没有收益。与 2608.02365 压缩 action DiT 至一层不同，这篇主要减少未来视觉表示的重复计算。

## Faster-WAM: Do World Action Models Need Deep Action Modules?
[GPT-5] 将 30 层 WAM action DiT 缩成单层并复用视频骨干各层 KV | 👤 Huawei Noah’s Ark Lab, Liheng Ma, Rui Heng Yang | 🌐 - | [📃 2608.02365](https://hjfy.top/arxiv/2608.02365) | [✨](https://www.alphaxiv.org/abs/2608.02365) | 📂 -

![Faster-WAM 架构](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/fasterwam_architecture.svg)

Faster-WAM 使用 30 层 Wan2.2-TI2V-5B 作为视频骨干并缓存每层 KV。KV-Fusion 先把这些 KV 投影到 action feature space，再通过每个 attention head 的可学习权重融合不同视频层。模型随后撤销 video KV 的 3D RoPE 并改用 action query 的 1D RoPE，最后让单层 action DiT 通过 flow matching 生成 32 步 action chunk。训练时联合更新视频骨干、KV-Fusion 和 action head。

它只减少 action 侧计算，完整视频骨干仍需前向运行。实验只有 LIBERO、LIBERO-Plus 和 RoboTwin 2.0 仿真，没有真机验证；论文报告单次 action chunk 推理为 66.5 ms。

## BridgeVLA++: A Data-Efficient, Generalizable, and Memory-Augmented Vision-Language-Action Framework for 3D Manipulation
[GPT-5] 在 BridgeVLA 的热图动作预测上加入时空记忆，使策略能利用历史步骤和被遮挡的早期几何 | 👤 中国科学院自动化研究所, Peiyan Li, Yan Huang | [🌐](https://bridgevla-plus.github.io/) | [📃 2608.05042](https://hjfy.top/arxiv/2608.05042) | [✨](https://www.alphaxiv.org/abs/2608.05042) | [📂](https://github.com/BridgeVLA/BridgeVLA)

![BridgeVLA++ 架构](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/bridgevla_plus_architecture.png)

BridgeVLA 先把点云渲染成三个正交视图并让 VLM 预测二维热图，再将热图峰值反投影成三维 waypoint。BridgeVLA++ 在 coarse stage 加入初始帧、最近两个 keyframe 和筛选后的 subgoal keyframe token，用于判断下一步做什么。在 fine stage 保存初始点云并按当前 waypoint 重新裁剪渲染，用较少遮挡的几何辅助精确定位。训练时还用二分类损失监督 subgoal keyframe selector。

历史帧以编码后的视觉 token 缓存，空间记忆则在每个决策步重新渲染初始点云。新增记忆约占 2.7 亿参数并增加推理延迟，subgoal selector 仍依赖人工分段标注。

## DROID: A Large-Scale In-the-Wild Robot Manipulation Dataset
[GPT-5] 构建统一硬件和采集协议的多场景机器人操作数据集，并验证其对策略泛化的帮助 | 👤 Stanford University, Alexander Khazatsky, Chelsea Finn | [🌐](https://droid-dataset.github.io/) | [📃 2403.12945](https://hjfy.top/arxiv/2403.12945) | [✨](https://www.alphaxiv.org/abs/2403.12945) | [📂](https://github.com/droid-dataset/droid_policy_learning)

![DROID 机器人平台](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/droid_setup.png)

DROID 通过 18 台 Franka Panda、两台可调 Zed 2 立体相机、腕部 Zed Mini 和 Oculus Quest 2 遥操作装置，在 13 个机构的 564 个场景采集 7.6 万条示范。每条数据包含多视角图像、深度、动作、语言指令和相机标定。

若要复现，则搭建同一硬件平台，在新场景中标定相机并随机抽取任务让操作者完成，再用现有 Diffusion Policy 等方法训练，比较加入 DROID 前后的 6 个任务和 4 个地点的常规及分布外表现。

DROID 的贡献主要是数据规模、场景多样性和采集规范，不是新的策略结构。数据统一使用 Franka 形态，且部分自动相机标定在杂乱或视角重叠很少的场景中仍会失败。

## CUPID: Curating Data your Robot Loves with Influence Functions
[GPT-5] 用 influence functions 估计每条机器人示范对闭环回报的影响并据此筛选训练数据，支持过滤旧数据和选择新轨迹 | 👤 Stanford University, Christopher Agia, Jeannette Bohg | [🌐](https://cupid-curation.github.io/) | [📃 2506.19121](https://hjfy.top/arxiv/2506.19121) | [✨](https://www.alphaxiv.org/abs/2506.19121) | [📂](https://github.com/agiachris/cupid)

![CUPID 方法图](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/cupid_method.png)

CUPID 先用行为克隆训练 diffusion policy，再收集闭环 rollout 及回报。它用 TRAK 等方法计算训练状态动作对 rollout 动作的 influence，再按 rollout 回报加权汇总成每条示范的 performance influence。过滤任务删除负面影响最大的示范，选择任务保留正面影响最大的示范，最后重新训练策略。代码仓库提供训练、评估、influence 计算、生成筛选配置和重训四阶段流程。

实验覆盖 RoboMimic 和 Franka 真机任务，CUPID 能识别低质量示范、分布偏移下的脆弱策略和背景诱导的伪相关。主要限制是 influence 计算成本接近一次策略训练，rollout 数量过少时 REINFORCE 风格估计方差较大。

## ATHENA: Accelerated Multi-Task Heterogeneous Influence Functions for Robot Data Curation

[GPT-5] 用闭环 rollout 的 influence function 给多任务 VLA 示范排序，再保留高价值子集进行联合微调 | 👤 Tongji University, Tao Xu, Yong-Lu Li | [🌐](https://sii-quantum.github.io/ATHENA.github.io/) | [📃 2606.16208](https://hjfy.top/arxiv/2606.16208) | [✨](https://www.alphaxiv.org/abs/2606.16208) | 📂 -

![ATHENA 系统图](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/ATHENA-system.png)

论文要把 CUPID 一类 influence function 数据筛选扩展到 3.3B 参数的多任务 VLA。复现时先微调 $\pi_0$ 并执行带成功或失败标签的闭环 rollout；对训练样本计算 flow-matching loss gradient，对 rollout action 计算 square-flow surrogate gradient；利用线性层梯度 $\delta x^\top$ 的 Kronecker 结构分别投影 activation 和 backpropagated error，避免构造完整参数梯度；再对投影梯度矩阵做 rank-$r$ Random Truncated Approximation，用低维近似代替稠密 Hessian inversion，最后聚合 timestep influence 得到每条 demonstration 的分数。

多任务筛选使用 Multitask Influence Interaction，分别计算 demonstration 对自身任务的 local influence 和对其他任务的 cross-task influence，将二者按任务内排名归一化后相乘。若直接使用全局 influence 排名，梯度较强的任务会占据保留数据，部分任务可能几乎被删空。

ATHENA 面向 VLA fine-tuning data curation，没有验证预训练数据筛选。方法仍需要为每个任务执行真实机器人 rollout，任务数量扩大后数据采集成本较高；低秩 Hessian 和一阶 influence 也只是局部近似。论文在 RoboTwin 2.0 的 50 个任务及 6 个真机任务上验证，使用一半到三分之二的数据可达到或超过全量联合微调。

## RL-100: Performant Robotic Manipulation with Real-World Reinforcement Learning

[GPT-5] 从 Diffusion Policy 开始做迭代离线和在线 PPO，再用一致性蒸馏得到单步控制器 | 👤 Shanghai Qizhi Institute, Kun Lei, Huazhe Xu | [🌐](https://lei-kun.github.io/RL-100/) | [📃 2510.14830](https://hjfy.top/arxiv/2510.14830) | [✨](https://www.alphaxiv.org/abs/2510.14830) | [📂](https://github.com/Lei-Kun/RL-100)

![RL-100 训练流程](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/RL-100-pipeline.png)

论文要把依赖人类示范的 Diffusion Policy 继续优化到稳定真机部署。复现时先用 teleop 数据训练 Diffusion Policy，再在每个环境动作内部的 K 个 denoising step 上共享同一个 advantage 并计算 clipped PPO loss；离线阶段用 IQL 训练 Q 和 V，以 AM-Q OPE 只接受估计性能提升的 policy，部署新 policy 采集 rollout 后合并回数据集并重新做 imitation learning，最后用 GAE 做少量 on-policy fine-tuning。训练期间同步加入 consistency distillation loss，将多步 diffusion teacher 压成单步 consistency policy。

主要代价是每个任务仍需明确 reward、真实机器人 rollout、reset 和安全监控。100% 来自论文任务设定和有限评测次数，不能直接推为开放环境中的通用可靠性；单步 consistency policy 对噪声和动作不连续更敏感。

## Robust-WAM: Bridging Generative Pretraining and Semantic Foresight in World-Action Models

[GPT-5] 保留预训练 WAM 的视频生成路径，用未来帧的 DINOv3 语义监督动作流 | 👤 The Hong Kong University of Science and Technology (Guangzhou), Haodong Yan, Haoang Li | [🌐](https://haodong-yan.github.io/robust-wam-project-page/) | [📃 2608.05903](https://hjfy.top/arxiv/2608.05903) | [✨](https://www.alphaxiv.org/abs/2608.05903) | [📂](https://github.com/Haodong-Yan/Robust-WAM-release)

![Robust-WAM 方法图](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/Robust-WAM-method.png)

论文针对 VAE latent 重像素细节导致 WAM 在光照等视觉变化下动作不稳的问题。复现时保留预训练 WAM 的 VAE、video DiT 和 action DiT，在每个未来时间步和相机视角加入一个 learnable query token，并复用对应 action token 的 positional encoding；训练时用 frozen DINOv3 ViT-B/16 提取未来真值帧 CLS feature，经 linear head 将 query output 与其做 cosine alignment，原视频生成和动作预测 loss 保持不变。推理时移除 DINOv3 和 alignment head，只保留 query token。

方法已接入 GE-Act 和 FastWAM，也在 LingBot-VA 上评测。LIBERO-Plus、RoboTwin 随机扰动和真机未知光照均有改善；常规环境表现没有下降。新增参数约 0.016M，推理延迟约增加 4%。目前只发布 GE-Act checkpoint；FastWAM、LingBot-VA checkpoint 和真机部署指南尚未发布。

## Transformer Transformer: A Unified Model for Motion-Conditioned Robot Co-design
[Gemini 3.1 Pro] 训练基于 RoboTokens 的扩散 Transformer，利用自身预测的动力学奖励梯度引导形态生成 | 👤 Stanford University, Huy Ha, Shuran Song | [🌐](https://transformer-transformer.github.io) | [📃 2607.25798](https://hjfy.top/arxiv/2607.25798) | [✨](https://www.alphaxiv.org/abs/2607.25798) | [📂]- |

为了解决特定任务的机器人形态设计问题，本文将机器人的物理结构和状态动作统一表示为 RoboTokens 并训练了一个扩散 Transformer。该模型通过掩码不同的 token 来同时学习形态生成和跨形态控制。在推理阶段，模型利用自身预测的完整动力学轨迹来计算奖励梯度，并用此梯度引导形态 token 的扩散去噪，从而生成针对目标轨迹优化的机器人设计。

实验发现增加推理时间的并行采样能提升设计质量，但计算收益会在一分钟左右遇到瓶颈。此外当前方法仅支持基于图元的几何体表示，尚未支持任意网格或可变形物体。

## Explicit Kinematic Guidance from Analytic Concepts for Vision-Language-Action Models
[Gemini 3.1 Pro] 引入物理概念专家先提取 3D 信息再微调 VLA | 👤 SJTU, Mingyang Sun, Jianhua Sun | [🌐]- | [📃 2607.26513](https://hjfy.top/arxiv/2607.26513) | [✨](https://www.alphaxiv.org/abs/2607.26513) | [📂]-

现有 VLA 模型依赖 2D 输入导致缺乏 3D 物理空间感知，本文引入一个概念专家模块，先用视觉基础模型估计物体的运动和结构参数，随后在推理时动态跟踪这些参数以对齐观察，并在微调时作为空间引导和密集奖励训练 VLA。

实验显示该结构化引导能提高监督学习和强化学习操作成功率。

## HiFi-UMI: Learning Deployable Manipulation Policies from High-Fidelity UMI Data Alone
[Gemini 3.1 Pro] 采集高保真数据以实现零真机数据的 VLA 部署 | 👤 Simple AI, Yuteng Wei, Xiaofei Li | [🌐]- | [📃 2607.25895](https://hjfy.top/arxiv/2607.25895) | [✨](https://www.alphaxiv.org/abs/2607.25895) | [📂]-

现用便携 UMI 采集的数据保真度低且需要混入真实机器人数据微调，本文设计了带头戴离线 SLAM 和 200 度双广角相机的微秒级同步采集系统，录制了两千小时数据，仅用这些数据后训的策略直接部署在真机上就能匹配同分布遥操的成功率。

## A Causality-aware Infer-diagnose-refine Framework for Test-time Modality Adaptation in VLA Models
[Gemini 3.1 Pro] 测试时动态调整视觉输入权重来细化 VLA 动作 | 👤 Tsinghua, Haoyu Zhang, Fan Li | [🌐]- | [📃 2607.25516](https://hjfy.top/arxiv/2607.25516) | [✨](https://www.alphaxiv.org/abs/2607.25516) | [📂]-

机器人操作在不同阶段对视觉观察的依赖程度不同，本文提出推断-诊断-细化框架，先在正常和视觉掩码两种反事实情况下推断动作，借此量化视觉特征的因果权重，最后用门控残差网络在免训练下细化动作预测。

## FELT: Generating Tactile Signals from Vision for Visuo-Tactile Manipulation
[Gemini 3.1 Pro] 从 RGB 图像生成双指不对称触觉特征辅助策略学习 | 👤 Tsinghua, Zinan Li, Daniel Seita | [🌐](https://felt-tactile.github.io/.) | [📃 2607.20683](https://hjfy.top/arxiv/2607.20683) | [✨](https://www.alphaxiv.org/abs/2607.20683) | [📂]-

触觉传感器脆弱且收集数据困难，本文利用冻结的视觉编码器和轻量查询解码器，将左右面板分两支独立解码，直接从 RGB 图像单向生成双指的高保真触觉特征。

生成的特征在推理时无需实体传感器即可提升接触任务成功率。

## WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning
[Gemini 3.1 Pro] 评价器兼顾状态预测和奖励估计捕捉时间动态 | 👤 Fudan, Senyu Fei, Xipeng Qiu | [🌐]- | [📃 2607.29613](https://hjfy.top/arxiv/2607.29613) | [✨](https://www.alphaxiv.org/abs/2607.29613) | [📂]-

传统 VLA 强化学习的评价器单帧输入难以捕捉操作中的跨时间动态，本文将轻量级 LeJEPA 架构引入作为评价器 WCM，让其同时预测未来潜在状态和估计回报，从而解决状态近似不足的问题，并兼容 Pi0 和 OpenVLA 强化训练。

## FA-RDP: A Frequency-Adaptive Reactive Diffusion Policy for Contact-Rich Manipulation
[GPT-5] 接触前保留多模态 diffusion 采样并在接触后切到单步高频力控 | 👤 上海交通大学, Lifeng Zhuo, Chuan Wen | [🌐](https://fa-rdp.github.io/) | [📃 2607.28596](https://hjfy.top/arxiv/2607.28596) | [✨](https://www.alphaxiv.org/abs/2607.28596) | [📂](https://github.com/zhuolifeng/FA-RDP)

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/fa-rdp-method.png)

FA-RDP 用一个视觉和力 Transformer 同时预测 10 Hz 的 16 步 chunk 与 30 Hz 的 48 步 chunk，两者都覆盖 1.6 秒。接触前 indicator 检测到动作仍有多种可行路径时，使用低频多步 DDIM；接触后动作不确定性下降时，改用高频单步模型并每步刷新 force token。高频模型通过 MCD 直接预测 clean action chunk，再由 DDPM 公式换算噪声并保留原始残差监督。

indicator 的监督来自冻结低频策略对同一观测采样 8 次后的平均 action 误差，并非人工接触阶段标签。评测只有三项 Flexiv 真机任务，每项 60 条示范。

## FA-RDP: A Frequency-Adaptive Reactive Diffusion Policy for Contact-Rich Manipulation
[Gemini 3.1 Pro] 接触任务中自适应切换扩散策略的推理频率 | 👤 SJTU, Lifeng Zhuo, Han Xue | [🌐]- | [📃 2607.28596](https://hjfy.top/arxiv/2607.28596) | [✨](https://www.alphaxiv.org/abs/2607.28596) | [📂]-

丰富接触任务在接触前需要低频多步采样以保持多模态，而接触后需要高频以反应反馈力，本文提出了频率自适应的反应式扩散策略，利用视觉-力混合 Transformer 根据接触状态动态预测高频和低频动作块。

## Hybrid Impedance-Admittance Control with Multi-Link Aerial Robot for Contact-Rich Surface Sliding Task
[Gemini 3.1 Pro] 为多连杆空中机器人设计混合阻抗-导纳控制 | 👤 Tsinghua, Zicheng Luo, Jinjie Li | [🌐]- | [📃 2608.01800](https://hjfy.top/arxiv/2608.01800) | [✨](https://www.alphaxiv.org/abs/2608.01800) | [📂]-

为了解决多连杆空中机器人在表面滑动时的接触稳定性问题，本文结合阻抗控制和导纳控制策略，使机器人可以在自由飞行和表面交互模式之间灵活稳定切换。

## The Gate, Not the Cache: Gate Provenance Bounds the Closed-Loop Reliability of Training-Free VLA Token Skipping
[Gemini 3.1 Pro] 指出决定免训练 Token 跳过机制可靠性的是门控信号来源 | 👤 UCB, Qi Luo, Hao Zhao | [🌐]- | [📃 2608.00391](https://hjfy.top/arxiv/2608.00391) | [✨](https://www.alphaxiv.org/abs/2608.00391) | [📂]-

为了在降低 VLA 推理延迟的同时保障控制可靠性，本文深入探究了免训练 Token 跳过机制的闭环表现，发现系统鲁棒性的关键边界由门控信号的计算来源和规律决定，而非缓存本身。

## Event-Based Upper-Body Humanoid Teleoperation Under Challenging Illumination
[Gemini 3.1 Pro] 融合事件相机信息提升人形机器人在极端光照下的遥操表现 | 👤 NVIDIA, Haoyu Fu, Chengze Li | [🌐]- | [📃 2607.29227](https://hjfy.top/arxiv/2607.29227) | [✨](https://www.alphaxiv.org/abs/2607.29227) | [📂]-

面对传统视觉遥操在强光或逆光下容易跟丢的问题，本文引入事件相机捕捉高动态范围光照特征，融合 RGB 信息提取上半身运动学参数，在恶劣光照下也实现了稳定的人形机器人遥操作。

## SM4RT: Learning Structured Motion Geometry for 4D Reconstruction
[Gemini 3.1 Pro] 将场景运动分解为 SE(3) 基重构 4D 运动几何 | 👤 Tsinghua, Yiming Yang, Li Yi | [🌐]- | [📃 2607.22534](https://hjfy.top/arxiv/2607.22534) | [✨](https://www.alphaxiv.org/abs/2607.22534) | [📂]-

本文提出结构化运动 4D 重构 Transformer，将密集的场景运动分解为由时间序列组成的 6D SE(3) 扭曲运动基，同物体的像素共享同一组刚体运动轨迹权重，从单目 RGB 视频直接端到端推断出 3D 几何和运动结构。

## Temporal Policy: History-Initialized Action Generation for Robotic Learning from Demonstration
[Gemini 3.1 Pro] 从机器人历史状态初始化生成流匹配降低推理延迟 | 👤 NVIDIA, Dylan Miller, Martin Jagersand | [🌐](https://github.com/dmiller12/TemporalPolicy.) | [📃 2607.29482](https://hjfy.top/arxiv/2607.29482) | [✨](https://www.alphaxiv.org/abs/2607.29482) | [📂](https://github.com/dmiller12/TemporalPolicy.)

生成式策略在示教学习中采样开销大，本文将动作生成建模为时间耦合传输问题，不从纯噪声而是从近期历史状态初始化流匹配过程，使得需要拟合的向量场更平直，从而大幅降低推理延迟并保持成功率。

## When Does Legacy Data Start to Help? Emergent Transfer in Cross-Configuration Robot Learning
[Gemini 3.1 Pro] 研究跨硬件机器人学习中历史数据的有效阈值 | 👤 Tsinghua, Tao Wang, Yang Gao | [🌐]- | [📃 2607.25593](https://hjfy.top/arxiv/2607.25593) | [✨](https://www.alphaxiv.org/abs/2607.25593) | [📂]-

当机器人硬件升级后复用旧配置数据往往不会立刻见效，本文通过测试发现存在一个转换临界点，只有新配置数据积累到最低任务能力要求后，与旧数据联合训练才会产生收益并迎来成功率急速增长。

## Ordered Action Tokens for Visuomotor Policy Learning
[Gemini 3.1 Pro] 按有序重要性量化连续动作为离散 Token 以灵活推理 | 👤 Tsinghua, Chaoqi Liu, Yilun Du | [🌐]- | [📃 2607.21670](https://hjfy.top/arxiv/2607.21670) | [✨](https://www.alphaxiv.org/abs/2607.21670) | [📂]-

现有的动作标记化方法缺乏结构性，本文设计了有序动作标记器 OAT，用 Transformer 将动作块离散为有序序列，前段 Token 包含粗略控制信息而后续 Token 补充残差细节，从而允许在推理时根据性能权衡灵活截断动作保真度。

## Learning Panorama-Aware VLA for Mobile Manipulation with Whole-Body Teleoperation
[Gemini 3.1 Pro] 采集带移动底盘的全景数据训练具有全局空间感知的移动 VLA | 👤 Beihang, Donglin Yang, Si Liu | [🌐]- | [📃 2608.02257](https://hjfy.top/arxiv/2608.02257) | [✨](https://www.alphaxiv.org/abs/2608.02257) | [📂]-

移动操作需要底盘与机械臂协同以及全局空间理解，本文开发了一套基于单 VR 接口的全身遥操系统采集多模态数据集，并利用全景编码器融合局部观察与机器人状态输出联合动作，解决了传统局部视角容易丢失目标的问题。

## FIRMGrasp: A Friction-Informed Risk Margin for Robust Grasp Synthesis
[Gemini 3.1 Pro] 考虑摩擦系数分布不确定性进行风险调整的抓取综合评价 | 👤 Boston University, Clinton Enwerem, Calin Belta | [🌐]- | [📃 2607.25049](https://hjfy.top/arxiv/2607.25049) | [✨](https://www.alphaxiv.org/abs/2607.25049) | [📂]-

经典抓取质量指标通常假设单一摩擦系数导致预测力闭合易失效，本文提出了基于条件风险价值的摩擦波动感知抓取指标 FIRMGrasp，它计算恶劣摩擦尾部分布折现后的力闭合裕度，从而准确筛选出被标称指标误判为高质量的高风险抓取。
