---
title: rsproxy-sparse
date: 2024-07-30 21:59:01
tags: ["mirrors", "rust"]
---
# rsproxy-sparse

??? info "Problem environment"

    - author: Julyfun MacOS14.5 M1
    - edited date: 2024-07-30
    - expected environment: Darwin floriandeMacBook-Air.local 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1 20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64

## Details of the problem / Steps to reproduce the error

_No details_

---

## Answer 1

??? info "Answer environment"

    - author: As in the problem
    - edited date: As in the problem
    - verified environment: As in the problem

### TLDR

in `~/.cargo/config.toml`

```
[source.crates-io]
replace-with = 'rsproxy-sparse'
[source.rsproxy]
registry = "https://rsproxy.cn/crates.io-index"
[source.rsproxy-sparse]
registry = "sparse+https://rsproxy.cn/index/"
[registries.rsproxy]
index = "https://rsproxy.cn/crates.io-index"
[net]
git-fetch-with-cli = true
```

- ref: https://rsproxy.cn/

