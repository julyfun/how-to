---
title: kex_exchange_identification: Connection closed by remote host
date: 2024-05-06 11:06:10
tags: []
---
# kex_exchange_identification: Connection closed by remote host

??? info "Problem environment"

    - expected environment: unix

## Details of the problem / Steps to reproduce the error

Some time when you try to connect to github, you may get this error:

```
kex_exchange_identification: Connection closed by remote host
```

### TLDR

Add this to your `~/.ssh/config`:

```
Host github.com
  Hostname 20.200.245.248
  Port 443
```

### What I've done before the problem is solved (don't know which one worked):

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

### Post test

- reopen clash for windows: still ok to ssh
- git clone: ok
- git pull and push: ok

### 24.9.27

- windows 上和 wsl2 中无法访问阿里云服务器 ssh
- solve: 关闭了 Clash Verge 的服务模式（未关闭 tun）
- solve2: 开启服务模式 + TUN 并选择直连也可以。这台机子如果不开 TUN, wsl2 的网速异常龟速，即使 win 内的网速正常。

