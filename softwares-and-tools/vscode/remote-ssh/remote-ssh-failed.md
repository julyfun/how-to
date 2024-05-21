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

