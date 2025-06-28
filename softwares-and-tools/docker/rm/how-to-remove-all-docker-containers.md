---
reliability: "20% estimated by the author"
language: "Chinese"
os: "Linux julyfun-Lenovo-XiaoXinAir-14IIL-2020 5.19.0-46-generic #47~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Wed Jun 21 15:35:31 UTC 2 x86_64 x86_64 x86_64 GNU/Linux"
author: "Julyfun Ubuntu22.04 amd64"
suppose-you-know: [computer]
date: 2024-05-06
title: "How to remove all Docker containers"
---

# How to remove all Docker containers

ref: https://stackoverflow.com/questions/35240278/how-to-remove-all-docker-containers

```
docker rm -v -f $(docker ps -qa)
# for fish
docker rm -v -f (docker ps -qa)
```

