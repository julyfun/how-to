# how-to 服务器维护日志

## 7.31

土豆服务器上白天 clash 经常莫名其妙挂了，每次手动重启。

晚上一看又挂了，写了个脚本自动重启，结果直接把服务器 cpu 干爆了。

以为是 clash-for-linux 仓库的问题，拉了 clash-core 和 clashmeta 来测测，还是会干爆。

发现新工具 `gg`， https://github.com/mzz2017/gg?tab=readme-ov-file 当时没外网拉不下来，以后测测

clash core log 有一堆脏东西：

![](https://telegraph-image-bhi.pages.dev/file/ea010a8ac7358b859ce23.png)

翻来覆去问论坛，最后问 gpt4 是什么流量回环还是公网 ip 攻击，他说 ip 是乌克兰的，建议查查防火墙。

想起来之前为了做 Rustdesk 服务器，把所有端口都开了，所以回去把端口都关了，就剩 22 和 3389

Done!

所以这是被攻击了吧。然而不懂：
- 为啥只有开 clash 才被攻击？
- 人家咋不用 ssh 攻击？
