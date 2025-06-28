---
reliability: "20% (author)"
os: "Linux DESKTOP-VDB57PP 5.15.153.1-microsoft-standard-WSL2+ #2 SMP Sun Oct 27 22:02:06 CST 2024 x86_64 x86_64 x86_64 GNU/Linux"
author: "4070s wsl julyfun"
assume-you-know: [computer]
date: 2024-11-24
title: Permission Denied when using docker from WSL
tags: []
---

# Permission Denied when using docker from WSL

ref: https://stackoverflow.com/questions/72528606/docker-rancher-permission-denied-when-using-docker-from-wsl

```
sudo addgroup --system docker
sudo adduser $USER docker
newgrp docker
# And something needs to be done so $USER always runs in group `docker` on the `Ubuntu` WSL
sudo chown root:docker /var/run/docker.sock
sudo chmod g+w /var/run/docker.sock
```

and remember to restart wsl to make this change eternal.

- [ok] 24.11.23, wsl ubuntu22.04

