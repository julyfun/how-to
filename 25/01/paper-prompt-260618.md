---
title: "Paper Prompt 260618"
date: 2026-06-18 01:23:19
tags: ["25", "01"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

## 输入

我会给你 网页 或 PDF。你需要先读材料，再写评价。

在写新 paper 评价之前，务必先做这些准备：

1. 阅读 `~/Documents/GitHub/julyfun/how-to/papers` 下所有 markdown，获取我已经了解的主要具身 paper。

## 输出格式

```text
## 论文标题
[模型名称] 一句话主要贡献，逗号最多一个（或者一句话复现方法） | <第一机构，第一作者，通讯作者> <项目网站（如能搜到）> | https://hjfy.top/arxiv/<arxiv_id e.g. 2505.11917>  | https://www.alphaxiv.org/abs/<arxiv_id> | <github 代码连接（如能搜到）>

正文第一段 0-3 个逗号，说贡献，可选对比前作的新增，在限制句数中让小白都能 get 到如何去复现这篇论文。

第二段可选，0-3 个逗号。用于指出局限性
```

```text
[Model] Cosmos Policy 直接把 Cosmos 后训成同时预测视频、动作和值的策略模型 | ...各种网站

Cosmos Policy 使用 Cosmos 作为预训练模型，然后让它同时预测 frame、value 和 action。做法很直接，关键假设是 Cosmos 的视频表征可以承载动作建模，这个假设未必成立，但作为一篇把 WM-VLA 路线推到简单极限的工作有参考价值。可以用来反推哪些精心设计的模块真的必要。
```

```text
[Model] 让 Pi0 VLM 输出 token 来决定是否 reasoning | 清华 Fanqi Lin, Yang Gao | https://one-two-vla.github.io | https://hjfy.top/arxiv/2505.11917 | https://www.alphaxiv.org/abs/2505.11917 | https://github.com/Fanqi-Lin/OneTwoVLA

为了引入 text-level reasoning 但又不想分为显式双系统，OneTwoVLA 使用 Pi0-like 架构中的 VLM 输出自回归输出 <BEGIN_OF_ACTION> 或 <BEGIN_OF_REASONING> token，如果是前者就继续走常规流程，后者就继续自回归生成 reasoning. 数据是分段手标的.
```

`[模型名称]` 由你当前实际模型填写，例如 `[GPT5.5]`

## 内容要求

一句话总结必须先出现，且只能有一个逗号或没有逗号。它要直接说明 paper 的核心位置，不要写成标题党，不要写“本文提出一种新框架”这种空话。

评价要保持模糊和克制。可以使用“看起来”“似乎”“可能”“需要看实验”“目前我会把它理解为”等表达。不要把没有精读过的 paper 评价成确定事实。

如果论文在以下方面信号明显，则可以回答这些问题，但不必全部覆盖：

- 这是一篇方法、benchmark、dataset、infra、survey、deployment report，还是系统整合？
- 它魔改自哪条路线：Pi-like、ACT-like、WM-VLA、WAM、DAgger、force-aware、humanoid tracking、world model、benchmark 还是新方法？
- 和哪些前作最应该比较？只提你真正能解释的前作，不要堆名字。
- 缺陷在哪里？优先看真机、任务范围、评测设置、架构是否过时、是否依赖手工 pipeline、是否看似只在仿真 benchmark 有优势。

## 写法约束

不要过度使用斜杠 `/` 来模糊表达。除了官方模型名或论文名里的斜杠，尽量不用斜杠。必须写清楚语义：

- 表示并列用 `和` 或 `、`。
- 表示选择用 `或`。
- 表示解释用 `i.e.`、`也即`。
- 表示包含关系用 `包括`。

不要使用比喻。不要写“医疗版 GR00T-Dreams”“纸面系统”“把 X 硬塞进 Y”“领域适配”这类模糊和冗长说法。适当使用简洁而通俗易懂说法，可以写：`本文似乎主要是缝合 GR00T-Dreams 和 GR00T-N1.5。`

不要堆叠你不确定的专有名词。不能用一串名字假装理解，例如不要写：`相对 Pi-0/Pi-0.5/GR00T-N1.5/RDT2/OpenVLA 没有引入流匹配或层次化推理改造`。如果要比较，只选 1 个最相关对象，并说出具体比较点。

不要引用论文自己的营销词来当评价。比如论文说 `physical red teaming`，你可以改成：`它主要测试物理扰动下策略是否失效。`

不要用“不是 A，是 B”，直接说 "是 B"。例：不要写 `WorldArena 2.0 不是方法论文，是 benchmark 扩展工作`，写 `WorldArena 2.0 是一个 benchmark。`。

不要使用“是 A，而不是 B”，直接说 ”是 A“.

少写：`层次化推理改造`、`范式级创新`、`统一闭环智能体架构`、`鲁棒性显著提升`、`它的结构更克制`。

多写：`先生成 subgoal image，再让 VLA 执行动作`、`只在 LIBERO 测，没有真机`、`动作头还是 Pi0-like`、`需要看是否有 Pi-like baseline`。

## 批判方式

批判要短、具体、可验证，并允许不确定。

好的写法：

- `问题：没有真机评测，实验仅 LIBERO。并且架构设计看起来沿用了 ACT-like，未采用较新的 Pi-like action expert，可能缺乏泛化能力。其在 LIBERO 上的 SOTA 可能有 overfit 风险。`
- `这个设计把动作稳定性的一部分压力转到了几何约束上，所以需要看遮挡、深度误差和相机外参偏移下的表现。`
- `它的价值主要在 benchmark 协议，但是否会被社区采用取决于评测是否容易复现。`
- `本文看起来是数据和工程规模驱动的工作，方法本身不复杂，但如果真机 demo 足够强，仍然值得读。`
- `它可以用来反推模块的必要性`

不好的写法：

- `批判地看，问题相当典型：评测困在 LIBERO 这种桌面抓取小盒子里做，所谓 physical red teaming 离 AMO、ExBody 那种 whole-body 还差一个量级。`
- `但坦白讲，这更像是一篇医疗版 GR00T-Dreams + GR00T-N1.5 适配报告。`
- `相对 Pi-0/Pi-0.5/GR00T-N1.5/RDT2/OpenVLA 没有引入流匹配或层次化推理改造。`
- `它值得读的点不是模块多，而是可以作为一条强 baseline，`
