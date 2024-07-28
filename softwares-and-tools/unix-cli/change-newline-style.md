---
reliability: "[20% (author), 0 / 0 (visitor)]"
date: 2024-06-25
language: "Chinese"
os: "Darwin 192.168.124.17 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1 20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64"
author: "Julyfun MacOS14.5 M1"
suppose-you-know: [computer]
keywords: []
---

ref: https://stackoverflow.com/questions/2613800/how-to-convert-dos-windows-newline-crlf-to-unix-newline-lf

ref: https://unix.stackexchange.com/questions/32001/what-is-m-and-how-do-i-get-rid-of-it

在 vim 中执行以下两行可以把 dos 类型的 CRLF 改为 unix LF:

```
:set ff=unix
:e ++ff=dos 
```

