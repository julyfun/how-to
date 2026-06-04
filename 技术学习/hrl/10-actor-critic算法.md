---
title: 10-actor-critic算法
date: 2024-11-11 21:59:18
tags: ["notes", "julyfun", "技术学习", "hrl"]
---
see: https://hrl.boyuai.com/chapter/2/actor-critic%E7%AE%97%E6%B3%95

## On-policy Actor-Critic

```python
states, actions, rewards, next_states, dones = rollout(pi_theta)
td_target = rewards + gamma * V_phi(next_states) * (1 - dones)
td_delta  = td_target - V_phi(states) # 这里减去 V_phi 只是为了降低方差（不改变期望）
log_probs = log(pi_theta(states)[actions])
actor_loss  = mean(-log_probs * detach(td_delta))
# 这里 td_target 其实在拟合更新前的 actor value，不过问题不大
critic_loss = mse(V_phi(states), detach(td_target))
actor_optim.zero_grad()
critic_optim.zero_grad()
actor_loss.backward(); critic_loss.backward()
actor_optim.step(); critic_optim.step()
```
