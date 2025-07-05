---
title: "flash.nvim with Neovim from Zero"
date: 2025-07-05 23:35:56
tags: ["notes", "julyfun", "25", "07"]
author: "julyfun-4070s-ubuntu2204"
os: "Linux julyfun-4070s-ubuntu 6.8.0-60-generic #63~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Tue Apr 22 19:00:15 UTC 2 x86_64 x86_64 x86_64 GNU/Linux"
assume-you-know: [computer]
---

本文假设你：
- 已经安装了 neovim
- 可能仅使用 neovim 的 init.vim
- 可能用过 easymotion

> vim 模式下，想要跳转到屏幕上某个随机位置，并不是很方便. `flash.nvim` 是一个理想选择，比 easymotion, leap.nvim 更符合直觉.

## 效果展示

这是当前状态，你想调到第一个 neovim 处.

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to20250705233907.png)

按下: `/ n e o` 后，会在多个匹配 neo 的地方显示一个标识字母，快速按下

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to20250705234039.png)

