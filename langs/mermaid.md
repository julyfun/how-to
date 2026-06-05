---
title: "mermaid"
date: 2026-06-01 19:19:51
tags: ["langs"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---


| 写法                | 样式      | 常见语义                     |
| ----------------- | ------- | ------------------------ |
| `A[text]`         | 矩形      | 普通步骤                     |
| `A(round)`        | 圆角矩形    | 一般 process               |
| `A([stadium])`    | capsule 形    | 起止/特殊状态                  |
| `A[[subroutine]]` | 双边矩形    | 子过程、模块（你那个 `vlm[[vlm]]`） |
| `A[(db)]`         | 圆柱      | 数据库                      |
| `A((circle))`     | 圆形      | connector / state        |
| `A{{decision}}`   | 菱形      | 判断分支                     |
| `A>text]`         | 非对称形    | 特殊处理（较少用）                |
| `A[/text/]`       | 平行四边形   | 输入输出                     |
| `A[\text\]`       | 反向平行四边形 | 输入输出变体                   |
| `A[/text\]`       | 梯形      | manual input             |
| `A[\text/]`       | 倒梯形     | manual operation         |


