---
title: 10-actor-critic算法
date: 2024-11-11 21:59:18
tags: ["notes", "julyfun", "技术学习", "hrl"]
---
see: https://hrl.boyuai.com/chapter/2/actor-critic%E7%AE%97%E6%B3%95

## On-policy Actor-Critic

训练 critic 来估计后续收益.

```python
states, actions, rewards, next_states, dones = rollout(pi_theta)
td_target = rewards + gamma * V_phi(next_states) * (1 - dones)
td_delta  = td_target - V_phi(states) # 这里减去 V_phi 只是为了降低方差（不改变期望）
log_probs = log(pi_theta(states)[actions]) # 这里 action 必须是离散的.
actor_loss  = mean(-log_probs * detach(td_delta))
# 这里 critic 其实在拟合更新前的 actor value，不过问题不大
critic_loss = mse(V_phi(states), detach(td_target))
actor_optim.zero_grad()
critic_optim.zero_grad()
actor_loss.backward(); critic_loss.backward()
actor_optim.step(); critic_optim.step()
```

如果是连续动作，则需要一个 `pi_theta` 来求概率密度函数，并不容易。

## Off-policy Actor-Critic

在 replay buffer 中采样 s, a

```python
replay_buffer.add(s, a, r, s2, done)          # 数据可能来自旧 policy
states, actions, rewards, next_states, dones = replay.sample()
next_actions = pi_theta(next_states)           # 当前 actor 给下一动作
td_target = rewards + gamma * Q_phi(next_states, next_actions) * (1-dones)
critic_loss = mse(Q_phi(states, actions), detach(td_target))
freeze(Q_phi)
actor_loss  = -mean(Q_phi(states, pi_theta(states)))
actor_optim.zero_grad()
critic_optim.zero_grad()
actor_loss.backward(); critic_loss.backward()
actor_optim.step(); critic_optim.step()
```

如果 off-policy 沿用上面 on-policy 的 advantage-based，则采样的 a 的分布不再满足推导式 $nabla_theta J(theta)$ 的要求，梯度有偏，训练崩溃，从而必须使用 importance sampling，而现代方法多使用 Q critic 绕开这个步骤.
