---
title: "Neovim control your window like tmux"
date: 2025-09-24 17:05:29
tags: ["notes", "julyfun", "25", "09"]
author: "Julyfun M4"
os: "Darwin tutianpeikeladeMac-mini.local 24.3.0 Darwin Kernel Version 24.3.0: Thu Jan  2 20:22:58 PST 2025; root:xnu-11215.81.4~3/RELEASE_ARM64_T8132 arm64"
assume-you-know: [computer]
confidence: 2
---


| 操作目的 | Tmux 快捷键 (前缀 `Ctrl+b`) | Neovim 快捷键 (前缀 `Ctrl+w`) |
| :--- | :--- | :--- |
| **垂直分屏** | `%` | `v` 或 `:vsp` |
| **水平分屏** | `"` | `s` 或 `:sp` |
| **关闭当前窗格/窗口** | `x` | `c` 或 `:q` |
| **切换窗格/窗口** | `o` 或方向键 | `w`（循环切换）或 `h`/`j`/`k`/`l`（定向切换） |

Ctrl+w + K/J/H/L: 将当前窗口移动到上/下/左/右极限

