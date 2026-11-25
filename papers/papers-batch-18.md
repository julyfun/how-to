---
title: "papers batch 18"
date: 2026-11-24 15:57:58
tags: ["papers"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 27.0.0 Darwin Kernel Version 27.0.0: Tue Aug 11 21:02:59 PDT 2026; root:xnu-13432.1.9~1/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

## Code as policies (141)

jacky liang, andy zeng, Google | https://www.alphaxiv.org/abs/2209.07753

应用 LLM 将自然语言翻译为 python 代码，并提出层级式代码生成：允许带未定义函数，稍后再定义.

## VoxPoser (142)

wenlong huang, feifei li, Stanford | https://www.alphaxiv.org/abs/2307.05973

VLM 进行检测和分割，LLM 编写多种类型的 python value map，然后零阶优化选择轨迹.

## SayCan (143)

andy zeng, google | https://www.alphaxiv.org/pdf/2204.01691

给出指令后用 LLM & 规则判断是否可行，进行 planning，再执行.

## MOKA (144)

fangchen liu, sergey, UCB | https://www.alphaxiv.org/abs/2403.03174

用冻结的 VLM 先标候选点，然后 motion planning.

## ReKep (145)

wenlong huang, feifei li, Stanford | https://www.alphaxiv.org/abs/2409.01652

<img src="https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20261125155126255.png"/>

DINOV2 提取关键点，在深度图上拿到三维点，然后用 VLM 写约束求解器.

## RISE (146)

chenxi wang, cewu lu | https://www.alphaxiv.org/abs/2404.12281

<img src="https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20261125161221690.png"/>

将点云直接作为 DP 输入. 体素化 + 稀疏 3d 卷积后先 transformer encode 后用 learnable embedding 去 query 出来（选择性保留重要信息）.

demo: pick and place.
