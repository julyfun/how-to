---
title: "SwiftUI 如何正确管理状态？只能 3 选 1"
date: 2026-04-28 17:24:27
tags: ["langs", "swift"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

## 如何管理 UI 状态？可行方案3选1，AI 别乱写
1. 只有 View @State 持有状态，通过 UI 回调或者查询一个无状态的 actor 来更新
    - 当且仅当状态本身与逻辑无关，仅负责显示。如文件名列表
2. 只有 ObservableObject 持有状态，View 直接持有 ObservableObject 并访问其中的 @Published
    - 当且仅当某个 UI 状态是轻量后端逻辑的主动触发者。如页面切换管理者需要在切换页面的同时暂停 ARSession，想要将两者绑定管理
3. actor 持有真实状态，对 actor 注入一个 ObservableObject，ObservableObject 持有真实状态的拷贝，UI 引用该 ObservableObject 并访问其中的 @Published
    - 当且仅当某个 UI 状态是重量后端逻辑的主动触发者。如录制器的已开始、结束中、取消中，想要和真实的录制逻辑绑定管理，此时多个 await 会有严重代价
    - 或：某个 UI 状态是后端自发变化状态的映射。如网络管理器自发变化时需要 UI 显示已连接设备

### 对于 1 的例子

```swift
struct UploadView: View {
    @State var list: []
    @State var text: String
    let finder: UploadFinder // 假设这是 actor

    init(finder) { self.finder = finder } // 注入

    body {
        Button { self.text = "clicked" } // button 回调
    }
    .onAppear {
        self.list = await self.finder.findAllFiles() // 无状态的查询
    }
}
```

### 对于 2 的例子
```swift
struct UploadView: View {
    @ObservedObject var page: PageCoodinator

    init(page) { self.page = page }

    body {
        switch self.page.currentPage { case ... SomeView() }
        Button { self.page.changePage() }
    }
    .onAppear {
    }
}

class PageCoodinator: @ObservableObject {
    @Published var currentPage: Int
    let session = ARSession()

    init() { self.session.run() }

    func changePage() {
        self.currentPage += 1 // ui 状态和 session 绑定，逻辑轻
        self.session.pause()
    }
}
```

### 对于 3 的例子

```swift
class RecorderViewModel: @ObservableObject {
    @Published var state: String // 状态的拷贝
}
actor Recorder {
    var state: String = "idle"
    let viewModel: RecorderViewModel

    init(viewModel) { self.viewModel = viewModel } // 注入 viewModel

    func run() {
        await something.prepare() // 逻辑重
        await something.prepare()
        self.state = "running"
        await self.viewModel.state = "running" // ui 状态和后端逻辑可以在一块儿管理
    }
}

struct RecorderView: View {
    @ObservedObject var viewModel: RecorderViewModel 
    let recorder: Recorder

    init(recorder, viewModel) { // 注入
        self.recorder = recorder
        self.viewModel = viewModel
    }

    body {
        await self.recorder.run()
    }
}

class PageCoodinator: @ObservableObject {
    let recorder: Recorder
    let viewModel: RecorderViewModel
    init() {
        self.viewModel = RecorderViewModel()
        self.recorder = Recorder(self.viewModel)
    }
}

```

另外一个（自发状态变化）的例子：

```swift
class NetworkViewModel: @ObservableObject {
    @Published var connected: Int = 0
}

actor Network {
    var connected: Int
    let viewModel: NetworkViewModel

    init(viewModel) { self.viewModel = viewModel; self.loop() }

    private func loop() {
        if ("new device found") {
            self.connected += 1
            self.viewModel.connected += 1
        }
    }
}
```

