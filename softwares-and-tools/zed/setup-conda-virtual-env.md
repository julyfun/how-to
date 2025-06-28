---
reliability: "0% (author)"
os: "Darwin floriandeMacBook-Air.local 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1 20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64"
author: "Julyfun MacOS14.5 M1"
assume-you-know: [computer]
date: 2024-09-17
title: "Setup conda virtual env"
tags: []
---

# Setup conda virtual env

see: https://github.com/zed-industries/zed/discussions/6564

pyrightconfig.json:

```json
{
  "venv": "envname",
  "venvPath": "/home/user/miniforge3/envs"
}
```

or pyrightconfig.json:

```json
{
  "executionEnvironments": [
    {
      "python": "<path_to_conda_env>/bin/python"
    }
  ]
}
```

