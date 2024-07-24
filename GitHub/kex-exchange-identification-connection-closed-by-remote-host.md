---
type: draft
date: 2024-05-06
language: "Chinese"
os: "Linux julyfun-Lenovo-XiaoXinAir-14IIL-2020 5.19.0-46-generic #47~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Wed Jun 21 15:35:31 UTC 2 x86_64 x86_64 x86_64 GNU/Linux"
author: "Julyfun Ubuntu22.04 amd64"
suppose-you-know: [computer]
keywords: []
---

# kex_exchange_identification: Connection closed by remote host

## What I've done before the problem is solved (don't know which one worked):

- Close clash for windows
- cancel `http_proxy` and other proxy ports in shell config file (config.fish) and `~/.gitconfig`
- delete all content in `~/.ssh/known_hosts`
- ref: `https://github.com/orgs/community/discussions/55269`, use `ssh -Tv -p 443 git@ssh.github.com`, or add this to `~/.ssh/config`:

```
Host github.com
  Hostname 20.200.245.248
  Port 443
```

> verified on 24/5/28, for a new user on Ubuntu, adding this content to `config` is useful.
> verified on 24/7/24, worked for wsl when suddenly can't connect git by cli.

## Post test

- reopen clash for windows: still ok to ssh
- git clone: ok
- git pull and push: ok


