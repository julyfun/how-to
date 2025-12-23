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

## 数据集大纲

```
HDF5 File: /home/julyfun/Documents/GitHub/RoboTwin2.0/data/beat_block_hammer/demo_randomized/data/episode0.hdf5
Content Outline:
Group: endpose
Group: joint_action
  Dataset: joint_action/left_arm (Shape: (116, 6), Type: float64)
  Dataset: joint_action/left_gripper (Shape: (116,), Type: float64)
  Dataset: joint_action/right_arm (Shape: (116, 6), Type: float64)
  Dataset: joint_action/right_gripper (Shape: (116,), Type: float64)
  Dataset: joint_action/vector (Shape: (116, 14), Type: float64)
Group: observation
  Group: observation/front_camera
    Dataset: observation/front_camera/cam2world_gl (Shape: (116, 4, 4), Type: float32)
    Dataset: observation/front_camera/extrinsic_cv (Shape: (116, 3, 4), Type: float32)
    Dataset: observation/front_camera/intrinsic_cv (Shape: (116, 3, 3), Type: float32)
    Dataset: observation/front_camera/rgb (Shape: (116,), Type: |S16480)
# 图像可能被编码为 Base64 字符串
  Group: observation/head_camera
    Dataset: observation/head_camera/cam2world_gl (Shape: (116, 4, 4), Type: float32)
    Dataset: observation/head_camera/extrinsic_cv (Shape: (116, 3, 4), Type: float32)
    Dataset: observation/head_camera/intrinsic_cv (Shape: (116, 3, 3), Type: float32)
    Dataset: observation/head_camera/rgb (Shape: (116,), Type: |S21457)
  Group: observation/left_camera
    Dataset: observation/left_camera/cam2world_gl (Shape: (116, 4, 4), Type: float32)
    Dataset: observation/left_camera/extrinsic_cv (Shape: (116, 3, 4), Type: float32)
    Dataset: observation/left_camera/intrinsic_cv (Shape: (116, 3, 3), Type: float32)
    Dataset: observation/left_camera/rgb (Shape: (116,), Type: |S17777)
  Group: observation/right_camera
    Dataset: observation/right_camera/cam2world_gl (Shape: (116, 4, 4), Type: float32)
    Dataset: observation/right_camera/extrinsic_cv (Shape: (116, 3, 4), Type: float32)
    Dataset: observation/right_camera/intrinsic_cv (Shape: (116, 3, 3), Type: float32)
    Dataset: observation/right_camera/rgb (Shape: (116,), Type: |S12776)
Dataset: pointcloud (Shape: (116, 0), Type: float64)
```

