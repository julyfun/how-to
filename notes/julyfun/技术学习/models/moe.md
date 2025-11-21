---
title: "MoE"
date: 2024-11-21 11:41:30
tags: ["notes", "julyfun", "技术学习", "models"]
author: "Julyfun MacOS14.5 M1"
os: "Darwin floriandeMacBook-Air.local 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1 20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64"
assume-you-know: [computer]
confidence: 2
---

- MoE: 门控选专家 → Top-K激活 → 加权求和
```python
 class MoELayer:
     def __init__(self, hidden_size=768, num_experts=8, top_k=2):
         self.gate = Linear(hidden_size, num_experts)
         self.experts = ModuleList([Expert(hidden_size) for _ in
 range(num_experts)])
         self.top_k = top_k

     def forward(self, x):
         B, S, H = x.shape
         x = x.view(-1, H)

         gates = softmax(self.gate(x), dim=-1)
         probs, indices = topk(gates, self.top_k, dim=-1)
         probs = probs / probs.sum(dim=-1, keepdim=True)

         out = zeros_like(x)
         for i in range(x.shape[0]):
             for j in range(self.top_k):
                 expert = self.experts[indices[i, j]]
                 out[i] += probs[i, j] * expert(x[i:i+1])

         return out.view(B, S, H)

 class Expert:
     def __init__(self, hidden_size):
         self.w1 = Linear(hidden_size, hidden_size * 4)
         self.w2 = Linear(hidden_size * 4, hidden_size)
         self.act = GELU()

     def forward(self, x):
         return self.w2(self.act(self.w1(x)))

 class TransformerBlock:
     def __init__(self, hidden_size, num_heads, num_experts=8):
         self.attn = MultiHeadAttention(hidden_size, num_heads)
         self.moe = MoELayer(hidden_size, num_experts)
         self.norm1 = LayerNorm(hidden_size)
         self.norm2 = LayerNorm(hidden_size)

     def forward(self, x):
         x = self.norm1(x + self.attn(x))
         x = self.norm2(x + self.moe(x))
         return x
```

- 负载均衡：与均匀分布做一个 loss

