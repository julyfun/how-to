---
reliability: "[70% (author), 0 / 0 (visitor)]"
date: 2024-05-08
language: "English"
os: "Darwin floriandeMacBook-Air.local 22.5.0 Darwin Kernel Version 22.5.0: Mon Apr 24 20:53:44 PDT 2023; root:xnu-8796.121.2~5/RELEASE_ARM64_T8103 arm64"
author: "Julyfun MacOS13.4 M1"
suppose-you-know: [computer]
keywords: []
---

# Enable mouse

ref: https://www.nodeseek.com/post-18315-1
ref: https://unix.stackexchange.com/questions/516800/how-do-i-enable-tmux-mouse-support

for `tmux 3.0a` on ubuntu 20.04:

```
ctrl + b
:set -g mouse on
```

## In source file

you can add that command to `~/.tmux.conf` (with no `:`)

and then:

```
exit tmux
tmux kill-server
tmux
```

> verified on 24.5.9, ubuntu 20.04, 4090
> verified on 24.5.10

