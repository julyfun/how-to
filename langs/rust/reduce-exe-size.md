---
title: reduce-exe-size
date: 2024-01-15 01:10:05
tags: ["langs", "rust"]
---
```toml
[profile.release]
opt-level = 'z'     # Optimize for size
lto = true          # Enable link-time optimization
codegen-units = 1   # Reduce number of codegen units to increase optimizations
panic = 'abort'     # Abort on panic
strip = true        # Strip symbols from binary*
```

