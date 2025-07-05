---
title: 11-trpo算法
date: 2024-11-11 22:29:41
tags: ["notes", "julyfun", "技术学习", "hrl"]
---
- 对 AC 做了非常多优化
- 【策略目标】
    - 修改成新策略 $pi_(theta^prime)$ 下的形式
    - 并做近似
    - 近似过程要求 $theta^prime$ 和 $theta$ 不能差太多，故 KL 散度约束到 $delta$ 之内.
- 【近似求解】 
    - 对目标函数 1 阶近似，带 $g$，KL 约束 2 阶近似，带海森矩阵 $H$.
    - 可直接用 KKT 导出问题的解 $theta_(k + 1)$.
- 【共轭梯度】
    - 直接假设每一步 KL 散度都更新到 $delta$，可简化 KKT 解
    - 直接用共轭梯度法解算  $H x = g$
- 【线性搜索】
    - 由于多处近似，解可能不满足 KL 散度约束
    - 取 $(0, 1)$ 之间的超参数 $alpha$，求最小非负整数 $i$ 使得 $alpha^i$ 倍变化量满足 KL 散度限制.
- 【广义优势估计】
    - 上面还没估计优势函数 [?]
    - 设时序差分误差 $delta_t = r_t + gamma V(s_(t + 1)) - V(s_t)$
    - 令 $A_t^((k)) = sum_(l = 0)^(k - 1) gamma^l delta_(t + l)$
    - 对 $A$ 进行指数加权平均.

## 代码实践

- 如果动作时连续的，策略网络可输出动作高斯分布的均值和标准差，形同:

```py
        mu, std = self.actor(states)
        old_action_dists = torch.distributions.Normal(mu.detach(),
                                                      std.detach())
        old_log_probs = old_action_dists.log_prob(actions)
        critic_loss = torch.mean(
            F.mse_loss(self.critic(states), td_target.detach()))
        self.critic_optimizer.zero_grad()
        critic_loss.backward()
```
