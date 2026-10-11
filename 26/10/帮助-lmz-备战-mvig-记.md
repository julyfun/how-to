---
title: "帮助 lmz 备战 MVIG 记"
date: 2026-10-12 00:10:36
tags: ["26", "10"]
author: "4070s wsl julyfun"
os: "Linux DESKTOP-VDB57PP 5.15.153.1-microsoft-standard-WSL2+ #2 SMP Sun Oct 27 22:02:06 CST 2024 x86_64 x86_64 x86_64 GNU/Linux"
assume-you-know: [computer]
confidence: 2
---

话说为了给 lmz 备战周日的 MVIG 面试，周五她上晚课之前，我从 CNN -> ViT -> Pi05 -> WAM，帮 lmz 全部复习一遍. 而 lmz 居然也都理清楚了。

还是那句话，心里有 Pi05 和 MoT 那张图，目前的 manipulation model 架构都是在上面史上雕花，看论文一眼就能看懂.

随后周六还是无所事事了一天，直到晚上 23:00 才赶紧复习。这次计划是针对简历大读特读，然后写 PPT. 然而，这一搞居然就是不间断也不吃饭的 15 小时. Let's review what happened.

- 23:00 lmz 看她的 Tac-DINO 而我用 zed 写 mermaid 知识结构图 (其实没有什么用).
- 0:00 我在 alphaxiv 仔细阅读 Tac-DINO 细节.
- 1:00 我还在看 Tac-DINO 硬件等.
- 2:00 交流各个论文细节，回顾 RL 基础知识.
- 3:00 在丁真简历里的各种东西. lmz 在 PPT 列第一版信息.
- 5:00 GPT 提问题，复习优化器等 deep-learning & robot & agent 基础知识.
- 6:00 尝试搞第二版 PPT，从个人背景开始，中间切换排版风格，再调整 Tac-DINO 开始的三篇文章，然后是项目以及最后 Interests.
- 9:00 PPT 写到最后一页了，让 GPT 列细分方向，逐条分析兴趣. - ps: RoboPocket 那个算法是 Interactive Robot Learning 方向.
- 10:00 对简历查漏补缺.
- 11:00 让 GPT 对简历和 PPT 写第一版稿子.
- 12:00 模拟以稿子为提纲 3min 介绍自己，微调稿子
- 12:40 模拟 7min 对着简历刁钻提问.
- 13:30 lmz 自己补充 DL / RL 常识. 我困得快死了~
- 14:00 我躺床上刷手机缓一下.
- 14:20 正襟危坐等待进腾讯会议室.

也不知道最后能不能进，看面试互动我感觉理论非常稳.

### 细分方向

1. 👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎 触觉表征学习 ⇒ 硬件瓶颈
2. in-hand manipulation （灵巧手），我们公司有 WUJI 灵巧手
3. 灵巧手动作重定向 retargetting
4. ⭐️ in-context learning. 
    - 不想做数据工程（数据处理、采数据、任务设计、benchmark）。cwd 和 wenchuan 包调任何方向，自由实验室。 ⇒ 太过于工程，本质一堆人写任务
    - 不想做工程，想做算法。氛围期望：不要是 leader 纯派任务，在多多讨论的氛围中做事情.
5. ⭐️ reactive & 力控 (implicit-RDP, LIFT）
6. 👎👎👎👎👎👎👎 触觉
7. agent policy (GPT-gated DAgger, GPT-as-teacher DAgger, VLA 介入门控 & feedback)
    1. 中等 LLM 接入.
    2. ⭐️⭐️ agent RL
8. VLA-RL ，不喜欢
9. 利用 RL 思想（pi06）训了一个 value function，帮助标注和加权监督训练.
10. LLM-style 第三步 RL ，必须还
11. VLA 细分方向，疯狂加输入表征和辅助 loss (guided vla)
12. 0.01⭐️ WAM 疯狂改架构加表征史上雕花
13. 记忆能力（实验室没人会做）. MEM
14. 👎 sim2real（实验室没人做 sim 并且 wc 和 cwd 两大 mentor 目前觉得仿真永远做不出来）
15. 👎👎👎👎👎 benchmark
16. ⭐️ 真机 deploy，有 learning 算法的部分也有工程的部分. 然而，我们实验室目前有0人在推进。
17. ⭐️⭐️ 如何 leverage Ego 数据
18. ⭐️ scaling: 如何利用跨本体以及各种的预训练数据（FJJ大作在此. no paper）
19. 如何提升 policy 的跨本体能力 (Cross Embodiment) 跨本体迁移
20. ⭐️⭐️ 持续学习 continual learning
