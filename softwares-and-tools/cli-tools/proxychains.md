---
author: julyfun
location: 杭州，刚从 SJTU 回来
system: Ubuntu 22.04
date: 2024-01-31
title: proxychains
tags: ["softwares-and-tools", "cli-tools"]
---
## 问题情况

从 SJTU 开着梯子访问 github 比较流畅，不排除是因为 SJTU 网络自带 github。回杭州以后开着梯子上 Ubuntu，能 Chrome 上 github 但命令行 ssh -T git@github.com 都不行。

> 其实写完此文以后第二天莫名其妙又可以直接 ssh -T git@github.com 了。

## 安装 proxychains

首先需要一个梯子。比如 clash-for-windows + 一个机场，clash-for-windows 的 port 为 7890

ref: https://zhuanlan.zhihu.com/p/166375631

```
sudo apt install proxychains
```

## 配置 proxychains

```
sudo vim /etc/proxychains.conf
```

- `dynamic_chain` 的注释；注释掉 `strict_chain`
- 在末尾 `[ProxyList]` 中添加 `socks5 127.0.0.1 7890` 其中端口号取决于你 vpn 的 port

## （通常不需要）设置 git 的代理

```
git config --global https.proxy 'socks://127.0.0.1:7890'
git config --global http.proxy 'http://127.0.0.1:7890'
```

## （通常不需要）检查 Shell 配置文件中是否正确配置了 proxy 环境变量

例如在 fish shell 中是：

```
set -gx https_proxy http://127.0.0.1:7890
set -gx http_proxy http://127.0.0.1:7890
set -gx all_proxy socks5://127.0.0.1:7890
```

## 使用 proxychains

```
proxychains ssh -T git@github.com
```

Output 例如：

```
ProxyChains-3.1 (http://proxychains.sf.net)
|DNS-request| github.com 
|D-chain|-<>-127.0.0.1:7890-<><>-4.2.2.2:53-<><>-OK
|DNS-response| github.com is 20.205.243.166
|DNS-request| github.com 
|D-chain|-<>-127.0.0.1:7890-<><>-4.2.2.2:53-<><>-OK
|DNS-response| github.com is 20.205.243.166
|D-chain|-<>-127.0.0.1:7890-<><>-20.205.243.166:22-<><>-OK
Hi julyfun! You've successfully authenticated, but GitHub does not provide shell access.
```

## 若 proxychains git push 要你输入 http://github.com 的若 

应该强制 git 走 ssh

ref: https://ricostacruz.com/posts/github-always-ssh

```
git config --global url."git@github.com:".insteadOf "https://github.com/"
```

> verified on 2024-5-6, ubuntu 20.04

