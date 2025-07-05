---
title: Swift-糟糕设计
date: 2025-06-18 16:02:58
tags: ["notes", "julyfun", "25", "06"]
---
### 隐式导入
- 一个项目所有符号都在全局.
- 导致学习 Swift 时不清楚每个符号的来源.
    - 难以了解模块依赖和 in-out 功能.
    - 比如 ARView 实际上不是 ARKit 而是 RealityKit
- no namespace
    - 只能用 class 模拟 namespace

好处:
- 随便改变文件夹结构不用重写 import.（然而等于无视了现代编辑器自动改 import 路径的功能）

## 隐式 self
- 难以阅读函数符号是全局函数还是成员函数.
    - 两者依赖的状态完全不同.

## struct 和 class 区分（可变性、移动性）
- 额外的心智负担，而灵活性又不高.

## 双参数名
- 等于完全无视了现代编辑器的参数名提示功能.

