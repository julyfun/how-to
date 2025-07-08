---
title: "Pull remote main without checkout"
date: 2025-07-08 13:41:47
tags: ["softwares-and-tools", "git", "pull"]
author: "Julyfun M4"
os: "Darwin tutianpeikeladeMac-mini.local 24.3.0 Darwin Kernel Version 24.3.0: Thu Jan  2 20:22:58 PST 2025; root:xnu-11215.81.4~3/RELEASE_ARM64_T8132 arm64"
assume-you-know: [git pull]
---

强制更新本地 main 分支，使其与远程 main 分支保持一致 (移动语法, -f = force)

```
git branch -f main origin/main
```

