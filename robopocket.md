---
title: "RoboPocket"
date: 2025-01-11 02:41:38
tags: ["robopocket"]
author: "julyfun arch y9000p"
os: "Linux archfun 6.18.2-arch2-1 #1 SMP PREEMPT_DYNAMIC Thu, 18 Dec 2025 18:00:18 +0000 x86_64 GNU/Linux"
assume-you-know: [computer]
confidence: 2
---

## Preview v0.2.3
### Performance
- BSON 写入速度提升 200 倍.

### Upload
- 上传队列新增 Rerun 按钮
- Rerun 视频播放器添加进度条
- 修复 UploadQueueView 中的手势拦截问题，现在可以正常滚动列表。

### General
- 重构到 Swift 6 语言版本

## Preview v0.2.2
### DAgger
- 添加 vizNum 和 action horizon 滑动条，可分别调整可视化数量和动作预测时域。

### Record
- 录制数据格式 (.bson) 新增字段：
  - `problems`: 记录录制过程中的问题和异常
  - `extra.rawFeaturePoints`: 原始 AR 特征点数据，便于后续离线分析

## Preview v0.2.1
### DAgger
- 新增容忍度滑动条。推荐在早期 Follow up 时提高容忍度，后期降低容忍度以精确复刻机器人轨迹.

### Record
- 录制结束时添加上传/删除最近一条的按钮，十分的方便.

### UI
- 首页添加低电量模式、电量和热量检查.
- 退出重进录制界面将会保留上一次左右分割 UI 的比例.
- 调整控制面板，主要按钮提前.
- 统一工具面板的点按逻辑，去除长按.

