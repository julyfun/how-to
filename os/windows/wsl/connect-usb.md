- reliability: "20% (author)"
- date: 2024-10-28
- os: "win11; wsl2 ubuntu 22.04; 5.15.153.1-microsoft-standard-WSL2+ #2 SMP Sun Oct 27 22:02:06 CST 2024 x86_64 x86_64 x86_64 GNU/Linux"
- author: "4070s wsl julyfun"
- assume-you-know: [computer]

# connect usb

- 首先参考官方 : https://learn.microsoft.com/zh-cn/windows/wsl/connect-usb#attach-a-usb-device.
- 再使用本文中的 chmod 和简易 test.py 测试 : https://blog.csdn.net/weixin_37210821/article/details/135137942
- 如果失败，则执行本文的编译内核，其中内核 tag 版本号可修改为 uname -a 中的版本

> 24.10.28，先重装内核再执行 ms 官方的挂载命令，可通过 test.py 测试

每次重启电脑后，均需要

```
# powershell
usbipd list
usbipd bind --busid <busid, ex: 4-4>
usbipd attach --wsl --busid <busid>

# wsl
sudo chmod 777 /dev/video0 
```
