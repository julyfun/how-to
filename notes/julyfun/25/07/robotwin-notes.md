---
title: "RoboTwin notes"
date: 2025-07-10 16:34:31
tags: ["notes", "julyfun", "RoboTwin", "simulation", "manipulation"]
author: "Julyfun M4"
os: "Ubuntu22.04 4070S"
assume-you-know: [computer]
---

## Menu
数据集目录 https://robotwin-platform.github.io/doc/tasks/index.html

## Setup notes
uv setup.
- [note] `uv pip install "git+https://github.com/facebookresearch/pytorch3d.git@stable" --no-build-isolation`
- OK. all setup.

## Visualize collection process

task-config 仅含环境配置. `bash collect_data.sh beat_block_hammer demo_randomized 0` 中，demo_randomized 寻找环境 .yml，beat_block_hammer 则寻找 .py.

