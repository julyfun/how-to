---
type: verified
language: "Chinese"
os: "Darwin floriandeMacBook-Air.local 22.5.0 Darwin Kernel Version 22.5.0: Mon Apr 24 20:53:44 PDT 2023; root:xnu-8796.121.2~5/RELEASE_ARM64_T8103 arm64"
author: "Julyfun MacOS13.4 M1"
suppose-you-know: [computer]
date: 2024-04-06
title: How to publish a package on crates.io correctly?
tags: []
---

# How to publish a package on crates.io correctly? 

> 在 crates.io 发布 0.1.1 版本后，接下来的小改动先上传到 github 上，此时是否如何修改 `Cargo.toml` 中的版本号（比如修改为 0.1.2 或 0.1.1.1）？

根据 https://github.com/rust-random/rand/blob/master/Cargo.toml 中的做法，在已发布到 crates.io 的版本基础上进行的小改动不修改版本号，仍然是 0.1.1。

