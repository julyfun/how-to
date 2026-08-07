---
title: "285 hw5: Offline RL"
date: 2026-08-04 20:01:04
tags: ["技术学习", "285"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

## 1. Offline RL: SAC+BC
### 回忆提纲
本章节训练部分的 Q loss 和 SAC 基本一样，不知为什么魔改为 2 critic + 2 target critic (上划线为 target):
![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20260805172449512.png)

而 actor loss 添加了 alpha * BC 损失. alpha 取值 3 ~ 1000 不等，显然这个东西比较难调.

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20260804200015793.png)

### 回答问题

**Cube 任务**：看起来模仿学习权重 300 和 100 是比较好的，对权重也是相当敏感:

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20260805173344415.png)

根据教程，q_min 应该收敛到 -50 ~ -70 而 q_max 应该收敛到 0，确实如此:

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20260805173659309.png)

**Ant soccer 任务**：

看起来 a = 3 和 a = 10 比较好:

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20260805202116672.png)

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20260805201949248.png)

## 2. IQL

### 回忆提纲

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20260807163940796.png)

### 回答问题

下图中的 a 是指数 exp(alpha * A) 的 alpha. 可以看出，cube 任务 a=1,3,10 都不错，而 ant 任务是 a=10 最好.

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/merged-image-6.png)

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/merged-image-5.png)

## 3. FQL
