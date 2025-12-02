---
title: "7月3日让网站支持 Typst"
date: 2025-07-03 17:29:13
tags: [notes, julyfun]
author: "Julyfun M4"
os: "Darwin tutianpeikeladeMac-mini.local 24.3.0 Darwin Kernel Version 24.3.0: Thu Jan  2 20:22:58 PST 2025; root:xnu-11215.81.4~3/RELEASE_ARM64_T8132 arm64"
assume-you-know: [computer]
---

过程挺浪费时间的. 首先探索 Wypst 方案，发现支持不太行，很难成功 `bun dev`。Wypst 不维护了应该也是因为 typst 已经支持导出 svg 了，手动转义 AST 到 latex symbol 有点原始人了.

Obsidian-wypst 更是依赖极其原始的 wypst:0.4.0。感觉 npm 这套依赖管理的 backward compability 和一致性不怎么样.

谷歌找到 "@myriaddreamin/rehype-typst"，尝试替代 `rehype-mathjax`。这是直接用 typst wasm 导出 svg. 但是这玩意儿怎么依赖 katex 呢，有点怪.

起初渲染 typst 公式颜色不对，且独占一行. 使用 `https://hanwen.io/zh/posts/use_typst_for_math_in_blog/` 中的 css + AI 写的 typst-inline 检测，看起来正常多了. 折腾了几个 commit 以后成功渲染 typst, 缺点是只支持 typst 而不支持 latex. 如果任何 `$` 后不符合 typst 语法都会导致一篇文章无法部署.

## Simple solution: see

- https://github.com/julyfun/yi-how-to/commit/38bb7c9d0c2f7ea81e06ccd44d5d7c6c6b0228a3
- https://github.com/julyfun/yi-how-to/commit/0e573417a4e19cd92abf0f46731dcb52b44155a0#diff-c1c322616098d4351e10768cd3ad654e2b79fcf30cff1606ff4e79b7893fbe5bR293

ref: https://hanwen.io/zh/posts/use_typst_for_math_in_blog/

## Typst 群友 @纸夜 做的 Typst 前端集成决策树.

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/f293f7c68160345a0feb00d31abead6c.png)

