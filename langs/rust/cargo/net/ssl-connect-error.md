---
reliability: '[35% (author), 0 / 0 (visitor)]'
language: en
os: 'Darwin floriandeAir.bbrouter 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1
  20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64'
author: Julyfun MacOS14.5 M1
suppose-you-know:
- computer
date: 2024-06-16
title: SSL connect error
tags: ["langs", "rust", "cargo", "net"]
---
# SSL connect error

```
warning: spurious network error (3 tries remaining): [35] SSL connect error (Recv failure: Connection reset by peer)
```

ref: https://stackoverflow.com/questions/41937618/cargo-is-unable-to-download-a-file-due-to-a-ssl-connect-error

Try something like:

```
CARGO_HTTP_CHECK_REVOKE=false cargo add xxx
```

## Or

Create `~/.cargo/config.toml` and add

```
[http]
check-revoke = false
```

