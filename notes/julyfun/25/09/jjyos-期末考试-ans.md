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
- System V ABI规定进程的初始栈中有一些auxiliary vector entries. 根据你对操作系统的理解，可以有哪些辅助数据，又有什么作用?
    - AT_EXECFD: 执行文件的文件描述符 现代不再使用
    - AT_PHDR: 程序头表的地址
        - 头表描述如何将文件的各个部分映射到进程的虚拟地址空间。头表存储在硬盘文件中.
    - AT_PHNUM: 程序头表中的条目数
    - AT_PAGESZ: 系统页面大小
    - AT_BASE: 动态链接器的基地址
    - AT_FLAGS: 进程标志
    - AT_ENTRY: 程序入口点地址
    - AT_UID, AT_EUID, AT_GID, AT_EGID: 用户和组ID信息
    - 作用: 提供给程序运行时环境所需的关键信息，帮助动态链接器加载共享库，设置内存布局.

extra:
- 当您在 Shell 中输入 ./my_program 时，Shell 会调用 execve 系统调用。内核会检查该文件的开头几个字节（称为“魔数”）。如果魔数与 ELF 格式的定义匹配（0x7f 0x45 0x4c 0x46，即 0x7f 'E' 'L' 'F'），内核就将其作为 ELF 文件来解析和加载. 大多可执行文件都是 ELF 格式. 其余还有 shebang, a.out 等格式.
- gcc
    - gcc -c test.c → 生成 test.o
        - 预处理（.c→.i）：处理宏和头文件
        - 编译（.i→.s）：生成汇编代码
        - 汇编（.s→.o）：生成二进制目标文件
    - ar rcs libtest.a test.o → 生成静态库
    - gcc test.o -ltest → 链接生成 a.out (.a, .so 都可以)
    - gcc -fPIC -shared -o libtest.so test.c → 生成共享库

