---
title: Use clash on remote linux, using pure cli
date: 2024-07-29 01:21:57
tags: []
---
# Use clash on remote linux, using pure cli
- date: 2024-07-29
- os: ubuntu 22.04
- author: Julyfun MacOS14.5 M1
- suppose-you-know: nothing

> These are minimal steps

- Get a web url for vpn subscription
- Use this shell tool: see: https://github.com/Elegycloud/clash-for-linux-backup (some clash core are included)
- Use `proxychains`. Search `proxychains` under this how-to repo.

> Verified on 24.7.29
>
> On 24.7.30, it crashed. Successfully restarted by using tmux on remote, kill and start the whole clash-for-linux-backup. If UI is missing, try `killall clash-for-linux`

