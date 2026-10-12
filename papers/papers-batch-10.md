---
title: "papers batch 10"
date: 2026-10-12 22:21:23
tags: ["papers"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 27.0.0 Darwin Kernel Version 27.0.0: Tue Aug 11 21:02:59 PDT 2026; root:xnu-13432.1.9~1/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

## 李飞飞的 OpenWAM (75)

⭐️⭐️⭐️ Heng Yu, Ehsan Adeli; Stanford | https://www.alphaxiv.org/pdf/2610.07922

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20261012231026156.png)

常规架构，各种 ablate. VTA 就是 IDM.
- 固定 VTA/Joint 下，机器人视频因果预训练将 LIBERO-Long 成功率从 Wan2.2 的 68.4%/62.2% 提升至 97.8%/96.6%
- 相同预训练与训练设置下，MoT 相比非 MoT 将 VTA/Joint 成功率分别提高 5.0/3.0 个百分点
- 四种交互模式中，VTA 的 LIBERO 平均成功率最高为 98.6% 且 ATV 最低为 96.8%
- 目标任务迁移中，local-context IDM (no history) 加反事实数据的平均成功率为 84.0% 而仅用示范为 21.5%
- 混合监督下，local-context IDM 目标任务成功率比 full-context IDM 高 37 个百分点且源任务成功率为 94.4% [IDM Transfer](https://www.alphaxiv.org/abs/2610.07922?page=8)
- Local-context IDM 的反事实单独训练与混合训练迁移表现接近，四任务平均成功率分别为 84.5% 和 84.0% [IDM Transfer](https://www.alphaxiv.org/abs/2610.07922?page=8)
- FDM 加入反事实监督后，RGB MSE 下降 34.5% 且 16 个同状态结果的识别准确率从 21.1% 升至 71.3% [FDM Results](https://www.alphaxiv.org/abs/2610.07922?page=8)
- 单一多目标模型的策略成功率为 92.8% 低于专用策略模型的 97.8% 且其反事实 FDM 误差也高于专用 FDM [Multiobjective Comparison](https://www.alphaxiv.org/abs/2610.07922?page=18)
