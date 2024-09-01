- reliability: "40% (author)"
- date: 2024-09-01
- language: "zh-hans"
- os: "Linux server 5.15.0-117-generic #127~20.04.1-Ubuntu SMP Thu Jul 11 15:36:12 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux"
- author: "julyfun on yuanzhi laptop-server"
- assume-you-know: [computer]

# Linux VsCode 无法输入中文

ref: https://www.cnblogs.com/dechinphy/p/vscode-cn.html

可能是使用了 snap 阉割版的 code 导致的。

```
sudo snap remove code
```

然后使用官网的 code.

> verified on ubuntu 22.04, 24.9.1

