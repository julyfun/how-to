---
reliability: "20% (author)"
language: "zh-hans"
os: "Darwin floriandeAir 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1 20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64"
author: "Julyfun MacOS14.5 M1"
assume-you-know: [computer]
date: 2024-08-19
title: git status 显示中文乱码
tags: []
---

# git status 显示中文乱码

```
git config --global core.quotepath false 
git config --global gui.encoding utf-8
git config --global i18n.commit.encoding utf-8 
git config --global i18n.logoutputencoding utf-8 
```

再执行 `git status` 发现能正常显示中文了。

> verified in env above

