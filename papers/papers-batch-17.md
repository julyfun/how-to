---
title: "papers batch 17"
date: 2026-11-18 15:56:20
tags: ["papers"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 27.0.0 Darwin Kernel Version 27.0.0: Tue Aug 11 21:02:59 PDT 2026; root:xnu-13432.1.9~1/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

## Robometer (133)

⭐️⭐️⭐️ 南加州 Anthony Liang, Jesse Zhang | https://www.alphaxiv.org/abs/2603.02115

通用进度模型。用 100w eps，在 t/T 进度监督的基础上构造偏好监督，即同一任务的两条轨迹判断哪条轨迹更好（通过失败轨迹、倒放和错配任务自动构造数据）.

基模: Qwen-VL-4B-Instruct. 实验先用 IQL 训练 critic 然后 SAC-DSRL 微调 pi0. 不过任务也是比较简单. 基本就是 pick and place & singletask.
