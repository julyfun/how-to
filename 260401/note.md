 仔细阅读参考这里的 UI 设计 /Users/florian/Documents/Github/zed。反思我们的 src/ar/ArManagerV1.swift 。由于通过 EventBus.shared 订阅事件并没有锁定主线程，导致我们在
    subscribe() 的回调中常需要使用 DispatchQueue.main.async。但是这样其实会导致 Sending self，导致编译器报错，如何模仿 zed 改进？. 另外请思考：通常 @ObservableObject
  应
    该是一个 @MainActor 吗？ . 注意不是让你来过度批判的，客观分析改进方向或重构方向。    

```
• GPUI 不是靠一个全局 EventBus 统一解决所有跨模块通信，它更常用这几种方式：

  1. 实体直接持有别的实体句柄

  - 一个模块拿着另一个模块的 Entity<T> / WeakEntity<T>
  - 需要交互时直接 update(...)、read(...)
  - 这是最常见的“定向通信”

  2. 实体发自己的强类型事件

  - 某个 view/model impl EventEmitter<E>
  - 相关方通过 cx.subscribe(...) / cx.subscribe_self(...) 订阅
  - 这更像“对象级事件”，不是全局广播

  3. 共享全局状态用 global/store

  - 一些真正全局的配置、状态、服务，会挂到 app context 里
  - 其他模块通过 context 读取或观察
  - 更像依赖注入，不像 event bus

  4. 后台任务算完，再定向更新目标实体

  - 后台 async 逻辑拿到结果后，不广播
  - 而是 this.update(cx, ...) 或更新某个明确的 entity

  所以它的思路是：

  - 有明确接收者：直接拿句柄调用
  - 有明确所有者的事件：订阅该对象的 typed event
  - 真全局的数据：挂 global/store
  - 很少用“谁都能发、谁都能收”的全局总线

  对应你们这里可以这样套：

  - Peers -> ArManager 的 collaboration data：定向接口/弱引用，不要广播
  - ArManager -> Peers 的 publish 行为：保留直接依赖或抽 protocol
  - RecordSaved、Ui.Notif 这种多方都可能关心的：才适合 EventBus
  - RecordCmd 如果实际上只有一个 owner 处理：改成 command sink，不要伪装成广播事件

  一句话，GPUI 更像“对象图 + 定向消息 + typed event”，不是“全局总线优先”。
````

