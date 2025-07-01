---
title: nvcc-shows-wrong-version
date: 2024-03-21 09:26:42
tags: ["softwares-and-tools", "nvidia"]
---
## check your /usr/local/

if there is cuda-right-version, it's easy to fix this problem;

```
export CUDA_HOME=/usr/local/cuda-9.2
export PATH=/usr/local/cuda-9.2/bin:$PATH
```

> Reproduced and solved on 2024-2-1.

