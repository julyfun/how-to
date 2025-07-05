---
reliability: 20% (author)
os: 'Linux DESKTOP-VDB57PP 5.15.153.1-microsoft-standard-WSL2+ #2 SMP Sun Oct 27 22:02:06
  CST 2024 x86_64 x86_64 x86_64 GNU/Linux'
author: 4070s wsl julyfun
assume-you-know:
- computer
date: 2024-11-01
title: devices[i].processes[j].gpu_memory_percentage <= 100
tags: ["os", "windows", "wsl", "nvidia"]
---
# devices[i].processes[j].gpu_memory_percentage <= 100

```
nvtop: ./src/extract_gpuinfo.c:205: gpuinfo_populate_process_infos: Assertion `devices[i].processes[j].gpu_memory_percentage <= 100' failed.
[2] 28194 IOT instruction nvtop
```

Solution:

```
sudo add-apt-repository ppa:flexiondotorg/nvtop
sudo apt install nvtop
```

> ok on 24.11.1 

