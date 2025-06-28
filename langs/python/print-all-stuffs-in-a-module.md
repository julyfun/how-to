---
title: "print-all-stuffs-in-a-module"
date: 2024-01-15 01:10:05
tags: []
---

TL;DR of answers below: use dir to return functions and variables; use inspect to filter functions only; and use ast to parse without importing. – 
Jonathan H
 Mar 20, 2018 at 9:55 

```py
import mod
print(dir(mod))
```

https://stackoverflow.com/questions/139180/how-to-list-all-functions-in-a-module

