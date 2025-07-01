---
title: auto-generate-headers-from-c
date: 2024-01-15 01:10:05
tags: ["langs", "c"]
---
## Sol 1

https://github.com/taylordotfish/autoheaders

使用 git clone + pip 安装（建议虚拟环境），用法：

```
autoheaders src/lib.c -o include/tmp.h
```

有一些 bug，比如无法解析 lib.c 引用其他头文件的 typedef struct 类型，直接会报错。所以大概对简单的源文件才能使用。并且这仓库已经几年没更新了。

