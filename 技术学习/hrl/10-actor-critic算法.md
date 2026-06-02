---
title: 10-actor-critic算法
date: 2024-11-11 21:59:18
tags: ["notes", "julyfun", "技术学习", "hrl"]
---
see: https://hrl.boyuai.com/chapter/2/actor-critic%E7%AE%97%E6%B3%95

上一章用 $G_t$ 代替 $Q^pi (s, a)$，现在用时序差分残差公式(当前动作带来的额外奖励期望)代替之.
- 因为 $Q = r + gamma V$, 所以训练一个 $V$ 网路就行

训练一个价值网络 V:
- Input : 可微状态 $s$
- Output : $V(s)$
- Loss: $$1 / 2 (r + gamma V_omega (s_(t + 1)) - V_omega (s_t))^2$$
    - 其中 $r + gamma V_omega (s_(t + 1))$ 不参与梯度计算. 代码中使用 `detach()` 直接实现，不用双网络.
    - 和 DQN 一样训练数据来源于采样池.
    - 训练过程和 Actor 的关系？Actor 产生了采样池，Actor 变强后采样分布会变化
        - 采样数据为 $(s_i, a_i, r_i, s_i^prime)$.
        - 注意采样的 $a$ 并不影响 $V$ 梯度下降，乱采样也能训练出正确的 $V$ 网络

其他：
- 这种方法在数学上要求 on-policy，如果产生的动作概率和实际执行的 action 不是来自一个 net，那么梯度计算是错误的，除非补上 $pi(a) / pi(b)$ 项.
- 以下代码也是 on-policy 的
- 原文已经很简短了，可以看原文

```python
class ActorCritic:
    # self.critic = ValueNet(state_dim, hidden_dim).to(device)  # 价值网络
    ...
    def update(self, transition_dict):
        states = torch.tensor(transition_dict['states'],
                              dtype=torch.float).to(self.device)
        actions = torch.tensor(transition_dict['actions']).view(-1, 1).to(
            self.device)
        rewards = torch.tensor(transition_dict['rewards'],
                               dtype=torch.float).view(-1, 1).to(self.device)
        next_states = torch.tensor(transition_dict['next_states'],
                                   dtype=torch.float).to(self.device)
        dones = torch.tensor(transition_dict['dones'],
                             dtype=torch.float).view(-1, 1).to(self.device)

        # 时序差分目标
        td_target = rewards + self.gamma * self.critic(next_states) * (1 -
                                                                       dones)
        # 时序差分差. 即：当前动作带来的额外奖励期望（在 critic 精准的情况下）
        td_delta = td_target - self.critic(states)
        log_probs = torch.log(self.actor(states).gather(1, actions))
        actor_loss = torch.mean(-log_probs * td_delta.detach())
        # 均方误差损失函数，这里直接 detach() 来实现类似 Double DQN 的效果
        critic_loss = torch.mean(
            F.mse_loss(self.critic(states), td_target.detach()))
        self.actor_optimizer.zero_grad()
        self.critic_optimizer.zero_grad()
        actor_loss.backward()  # 计算策略网络的梯度
        critic_loss.backward()  # 计算价值网络的梯度
        self.actor_optimizer.step()  # 更新策略网络的参数
        self.critic_optimizer.step()  # 更新价值网络的参数

class PolicyNet(torch.nn.Module):
    def __init__(self, state_dim, hidden_dim, action_dim):
        super(PolicyNet, self).__init__()
        self.fc1 = torch.nn.Linear(state_dim, hidden_dim)
        self.fc2 = torch.nn.Linear(hidden_dim, action_dim)

    # 输入状态 states: [batch_size, state_dim]
    # 输出动作概率分布
    def forward(self, x):
        x = F.relu(self.fc1(x))
        return F.softmax(self.fc2(x), dim=1)

class ValueNet(torch.nn.Module):
    def __init__(self, state_dim, hidden_dim):
        super(ValueNet, self).__init__()
        self.fc1 = torch.nn.Linear(state_dim, hidden_dim)
        self.fc2 = torch.nn.Linear(hidden_dim, 1)

    # 输入状态 states: [batch_size, state_dim]
    # 输出状态价值 V(s): [batch_size, 1]
    def forward(self, x):
        x = F.relu(self.fc1(x))
        return self.fc2(x)
```

- 效果：抖动比基于蒙特卡洛的 REINFORCE 收敛更快，且非常稳定.

## BORA: zhongxi_chen
