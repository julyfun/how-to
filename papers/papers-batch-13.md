---
title: "papers batch 13"
date: 2026-10-28 16:50:31
tags: ["papers"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 27.0.0 Darwin Kernel Version 27.0.0: Tue Aug 11 21:02:59 PDT 2026; root:xnu-13432.1.9~1/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---
## RynnVLA-Latent (101)

⭐⭐⭐️ 达摩院 | https://www.alphaxiv.org/abs/2610.34356

<img src="https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20261028172041584.png"/>

LAPA style，但是监督了残差(Depth Anything 3 两帧直接相减) + 3D Flow + 相机位姿. 处理了 3w 小时 robot, ego & sim 数据.

灵巧仿真 & 夹爪真机上 demo 还可以.

## VLA-Delta (102)

⭐ Qi Lu, Xuhong Zhang, OmniAI, ZJU | https://www.alphaxiv.org/pdf/2610.21306

加了光流、结构化、difference text 监督... Qwen backbone... 调参大师来了...

整个网站、文章和图都非常 vibe.

## ATM (103)

👍 Chuan wen, pieter abbeel | https://www.alphaxiv.org/abs/2401.00025

早期一种利用无标签数据的方式. 让一个 transformer 预测二维点轨迹，再训练一个 ViT 风格的下游策略，输入二维轨迹 & img 输出动作.

训练时随机撒点筛选动静大的点作为预测目标，推理时由于无法预知哪些点动静大，故 4x8 均匀撒点后预测. 这是因为作者认为 Track Transformer 本身具备置换不变性（Permutation Invariance）.

## Contact Trajectory Prompting (104)

👍 xian nie, shuicheng yan, TARS | https://www.alphaxiv.org/abs/2610.18848

BPP 的触觉版本. VAE 训练一个动作和触觉编码器 (token decode 还原动作和触觉)，然后每对数据是用同一任务里另一 episode[1] 的触觉数据来 prompting 接下来的动作

1. 考虑推理 ICL 不是让你复制这个触觉对应的动作，所以需要另一 episode.

## TacForesight (105)

👍 xian nie, wenchao ding, TARS | https://www.alphaxiv.org/abs/2610.18848

## CR-Dagger (106)

⭐⭐⭐️ xiaomeng xu, shuran song, Stanford | https://www.alphaxiv.org/abs/2506.16685

<img src="https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20261029190857460.png"/>

早就看过了，明确一些细节.
- 动机：解决 contact-rich 任务传统人工 dagger 不平滑的问题.
- 方法：
	1. 机械臂带力反馈。rollout dagger 时人类轻轻把机械臂往正确方向推.
	2. 此时机械臂并不是因为受力直接被推开，而是根据一个虚拟弹簧公式改变位控目标，同时记录位置差值和末端收到的外力.
	3. 训练 residual policy，输入和原始一样，输出位置差和目标外力.
	4. rollout 预测 delta 和期望外力，用导纳控制（如果目标力大于真实力，则贴得更紧）
- 结果：翻书、皮带装配、齿轮插入和线缆布设.



- Agentic World Action Models
- imagewam
- PhysCanvas
