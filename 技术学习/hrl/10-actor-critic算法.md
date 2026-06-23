---
title: 10-actor-critic算法
date: 2024-11-11 21:59:18
tags: ["notes", "julyfun", "技术学习", "hrl"]
---
see: https://hrl.boyuai.com/chapter/2/actor-critic%E7%AE%97%E6%B3%95

普通 Policy Gradient 通常使用蒙特卡洛求一整条轨迹的 `G_t`，方差大且要求完整轨迹.

引入 critic 可以用 TD 估计优势，边采样边更新而且方差更低，但会因为 critic 的网络参数引入一点 bias.

## On-policy Actor-Critic

训练 critic 来估计后续收益. 下面确实是 Time-delta advantage.

```python
states, actions, rewards, next_states, dones = rollout(pi_theta)
td_target = rewards + gamma * V_phi(next_states) * (1 - dones)
td_delta  = td_target - V_phi(states) # 这里减去 V_phi 只是为了降低方差（不改变期望）。这就是优势函数 A.
log_probs = log(pi_theta(states)[actions]) # 这里 action 必须是离散的.
actor_loss  = mean(-log_probs * detach(td_delta))
# critic 数学上含义是 V(s) = E_(pi_theta) (G_t | S_t = s),
# 但这里 critic 其实拟合的 td_target 来自更新前的 pi_theta，怎么回事？285 表示问题不大.
critic_loss = mse(V_phi(states), detach(td_target))
actor_optim.zero_grad()
critic_optim.zero_grad()
actor_loss.backward(); critic_loss.backward()
actor_optim.step(); critic_optim.step()
```

如果是连续动作 on-policy，则可使用 mean_net 和 logstd 参数，比如 285 Hw2 就是这么做的.

## Off-policy Actor-Critic

考虑在 replay buffer 中采样 (s, a)。然而，采样后不可再沿用上面 on-policy 的 advantage-based.
1. critic 的 loss 是错误的. 比如，采样得到的 (s, a) 都特别笨，导致奖励 r(s, a) 都很糟糕，而 critic 却拟合了这些.
2. actor 的梯度也是错误的，具体原因要看 actor 的梯度公式推导. 从而必须使用 importance sampling（如 PPO），当然我们也可以使用 critic 绕开这个步骤. actor 的优化目标直接改为使得 Q(s, actor(s)) 最大化，如下:
- 以下方法拆分 target network 和 online network 就是 DDPG 了.
- 以下方法的 actor 直接输出最优解而不是概率，因而适用于连续动作.

```python
replay_buffer.add(s, a, r, s2, done)
states, actions, rewards, next_states, dones = replay.sample() # 数据可能来自旧 policy
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
