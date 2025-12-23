---
title: Install configure uninstall ubuntu
date: 2024-01-15 01:10:05
tags: ["os", "ubuntu"]
---
- 时间: 23.7.3
- 系统: 双系统 win11 + ubuntu 22.04

## Uninstall

1. F2 进入 BIOS，进入 Boot，把 Windows 移到最上面，Save and Exit
2. Win + R listpart 删除 Ubuntu 分区（由 15 GB 开头的“未知”分区）。给系统分区命名，然后用管理员打开记事本，打开其中文件资源管理器删除系统分区下 EFI 下 Ubuntu。

see: https://blog.csdn.net/Wenyuanbo/article/details/126381967

注意：就算你装 ubuntu 的时候没有手动分出 efi，仍然需要删除该教程中第一个 EFI/ubuntu 文件夹（用记事本那个），但第二个 EFI 分区不用删。

1. 进入 BIOS，把 Windows 移到最先启动，保存退出
2. 如下

```
# win + R, diskpart
list disk
# 选择 ubuntu 所在磁盘
select disk 0
# 选择 ubuntu 所在分区，类型必为未知，可在磁盘管理中查看
select partition 5
delete partition override
# 选择 ubuntu EFI 所在分区，一般是 1
select partition 1 # Ubuntu EFI
assign letter=P
# 管理员打开 notepad，点击 文件 -> 打开 -> 找到 P 盘 -> 删除其中的 EFI/ubuntu
remove letter=P
# 以上 25/12/24 ok again
```
Done. 进磁盘管理看看 ubuntu 分区是不是变成未分配了。

## Install

- ref: https://zhuanlan.zhihu.com/p/461271487
- ref: https://www.cnblogs.com/easy5weikai/p/17470402.html
- y9000p: https://blog.csdn.net/qq_42786957/article/details/127708237
- y9000p: https://zhuanlan.zhihu.com/p/594500341

1. 买一个 U 盘
2. 下载 ubuntu-amd64.iso
3. 用 Rufus 软件把 U 盘变成启动盘（需下载）
4. 计算机管理 -> C 盘压缩出 200 MB 作为 存放 Ubuntu EFI。另外开一个未知分区作为 Ubuntu 硬盘（很可能不需要）
5. 重启进入 BIOS，修改 Boot Mode 为 UEFI Only，然后把 U 盘放在 Windows 上面
6. 分区，200 MB 作为 efi ，剩下所有作为 `/`
7. Install，改 BIOS 中的启动顺序

## 特殊系统

### win10 + 华硕主板

- 进入 bios 很难，见：

https://zhuanlan.zhihu.com/p/374951491

- 开启 CSM 也不方便，见：

https://www.machunjie.com/linux/302.html

> 以上在 24-6-24 测试成功。

## Configure to your style

### 终端

```
sudo apt install konsole
sudo apt install neovim # 这个版本会比较老，之后去 neovim release 下个新的
sudo apt install git
sudo apt install curl
```

### apt 源

下面这个是 ubuntu 22.04 arm64 好用的清华源：

```
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ jammy main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ jammy main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ jammy-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ jammy-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ jammy-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ jammy-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ jammy-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ jammy-security main restricted universe multiverse

# 预发布软件源，不建议启用
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ jammy-proposed main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ jammy-proposed main restricted universe multiverse
```

### ssh 和 mfans 服务器

```
ssh-keygen -t rsa
ssh-copy-id username@remote-server
```

现在可以免密码连接服务器了。

```
nvim ~/.ssh/config
Host mfa
    HostName mfans.fans
    User julyfun
```

### fish shell

```
sudo apt-add-repository ppa:fish-shell/release-3
sudo apt update
sudo apt install fish
chsh -s /usr/bin/fish
gnome-session-quit
mkdir -p ~/Documents/GitHub
cd ~/Documents/GitHub
scp -r mfa:~/Documents/GitHub/mfa.fish .
```

```
vim .../config.fish
source .../mfa.fish
```

```
mfa init
```

接下来可以用另一台电脑传递文件和信息了。


### clash for windows

下载 Clash for windows，运行可执行文件，放入配置文件 (.yaml)

- 记住 Ubuntu 中必须把 Settings -> Network proxy 改成 127.0.0.1:7890（我把 http, https, socks5 都改成这个了，可以）

cfw 会调用 clash。如果 ./cfw 报错：

```
FATA[0000] Parse config error: yaml: unmarshal errors:
  line 1: cannot unmarshal !!str `c3M6Ly9...` into config.RawConfig
```

那是因为 ~/.config/clash 里面的配置废了。rm -rf 以后在重新运行一次 clash，输出三行后可以退出。

> 同样把可以用的 profiles.yaml 传过去，用 clash for windows 打开.

## Oh my fish

github 搜 oh-my-fish. 用 curl 下载的。

```
curl https://raw.githubusercontent.com/oh-my-fish/oh-my-fish/master/bin/install | fish
```

bass

```
omf install bass
omf install l
```


### neovim

In ~/.config/nvim/init.vim

```
set number
set relativenumber
```

见 neovim 相关文章。

### 搜狗拼音

按照官方教程装。

如果你出现假的输入法切换，那么你就

```
sudo vim /etc/environment
GTK_IM_MODULE=fcitx
QT_IM_MODULE=fcitx
XMODIFIERS=@im=fcitx
```

不断地 logout。

- [later 2025] For ubuntu 22.04, 我没有成功使用 sogou pinyin，最后用的 Google Pinyin (同样是 fcitx 框架）
- [25.5.18] update: 又给 22.04 成功装上了 sogou pinyin, 见摸鱼日志.md

### 常用软件

```
wget http://fishros.com/install -O fishros && bash fishros
```

- Github Desktop
- ros

### VSCode

- rose-pine
- clangd

打开一个 cpp 自动安装 clangd，好吧其实不一定成功，那么下载 clangd 的 zip 然后解压，在 vscode clangd 的位置参数里面填位置。

- cmake
- code spell checker
- tabnine
- neovim
- clang-format

pip install clang-format

- clang-tidy

pip install clang-tidy

- error lens

### cuda

```
nvidia-detector
> nvidia-driver-535
# 下面这句不一定对
sudo apt install nvidia-utils-535
sudo ubuntu-drivers autoinstall
```

reboot

现在 nvidia-smi 正常了。

看看教程 https://jackfrisht.medium.com/install-nvidia-driver-via-ppa-in-ubuntu-18-04-fc9a8c4658b9

在类似 https://developer.nvidia.com/cuda-toolkit 的网站找到你的 cuda 版本对应的 toolkit，选择了 deb(network)，官网会告诉你命令。

到 tensorrt download。结果没有任何直接给 12.2 的版本。下载个 12.0 到 12.1 版本的试试吧。

```
sudo dpkg -i nv-tensorrt-repo-ubuntu1604-cuda10.0-trt7.0.0.11-ga-20191216_1-1_amd64.deb
sudo cp /var/nv-tensorrt-local-repo-ubuntu2204-8.6.1-cuda-12.0/nv-tensorrt-local-42B2FC56-keyring.gpg /usr/share/keyrings/
sudo apt update
sudo apt install tensorrt
```

然后是 cudnn。遵循下面这个教程：https://github.com/wang-xinyu/tensorrtx/blob/master/tutorials/install.md

下次也可以试试这个教程，这个教程甚至没有去官网找东西：https://gist.github.com/denguir/b21aa66ae7fb1089655dd9de8351a202

### tldr

pip install tldr
