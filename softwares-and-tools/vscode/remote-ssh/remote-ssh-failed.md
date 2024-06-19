## 无法在远程服务器上自动安装 VSCode Server

关了梯子试试。23.9.18 这样解决的。但是随即又失败了，没有解决啊。

## 无法连接远程，但插件 Output 有正常输出

试试 https://stackoverflow.com/questions/64034813/vs-code-remote-ssh-connection-not-working 中的所有方法

### 24.5.21

* （应该没有用）先删除本地 known_hosts

* 删除远程 `~/.vscode-server/`

* 在本地 VSCode Settings 文件中加入

```
    "remote.SSH.useLocalServer": false,
    "remote.SSH.useExecServer": false,
```

成功。

### 24.6.19

* error: 无法连接远程，插件输出 connectionTimeout
* problem: 在插件输出中发现 ssh 命令是 `ssh -v -T -D 49942 -o ConnectTimeout=15 47.103.61.134`，没有用户名很奇怪（虽然使用 remote-ssh 的时候我是带用户名的）
* 在 ~/.ssh/config 中添加一个 config 记录，手动指定用户名和服务器

```
Host mfa
    HostName 47.103.61.134
    User julyfun
```

* 再检查检查有没有重复的 HostName，删除重复的
* 成功

