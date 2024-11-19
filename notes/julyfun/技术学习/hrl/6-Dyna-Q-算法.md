- 在 Q-learning 之上自己再学个超级简单的环境，每次 Q-learning 完之后再根据这个环境去随机更新 $N$ 个.
    - 什么超绝朴素想法。

![image.png](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20241108222049.webp)

```python
class DynaQ:
    ...
    def q_learning(self, s0, a0, r, s1):
        td_error = r + self.gamma * self.Q_table[s1].max(
        ) - self.Q_table[s0, a0]
        self.Q_table[s0, a0] += self.alpha * td_error

    def update(self, s0, a0, r, s1):
        self.q_learning(s0, a0, r, s1)
        self.model[(s0, a0)] = r, s1  # 将数据添加到模型中
        for _ in range(self.n_planning):  # Q-planning循环
            # 随机选择曾经遇到过的状态动作对
            (s, a), (r, s_) = random.choice(list(self.model.items()))
            self.q_learning(s, a, r, s_)
```

done.
