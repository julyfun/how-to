---
title: "Compiler PKU"
date: 2025-12-25 03:32:10
tags: ["25", "12"]
author: "julyfun-4070s-ubuntu2204"
os: "Linux julyfun-4070s-ubuntu 6.8.0-90-generic #91~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Thu Nov 20 15:20:45 UTC 2 x86_64 x86_64 x86_64 GNU/Linux"
assume-you-know: [computer]
confidence: 2
---

bookmark
- https://pku-minic.github.io/online-doc/#/lv0-env-config/docker
- https://github.com/pku-minic/koopa/blob/master/koopa/examples/brainfuck/main.rs

execute
- `docker run -it --rm -v /home/julyfun/Documents/GitHub/julyfun/compiler/:/root/compiler maxxing/compiler-dev bash`
- `cargo run -- -koopa hello.c -o hello.koopa`

## Lv0
## Lv1
- sysy: C-like lang for education
