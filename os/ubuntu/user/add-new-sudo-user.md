---
reliability: '[60% (author), 0 / 0 (visitor)]'
language: Chinese
os: 'Darwin floriandeMacBook-Air.local 22.5.0 Darwin Kernel Version 22.5.0: Mon Apr
  24 20:53:44 PDT 2023; root:xnu-8796.121.2~5/RELEASE_ARM64_T8103 arm64'
author: Julyfun MacOS13.4 M1
suppose-you-know:
- computer
date: 2024-05-09
title: Add new sudo user
tags: ["os", "ubuntu", "user"]
---
# Add new sudo user

ref: https://blog.csdn.net/u011119817/article/details/100709942

## Under root

```
adduser <name>
# type some unimportant infomation then

usermod -aG sudo <name>
```

## Appendix

```
# output user group
groups <name>
```

