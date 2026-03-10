---
title: "为什么 Swift 大型软件开发是一坨构式"
date: 2026-03-10 14:31:45
tags: ["26", "03"]
author: "Julyfun MacOS14.5 M1"
os: "Darwin floriandeMacBook-Air.local 25.2.0 Darwin Kernel Version 25.2.0: Tue Nov 18 21:09:55 PST 2025; root:xnu-12377.61.12~1/RELEASE_ARM64_T8103 arm64"
assume-you-know: [computer]
confidence: 2
---

- Swift 不严格的竞态检查，例如在非主线程写入 UI 变量有 99.95% 的概率告诉你一个警告和 0.05% 的概率 crash，导致开发期找不出 bug，上线了一个劲崩溃。并且我至今没有发现如何开这些警告 backtrace，你只知道有警告
- 两百多关键字，海量隐式语言特性，比如 @ObservedObject 不可嵌套，你嵌套了也没有任何报错和警告，在某一天你会发现它影响 UI 更新，然后在某个博客里读到不可嵌套。在注释和官方文档里都没有提这些语言特性
- 构式的官方文档比其他语言 std 注释还短，全靠开发者论坛云里雾里全程摸黑，并且苹果论坛很快就会关闭帖子.
- 构式的内置框架，如多点通信会随机断连
- Xcode 的防开发者设计：2s 更新一次编译信息，使用不是二进制也不像文本的 xcodeproj 格式管理项目（防 git 设计），它的 debug 窗口不像一般的终端而是 0.3s 刷新一次(Why??)
- 包很少，三方包质量很差，fetch 对网络要求高，构建系统稀烂，即使简单几个包也会冲突，有的包为了非常少用的功能放弃 Swift 5，而 swift 5 迁移到 swift 6 会多几百个编译错误
- iOS 的不同版本竟然会影响 Swift 语言特性，比如 iOS 16 的 onChange 和 iOS 17 的 onChange 函数参数不兼容也没有提供向下兼容版本
- Swift 编译
- ...
- ...
- ...很
- ...
- ...
- 慢
- Swift 是唯一一个嵌套达到一定层数就会把报错信息呈现为最外层几百行的 "Cannot resolve this block"（在这几百行报错中你需要自己找某个地方语法错误）的语言 / "The compiler is unable to type-check this expression in reasonable time"
- lsp 响应时间在 1s ~ 10s 之间，是唯一一个 lsp 响应比 ai query 慢的语言。AI 常需要提醒自己“等等，这里的报错是 lsp 缓存过时”
- 只能全局 import 是一种防开发者设计
- Coding Agent 写 Swift 最终会写出一坨构式
- Cache 很大，而苹果的硬盘和金子一样贵
- 编写宏需要单独开一个 package(why??)，并且只能在 AST 层操作
- 序列化一坨构式
- 互联网信息过时，Google 和 Gemini 能给你的方案可能过时麻烦又折腾
- 操作 C 需要一层 OC 层，而 OC 是全世界最防人类的语言

