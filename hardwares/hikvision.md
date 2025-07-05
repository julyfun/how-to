---
date: 2024-01-15 01:10:05
title: hikvision
tags: ["hikvision", "hardware", "cv", "hardwares"]
---
## libs

https://www.hikrobotics.com/cn/machinevision/service/download?module=0

copy your four `.so` to /usr/lib

## MVS 客户端参数测试

```toml
[客户端.右边.Image Processing]
Offset X = 有裁剪的情况下，你让画面从裁剪正中向右便宜多少
Offset Y = 向下偏移
```

修改相机名字：搜 user id

## 相机灯光状态

蓝灯一秒闪三次：软触发中

## 图像亮度

Gain Auto 调节成 Continuous 以后，亮度增益会根据 Brightness 参数自动调整，还不错捏。
