---
type: verified
language: "Chinese"
os: "Darwin floriandeMacBook-Air.local 22.5.0 Darwin Kernel Version 22.5.0: Mon Apr 24 20:53:44 PDT 2023; root:xnu-8796.121.2~5/RELEASE_ARM64_T8103 arm64"
author: "Julyfun MacOS13.4 M1"
suppose-you-know: [computer]
date: 2024-04-28
title: How do I write a Rust unit test that ensures that a panic has occurred?
---

# How do I write a Rust unit test that ensures that a panic has occurred?

ref: https://stackoverflow.com/questions/26469715/how-do-i-write-a-rust-unit-test-that-ensures-that-a-panic-has-occurred

```
#[test]
#[should_panic(expected = "invalid var name: \"1x\"")]
fn test_invalid_name() {
    let s = "(let (1x 2) 3)";
    let _ = parse(s);
}
```

