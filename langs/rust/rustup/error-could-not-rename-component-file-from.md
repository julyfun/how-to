---
reliability: "[20% (author), 0 / 0 (visitor)]"
date: 2024-07-14
language: "zh-hans"
os: "Darwin floriandeMacBook-Air.local 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1 20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64"
author: "Julyfun MacOS14.5 M1"
suppose-you-know: [computer]
keywords: []
---

# error: could not rename component file from

ref: https://github.com/rust-lang/rustup/issues/2729

> This happens if the component file gets corrupted. The easiest fix is to uninstall and reinstall the toolchain.

```
    3  rustup toolchain uninstall stable-aarch64-unknown-linux-gnu
    4  rustup toolchain install stable-aarch64-unknown-linux-gnu
```

verified in arm linux docker.

