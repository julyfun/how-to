---
title: internal-if-or-if-you-wanna-call-it-filter
date: 2024-01-15 01:10:05
tags: ["langs", "python"]
---
use filter.

```py
    e = list(filter(lambda x: x is not None, [None if random.random() < 0.75 else (i, j) 
            for i in range(1, n) for j in range(i + 1, n + 1)]))
```

also:

```py
    edges = [(i, j) for i in range(1, n) for j in range(i + 1, n + 1) if random.random() < 0.75]
```
