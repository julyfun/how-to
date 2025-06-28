---
title: nvidia-driver.1
date: 2024-01-15 01:10:05
tags: []
---
test on: 16.04

```
Linux ubuntu16-1080Ti 4.15.0-112-generic #113~16.04.1-Ubuntu SMP Fri Jul 10 04:37:08 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
```

## nvidia-smi and nvidia-detector

看起来天生自带的。

Now, nvidia-detector cmd shows `none`.

## when there's no nvidia-smi

我 `apt install nvidia-384` 然后报错了，直接搞没啦！

```
junjie@ubuntu16-1080Ti:~$ nvidia-smi
Failed to initialize NVML: Driver/library version mismatch
```

Well you should reboot! as in https://stackoverflow.com/questions/43022843/nvidia-nvml-driver-library-version-mismatch

如果不行，执行下面的东西，你看得懂吧？

https://askubuntu.com/questions/902636/nvidia-smi-command-not-found-ubuntu-16-04

```
sudo apt purge nvidia-*
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt update
sudo apt install nvidia-384
```

