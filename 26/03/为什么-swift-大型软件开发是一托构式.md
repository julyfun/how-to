---
title: "为什么 Swift 大型软件开发是一托构式"
date: 2026-03-10 14:31:45
tags: ["26", "03"]
author: "Julyfun MacOS14.5 M1"
os: "Darwin floriandeMacBook-Air.local 25.2.0 Darwin Kernel Version 25.2.0: Tue Nov 18 21:09:55 PST 2025; root:xnu-12377.61.12~1/RELEASE_ARM64_T8103 arm64"
assume-you-know: [computer]
confidence: 2
---

1. 官方文档采用极简主义，比其他语言 std 注释还短，靠论坛开发者自行摸黑，苹果工程师的回答敷衍了事，苹果开发者的反馈渠道 ¥688 年度 VIP 才可开启，入口也藏的很深，然而其 code-level support 只提供行政支持，技术上基本不可能有回复.
2. Swift 5 和 6 的早期版本拥有不严格的竞态检查，缺乏 fail-fast，e.g. data race 有 99.95% 的抛出 runtime 警告和 0.05% 的概率 crash，容易导致数据流复杂的异步项目开发期找不出 bug，上线猛出问题。backtrace 难以开启，只抛出警告却不知道是项目里哪行代码引起的
3. 200+ 关键字 + 过度使用的宏，海量酸爽隐式语言特性，e.g. @ObservedObject 嵌套了也没有任何警告，在某一天你会发现嵌套似乎影响了 UI 更新，然后在某个博客里读到不可嵌套。在注释和官方文档里都没有提这些语言特性 https://github.com/swiftlang/swift-syntax/blob/main/Sources/SwiftSyntax/generated/Keyword.swift
4. 不充 688 VIP 编译到手机十分容易触发 "Your Development Team Has Reached Maximum Registered iPhone Devices"。即使 VIP 也有 bug 会触发此信息.
5. 内置框架很糟糕，e.g. 多点通信 MCSession 会随机断连而没有打上 deprecated 标记，论坛开发者嗷嗷叫苦
6. Xcode 具有一系列防开发者设计：编译时每隔 2s 才更新一次编译信息，使用不是二进制也不像文本的 xcodeproj 格式管理项目（防 git 设计），它的 debug 窗口每隔 0.3s 才刷新一次
7. 包数量少，patterns、网络、算法、容器、序列化方向三方包质量很差，即使简单几个包也会冲突，有的包为了非常少用的功能放弃 Swift 5，而中等项目 swift 5 迁移到 swift 6 会多几百个编译错误，并分裂了包生态
8. target iOS 的不同版本会影响许多库特性，比如 iOS 16 的 onChange 和 iOS 17 的 onChange 函数参数不兼容也没有提供向下兼容版本
9. Swift 编译慢（比 rust 快）
10. Swift 是唯一一个嵌套达到一定层数就会把报错信息呈现为最外层几百行的 "Cannot resolve this block, The compiler is unable to type-check this expression in reasonable time" 的语言
11. lsp 响应时间在 1s ~ 10s 之间，是唯一一个 lsp 响应比 ai query 慢的语言。AI 常需要提醒自己“等等，这里的报错是 lsp 缓存过时导致的”
12. xcode 的 swift 项目默认不提供与 ide 解耦的语言支持，尽管 sourcekit-lsp 本身设计解耦，但需要一个为爱发电的三方 build-system bridge，有效防止了我带的新人开箱即用
13. 只能 import all symbols 是一种防开发者设计
14. swift 十分鼓励隐式控制流，e.g. getter-setter, property wrappers, computer property, swiftui DSL, optional chaining, 混合 exception 和没有错误传播符的 Result，而官方包仍广泛使用 exception，尽管 rust 的 unwrap() 已经让人畏惧，而 swift 用 `Type!` 和 `variable!` 轻松 panic，你的新人用 GPT5.5 / Opus4.8 写 Swift 最终仍会写出海量构式，构造史山的能力显著强于其他语言
15. Cache 很大，而苹果的硬盘很贵
16. 编写宏需要单独开一个 package，并且只能在 AST 层操作
17. 序列化一托构式，e.g. enc-dec 的默认值支持需要大量样版代码，序列化规则独树一帜
18. 互联网 swift 信息落后，Google 和 coding agent 能给出的方案可能过时麻烦又折腾
19. 操作 C 需要一层 OC binding，而 OC 是全世界最防人类的语言
20. 新旧异步编程模式具有海量副作用，而没有权威 tutorial.
21. Swift 也有一些优秀设计，比如 actor，使用 swift 6 的一个子集能写出比较优雅的代码，然而其历史包袱和苹果控制的工具链生态导致它的总体开发体验糟糕，甚至不如 C++.

didSet / willSet：属性赋值时自动触发回调，本质是“隐藏的 setter 包装逻辑”。
property wrappers（@State, @Published）：访问变量时其实走了一层隐式 getter/setter 转换。
computed property：看似字段访问，实际是函数调用（getter/setter 隐式执行）。
Result Builders（如 SwiftUI DSL）：花括号里的代码会被编译器重写成函数调用树。
async/await：看似顺序代码，底层被拆成状态机，控制流被编译器隐藏。
for-in + Sequence：循环语法依赖协议的 makeIterator()，控制流由类型驱动。
optional chaining（a?.b?.c）：短路逻辑由编译器插入多层分支展开。
defer：控制流“反向执行”，但触发时机由作用域退出隐式决定。
