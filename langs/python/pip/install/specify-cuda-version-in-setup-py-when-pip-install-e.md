---
reliability: 20% (author)
os: 'Linux DESKTOP-VDB57PP 5.15.153.1-microsoft-standard-WSL2+ #2 SMP Sun Oct 27 22:02:06
  CST 2024 x86_64 x86_64 x86_64 GNU/Linux'
author: 4070s wsl julyfun
assume-you-know:
- computer
date: 2024-11-26
title: Specify cuda version in setup.py when pip install -e .
tags: ["langs", "python", "pip", "install"]
---
# Specify cuda version in setup.py when pip install -e .

see: https://stackoverflow.com/questions/66738473/installing-pytorch-with-cuda-in-setup-py

In setup function, use something like:

```
"torch@https://download.pytorch.org/whl/cu111/torch-1.8.0%2Bcu111-cp37-cp37m-linux_x86_64.whl",
"torchvision@https://download.pytorch.org/whl/cu111/torchvision-0.9.0%2Bcu111-cp37-cp37m-linux_x86_64.wh",
"torchaudio@https://download.pytorch.org/whl/torchaudio-0.8.0-cp36-cp36m-linux_x86_64.whl"
```

version links are from: https://download.pytorch.org/whl/torch_stable.html

- method above is ok to download, but still failed to build.

The following succeeds for building sam-2 with cu118:

```
pip install torch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 --index-url https://download.pytorch.org/whl/cu118
pip install --no-build-isolation -e .
# and delete these packages in `setup.py`
```

