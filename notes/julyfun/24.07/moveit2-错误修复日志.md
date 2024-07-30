## 7.30 启动双机械臂报错一大堆关节找不到，可以 Plan 不能 Execute

重启电脑解决。

## 有一个机械臂的 urdf 如何配置双机械臂

众所周知 moveit setup assistant 输入 urdf 输出所有配置文件。所以你需要修改你原有的 urdf：所有 joint 和 link 加上 `left_` 前缀，再复制 `<robot>` 标签内的所有内容，所有 joint 和 link 加上 `right_` 前缀，两机械臂相对位置用 `world_to_(left/right)_base` 表示。接下来用 setup assistant 就行了。

> 官网教程让你手动改输出的配置文件，太蠢了。
>
> verified on 24.7.29

## 启动带 MoveitGroupInterface 节点是报错 runtime error: can't load urdf..

- launch 文件里面别乱传参数，删除 parameters = xxx.urdf 解决了此问题

## tf 查找不到一个显然存在的 frame

- tf 查找别放在构造函数里，解决。

## joint angles 0.000000s

- 现在直接跑 demo.launch.py + hello_moveit 并不会报这个错了，能顺利规划和执行
- 但是跑别的报这个错还是不知道
- 应该是因为 spin 的位置，当前节点无法与其他节点通信导致的

## 启动节点但是 nothing happens

是忘记注册 rclcpp_register_component_node 了，或者 add_library 没有 add 对应的源文件

## 7.15 win 蓝牙没了

去 ubuntu 下 rmmod modprobe，修好了

## 之前 hello_moveit plan 后关节没法移动的原因是

有节点冲突，重启电脑解决

## 包带 moveit，编译报错，找到了 /mnt (msys2 的) 相关

- 问 chat cmake 用什么环境变量，给了个 bash 输出
- 输出 $PATH 发现带有 /mnt 和 /

* 网上搜 wsl 如何关闭共享 win 环境变量
* 解决
