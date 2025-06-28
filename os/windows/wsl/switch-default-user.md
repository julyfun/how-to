---
reliability: "[20% (author), 0 / 0 (visitor)]"
language: "Chinese"
os: "Darwin floriandeMacBook-Air.local 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1 20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64"
author: "Julyfun MacOS14.5 M1"
suppose-you-know: [computer]
date: 2024-05-19
title: "Switch default user"
---

# Switch default user

In windows terminal:

ref: https://blog.csdn.net/qq_37085158/article/details/131041223

First, 

```
adduser <name>
usermod -aG sudo <name>
```

```
ubuntu2204.exe config --default-user <name>
```

> 可能使用 ubuntu.exe

