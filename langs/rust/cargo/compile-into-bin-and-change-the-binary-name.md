---
title: compile-into-bin-and-change-the-binary-name
date: 2024-01-15 01:10:05
tags: ["langs", "rust", "cargo"]
---
According to:

https://www.rustadventure.dev/building-a-digital-garden-cli/structopt-0.3/changing-the-name-of-the-default-cargo-binary

In the `Cargo.toml`:

```toml
[[bin]]
name = "garden"
path = "src/main.rs"
```

## How to get the bin file

When you try `cargo run` or `cargo build`, it automatically build a bin file called like `target/release/rust`.

