---
title: "jjyos 期末考试 ans"
date: 2025-09-23 11:21:07
tags: ["notes", "julyfun", "25", "09"]
author: "Julyfun MacOS14.5 M1"
os: "Darwin floriandeMacBook-Air.local 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1 20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64"
assume-you-know: [computer]
confidence: 2
---

### 1
- 为什么说linux的管道是一种进程间通信的机制
    - 内核的管道缓冲区在数据被读取前会暂存它们，协调两个进程的读写速度差异
- 操作系统如何处理备引发的中断
    - 保存现场: 网卡发出中断信号。
    - 识别中断源（中断控制器）: CPU保存当前进程状态，识别出中断来自网卡。
    - 执行网卡驱动程序的中断服务程序。
        - 该程序从网卡缓冲区读取数据包，并将其放入操作系统的网络协议栈进行处理。
    - 恢复现场: 处理完成后，恢复被中断的进程。

### 2
- 简述mmap的作用(无须写出定义)
把硬盘文件映射到内存.
- 怎么判断1号进程到底是哪一个二进制文件?
    - `ps -p 1` or `readlink /proc/1/exe`
- libc 全局变量
    - `stdin`, `stdout`, `stderr` (指向标准输入（文件描述符 0）的 FILE 结构体)
    - `environ` 数组，每个变量是 `NAME=VALUE` 形式的字符串
    - `errno`: 记录系统调用和库函数发生的最近一次错误
    - `optarg`, `__progname`, `locale 本地化规则`
