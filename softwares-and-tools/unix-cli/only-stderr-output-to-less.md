---
type: verified
language: Chinese
os: 'Darwin floriandeMacBook-Air.local 22.5.0 Darwin Kernel Version 22.5.0: Mon Apr
  24 20:53:44 PDT 2023; root:xnu-8796.121.2~5/RELEASE_ARM64_T8103 arm64'
author: Julyfun MacOS13.4 M1
suppose-you-know:
- computer
date: 2024-04-11
title: Only stderr output to less
tags: ["softwares-and-tools", "unix-cli"]
---
# Only stderr output to less

```sh
./1 light2.ppm 2>&1 >/dev/null | less
```

