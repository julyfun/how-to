---
title: "Setup mamba from zero"
date: 2025-07-09 17:36:20
tags: ["langs", "python", "mamba"]
author: "Julyfun M4"
os: "Darwin tutianpeikeladeMac-mini.local 24.3.0 Darwin Kernel Version 24.3.0: Thu Jan  2 20:22:58 PST 2025; root:xnu-11215.81.4~3/RELEASE_ARM64_T8132 arm64"
assume-you-know: [conda]
---

```console
# can't be 1.bash
curl -fsSL https://github.com/conda-forge/miniforge/releases/download/25.3.0-3/Miniforge3-25.3.0-3-Linux-x86_64.sh > 1.sh
bash 1.sh
# this will modify rc
~/miniforge3/bin/conda init fish
```

