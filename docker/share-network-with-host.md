docker build . --network=host

https://www.cnblogs.com/freeaihub/p/13206077.html

在 Dockerfile 中这么写：

```Dockerfile
ENV https_proxy "127.0.0.1:7890"
```

## #source #dialog xy_cpp

docker-compose 桥接要这么写:

```yml
environment:
  - http_proxy=http://host.docker.internal:7890
  - https_proxy=http://host.docker.internal:7890
  - MYSQL_PASSWORD=nextcloud
```

docker-compose up -d

参考一个 xy_cpp 的 Dockerfile

```
ARG CUDA_VERSION=12.0.0
ARG CUDNN_VERSION=8
ARG OS_VERSION=22.04

# 拉取基础镜像
FROM nvidia/cuda:${CUDA_VERSION}-cudnn${CUDNN_VERSION}-devel-ubuntu${OS_VERSION}
LABEL maintainer="XY_cpp"
WORKDIR /root

# 时区
ENV TZ=Asia/Shanghai \
    DEBIAN_FRONTEND=noninteractive
RUN apt update && \
    apt install -y tzdata && \
    ln -fs /usr/share/zoneinfo/${TZ} /etc/localtime && \
    echo ${TZ} > /etc/timezone && \
    dpkg-reconfigure --frontend noninteractive tzdata && \
    rm -rf /var/lib/apt/lists/*

# TensorRT
ARG TRT_VERSION=8
COPY TensorRT${TRT_VERSION}-${CUDA_VERSION}.tar.gz tensorrt.tar.gz
RUN tar -xzvf tensorrt.tar.gz && mv TensorRT-* /opt/TensorRT && rm -rf tensorrt.tar.gz
ENV LD_LIBRARY_PATH=/opt/TensorRT/lib${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}

# 开发环境
#  项目源代码
VOLUME SRM-IC-2022
#  基础软件包
RUN apt update && \
    apt install -y g++ cmake clangd && \ 
    apt install -y wget vim git zsh && \ 
    apt install -y libceres-dev libopencv-dev && \
    rm -rf /var/lib/apt/lists/*
#  海康相机库
COPY MVS.tar.gz MVS.tar.gz
RUN tar -xzvf MVS.tar.gz && mv MVS /opt/MVS && rm -rf MVS.tar.gz

# zsh(更好看的终端，可选)
RUN apt update && \
    apt install -y git wget vim zsh && \
    rm -rf /var/lib/apt/lists/*
#  请将此处修改为梯子的代理端口，否则无法连接到Github
ENV https_proxy "127.0.0.1:7890"
RUN wget --no-check-certificate https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh && \
	git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-autosuggestions && \
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting && \
    chsh -s $(which zsh) && \
    rm -rf /var/lib/apt/lists/*
COPY zshrc /root/.zshrc
RUN unset https_proxy
CMD ["/bin/zsh"]

# bash(不好看的终端，可选)
#CMD ["/bin/bash"]
```

