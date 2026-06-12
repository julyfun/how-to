---
title: "为什么 Swift 大型软件开发是一托构式"
date: 2026-03-10 14:31:45
tags: ["26", "03"]
author: "Julyfun MacOS14.5 M1"
os: "Darwin floriandeMacBook-Air.local 25.2.0 Darwin Kernel Version 25.2.0: Tue Nov 18 21:09:55 PST 2025; root:xnu-12377.61.12~1/RELEASE_ARM64_T8103 arm64"
assume-you-know: [computer]
confidence: 2
---

1. Swift 拥有不严格的竞态检查，data race 有 99.95% 的抛出 runtime 警告和 0.05% 的概率 crash，数据流复杂的异步项目容易导致开发期找不出 bug，上线了一个劲崩溃。backtrace 难以开启，你只知道有警告却不知道是项目里哪行代码引起的
2. 200+ 关键字，海量酸爽隐式语言特性，比如 @ObservedObject 嵌套了也没有任何报错和警告，在某一天你会发现嵌套似乎影响了 UI 更新，然后在某个博客里读到不可嵌套。在注释和官方文档里都没有提这些语言特性
3. 官方文档采用极简主义，比其他语言 std 注释还短，论坛开发者全靠自行摸黑，苹果工程师的回答敷衍了事，苹果开发者的反馈渠道 ¥688 年度 VIP 才可开启，入口也藏的很深，然而只提供行政支持（这也叫开发者反馈？）技术上基本不可能有回复.
4. 不充 688 VIP 编译到手机十分容易触发 "Your Development Team Has Reached Maximum Registered iPhone Devices"。即使 VIP 也有 bug 会触发此信息.
5. 内置框架很糟糕，如多点通信 MCSession 会随机断连，论坛开发者嗷嗷叫苦
6. Xcode 具有一系列防开发者设计：编译时每隔 2s 才更新一次编译信息，使用不是二进制也不像文本的 xcodeproj 格式管理项目（防 git 设计），它的 debug 窗口竟然每隔 0.3s 才刷新一次
7. 包很少，三方包质量很差，fetch 对网络要求高，构建系统稀烂，即使简单几个包也会冲突，有的包为了非常少用的功能放弃 Swift 5，而中等项目 swift 5 迁移到 swift 6 会多几百个编译错误
8. iOS 的不同版本竟然会影响 Swift 语言特性，比如 iOS 16 的 onChange 和 iOS 17 的 onChange 函数参数不兼容也没有提供向下兼容版本
9. Swift 编译慢（比 rust 快）
10. Swift 是唯一一个嵌套达到一定层数就会把报错信息呈现为最外层几百行的 "Cannot resolve this block, The compiler is unable to type-check this expression in reasonable time" 的语言
11. lsp 响应时间在 1s ~ 10s 之间，是唯一一个 lsp 响应比 ai query 慢的语言。AI 常需要提醒自己“等等，这里的报错是 lsp 缓存过时导致的”
12. Xcode 之外配 swift lsp 需要三方工具，防小白
13. 只能 import all symbols 是一种防开发者设计
14. Coding Agent 写 Swift 最终会写出一坨构式
15. Cache 很大，而苹果的硬盘和金子一样贵
16. 编写宏需要单独开一个 package，并且只能在 AST 层操作
17. 序列化一托构式
18. 互联网 swift 信息落后，Google 和 coding agent 能给你的方案可能过时麻烦又折腾
19. 操作 C 需要一层 OC 层，而 OC 是全世界最防人类的语言
20. 新旧异步编程模式具有海量副作用，而没有权威 tutorial.
21. Swift 也有一些优秀设计，比如 actor，使用 swift 6 的一个子集能写出比较优雅的代码，然而其历史包袱和苹果控制的工具链生态导致它的总体开发体验糟糕，甚至不如 C++.
