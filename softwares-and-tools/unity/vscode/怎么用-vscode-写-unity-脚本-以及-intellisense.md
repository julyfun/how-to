---
title: 怎么用-vscode-写-unity-脚本-以及-intellisense
date: 2024-01-15 01:10:05
tags: ["softwares-and-tools", "unity", "vscode"]
---
https://zhuanlan.zhihu.com/p/245846735

其中的 Mono SDK 似乎不用安装也可以。

安装后重启电脑！然后再从 unity 打开脚本，intellisense 可以正常用了！甚至可以点开外部库函数！

> 以上测试日期 23-11-3，`uname -a` 为：

```
Darwin floriandeMacBook-Air.local 22.5.0 Darwin Kernel Version 22.5.0: Mon Apr 24 20:53:44 PDT 2023; root:xnu-8796.121.2~5/RELEASE_ARM64_T8103 arm64
```

但是过了一会儿 intellisense 又没了。又提示“在计算机上找不到已安装的 .NET SDK”。所以我再次重启电脑。重启后 vscode C# 插件通知：某插件只适用于 SDK 样式项目，是否要为工作区使用 C# 插件？我说好的，然后 intellisense 又回来了。

## 过几天没有 intellisense 了，提示 C# 插件只适用于 SDK 样式项目

让你选择要不要为工作区使用 C# 插件。你就选择使用。然后它让你重启工作区，就有智能提示了。

## 过几天又“在计算机上找不到 .NET SDK” ... path...

重启电脑，没啥办法。

## 另一个可能的方案

https://zhuanlan.zhihu.com/p/601343633?utm_id=0

