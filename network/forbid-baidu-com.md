---
title: forbid-baidu-com
date: 2023-11-16 19:03:00
tags: ["network"]
---
```
vim /etc/hosts
```

添加：

```
127.0.0.1 baidu.com
```

### ChatGPT says

当你在 hosts 文件中添加了 127.0.0.1 baidu.com 这一行后，你的操作系统会尝试解析 baidu.com 域名时，会将其指向本地主机（127.0.0.1），即你自己的计算机。

这意味着，当你尝试访问 baidu.com 时，你的浏览器会尝试连接到本地计算机上运行的服务或者尝试通过本地网络来查找 baidu.com，但由于没有在本地设置对应的服务，通常会显示连接错误或无法访问的信息。实际上，这会导致浏览器无法正确加载 baidu.com 上的内容。
