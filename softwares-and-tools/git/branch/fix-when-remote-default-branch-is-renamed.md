---
type: verified
language: Chinese
os: 'Darwin floriandeMacBook-Air.local 22.5.0 Darwin Kernel Version 22.5.0: Mon Apr
  24 20:53:44 PDT 2023; root:xnu-8796.121.2~5/RELEASE_ARM64_T8103 arm64'
author: Julyfun MacOS13.4 M1
suppose-you-know:
- computer
date: 2024-04-21
title: Fix when remote default branch is renamed
tags: ["softwares-and-tools", "git", "branch"]
---
# Fix when remote default branch is renamed

ref: github tip

```
git branch -m <old> <new>
git fetch origin
git branch -u origin/<new> <new>
git remote set-head origin -a
```

