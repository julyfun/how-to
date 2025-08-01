---
title: how-to 服务器维护日志
date: 2024-09-25 16:58:43
tags: ["notes", "julyfun", "24", "07"]
---
# how-to 服务器维护日志

## 25.3.14

- [ok]

```
bash
sudo bash start2.sh
proxy_on
```

## 12.25

- 又挂了。[ok] 重进 dashboard 的时候记得:

```
在`API Base URL`一栏中输入：`http://<ip>:10050`，在`Secret(optional)`一栏中输入    启动成功后输出的Secret。
```

## 10.20

- 最近又挂了，不得不重新开放 external 端口
- 在阿里云开放自定义端口
- 删除 clash-for-linux-backup 中的 conf/config.yaml
- 重新 `sudo bash start.sh`
- 修改 conf/config.yaml 中的 external 端口
```
sudo bash restart.sh
source /etc/profile.d/clash.sh
proxy_on
```
- 访问 10050 看看
- [240205] 按照上述方法 ok。我还修改了 start.sh 使之可以读取本地文件.

## 7.31

土豆服务器上白天 clash 经常莫名其妙挂了，每次手动重启。

晚上一看又挂了，写了个脚本自动重启，结果直接把服务器 cpu 干爆了。

以为是 clash-for-linux 仓库的问题，拉了 clash-core 和 clashmeta 来测测，还是会干爆。

发现新工具 `gg`， https://github.com/mzz2017/gg?tab=readme-ov-file 当时没外网拉不下来，以后测测

clash core log 有一堆脏东西：

![](https://telegraph-image-bhi.pages.dev/file/ea010a8ac7358b859ce23.png)

翻来覆去问论坛，最后问 gpt4 是什么流量回环还是公网 ip 攻击，他说 ip 是乌克兰的，建议查查防火墙。

想起来之前为了做 Rustdesk 服务器，把所有端口都开了，所以回去把端口都关了，就剩 22 和 3389

Done! clash 又正常了，所以你才能看到这篇博客。

所以这是被攻击了吧。

> xy 说给 9090 端口设置密码就行。不过我已经把端口关了。

或许昨天白天不是 clash 挂了而是节点挂了，晚上是设置过于简单密码才被轰炸的。果真如此的话还是得开 9090 端口去选节点。

