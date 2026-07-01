---
title: "Paper Prompt 260618"
date: 2026-06-18 01:23:19
tags: ["25", "01"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

## 阅读论文后输出 markdown 格式

```markdown
## 论文标题
[LLM 模型] 一句话主要贡献，逗号最多一个（或者一句话复现方法）[<主要机构，第一作者，通讯作者>]
<空行>
| 🦾 <项目网站（如能搜到）> | 📃 https://hjfy.top/arxiv/<arxiv-id e.g. 2505.11917>  | ✨ https://www.alphaxiv.org/abs/<arxiv-id> | 💻 <github 代码连接（如能搜到，通常在项目网站中有，如果说 TBA 就写 TBA）> |
|-|-|-|-|
<空行>
正文第一段 0-3 个逗号，说贡献，可选对比前作的新增，在限制句数中让小白都能 get 到如何去复现这篇论文。
<空行>
第二段可选，0-3 个逗号。用于指出局限性
```

正文示例：
```
1. 所有帧共享 8 个 learnable gist query embedding，这样就可以每帧留下 8 个 gist embed 和对应 kv cache.（完整视觉 token 是 120 个）.
2. 滑动窗口完整视觉 token
3. 起始帧完整视觉 token

其他结构则是 Pi-like Video DiT + action expert DiT.
```

```
Cosmos Policy 使用 Cosmos 作为预训练模型，然后让它同时预测 frame、value 和 action。做法很直接，关键假设是 Cosmos 的视频表征可以承载动作建模，这个假设未必成立，但作为一篇把 WM-VLA 路线推到简单极限的工作有参考价值。可以用来反推哪些精心设计的模块真的必要。
```

```
为了引入 text-level reasoning 但又不想分为显式双系统，OneTwoVLA 使用 Pi0-like 架构中的 VLM 输出自回归输出 <BEGIN_OF_ACTION> 或 <BEGIN_OF_REASONING> token，如果是前者就继续走常规流程，后者就继续自回归生成 reasoning. 数据是分段手标的.
```

一句话总结示例:
```
Cosmos Policy 直接把 Cosmos 后训成同时预测视频、动作和值的策略模型
```

```
让 Pi0 VLM 输出 token 来决定是否 reasoning
```

`[LLM 模型]` 由你当前实际模型填写，例如 `[GPT5.5]`

## 写法约束

不要过度使用斜杠 `/` 来模糊表达。除了官方模型名或论文名里的斜杠，尽量不用斜杠。必须写清楚语义：

- 表示并列用 `和` 或 `、`。
- 表示选择用 `或`。
- 表示解释用 `i.e.`、`也即`。
- 表示包含关系用 `包括`。

不要使用比喻。不要写“医疗版 GR00T-Dreams”“纸面系统”“把 X 硬塞进 Y”“领域适配”这类模糊和冗长说法。适当使用简洁而通俗易懂说法，可以写：`本文似乎主要是缝合 GR00T-Dreams 和 GR00T-N1.5。`

不要猜测，不确定方法直接读代码.

不要堆叠你不确定的专有名词。不能用一串名字假装理解，例如不要写：`相对 Pi-0/Pi-0.5/GR00T-N1.5/RDT2/OpenVLA 没有引入流匹配或层次化推理改造`。如果要比较，只选 1 个最相关对象，并说出具体比较点。

不要引用论文自己的营销词来当评价。比如论文说 `physical red teaming`，你可以改成：`它主要测试物理扰动下策略是否失效。`

不要用“不是 A，是 B”，直接说 "是 B"。例：不要写 `WorldArena 2.0 不是方法论文，是 benchmark 扩展工作`，写 `WorldArena 2.0 是一个 benchmark。`。

不要使用“是 A，而不是 B”，直接说 ”是 A“.

少写：`层次化推理改造`、`范式级创新`、`统一闭环智能体架构`、`鲁棒性显著提升`、`它的结构更克制`。

多写：`先生成 subgoal image，再让 VLA 执行动作`、`只在 LIBERO 测，没有真机`、`动作头还是 Pi0-like`、`需要看是否有 Pi-like baseline`。

不好的写法：

- `批判地看，问题相当典型：评测困在 LIBERO 这种桌面抓取小盒子里做，所谓 physical red teaming 离 AMO、ExBody 那种 whole-body 还差一个量级。`
- `但坦白讲，这更像是一篇医疗版 GR00T-Dreams + GR00T-N1.5 适配报告。`
- `相对 Pi-0/Pi-0.5/GR00T-N1.5/RDT2/OpenVLA 没有引入流匹配或层次化推理改造。`
- `它值得读的点不是模块多，而是可以作为一条强 baseline，`
