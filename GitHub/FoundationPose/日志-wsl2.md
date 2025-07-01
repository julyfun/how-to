---
reliability: 20% (author)
os: 'wsl2 in win11, cuda 12.3, Driver Version: 560.94, 4070s'
author: Julyfun MacOS14.5 M1
assume-you-know:
- computer
date: 2024-10-29
title: 日志 install on wsl2
tags: ["GitHub", "FoundationPose"]
---
# 日志 install on wsl2

- xhost: command not found, when `bash docker/run_container.sh`
    - `winget install vcxsrv` on windows and `sudo apt install x11-xserver-utils x11-apps`
    - done.
- `subprocess-exited-with-error` when `bash build_all.sh`
    - ref: https://github.com/NVlabs/FoundationPose/issues/117
        - Try setting `$CUDA_HOME` systemwide, in `/etc/bash.bashrc` (neither `/etc/environment` nor `/etc/profile`)
        - I did it, it does not work but I went on:
    - ref: https://github.com/NVlabs/FoundationPose/issues/27
        - Use this instead of the original docker pull:
        - `docker pull shingarey/foundationpose_custom_cuda121:latest && docker tag shingarey/foundationpose_custom_cuda121 foundationpose`
- ok to run `python run_demo.py` !

