---
title: "papers batch 14"
date: 2026-10-30 00:06:49
tags: ["papers"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 27.0.0 Darwin Kernel Version 27.0.0: Tue Aug 11 21:02:59 PDT 2026; root:xnu-13432.1.9~1/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

go on this:
https://axi404.top/blog/eai-papers#%E6%9C%BA%E5%99%A8%E4%BA%BA%E6%95%B0%E6%8D%AE%E9%9B%86
## ImageWAM (109)
️️⭐️️⭐️⭐️ Wenyao Zhang, Xiaokang Yang, SJTU | https://www.alphaxiv.org/abs/2606.19531

- 动机：也许不需要 VM，只需要 edit.
- 方法：
	1. MoT 架构不变，换为 FLUX.2 4B (flow-matching)，编辑目标是 16 帧以后的观测图像，进行监督，推理时仅前向一次干净图像.
- 结果：
	1. 真机 demo 是 pick and place，精度和流畅度不错
	2. 点数挺高, robotwin  c2c r2r ~93%

## RL-token (110)
⭐⭐️️⭐️️⭐️️️️ Charles Xu, PI |https://www.alphaxiv.org/abs/2604.23073 

- 动机：想通过小 RL 提升动作 precision 和 speed，但是 DSRL 能调节的局限性又太强.
- 方法：VLA 输出额外 token，第一阶段用它重建 VLA 输入. 第二阶段冻结 VLA 和提取器，训练 actor critic，这俩都会接收 RL token. actor 还额外接收 VLA 给出的参考动作块&带正则化防偏离，critic 则接收待评估动作块. 给人工标注的成功/失败奖励即可.
- 结果：成功率和 DSRL 差不多，但是 RLT 更快.
