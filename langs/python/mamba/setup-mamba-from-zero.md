---
title: "Setup mamba from zero"
date: 2025-07-09 17:36:20
tags: ["langs", "python", "mamba"]
author: "Julyfun M4"
os: "Ubuntu 22.04"
assume-you-know: [conda]
---

```console
# can't be 1.bash
curl -fsSL https://github.com/conda-forge/miniforge/releases/download/25.3.0-3/Miniforge3-25.3.0-3-Linux-x86_64.sh > 1.sh
bash 1.sh
# this will modify rc, assume you use fish
~/miniforge3/bin/conda init fish
conda config --set auto_activate_base false
# add this to rc
/home/julyfun/miniforge3/bin/mamba shell hook --shell fish | source
# Note: mamba can't init fish 4.0. See https://github.com/mamba-org/mamba/issues/3847
#   Use micromamba instread.
```

Works today!

