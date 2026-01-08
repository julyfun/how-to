---
title: "Papers"
date: 2025-11-07 04:28:30
tags: [""]
author: "julyfun-4070s-ubuntu2204"
os: "Linux julyfun-4070s-ubuntu 6.8.0-84-generic #84~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Tue Sep  9 14:29:36 UTC 2 x86_64 x86_64 x86_64 GNU/Linux"
assume-you-know: [computer]
confidence: 2
---

## 11/26
Generalist: 如夹爪的量程设计和末端尖锐度,黄色更多是柔性材料，黑色是刚性材料
- 机械臂是带力控 [q] 

## 11/25
- AINA [ok]

## General
CoRL: (conf on robot learning)
- Conf: ~11/6
[papers]
- DexUMI (2025 Best FL)
- UMI-on-Legs (2024 X-Embodiment Workshop CoRL)

IROS:
- DDL: 1/5 - 3/2,
- Accept: 6/30
- Conf: 
[papers]
- Improved-3D-Diffusion-Policy (2025) @Yanjie Ze

RSS:
- DDL: 1/24
- Rebuttal: 3/24
- Accept: 4/10
- Conf: 6/21
[papers]
- UMI

## CV
ICLR:
- .
[papers]
- DuoAttention

IEEE:


## VLA
Stereo VLA @shengliang deng @he wang @25/12/26
- 双目视觉输入，用 Foundation Stereo + 左目 DINO + SigLIP

Evo-1 @赵波的 @25/11

$pi_0$
- new from OXE: 预训练 + finetune
- OXE 并没有预训练 - 后训练.

$pi_(0, "fast")$

$pi_(0.5)$ @25/04
- 相比 pi0 主打场景泛化 "entirely new environments" "generalize to new settings"
- Co-training: train on different data sources
    - "requires the right mixture of co-training tasks"

$pi_(0.6)$ @25/06
- blog: https://blog.csdn.net/v_JULY_v/article/details/154989166
- [不同之处.stage-pretain]
- VLA{VLM+FM}: img,lang,It(二值化优势指示符) => action(好/坏)
- ValueModel: 预测成功还需要多少步
- 然后特定任务few-shot SFT
- [不同之处.stage-exp]
- 即使rollout成功，也可以用 vm 判断是优势还是劣势.
- vm 也会更新.
    
## VLA-RL
In-Context @Jason Ma
- https://www.alphaxiv.org/abs/2411.04549
- 就是不用 权重 而是用 kv_cache 来学习新任务（任务例如判断视频进度）

## Dataset
RoboCoin 25/11 @北京智源
- [abs] [q] 如何证明 RTML 独立提点?
    - [q] 异构性如何解决 ？
    - [q] 数据后处理和验证 ?
    - [q] 采了多久?

Gen0 25/11/4 `https://generalistai.com/blog/nov-04-2025-GEN-0`
- 27000h 数据, 10B+ VLA
- 7B VLA 不会 ossification 僵化，而 LLM 通常是 O(10M)
- 这个 blog 里有 in-the-wild 都有复杂背景
- 似乎有一套自己的 inference 代码
- 预训练技巧: 高 pred error 和反向 KL 适合 RL

RoboMind 24/12

## Data Generation
DemoGen: 24/10 @THU AI Lab @Zhengrong Xue @Shuying Deng @Huazhe Xu
- RSS & CVPR
- 给一条演示数据，只编辑点云，不仿真不生成图像
- 分解为运动段和技能段
- 运动短重新规划
- 技能段的 contact-rich 得到保留（没怎么变）

## Hardware
UmiGEN: @Yan Huang, @Wenbo Ding
- Hardware: L515 深度 + T265 定位 (L515 提供1280x720Depth,无法提供6dof)
- 主要贡献: 第一视角 DemoGen | Gen train 时 Crop 视觉范围内点云，以免 inference OOD

## UMI


## DAgger
SOP 26/1/7 @jianlan luo
- [site] post-training problem:
    - shift, speed, degeneralize
    - online, multirobot, mutlitask

