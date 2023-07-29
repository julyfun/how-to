- 时间: 23.7.3
- 系统: 双系统 win11 + ubuntu 22.04

## Uninstall

1. F2 进入 BIOS，进入 Boot，把 Windows 移到最上面，Save and Exit
2. Win + R listpart 删除 Ubuntu 分区（由 15 GB 开头的“未知”分区）。给系统分区命名，然后用管理员打开记事本，打开其中文件资源管理器删除系统分区下 EFI 下 Ubuntu。

## Install

1. 买一个 U 盘
2. 下载 ubuntu-amd64.iso
3. 用 Rufus 软件把 U 盘变成启动盘
4. 计算机管理 -> C 盘压缩出 200 MB 作为 存放 Ubuntu EFI。另外开一个未知分区作为 Ubuntu 硬盘
5. 重启进入 BIOS，修改 Boot Mode 为 UEFI Only，然后把 U 盘放在 Windows 上面
6. 分区，200 MB 作为 efi ，剩下所有作为 `/`
7. Install，改 BIOS 中的启动顺序

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


### clash

github 搜 clash

```
mfa ul clash.gz
mfa dl clash.gz
gzip -d clash.gz
mv clash /usr/local/bin
```

同样下载 `clash_for_windows_pkg`

同样把可以用的 profiles.yaml 传过去，用 clash for windows 打开.


然后呢 settings Network proxy 改成 127.0.0.1:7890

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

