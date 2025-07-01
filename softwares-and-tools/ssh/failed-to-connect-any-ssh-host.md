---
reliability: '[40% (author), 0 / 0 (visitor)]'
language: Chinese
os: Ubuntu
author: Julyfun MacOS14.5 M1
suppose-you-know:
- computer
date: 2024-05-28
title: Failed to connect any ssh host
tags: ["softwares-and-tools", "ssh"]
---
# Failed to connect any ssh host

env: ubuntu

ref: https://blog.csdn.net/C_W_0/article/details/122953132

- Please check first if you have installed `openssh`.
- And try restarting `sshd` service:

```
sudo service ssh restart
sudo service sshd restart
sudo /etc/init.d/ssh restart
```

> this worked, on 24/5/28, for a new user on Ubuntu.

