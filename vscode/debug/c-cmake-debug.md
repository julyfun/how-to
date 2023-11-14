原理是这样的，你编译出来的可执行文件只要是编译的时候开了 Debug 的时候，是可以直接调试的。

所以你在 cmakelists.txt 加上：

```cmake
set(CMAKE_BUILD_TYPE "Debug")
```

然后去 cmake + make 一下。

现在，用 vscode 命令面板唤出 debug 面板。

面板里有一个链接让你创建 `launch.json`。你点击会让你选择调试环境，你选 LLDB 他生成一个 json，然后这个 json 内容改成这样：

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug",
            "program": "${workspaceFolder}/build/demo",
            "args": [],
            "cwd": "${workspaceFolder}"
        }
    ]
}
```

这边 "program" 条目你改成要执行的文件。没错直接可执行文件就行了。

现在在源文件里面加一个断点，然后捏点击 debug 面板上方的播放按钮。他就会停在断点了。还会出现一个小长条工具栏，用来到下一行、跳转行等。一般你用 F10 逐过程，避免进入每个函数。

