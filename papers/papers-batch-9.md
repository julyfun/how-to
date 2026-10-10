---
title: "papers batch 9"
date: 2026-09-30 19:31:29
tags: ["papers"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 27.0.0 Darwin Kernel Version 27.0.0: Tue Aug 11 21:02:59 PDT 2026; root:xnu-13432.1.9~1/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

## SmolVLA (67)

⭐️⭐️⭐️ huggingface | https://www.alphaxiv.org/pdf/2506.01844

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20261009120733328.png)

裁剪 MoT 并交错使用 CA 和 SA 以让模型更轻量化.

## VPP2 (68)

⭐️⭐️⭐️ 郭彦江, 陈建宇，清华&星动纪元 | https://www.alphaxiv.org/abs/2610.10270

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20261009131821308.png)

架构没变化仍然是 MoT IDM. 数据上扩展了 ego 和通用视频，并按照语义切分为 1-12 秒事件，预训练让 VM 完整预测整个不定长事件; 要求事件内的文字描述十分明确. 训练流程三阶段如上图.

消融表明按事件预测显著提升按照指令预测视频的效果；VLM 上层规划大幅提升 SR. 发布时登顶 dojo (32.26%)，但 dojo 并没有使用 VLM 上层规划.

注：VPP1 的架构 query UNet 中间特征交给 AE，但是本作向 MoT 投降了.

## Ctrl-world (69)

⭐️⭐️ 郭彦江, Chelsea Finn, Stanford | https://www.alphaxiv.org/abs/2510.10125

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20261009143623498.png)

WM simulator rollout，然后人工从中选择后训练数据

## EgoRecovery (70)

⭐️⭐ 葛祖浩，周宇辰，贾晓松, Yu Gang Jiang, FDU&SimpleAI | https://www.alphaxiv.org/abs/2607.19745

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20261009214912158.png)

从手工设计的失败情形录制人类 Ego 纠正数据，以及机器人rollout失败的时候，人类手动摆出失败配置并纠正; 提取意图调制 Gated 动作解码

## PhysicalRSI (71)

⭐️⭐️ mmlab | https://mmlab.hk/research/PhysicalRSI

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20261010160023089.png)

让 GPT 自己决定 调用 VLA / "move_eef" "rotate_wrist_pitch" / task-specific 规控，写 SKILL.

## RealtimeWAM (72)

[TODO]

## GPT-6 Astra as Embodied Policies (73)

⭐️⭐️ 银河通用 | https://www.alphaxiv.org/pdf/2609.38537

对于 pi05 提交的每一个 chunk，经过 FK 后 GPT 直接看 image + chunk，决定是否接管. Astra 选择接受其前 1–15 步，或替换为 1–5 步的末端执行器修正动作. 仿真分数比单纯 GPT 和单纯 pi05 都高.

每个 episode 消耗 token 12M+.

---
long-wam
another openwam
robolab
