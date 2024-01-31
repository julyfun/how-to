跟 cmake debug 类似。Vscode 的 Debug 程序只是运行一个用 `-g` 编译的可执行文件而已。

你只需要先用 `g++ -g` 命令编译出一个可执行文件，并在 Vscode Debug launch.json 中把 configurations -> program 参数改成可执行文件的位置就可以了。

