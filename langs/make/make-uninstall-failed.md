---
title: make-uninstall-failed
date: 2024-01-15 01:10:05
tags: []
---
## 现象

无法构建 uninstall.

## Solution

```
xargs rm < install_manifest.txt
```

