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
- CFM: ?
- 教材笔记，详实简单: https://arxiv.org/pdf/2506.02070
## Lec 1
- https://diffusion.csail.mit.edu/docs/slides_lecture_1.pdf
- Diffusion network 预测的就是向量场（输入: t, X 当前位置. 输出: X 速度）
![Screenshot from 2025-11-10 01-25-29.png](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-toScreenshot%20from%202025-11-10%2001-25-29.png)
- 改为神经网络形式（引入 $theta$）. 注意这里 $sigma_t$ 可以由时间变化:
- ![Screenshot from 2025-11-10 01-24-27.png](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-toScreenshot%20from%202025-11-10%2001-24-27.png)
- [qm] 为何噪声到图像的过程可以建模为带布朗运动的 SDE?

## Lec 2
- Conditional Probability Path: 给定目标点 $z$（例如 diffusion 中的最终图像），求 $x$ 下一步路径
- Marginal Probability Path: 不给定条件（所有分布的加权平均），求下一步路径
	- 两者在 $t_0$ 是完全一样的，从第二步开始才有区别.
- 向量场函数（也可视为梯度或者速度）：$$"def" u(x: RR^d, t: [0, 1]) |-> RR^d$$
- ![image.png|700](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20251111103019.webp)
- [qm] 为何 score function 这样定义


[附]
- 很好的散度讲解: https://zhuanlan.zhihu.com/p/165479232kj

## Lec3 ok

## Lec4: Guided (conditional) DDM
- condition 是怎么加入 UNet:
- ![截屏2025-11-11 11.10.16.png|700](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/%E6%88%AA%E5%B1%8F2025-11-11%2011.10.16.webp)
