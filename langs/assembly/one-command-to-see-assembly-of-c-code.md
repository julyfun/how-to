---
title: one-command-to-see-assembly-of-c-code
date: 2024-02-21 21:40:01
tags: []
---
```
gcc -c 1.c && objdump -Sd 1.o | nvim
```

