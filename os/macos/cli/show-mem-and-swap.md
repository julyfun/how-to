---
ref: false
date: 2024-10-29 18:42:52
title: show-mem-and-swap
tags: ["os", "macos", "cli"]
---
```
top -l 1 -s 0 | grep PhysMem
sysctl -n vm.swapusage
```

> verified on mac 14.5

