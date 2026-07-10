---
title: "2026 RL answer these questions one by one"
date: 2026-06-14 04:52:32
tags: ["26"]
author: "4070s wsl julyfun"
os: "Linux DESKTOP-VDB57PP 5.15.153.1-microsoft-standard-WSL2+ #2 SMP Sun Oct 27 22:02:06 CST 2024 x86_64 x86_64 x86_64 GNU/Linux"
assume-you-know: [computer]
confidence: 2
---

sheriyuo @zhihu
由于见到了拿到 PhD offer 但直接春招上岸大包的例子，本人也在想是否不登校了早点套现。于是这个合集蒸馏了知乎上所有和 RL 相关的面经，加上本人的一些最新讨论见解，整理出了最有深度的 35 道题作为合集，也算是造了个 benchmark
注意：
1.这里的问题没有严格区分 LLM RL 和 Agentic RL，但是一部分问题下 Agent 场景会有不同
2.几乎所有问题可延伸 / 追问的空间都相当大，此处不提供参考答案，使用 LLM 请反复交互并打开联网搜索
3.现在的 RL 招人需求就是尽可能全栈，不存在你做算法就不问 Infra 的情况，相反也如此
4.这里没有收集 Data 相关的题目，因为几乎没法背，全靠你的相关经历
5.切记背八股 / 面经不一定有用，打铁还需自身硬

算法部分
1. 为什么要用 Actor-Critic 而不是纯 Critic？💬 critic-only 需要取最大奖励动作，对离散适用，但连续动作空间太大无法全部计算. SAC 和 DQN 接近但引入 actor，从最大奖励动作改为动作分布，支持连续动作空间.
2. KL 散度和交叉熵、MLE 的关系？
3. 不同 RL 场景应该如何设计 Reward？
4. 如何理解 RL 中的 importance sampling / rejection sampling 等 monte carlo 方法？
5. PPO / GRPO 的 advantage 是怎么算的，为什么要减去 baseline，这里一定要除以 std 吗？
6. RL training 和 test-time scaling 各自是如何 explore 的？
7. PPO 是如何 clip 的，为什么要取 min，不 clip 会怎么样，CISPO 是怎么做的
8. GRPO 为什么加上 KL 散度，KL 散度怎么计算，为什么 DAPO、GSPO 又去掉了 KL 散度？
9. 在 LLM 训练时，如果不小心多 All Reduce 了几次 loss，会发生什么？
10. DPO 的 reward 是什么，会不会 reward hacking，如何解决？
11. 有哪些解决 MoE 训推不一致问题的算法，各自是什么原理？
12. RL 训练时，group size / learning rate / ppo epoch / generation length 如何设置？
13. 相比 GRPO，Dr.GRPO / DAPO / GSPO / CISPO / SAPO / DPPO / MaxRL / SimKO 是如何改进的，各自又有什么缺点？
14. TRPO / DPPO / AReaL 是如何用 trust region 约束 RL objective 的
15. RL 能否拓展 LLM 的能力边界？
16. 结合 ProRL 等工作，谈谈如何 scale RL 训练边界？
17. OPD 相比于传统 RL / SFT 的改进，有哪些 OPD 的应用？
18. LLM 推理能力是在哪一个训练阶段产生的？
19. DeepSeek R1 到 V3.2 / V4，RL 部分有哪些改进，MoE RL 有什么不同？

Infra 部分
1. 不考虑 cpu offload，GRPO 训练时显存里有几个模型，考虑了能省多少显存？
2. 分布式推理：KV cache 传输优化、多卡通信优化策略
3. INT8 与 FP8 优劣对比，训推分别用什么精度
4. RL rollout 中的长尾问题是什么，有哪些解决方案？
5. continuous batching 在 RL 训练时会有什么问题，vLLM 和 SGLang 的区别？
6. vLLM / SGLang 怎么看利用率，KV cache 在训练里的利用率怎么看？
7. 多机多卡 RL 训练时如何实现反向传播？
8. RL 训练有哪些异步框架，解决了同步训练的什么问题？
9. AReaL 或者其他 partially rollout 框架，在 rollout 时，会不会保存之前 policy 的 KV cache？
10. MoE 的 EP 对 throughput 的影响
11. Long context 场景下的 compute-communication overlap，megatron 和 fsdp 各自的 parallelism
12. 确定性模式怎么开，什么是 batch invariance，是什么导致的，有没有 atom add，atom add 能解决吗？
13. AReaL 和 slime 对 RL rollout bottleneck 的理解有什么不同？
14. full async staleness 怎么看，训练时大概是多少？
15. slime 里 data 怎么流，megatron 怎么结合，loss 怎么算？
16. VeRL / TRL / Unsloth / AReaL / slime 你会选哪个？
