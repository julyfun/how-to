## setup

- ref: https://hackmd.io/@jimmy801/docker_gui

```
docker run -it -h $(hostname) -e DISPLAY=$DISPLAY -e XAUTHORITY=/tmp/xauth -v ~/ws/docker2:/home -v ~/.Xauthority:/tmp/xauth -v /tmp/.X11-unix:/tmp/.X11-unix --net=host -d ros:humble-ros-base-jammy 
```

```
# [ex]
useradd -m -s /bin/bash -u 1000 julyfun
usermod -aG sudo julyfun
sudo passwd julyfun
su julyfun
```

- ref: https://github.com/waveshareteam/roarm_ws_em0.git

```
sudo apt update
sudo apt install -y software-properties-common
sudo apt install -y net-tools
sudo apt install -y ros-humble-moveit-*
sudo apt install -y ros-humble-foxglove-bridge
sudo apt autoremove ros-humble-moveit-servo-*
```

## Docker usage

```
docker exec -u julyfun -it 7f bash
```
