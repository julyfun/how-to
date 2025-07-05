---
reliability: '[60% (author), 0 / 0 (visitor)]'
language: Chinese
os: 'Darwin floriandeMacBook-Air.local 22.5.0 Darwin Kernel Version 22.5.0: Mon Apr
  24 20:53:44 PDT 2023; root:xnu-8796.121.2~5/RELEASE_ARM64_T8103 arm64'
author: Julyfun MacOS13.4 M1
suppose-you-know:
- computer
date: 2024-05-10
title: how to set up config.fish to auto run tmux every time start fish
tags: ["softwares-and-tools", "unix-cli", "tmux"]
---
# how to set up config.fish to auto run tmux every time start fish

ref: https://github.com/fish-shell/fish-shell/issues/4434

add this to the end of `config.fish`:

```
if status is-interactive
and not set -q TMUX
    exec tmux
end
```

