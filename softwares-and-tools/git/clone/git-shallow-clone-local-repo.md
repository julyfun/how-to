---
type: verified
language: Chinese
os: 'Darwin floriandeMacBook-Air.local 22.5.0 Darwin Kernel Version 22.5.0: Mon Apr
  24 20:53:44 PDT 2023; root:xnu-8796.121.2~5/RELEASE_ARM64_T8103 arm64'
author: Julyfun MacOS13.4 M1
suppose-you-know:
- computer
date: 2024-04-22
title: Git shallow clone local repo
tags: ["softwares-and-tools", "git", "clone"]
---
# Git shallow clone local repo

ref: https://stackoverflow.com/questions/40383230/git-clone-warning-depth-is-ignored-in-local-clones-use-file-instead

```
git clone --depth 1 file://$(pwd)/src_repo new_repo
```

