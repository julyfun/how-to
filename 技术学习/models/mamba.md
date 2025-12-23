---
title: "MAMBA"
date: 2024-11-21 11:41:01
tags: ["notes", "julyfun", "技术学习", "models"]
author: "Julyfun MacOS14.5 M1"
os: "Darwin floriandeMacBook-Air.local 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1 20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64"
assume-you-know: [computer]
confidence: 2
---

kimi:
```python
 class MambaBlock:
     def __init__(self, d_model, d_state=128, d_conv=4, expand=2):
         self.d_inner = expand * d_model
         self.x_proj = Linear(d_model, self.d_inner * 2)
         self.conv1d = Conv1d(self.d_inner, self.d_inner, d_conv,
 groups=self.d_inner)
         self.dt_proj = Linear(self.d_inner, self.d_inner)
         self.A = nn.Parameter(torch.arange(1, d_state + 1).repeat(self.d_inner,
 1))
         self.D = nn.Parameter(torch.ones(self.d_inner))
         self.out_proj = Linear(self.d_inner, d_model)

     def forward(self, x):
         y = self.x_proj(x)
         x, z = y.chunk(2, dim=-1)
         x = self.conv1d(x.transpose(1, 2)).transpose(1, 2)
         x = silu(x)
         dt = softplus(self.dt_proj(x))
         y = selective_scan(x, dt, self.A, self.D)
         return self.out_proj(silu(y) * silu(z))

 def selective_scan(x, dt, A, D):
     return torch.cumsum(dt * x.unsqueeze(-1) * A, dim=1).sum(-1) + D * x

florian✨ 解释
Mamba = SSM + 门控 + 硬件友好扫描

 1 x_proj
   把输入劈两半：一路做SSM，一路做门控（像Transformer的GLU）
 2 conv1d
   因果卷积，给局部上下文，权重组共享（groups=dim）省参数
 3 selective_scan
   核心：Δ(t) 动态生成，把固定A变成随输入变化的“可变状态矩阵”。
   cumsum 就是硬件友好的并行前缀和，等价于线性递推 y_t = A_t y_{t-1} + B_t
   x_t，但一次scan做完。
 4 门控乘
   silu(y) * silu(z) 控制信息流，类似GRU的更新门。
 5 无attention
   全程O(n)内存，序列长度线性扩展，训练推理都省显存。

一句话：用“动态SSM+卷积+门控”代替attention，线性复杂度，长上下文不吃显存。
```

