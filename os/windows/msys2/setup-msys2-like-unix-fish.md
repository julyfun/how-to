---
reliability: "20% (author)"
os: "Darwin floriandeMacBook-Air.local 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1 20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64"
author: "Julyfun MacOS14.5 M1"
assume-you-know: [computer]
date: 2024-09-24
title: "Setup MSYS2 like unix fish"
tags: []
---

# Setup MSYS2 like unix fish

## Start shell

In `msys2.ini`and `mingw64.ini`, add line:

```
SHELL=/usr/bin/fish
```

## conda

Install common win64 conda.

run `conda init fish` in powershell and copy contents in `C:/Users/<user>/.config/fish/config.fish` to msys2 path

