---
title: nn-module-train-or-eval
date: 2024-01-15 01:10:05
tags: []
---
https://chat.openai.com/share/2e09879f-32dc-442b-828c-f29402163858

他说 m.train() 和 m.eval() 会把 m: nn.Module 设置为不同的模式。在 train mode 下，Dropout 层会引入丢弃操作，将一些输入中的元素置零。


