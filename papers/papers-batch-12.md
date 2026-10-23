---
title: "papers batch 12"
date: 2026-10-23 11:06:38
tags: ["papers"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 27.0.0 Darwin Kernel Version 27.0.0: Tue Aug 11 21:02:59 PDT 2026; root:xnu-13432.1.9~1/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

时间预算非常不够，大概读一下，只看 idea.

## Dream1 (91)

https://dreamlabs.ai/research/dream-1/

没有提到架构，只说 eef, 并且认为 WAM 有自动适应本体和头部视角的能力.

其实 demo 拍摄的比较拉，但是我们真机 zero-shot 实测其实还可以.

## BOE (92)

⭐️⭐️ 方佳鑫, FDU, 椰青分享 | https://www.alphaxiv.org/abs/2610.14746

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20261023150719804.png)

用 learnable query （直接放 video dit） 代替 MoT. ae 只有两层.

主要是为了加速，以及（据称）减少无关视觉干扰.

## ForceWAM (93)

zijun xu, wendi chen, FDU, SJTU, 杨理欣

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20261023161010589.png)

训练一个预测未来六轴力矩的 WM，然后小型 IDM, reactive.

训练数据有 demo & play，其中 play 是探索性按压等非成功操作. Play 数据只用于训练 IDM.


