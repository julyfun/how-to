---
reliability: "20% (author)"
os: "Linux server 5.15.0-122-generic #132~20.04.1-Ubuntu SMP Fri Aug 30 15:50:07 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux"
author: "julyfun on shadow251"
assume-you-know: [computer]
date: 2024-09-29
title: "Restart network"
tags: []
---

# Restart network

Ubuntu 22.04

```
service network-manager restart
# or
sudo systemctl restart NetworkManager
```

