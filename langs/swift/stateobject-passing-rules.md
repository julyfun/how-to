---
title: "@StateObject passing rules"
date: 2025-07-04 23:49:54
tags: ["langs", "swift"]
author: "Julyfun M4"
os: "Darwin tutianpeikeladeMac-mini.local 24.3.0 Darwin Kernel Version 24.3.0: Thu Jan  2 20:22:58 PST 2025; root:xnu-11215.81.4~3/RELEASE_ARM64_T8132 arm64"
assume-you-know: [computer]
---

### This is bad and ViewB reinits at unexpected time (can run directly)

```swift
import SwiftUI

class Manager: ObservableObject {
    @Published var cnt: Int = 0
}

class Manager2: ObservableObject {
    @ObservedObject var m: Manager;
    init(m: Manager) {
        self.m = m
    }

    func f() {
        self.m.cnt += 1
    }
}

struct ViewB: View {
    @ObservedObject var m: Manager
    @ObservedObject var m2: Manager2
    init(m: Manager) {
        print("init")

        self.m = m
        self.m2 = .init(m: m)
    }

    var body: some View {
        Button(action: {
            print("Clicked")
            self.m2.f()
            print("After Clicked")
        }) {
            Text("Click me")
                .font(.system(size: 40))
        }
    }
}

struct ContentView: View {
    @ObservedObject var m = Manager();
    var body: some View {
        ViewB(m: self.m)
    }
}

#Preview {
    ContentView()
}
```

### To fix it (can run directly)

```swift
import SwiftUI

class Manager: ObservableObject {
    @Published var cnt: Int = 0
}

class Manager2: ObservableObject {
    var m = Manager();
    init() {
    }

    func f() {
        self.m.cnt += 1
    }
}

struct ViewB: View {
    @ObservedObject var m2: Manager2
    @ObservedObject var m: Manager
    var printer = DeallocPrinter()

    var body: some View {
        Button(action: {
            print("***\nClicked")
            self.m2.f()
            print(self.m.cnt)
            print("After Clicked")
        }) {
            Text("\(self.m.cnt)")
                .font(.system(size: 40))
        }
    }
}

class DeallocPrinter {
    deinit {
        print("deallocated")
    }
}

struct ContentView: View {
    @StateObject private var m2: Manager2

    init() {
        self._m2 = StateObject(wrappedValue: Manager2())
    }

    var body: some View {
        ViewB(m2: self.m2, m: self.m2.m)
    }
}

#Preview {
    ContentView()
}
```
