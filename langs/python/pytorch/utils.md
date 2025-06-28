---
title: "Pytorch utils"
date: 2025-06-24 14:36:22
tags: []
---

## print parameters num

sum(p.numel() for p in model.parameters())

```python
def numel(model):
    return sum(p.numel() for p in model.parameters())
```

