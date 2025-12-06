---
title: "Blender cheatsheat"
date: 2025-12-04 16:28:32
tags: ["notes", "julyfun", "25", "12"]
author: "Julyfun M4"
os: "Darwin tutianpeikeladeMac-mini.local 24.3.0 Darwin Kernel Version 24.3.0: Thu Jan  2 20:22:58 PST 2025; root:xnu-11215.81.4~3/RELEASE_ARM64_T8132 arm64"
assume-you-know: [computer]
confidence: 2
---

ref: https://www.bilibili.com/video/BV1kX4y1m7G5/

version: 5.0.0

## 视角
- 中键: 旋转
- shift-中键: 平移
- cmd-7: 从 -z 看向物体
- home: 看清所有物体

## 创建
- `Preference - Input` 可打开模拟键盘，这样按顶部数字等于按小键盘
- shift-a: 添加物体

## 选择
- alt-z: 透显，可选中看不见的点

## 移动
- g, z: 拖动沿 Z 轴移动（hint: 选中点可以移动点）

## 参考点
- shift-d, 复制点
    - ? 这个点 K 模式下怎么不能吸附

## 镜像
- 选中物体 - 右键 - mirror
- 修改器: ...

## Looking for some info
- 绝对变换: ![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/7rcv3.png)

## 缩小物体
打开 Blender 加载模型后，选中模型，按Tab键切换到编辑模式，接着用快捷键B框选或C刷选需要缩小的顶点。
按快捷键S启动缩放功能，拖动鼠标可自由缩小，若需精准比例缩小（如缩小至 50%），直接输入数值（如0.5），按下Enter键确认缩小操作。

## 旋转物体
- r, x, 输入角度

## 重设物体中心
- 编辑模式 -> 选中所有点 -> S -> 游标到物体 -> 物体模式 -> 顶部菜单-物体 > 设置原点 > 原点到 3D 游标

