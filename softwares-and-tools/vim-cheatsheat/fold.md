---
title: "fold"
date: 2025-11-07 04:59:25
tags: ["softwares-and-tools", "vim-cheatsheat"]
author: "julyfun-4070s-ubuntu2204"
os: "Linux julyfun-4070s-ubuntu 6.8.0-84-generic #84~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Tue Sep  9 14:29:36 UTC 2 x86_64 x86_64 x86_64 GNU/Linux"
assume-you-know: [computer]
confidence: 4
---

- zc: fold subscope
- zo: unfold subscope

- zC: fold current scope
- zO: unfold current scope

- zM: fold all
- zR: unfold all

```zig
//  This is current scope.
//  │       Cursor here.
//  ↓       │    This is subscope.
    { //    ↓    ↓
        comptime {

        }
    }
```

