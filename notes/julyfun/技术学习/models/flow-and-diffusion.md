---
title: Flow and diffusion
date: 2025-11-10 00:39:48
tags:
  - notes
  - julyfun
  - 技术学习
  - models
author: julyfun-4070s-ubuntu2204
os: "Linux julyfun-4070s-ubuntu 6.8.0-87-generic #88~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Tue Oct 14 14:03:14 UTC 2 x86_64 x86_64 x86_64 GNU/Linux"
assume-you-know:
  - computer
confidence: 2
---
- ODE（常微分方程） SDE（随机微分方程, 带随机波动的变化）
- SDE: 系统的未来状态不仅依赖当前状态，还包含非决定性的随机波动（噪声），因此未来状态是一个概率分布. 方程中多了随机项（通常用布朗运动表示）
## Lec 1
- https://diffusion.csail.mit.edu/docs/slides_lecture_1.pdf
- Diffusion network 预测的就是向量场（输入: t, X 当前位置. 输出: X 速度）
![Screenshot from 2025-11-10 01-25-29.png](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-toScreenshot%20from%202025-11-10%2001-25-29.png)
![Screenshot from 2025-11-10 01-24-27.png](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-toScreenshot%20from%202025-11-10%2001-24-27.png)
- [qm] 为何噪声到图像的过程可以建模为 SDE
