---
title: "哪个模型读 paper 更好？"
date: 2026-06-18 01:39:29
tags: ["26", "06"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

提示词也在本仓库.

[Opus 4.8] RoboPocket 用手机 AR 把策略预测轨迹画给人看，从而不接触真机就能做 DAgger 式纠正采集

来自 SJTU，通讯作者 Cewu Lu。这是一篇系统和部署工作，核心是把 UMI
式手持采集搬到 iPhone 上，并用 AR
把策略预测的末端轨迹投影到真实画面，让采集者不碰真机就能看到策略意
图、发现失败区域并补采纠正数据，后台再用 RLPD 式加权采样（一半离线
数据加一半新在线数据）做在线微调。它最接近你熟悉的 DAgger
这条交互式纠正线，本质是把 DAgger 里"真机执行暴露 OOD
状态"这一步换成"AR 虚拟执行"，省掉真机成本和风险，代价是人只能看到
几何轨迹投影，拿不到真实接触和动力学反馈。

缺陷主要在策略本体和评测范围。它的 policy 是 CNN-based Diffusion
Policy，并且 observation horizon 设为 1
直接丢弃历史，架构偏旧，不是 Pi-like action expert。真机评测仅限
Flexiv 单双臂的桌面 block
sorting、倒调料和叠毛巾，任务范围窄，而且声称的 2x 数据效率是相对纯
 IL 和 offline PI baseline。它值得读的点在于把 DAgger
去真机化的工程设计，如果 demo 视频够强可以一读。这里我对"无真机执行
采到的纠正数据是否真的能转移到真机动力学"还不确定，需要你精读确认
AR foresight 在 contact-rich 任务上是否够用。

评价：⭐️⭐️ 有点啰嗦，关注了一些非重点，而且怎么读成 cnn-based 了.

---

[Composer 2.5] RoboPocket 是无真机版 DAgger，用手机 AR 把策略弱点可视化成纠错采集

来自 SJTU。这是卢策吾和 Chuan Wen 团队在数据采集与 policy iteration
 方向的系统论文，不是新 VLA 架构。核心做法是把 UMI
式手持夹爪采集和远程推理接起来，在 iPhone 上用 AR
叠加策略预测的末端轨迹，让人主动在弱点区域补 demo，同时后台用 RLPD
式 50% 离线加 50%
在线采样做异步在线微调，再把新权重推回手机。和我熟悉的线最接近
DAgger 和 ALOE 的干预闭环，但把“看机器人 rollout 找失败”换成了“看
AR 轨迹找失败”，策略本体仍是 Diffusion Policy 加 CLIP 或
DINOv2，不是 Pi-like VLA。

真机评测覆盖四任务且分布式 12 条纠错就能涨成功率，工程 demo
看起来比方法新颖度更强。主要风险是 AR
预览的是预测轨迹而不是真实接触动力学，接触丰富或遮挡严重时，AR
标出的弱点是否和真机失败一致需要看实验细节；另外整套流程依赖 WiFi
远程 GPU 和手持硬件同构，复现门槛不低。若你关心野外数据采集 infra
或低成本 policy iteration，值得精读系统设计和 IL 加 Instant PI 对比
 IL 加 Offline PI 的 ablation；若只追新 action
model，优先级可以放低。这里我对在线微调的具体步频、以及 AR
轨迹在双臂和可变形物体任务里的对齐误差还不确定，需要你精读确认。

评价：⭐️⭐️ 跟你说了别用`不是而是`，你还用。第二段还可以。

---

[GPT5.5] RoboPocket 是把 UMI 式手机采集改成可在线纠错的 robot-free DAgger 系统

来自 SJTU、上海创新研究院和 Noematrix。这是 Cewu Lu
团队的工作，重点是系统和数据闭环，不是新 VLA
架构。它用手机采集示教，同时把当前策略预测的轨迹用 AR
显示给采集者，让人主动补策略弱点数据，再异步在线微调 Diffusion
Policy。和你熟悉的 ALOE 更接近，但它把真机 rollout 和 critic
干预换成了手机端可视化纠错，代价是依赖 SLAM、IK、AR
对齐和手机夹具同构性。

问题是它的“on-policy”其实是手机场景里的策略意图反馈，不等同于真实机
器人执行后的状态分布。实验有真机评测和四类任务，但模型还是 CLIP 或
DINOv2 加 Diffusion Policy，方法价值主要在数据系统。需要精读的是 AR
 预测轨迹在接触、遮挡、形变物体和双臂任务里是否真的足够准；这里我对
 AR Visual Foresight 和真实 rollout
分布的差距还不确定，需要你精读确认。

评价：⭐️⭐️ 和 ALOE 关系不大。

