### 隐式导入
- 一个项目所有符号都在全局.
- 导致学习 Swift 时不清楚每个符号的来源.
    - 难以了解模块依赖和 in-out 功能.
    - 比如 ARView 实际上不是 ARKit 而是 RealityKit
- no namespace
    - 只能用 class 模拟 namespace

好处:
- 随便改变文件夹结构不用重写 import.

## 隐式 self
- 难以阅读函数符号是全局函数还是成员函数.
    - 两者依赖的状态完全不同.

## struct 和 class 区分
- 额外的心智负担，而灵活性又不高.

