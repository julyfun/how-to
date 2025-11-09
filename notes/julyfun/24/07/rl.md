---
title: "RL"
date: 2024-07-01 15:26:42
tags: ["notes", "julyfun", "24", "07"]
author: "julyfun-4070s-ubuntu2204"
os: "Linux julyfun-4070s-ubuntu 6.8.0-87-generic #88~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Tue Oct 14 14:03:14 UTC 2 x86_64 x86_64 x86_64 GNU/Linux"
assume-you-know: [computer]
confidence: 2
---
https://rail.eecs.berkeley.edu/deeprlcourse-fa23/
- hw1: https://rail.eecs.berkeley.edu/deeprlcourse-fa23/deeprlcourse-fa23/static/homeworks/hw1.pdf

## 符号
- $J(theta)$: 策略的累积奖励的期望，需要最大化
- 顺序: $s_1 => a_1 => s_2$
- $tau$: 轨迹，表示所有 $s, a$

- $pi(a | s)$：状态 $s$ 下采取 $a$ 的概率
- $V^pi (s) eq.def EE_pi [G_t | S_t = s]$ **状态价值函数 state-value function**，即还不确定 $a$
- $Q^pi (s, a) = EE_pi [G_t | S_t = s, A_t = a]$ **动作价值函数 action-value function**，即确定了 $a$
    - 有 $V^pi (s) = sum_(a in A) pi(a | s) Q^pi (s, a)$
    - 有 $Q^pi (s, a) = r(s,a) + gamma sum_(s^prime in S) P(s^prime | s, a) V^pi (s^prime)$
    - $s -->^pi a_i -->^P s^prime$

## 强化学习类型
- Policy Gradient: 求 $EE[r]$ 对 $theta$ 的导数.
	- 训练:
		- Actor: 输入 `[机械臂状态，观测]`
		- 输出 `[动作]` 或者 `[动作的概率分布]`
	- 推理: 一样
- Value Based (DQN): 直接训练一个 Q / V，取最大值对应的动作索引 (no explicit policy)
- Actor-Critic: 有 A 有 Q
- Model-based: 有模型自行估计 $s$ 经过 $a$ 如何转移 ( learn $p(s_(t + 1) | s_t, a_t)$ )

## On-off policy
- off-policy: able to improve the policy without generating new samples from that policy
- on-policy: any time the policy is changed (even a little bit) we need to generate new samples.
