---
reliability: "20% (author)"
os: "Linux DESKTOP-VDB57PP 5.15.153.1-microsoft-standard-WSL2+ #2 SMP Sun Oct 27 22:02:06 CST 2024 x86_64 x86_64 x86_64 GNU/Linux"
author: "4070s wsl julyfun"
assume-you-know: [computer]
date: 2024-11-24
title: npm.ps1，因为在此系统上禁止运行脚本
tags: []
---

# npm.ps1，因为在此系统上禁止运行脚本

ref: https://blog.csdn.net/pro_fan/article/details/120457551

```
在终端输入get-ExecutionPolicy查看执行策略/权限；
输出Restricted(受限制的)；
终端输入Set-ExecutionPolicy -Scope CurrentUser命令给用户赋予权限；
输入RemoteSigned；
终端输入get-ExecutionPolicy查看一下权限，显示RemoteSigned就可以了。
```

- [ok], 24.11.24

