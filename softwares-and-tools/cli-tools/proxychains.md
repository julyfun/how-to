---
author: julyfun
location: 杭州，刚从 SJTU 回来
date: 2024-1-31
system: Ubuntu 22.04
---

首先需要一个梯子。比如 clash-for-windows + 一个机场，clash-for-windows 的 port 为 7890

## 安装 proxychains

ref: https://zhuanlan.zhihu.com/p/166375631

```
sudo apt install proxychains
```

## 配置 proxychains

```
sudo vim /etc/proxychains.conf
```

- （可能不需要）取消前面 `dynamic_chain` 的注释；注释掉 `strict_chain`
- 在末尾 `[ProxyList]` 中添加 `socks5 127.0.0.1 7890` 其中端口号取决于你 vpn 的 port

## （可能不需要）设置 git 的代理

```
git config --global https.proxy 'socks://127.0.0.1:7890'
git config --global http.proxy 'http://127.0.0.1:7890'
```

## （可能不需要）检查 Shell 配置文件中是否正确配置了 proxy 环境变量

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