[crdagger] Compliant Residual DAgger @mengda xu @yifan hou
- [re] 冻结 base，训的是 residual，residual 50hz输出 delta pose 和 target force (target force 使用 admittance controller 施加)
- [idea] replay buffer 对 intervention data 的采样频率更高.
- [abs]:
    - [q] admittance control? [a] 虚拟弹簧
    - [q] without interrupting the ongoing?
    - [note] base + 动作残差 policy
- [q] '意图误解'？
- [q] 什么时候 ask for help?

[todo] ARMADA

[todo] Genie Centurion @智元 25/5

Data-Efficient Multitask DAgger 25/9
- https://arxiv.org/pdf/2509.25466
- @罗得岛州 布朗大学 @60 @Haotian Fu @cited 0
- TN: 成功率较低的任务会获得更高的优先级分数 (kalman filter 成功率)
- PG: 跟踪最近一次训练更新期间模仿损失的减少来衡量学习动量: PG = $max(0, L_(i, start) - L_(i, end))$
    - 其实就是加入这组 dagger 前后的 loss
- bench: 居然用的是仿真 (MetaWorld(Mujoco) & ISAAC Lab)

[ok] Diff-DAgger: @24/10 U Vir 弗吉尼亚 @275, @Sung-Wook Lee @cited 12
- [re] 推理时用 diffusion loss 判定机器人不确定(OOD) 并请求帮助
- 推理阶段，用 *loss 预测错误并且 ask for human help
    - LOSS: 给定 diffusion 时间步 t, LOSS = ||生成噪声 - 预测噪声||^2
    - DP 高损失值表示当前状态-动作对与训练分布显著不同
    - 通过允许机器人高度不确定时向专家寻求帮助来解决这个问题
    - ref: Ensemble-DAgger, ThriftyDAgger
        - Ensemble-DAgger: 训练多个策略并使用动作方差作为不确定性度量。然而，这种方法在多模态策略中会失效，因为在给定状态下存在多个有效动作

ThriftyDAgger UCB
- 训练 Q 函数估算当前策略下任务成功收敛的概率以界定风险状态

HGDAgger (human gated) 18/10 [自动驾驶]
- 专家认为进入不安全状态，就完全控制(注意不录制混合控制)，引导回安全状态就交还控制权.
- 计算一个多个 policy 输出的方差，作为不确定度，用最近的不确定度计算安全阈值，用于后续推理自主请求介入

[todo]:

5.  **《Soft DAgger: Sample-Efficient Imitation Learning for Control of Soft Robots》**
    -  **发布背景**：2023年发表于《Sensors》，是针对柔性机器人操作控制的开创性DAgger研究。柔性机器人因变形特性难以建模，传统控制方法依赖昂贵的探索技术或强化学习代理，实用性差。
    -  **核心创新**：提出Soft DAgger算法，构建动态行为映射，将机器人任务空间与驱动空间关联，该映射可基于机器人历史状态、专家演示和当前位置预测最优动作。设计了两种算法变体，无需依赖高成本探索即可实现泛化。
    -  **实验成果**：在双模块柔性机械臂的3D字母书写任务中验证，该算法不仅提升了任务复现精度和泛化能力，还持续缩短了优化时间、减少了所需样本量，为柔性机器人的复杂操作控制提供了实用方案。
6.  **《LazyDAgger: Reducing Context Switching in Interactive Imitation Learning》**
    -  **发布背景**：2023年提出，针对传统交互式DAgger中人类监督者频繁干预机器人导致的上下文切换成本高、效率低的问题，尤其适配布料等需要连续操作的机器人任务。
    -  **核心创新**：在Safe DAgger基础上优化，提出减少监督者与机器人自主控制间上下文切换的机制。通过合理延迟和规划干预时机，在不影响策略性能的前提下降低干预频率。

    -  **实验成果**：在3个连续控制仿真任务中，相比Safe DAgger平均减少60%的上下文切换；在ABB YuMi机器人的布料操作实验中，不仅保持了同样的上下文切换减少比例，还使任务成功率提升60%。

## 力控
ACP Adaptive Compliance Policy @Standford YifanHou ZeyiLiu Chengchi
- [q] Virtual target 是干啥用的？
是 observation 还是 action?
在采集数据过程中如何采集 virtual target？
- [a] 是采完以后用时间窗口算的. (virtual - ref) * K刚度 = F力

