 仔细阅读参考这里的 UI 设计 /Users/florian/Documents/Github/zed。反思我们的 src/ar/ArManagerV1.swift 。由于通过 EventBus.shared 订阅事件并没有锁定主线程，导致我们在
    subscribe() 的回调中常需要使用 DispatchQueue.main.async。但是这样其实会导致 Sending self，导致编译器报错，如何模仿 zed 改进？. 另外请思考：通常 @ObservableObject
  应
    该是一个 @MainActor 吗？ . 注意不是让你来过度批判的，客观分析改进方向或重构方向。    
