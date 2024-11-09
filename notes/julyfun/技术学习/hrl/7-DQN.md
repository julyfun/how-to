- 作用：对于连续的状态和离散的动作，可通过采样方式更新神经网络
    - Input: state
    - Output: value of all actions
    - 这就是学了个 $Q$，有了 $Q$ 策略就是选最大价值动作。
- ![image.png](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20241108230928.webp)
## 损失设计

- 由于 Q-learning 是这样的:
- ![image.png](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20241108231138.webp)
- 所以对于一个批量的采样 ${(s_i, a_i, r_i, s_i^prime)}$，可以这样设计损失函数:
    - 注意下面损失函数里有 $Q$ 本身，无法方便求损失，所以设计了训练网络和目标网络。这里 $w$ 是 MLP 权重。
- ![image.png](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20241108231239.webp)
- 损失函数为 $0$ 时，满足: 动作奖励函数 = 该动作奖励 + $gamma times$ 随机采样后续状态下最优动作奖励函数

## 经验回放 experience replay

将历次采样放入缓冲区，取缓冲区的若干次数据（而不是最近一次）作为一个小批量来优化 $Q_w$

## 目标网络 + 训练网络

其实就是复制两份网络，训练网络每次批量优化时都会更新（目标网络暂不更新），其中损失函数使用目标网络计算，每隔 $C$ 步将目标网络同步到训练网络。注意神经网络形式化的损失函数总是 $sum (F(x_i) - y_i^tilde)^2$，在下方原文中可以见到。

![image.png](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20241108231747.webp)

```python
# 常规 Q-learning
...
action = agent.take_action(state)
next_state, reward, done = env.step(action)
agent.update(state, action, reward, next_state)
state = next_state

class ...:
    def update(self, s0, a0, r, s1):
        td_error = r + self.gamma * self.Q_table[s1].max(
        ) - self.Q_table[s0, a0]
        self.Q_table[s0, a0] += self.alpha * td_error
```

```python
# DQN
class ...:
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

        q_values = self.q_net(states).gather(1, actions)  # Q值
        # 下个状态的最大Q值
        max_next_q_values = self.target_q_net(next_states).max(1)[0].view(
            -1, 1)
        q_targets = rewards + self.gamma * max_next_q_values * (1 - dones
                                                                )  # TD误差目标
        dqn_loss = torch.mean(F.mse_loss(q_values, q_targets))  # 均方误差损失函数
        self.optimizer.zero_grad()  # PyTorch中默认梯度会累积,这里需要显式将梯度置为0
        dqn_loss.backward()  # 反向传播更新参数
        self.optimizer.step()

        if self.count % self.target_update == 0:
            self.target_q_net.load_state_dict(
                self.q_net.state_dict())  # 更新目标网络
        self.count += 1


action = agent.take_action(state)
next_state, reward, done, _ = env.step(action)
replay_buffer.add(state, action, reward, next_state, done)
state = next_state
# 当buffer数据的数量超过一定值后,才进行Q网络训练
if replay_buffer.size() > minimal_size:
    b_s, b_a, b_r, b_ns, b_d = replay_buffer.sample(batch_size)
    transition_dict = {
        'states': b_s,
        'actions': b_a,
        'next_states': b_ns,
        'rewards': b_r,
        'dones': b_d
    }
    agent.update(transition_dict)
```

done.
    