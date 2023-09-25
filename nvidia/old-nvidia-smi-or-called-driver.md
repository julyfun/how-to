## 来自 yuanzhi 老学长的建议

直接搜 cuda-toolkit 装。

虽然 nvidia 官方貌似只提供 16.04 的 toolkit.run，然而似乎在 18.04 上也可以直接 run.

那么这个时候你要搜索老版本 ubuntu 上关闭图形界面以后装 nvidia 驱动的方式。为什么要禁用图形界面 + reboot 呢，老夫也不知道。而且 reboot 以后是一个分辨率很低的可视化界面，这时候你按 F1 进入命令行界面。

run 了以后是一个 TUI 打钩界面，其中甚至包含 nvidia-smi。一般有 smi 的情况下 smi 不打钩，但是如果没有 smi 就打钩。

23.9.19 以上方法（用 cuda.run 装 nvidia-smi）报错了，要先装 nvidia-smi 再装 cuda.

## 纯 ssh 尝试

这次是要把 nvidia-driver 384 换成 nvidia-driver 470. 因为 384 不支持 cuda 9.2.

先 `sudo apt purge nvidia-*`. 它删除了 1G 多的东西，其中看起来还有 cuda-toolkit 相关，只不过后缀有 384 所以我肯定就不要了。

先下载一个驱动.run:

- 搜索: https://www.nvidia.com/en-us/geforce/drivers/
- 搜索结果: https://www.nvidia.com/en-us/geforce/drivers/results/205995/

然后跑这个 run。跑得时候因为在 16.04 上，它会直接告诉你: You seem to be using an X server, stop it.

于是我就按照 https://askubuntu.com/questions/149206/how-to-install-nvidia-run    :

```
  990  top | grep Xorg
  991  kill -9 Xorg
  992  kill -9 1114
  993  sudo kill -9 1114
  994  ls
  995  ./470.run
  996  sudo ./470.run
  997  ps -ef | grep Xorg
  998  ps -ef | grep X
  999  sudo service lightdm stop
 1000  sudo lightdm stop
 1001  ls
 1002  sudo killall Xorg
```

然后可以跑了，跑的时候他说要不要 kernal xxx，我本来想退出的选了 No，然而它继续往下跑了，他说要不要装兼容 32 位的我说不要。


