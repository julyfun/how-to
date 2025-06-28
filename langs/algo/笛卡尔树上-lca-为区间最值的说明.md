---
reliability: "20% (author)"
language: "zh-hans"
os: "Darwin floriandeMacBook-Air.local 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1 20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64"
author: "Julyfun MacOS14.5 M1"
assume-you-know: [computer]
date: 2024-08-28
title: "笛卡尔树上 LCA 为区间最值的说明"
tags: []
---

# 笛卡尔树上 LCA 为区间最值的说明

若 x, y 的 LCA 为 a，则 a 为 x ~ y 的区间最小值。

- 每个结点的左延伸和右延伸是它作为最小值的极限范围
    - 因为左链再左边一个元素是你的某个祖先，而你的祖先都比你小
    - 而且你的子树中你是最小的
- 设 a 为 x, y 的 LCA。则必有其中一个在 a 左子树中（设为 x），y 在 a 右子树中
    - 故 x 在 a 左边，y 在 a 右边
    - 而且 x, y 在 a 作为最小值的范围内
- 补充：考虑 a 的父亲 f，由于 a 是 f 的子树故 x 和 y 都在 f 的同一边。故 f 不是在 x ~ y 区间内

