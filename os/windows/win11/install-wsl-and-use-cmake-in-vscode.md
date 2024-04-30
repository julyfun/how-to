---
reliability: "50% estimated by the author"
date: 2024-04-29
language: "Chinese"
os: "Darwin floriandeMacBook-Air.local 22.5.0 Darwin Kernel Version 22.5.0: Mon Apr 24 20:53:44 PDT 2023; root:xnu-8796.121.2~5/RELEASE_ARM64_T8103 arm64"
author: "Julyfun MacOS13.4 M1"
suppose-you-know: [Ubuntu basic usage, used to work on Ubuntu]
keywords: [wsl, win11, wsl2]
---

# Install wsl and use cmake in vscode

- 安装 wsl，ref: https://zhuanlan.zhihu.com/p/475462241

其实大多数 win11 电脑只需要在 PowerShell 中执行以下，等待安装（进度条可能显示 0% 很久）：

```
wsl --install -d Ubuntu
```

此时相当于在你的 windows 里安装一个 ubuntu，默认安装 Ubuntu 22.04。接下来它会自动创建 ubuntu 的管理员用户，让你输入用户名。

- 所以你就输入管理员用户名和密码，完成安装，关闭 PowerShell
- 在 Windows 的 vscode 中安装插件 WSL
- ctrl + shift + p 打开 vscode 命令面板，执行 WSL: 连接到 WSL，此时自动打开新窗口
- 在新窗口中 ctrl + shift + e 选择一个文件夹
- 按 ctrl + j 打开终端
- 执行 `sudo vim /etc/apt/source.list`，删除原有内容，添加下面链接中的镜像链接：

https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/

这一步是准备 cmake 的下载源。以下是 24.4.30 可用的 Ubuntu 22.04 apt 源： 

```
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse

deb http://security.ubuntu.com/ubuntu/ jammy-security main restricted universe multiverse
# deb-src http://security.ubuntu.com/ubuntu/ jammy-security main restricted universe multiverse

# 预发布软件源，不建议启用
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-proposed main restricted universe multiverse
# # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-proposed main restricted universe multiverse
```

- 安装 cmake：

```
sudo apt update # 更新下载源
sudo apt install cmake
```

- 现在你可以在 vscode 中的终端窗口中的 wsl ubuntu 命令行中正常使用 cmake 了
- 打开 win11 - 文件管理器，可以看到左侧栏目中有一个 Linux，这就是 wsl 所在的位置。你可以把 win11 的文件拖动到 `Linux - Ubuntu - home - 用户名` 文件夹中，也可以拖动到 vscode 打开 wsl 后的资源管理器中。

