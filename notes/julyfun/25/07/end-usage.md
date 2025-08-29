---
title: "End-Usage"
date: 2025-07-26 18:26:50
tags: ["notes", "julyfun", "25", "07"]
author: "4070s wsl julyfun"
os: "Linux DESKTOP-VDB57PP 5.15.153.1-microsoft-standard-WSL2+ #2 SMP Sun Oct 27 22:02:06 CST 2024 x86_64 x86_64 x86_64 GNU/Linux"
assume-you-know: [computer]
confidence: 2
---

一个工具如果处于依赖链的终端，那么其接口设计与非终端工具应该采取不同的原则.

End-usage:
- 同一功能可以有多种入口
e.g.
- Editor keybindings
- Excel：同一功能通常至少有两种入口
- shell language

非终端工具：
- git (自动化脚本)
- `lib.rs`
- 同一功能仅有一种最佳实现
e.g.
- git (自动化脚本)
- `lib.rs`
- 编程语言

