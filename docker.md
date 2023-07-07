## 有时你想要以非 sudo 使用 docker 命令

比如 vscode 的 Docker 插件想要访问 docker 容器。

那么你需要 https://github.com/microsoft/vscode-docker/wiki/Troubleshooting

## 用 ssh 连接 docker 容器？

in the container:

```
apt install openssh-server
service start ssh
```

似乎无法连接 root 用户。可以新建一个 sudo 用户

```
useradd nvidia
usermod -aG sudo nvidia
```

然后你在本机 `docker inspect <container> | grep "IPAddress"` 

下面要做什么就很显然了。

## 在 VSCode 中使用容器中的 clangd

用 Remote-ssh 插件链接这个容器

然后在左边插件栏目里对 ssh 的容器下载 clangd 插件

新建一个 1.cpp 然后打开这个 cpp，vscode 会提示你下载 clangd-server.

