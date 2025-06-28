---
title: "Update all submodules to latest commit"
date: 2024-07-28 22:03:59
tags: []
---
# Update all submodules to latest commit
- date: 2024-07-28
- os: Darwin floriandeMacBook-Air.local 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1 20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64
- author: Julyfun MacOS14.5 M1
- suppose-you-know: nothing

ref: https://stackoverflow.com/questions/5828324/update-git-submodule-to-latest-commit-on-origin

```
git submodule foreach git pull
```

