---
reliability: "[20% (author), 0 / 0 (visitor)]"
language: "en"
os: "Darwin floriandeMacBook-Air.local 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1 20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64"
author: "Julyfun MacOS14.5 M1"
suppose-you-know: [computer]
date: 2024-07-12
title: Can't display Chinese
---

# Can't display Chinese

ref: https://blog.csdn.net/weixin_39792252/article/details/80415550

verified on: docker, webtop - ubuntu-kde 22.04

```
sudo apt-get install language-pack-zh-hans
```

append this in `/etc/environment`

```
LANG="zh_CN.UTF-8"
LANGUAGE="zh_CN:zh:en_US:en"
```

touch file `/var/lib/locales/supported.d/local` and add:

```
en_US.UTF-8 UTF-8
zh_CN.UTF-8 UTF-8
```

```
sudo locale-gen
`sudo locale-gen
``

- Install chinese fonts. 

```
sudo locale-gen
```

- No need to reboot.

