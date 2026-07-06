---
title: "Paper Prompt 260618"
date: 2026-06-18 01:23:19
tags: ["25", "01"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

使用 arxiv api 获取论文，阅读后输出:

```markdown
## 论文标题
[当前模型 e.g. Gemini 3.1 Pro] 一句话主要贡献或复现方法，逗号最多一个 | 👤 第一作者学校或机构, 第一作者, 通讯作者 | [🌐](项目网站) 搜不到就占位符 - | [📃 <arxiv-id e.g. 2505.11917>](https://hjfy.top/arxiv/<arxiv-id>) | [✨](https://www.alphaxiv.org/abs/<arxiv-id>) | [📂](代码连接) 搜不到就 - |
<空行>
正文第一段 0-5 个逗号，说贡献，可选对比前作的新增，在限制句数中让小白都能 get 到如何去复现这篇论文。
<空行>
第二段可选，0-3 个逗号。用于指出局限性或总结实验中得到的一些有趣结论（不用说成功率提升多少之类的）
```

**正文示例:**

为 video dit 提供了三种 memory token:
1. 所有帧共享 8 个 learnable gist query embedding，这样就可以每帧留下 8 个 gist embed 和对应 kv cache.（完整视觉 token 是 120 个）.
2. 滑动窗口完整视觉 token
3. 起始帧完整视觉 token

除此之外继承了常见 WAM 的 Video DiT + action expert DiT.

---

Cosmos Policy 使用 Cosmos 作为预训练模型，然后让它同时预测 frame、value 和 action。文章说基于 Cosmos 的视频表征也可以建模动作的假设，这个假设未必成立.

---

为了引入 text-level reasoning 但又不想分为显式双系统，OneTwoVLA 使用 Pi0-like 架构中的 VLM 输出自回归输出 <BEGIN_OF_ACTION> 或 <BEGIN_OF_REASONING> token，如果是前者就继续走常规流程，后者就继续自回归生成 reasoning. 数据是分段手标的.

**一句话总结示例:**

Cosmos Policy 直接把 Cosmos 后训成同时预测视频、动作和值的策略模型

---

让 Pi0 VLM 输出 token 来决定是否 reasoning

## 写法约束

除了官方模型名或论文名里的斜杠，尽量不用斜杠，写清楚语义：

- 表示并列用 `和` 或 `、`。
- 表示选择用 `或`。
- 表示解释用 `i.e.`、`也即`。
- 表示包含关系用 `包括`。

不要使用比喻。不要写“医疗版 GR00T-Dreams”“纸面系统”“把 X 硬塞进 Y”“领域适配”这类模糊和冗长说法。适当使用简洁而通俗易懂说法，可以写：`本文似乎主要是缝合了 GR00T-Dreams 和 GR00T-N1.5。`

不要猜测，不确定方法直接读代码.

不要堆叠你不确定的专有名词。不能用一连串名词假装理解。如果要比较，只选 1 个最相关对象，并说出具体比较点。

不要引用论文自己的营销词来当评价。

不要用“不是...，是...”，不要使用“是...，而不是...”，直接说 "是..."。

不好的用词：`层次化推理改造`、`范式级创新`、`统一闭环智能体架构`、`鲁棒性显著提升`、`它的结构更克制`、`锚点`。

不好的写法：

- `批判地看，问题相当典型：评测困在 LIBERO 这种桌面抓取小盒子里做，所谓 physical red teaming 离 AMO、ExBody 那种 whole-body 还差一个量级。`
- `但坦白讲，这更像是一篇医疗版 GR00T-Dreams + GR00T-N1.5 适配报告。`
- `相对 Pi-0/Pi-0.5/GR00T-N1.5/RDT2/OpenVLA 没有引入流匹配或层次化推理改造。`
- `它值得读的点不是模块多，而是可以作为一条强 baseline，`

纠正示例：
- bad: `深度融合了视觉、语言、动作和触觉`
- good: 直接说明 `15x8 触觉传感数组 -> [MLP] -> 36 个触觉 token -> concat image&text token -> [VLM]`

好的用词（简单而能推测出复现方法）：`生成 subgoal image，经过 image encoder 送给 VLM`、`只有 LIBERO 测试，没有真机`.
