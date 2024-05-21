---
reliability: "[20% (author), 0 / 0 (visitor)]"
date: 2024-05-21
language: "Chinese"
os: "Darwin floriandeMacBook-Air.local 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1 20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64"
author: "Julyfun MacOS14.5 M1"
suppose-you-know: [computer]
keywords: []
---

# error: external filter 'git-lfs filter-process' failed

ref: https://blog.csdn.net/derteanoo/article/details/124432254

use this first:

```
git lfs install --skip-smudge
```

