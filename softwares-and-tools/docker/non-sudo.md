---
title: non-sudo
date: 2024-01-15 01:10:05
tags: []
---
## 有时你想要以非 sudo 使用 docker 命令

比如 vscode 的 Docker 插件想要访问 docker 容器。

那么你需要 https://docs.docker.com/engine/install/linux-postinstall/
- 备用 https://github.com/microsoft/vscode-docker/wiki/Troubleshooting

```
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
docker run hello-world
```

每次开新 shell 后需要:

```
newgrp docker
```

