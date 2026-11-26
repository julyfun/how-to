---
title: "papers batch 19"
date: 2026-11-25 16:59:44
tags: ["papers"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 27.0.0 Darwin Kernel Version 27.0.0: Tue Aug 11 21:02:59 PDT 2026; root:xnu-13432.1.9~1/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

## wall-oss-1.0 (150)

自变量 Ryan Yu, qian wang | https://x2robot.com/en/blog/wall-oss-1

主要是从 qwen3.5-base 开始就做 co-training，没有分阶段预训练. 另外一个 x-tokenizer 统一不同类型本体编码为离散动作.

demo 有一个用剪刀剪纸，其他没什么特别的.

## OmniAct (151)

UW 华盛顿大学，xiang fan | https://www.alphaxiv.org/abs/2611.33158v1

单策略适应百万种本体. 具体来说输入端构建运动学图用 Fourier 特征编码等方式编码完整本体信息，输出端则是老方法：对多余自由度 noise sampling mask & loss mask.

基模是 siglip2 + qwen2.5vl

## B-spline Policy (152)

哈佛 Xiaoshen Han, Yilun Du | https://www.alphaxiv.org/abs/2607.09648

从预测 action chunk 改为预测 B-spline 关键点. 本文声称能让轨迹更平滑，且可以调快慢. 实验接到 DP 和 ACT 上做的.
