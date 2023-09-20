## 来自 yuanzhi 老学长的建议

直接搜 cuda-toolkit 装。

虽然 nvidia 官方貌似只提供 16.04 的 toolkit.run，然而似乎在 18.04 上也可以直接 run.

那么这个时候你要搜索老版本 ubuntu 上关闭图形界面以后装 nvidia 驱动的方式。为什么要禁用图形界面 + reboot 呢，老夫也不知道。而且 reboot 以后是一个分辨率很低的可视化界面，这时候你按 F1 进入命令行界面。

run 了以后是一个 TUI 打钩界面，其中甚至包含 nvidia-smi。一般有 smi 的情况下 smi 不打钩，但是如果没有 smi 就打钩。

23.9.19 以上方法（用 cuda.run 装 nvidia-smi）报错了，要先装 nvidia-smi 再装 cuda.

