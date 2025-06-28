---
reliability: "[20% (author), 0 / 0 (visitor)]"
language: "zh-hans"
os: "Darwin floriandeMacBook-Air.local 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1 20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64"
author: "Julyfun MacOS14.5 M1"
suppose-you-know: [computer]
date: 2024-07-01
title: To install
---

# To install

by poe:

```
sudo apt-get update
sudo apt-get install -y software-properties-common
sudo apt-get install -y wget
wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key | sudo apt-key add -
sudo add-apt-repository "deb http://apt.llvm.org/$(lsb_release -cs)/ llvm-toolchain-$(lsb_release -cs)-18 main"
sudo apt update
```

Now install freely. like:

```
sudo apt install clangd-18
```

This will install a bin file named clangd-18.

> verified on 24.7.11, on wsl

