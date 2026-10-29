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

👍 

- Agentic World Action Models
- imagewam
- PhysCanvas
