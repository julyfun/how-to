---
- title: @ObservedObject or @StateObject
- date: 2025-07-02 16:59:01
- tags: [langs, swift, ai-then-me]
- author: "Julyfun M4"
- os: "Darwin 192.168.2.8 24.3.0 Darwin Kernel Version 24.3.0: Thu Jan  2 20:22:58 PST 2025; root:xnu-11215.81.4~3/RELEASE_ARM64_T8132 arm64"
- assume-you-know: [computer]
---

# @ObservedObject or @StateObject

在 SwiftUI 中，`@ObservedObject` 和 `@StateObject` 均可传播 @Published 更新.

| 场景           | 使用                | SwiftUI 是否负责生命周期 | 是否能被观察更新 |
| ------------ | ----------------- | ---------------- | -------- |
| 当前 View 创建对象 | `@StateObject`    | ✅ 是              | ✅ 是      |
| 外部传入的对象      | `@ObservedObject` | ❌ 否              | ✅ 是      |
| 值类型，或不需触发更新  | 不用                | ❌ 否              | ❌ 否      |

