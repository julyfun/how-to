---
title: "Windows OI 评测机环境配置"
date: 2025-10-07 14:24:22
tags: ["notes", "julyfun", "25", "10"]
author: "Julyfun MacOS14.5 M1"
os: "Windows 10"
assume-you-know: [computer]
confidence: 2
---

1. GitHub 镜像下载 msys2
1. msys2 下载 mingw-w64-x86_64-gcc
1. GitHub 下载 LemonLime
1. Lemonlime 打开选择 `C:\msys2\mingw64\bin\g++.exe`
1. 询问豆包寻找测试数据链接（对于 NOIP, CSP-S 类赛事）
    - 可能的来源: noi.cn 各年`成绩和申诉`，这是最靠谱的
    - noi.cn `题目与数据` (https://www.noi.cn/zxzy/lnzl/)
    - 洛谷提供网盘数据
1. Lemonlime 创建比赛. 将所有数据放在 Lemonlime 项目的 `data/` 文件夹内. 例如 `data/galaxy/, data/detect/`
1. Lemonlime -> 控制 -> 自动添加试题（会在 `data/` 下寻找试题），每道题勾选 `在子文件夹寻找`
1. Lemonlime -> 工具 -> 设置 -> 编译器 -> 高级选项 -> 添加比赛编译选项

