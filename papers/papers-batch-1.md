---
title: "Papers batch 1"
date: 2025-01-01 23:10:53
tags: ["papers"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

## RT-2
- https://hjfy.top/arxiv/2307.15818
和 OpenVLA 同属一派，将 VLM 的最后 256 个 token id 分配给动作，直接将 x, y, z, yaw, pitch, roll, gripper 划分为 256 个离散桶，七个动作维度共享 token id 并通过位置区分语义，直接拼接丢给 VLM 输出隐状态，一个 head 解码出 id 再映射回动作空间. 缺点是离散化和自回归导致的精度不够. 

TODO: 数据集这一块儿有空可以再看看.

## World Model for Robot Learning: A Comprehensive Survey
- https://hjfy.top/arxiv/2605.00080

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20260520212623754.png)

## Fast-WAM (Yuanet al., 2026)
可被视为该家族中的一个混合点：它采用具有共享注意力的 Transformer 混合体骨干网络 及耦合的视频与动作分支，但结论认为主要优势可能更多来自训练期间的视频协同训练，而非推理阶段 的显式未来想象。在这些变体中，视频分支越来越不再被视为需要忠实渲染的输出，而是被看作一种预 测性潜在过程，其隐状态用于指导动作生成.

## Lingbot-va
- https://hjfy.top/arxiv/2601.21998
- ?自回归扩散
    - ?对统一序列施加因果注意力掩码，确保预测的视觉状态和动作命令均受先前状态的约

## RTC
```python
# H: (Prediction Horizon), M: 动作维度 (Action Dim), O: 观测维度
def rtc_inference(v_net, o_t, A_prev, d, s, n=5, beta=5):
    # o_t: 观测 [O], A_prev: 旧动作块的残余部分 [H, M] (已 pad0 至H长度)
    # d: 推理延迟 s: 执行步长 n: 迭代步数 beta: 引导项裁剪值
    A_tau = torch.randn((H, M))             # [H, M] 采样初始噪声
    W = compute_soft_mask(d, s, H)          # [H, 1] 软掩码权重，1 ~ 0递减
    for tau in np.linspace(0, 1, n):        # n 步流匹配迭代
        v = v_net(A_tau, o_t, tau)          # [H, M] 当前速度场预测
        # A_hat_1: [H, M] 预估当前步如果去噪完成后的最终动作轨迹
        A_hat_1 = A_tau + (1 - tau) * v     
        # 计算带权重的 Inpainting 误差
        loss = 0.5 * (W * (A_prev - A_hat_1)**2).sum()  # 标量 Scalar
        # g: [H, M] 获取修正梯度，指引 A_tau 向 A_prev 靠拢
        g = torch.autograd.grad(loss, A_tau)[0] 
        scale = min(beta, get_weight_scale(tau)) # get_weight_scale 是一个随 tau 递减的权重
        # A_tau: [H, M] 结合原始预测与裁剪后的引导项进行更新
        A_tau += (1/n) * (v + scale * g) 
    return A_tau                            # [H, M] 平滑衔接的新动作块
```

