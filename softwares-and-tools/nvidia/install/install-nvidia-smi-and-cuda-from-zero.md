---
reliability: "[0% (author), 0 / 0 (visitor)]"
language: "zh-hans"
os: "Darwin 192.168.124.17 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1 20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64"
author: "Julyfun MacOS14.5 M1"
suppose-you-know: [computer]
date: 2024-06-26
title: "Install nvidia-smi and cuda from zero"
---

# Install nvidia-smi and cuda from zero

Now, you don't even have `nvidia-smi`

- developer.nvidia.com/cuda-download
- From archives, choose a version you like
- select system and run `.deb` or `.run`

the `.deb` way sometimes failed in the last step.

If so, try this: https://blog.csdn.net/u011119817/article/details/100520669

```
ubuntu-drivers devices
sudo ubuntu-drivers auto-install
sudo reboot
```

## 据我所知有几种方法，以下每一行是一个方法

- 系统应用程序 Softwares & Updates 直接下载驱动
- 进入文本界面，关闭图形化服务，运行 .run
- sudo ubuntu-drivers auto-install

