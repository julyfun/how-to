---
title: "285-hw4 LLM RL"
date: 2026-07-07 20:32:24
tags: ["技术学习", "285"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

## 回忆提纲
补全 GRPO 和 GE-REINFORCE. 这里的 GRPO 是近似 on-policy 的，只不过一次在线采样会做 `ppo_epochs` 次 optimize，从第二次 optimize 开始是略有 off-policy. 要填的空只有 8 个函数.

```python
for step in range(cfg.steps)  | 📂 hw4/hw4/train.py
├── task.sample_train_batch(...)
├── sampler.rollout(...)  | 对每个 prompt 生成多个 completion 作为一个 group | 📂 hw4/hw4/rollout/hf_sampler.py
├── 给每条 completion 打 reward
├── compute_group_advantages(...)  | group 内相对 advantage
├── 上述所有 rollout 制作成 minimatch
└──  for ppo_epoch in range(cfg.ppo_epochs)
    └── for minibatch in iter_minibatches(...)
        ├── ratio = exp(new_logp - old_logprobs)
        ├── PPO clip objective + KL
        └── backward / optimizer.step()
```

其他细节：使用 lora 微调，预训练模型都是 Qwen/Qwen2.5-Math-1.5B-Instruct.


## format_copy
输入：
```
system: You are a strict formatter.
Return the final answer as XML using exactly one tag: <answer>...</answer>.
Output only the XML tag and nothing else.
user: Copy this integer exactly: 4348
```

正确输出 `<answer>4348</answer>`. 模型早期会输出 `Here is the final answer using exactly one tag: <answer>-1748</answer>` 这种废话.

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/merged-image.png)

GRPO 一个 step 会多次更新，自然样本效率高点.

## math_hard

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/merged-image-3.png)

满分 1.1，取得了 0.4 的好成绩。

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20260711155628316.png)

kl 是相对刚开始的 baseline model，因此自然会越来越大. 而 kl loss 会抑制它增大。


## Answer questions

### 1. Approximate KL

Q: In a short paragraph, explain why the estimator e^∆−∆−1 is a valid sampled-token estimator for the KL term used in this assignment, and why computing the exact full-vocabulary KL at every token position would be much more expensive in both compute and memory.

A: 回顾：∆ = log prob - log prob_ref. 尽管 -∆ 也是一个 unbiased estimator，但可能为负数，且如果当前 policy 比 ref policy 对于某个 token 输出的概率小，则 -∆ > 0 从而奖励这种行为. "This is not a very natural surrogate for a divergence, since the role of KL term is to discourage deviations from the reference."

而 `e^∆−∆−1` 期望等于 `E(log prob - log prob_ref) = KL(pi || pi_ref)`. 而且总是非负，和 KL 的非负保持一致.

### 2. Implementation

Q: Briefly describe.

A: 按照 pdf 建议的顺序补全了 8 个函数.

one bug or confusion point: 写 GRPO 的时候我发现 GRPO loss 的量纲和 GR-REINFORCE loss 似乎不同，后者具有平凡 PG surrogate 的 `-logprob * adv`，而前者是 `-(logprob_new - logprob_old).exp() * adv`. 后来询问发现 GRPO 也是正确的 surrogate.

### 3. GR-REINFORCE vs. GRPO on math

Q: Compare the WandB curves for the math runs. How do the two methods differ over the first 200 iterations? Why is that comparison interesting given the way the provided commands were chosen?

A: GRPO reward 上升更快. 你说 interesting 在哪，可能是当前设置下每个 step 利用的样本数一样，可以显然确认 GRPO 样本效率更高吧。其实 GRPO 在同样 optimizer.step() 次数时上升稍慢，不过这当然是合理的。

### 4. GRPO ablation on format_copy

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/merged-image-4.png)

Q: Summarize the extra GRPO runs you tried. Which hyperparameters mattered most? Which settings made learning worse, and why do you think they did?

A: 主要有 ga1 导致初期 reward 上升快但是逐渐不稳定. ppo_epoch=5 当然样本效率更高，同样 step 上升更快.

## 5. Qualitative behavior

Q: Include one or two model-generation examples from WandB that you found informative or surprising from the math-hard task.

A: 注意奖励函数其实没有要求去掉推导过程.

1. 居然用中文思考了:
```
To solve the problem, we need to find three Fibonacci numbers \(F_a\), \(F_b\), and \(F_c\) that form an increasing arithmetic sequence, and satisfy the condition \(a + b + c = 2000\). We need to compute the value of \(a\).

First, let's recall that for three numbers to form an arithmetic sequence, the difference between consecutive terms must be the same. Therefore, we have \(F_b - F_a = F_c - F_b\), which simplifies to \(2F_b = F_a + F_c\).

We will use the properties of the Fibonacci sequence and the given condition \(a + b + c = 2000\) to find the values of \(a\), \(b\), and \(c\).通过 Slate的算法，我们发现\(a = 665\).

Thus, the value of \(a\) is \(\boxed{665}\).
```

2. 有的在思考过程中间某一步开始会输出乱码，十分地掉 san.
   ![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20260711170810795.png)
3. 题目怎么这么难
